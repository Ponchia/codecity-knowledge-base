#!/usr/bin/env python3
"""Build a local, LLM-friendly bibliography library from CodeCity_sources.csv.

Downloads PDFs, snapshots websites, clones repos (shallow), extracts basic text,
then produces a JSONL report assessing whether each download looks valid.
"""

import argparse
import base64
import csv
import hashlib
import json
import mimetypes
import os
import re
import shutil
import ssl
import http.cookiejar
from urllib.request import build_opener, HTTPCookieProcessor, HTTPSHandler
import subprocess
import sys
import time
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, parse_qs, quote, urljoin, unquote_to_bytes
from urllib.request import Request, urlopen

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

URL_RE = re.compile(r"https?://[^\s\)\]\"\'<]+")
S2_CACHE: Dict[str, Optional[dict]] = {}
S2_TITLE_CACHE: Dict[str, Optional[str]] = {}
OPENALEX_CACHE: Dict[str, Optional[dict]] = {}
WAYBACK_CACHE: Dict[str, Optional[dict]] = {}
COOKIE_JAR: Optional[http.cookiejar.MozillaCookieJar] = None
EXTRA_HEADERS: Dict[str, str] = {}
SKIP_IMAGES = False
TITLE_STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "into",
    "of",
    "on",
    "or",
    "the",
    "to",
    "through",
    "with",
}
TITLE_OA_DOMAINS = {
    "dl.acm.org",
    "www.sciencedirect.com",
    "ieeexplore.ieee.org",
    "link.springer.com",
    "onlinelibrary.wiley.com",
}
PAYWALLED_DOMAINS = {
    "dl.acm.org",
    "www.sciencedirect.com",
    "ieeexplore.ieee.org",
    "link.springer.com",
    "onlinelibrary.wiley.com",
}
INSECURE_SSL_HOSTS = {
    "www.cs.nmt.edu",
}
BLOCK_PATTERNS = [
    "access denied",
    "are you a robot",
    "captcha",
    "forbidden",
    "just a moment",
    "enable javascript",
    "enable cookies",
]
IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".tif",
    ".tiff",
    ".bmp",
    ".ppm",
    ".pgm",
    ".pbm",
}
OCR_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
    ".bmp",
    ".ppm",
    ".pgm",
    ".pbm",
}
MAX_IMAGE_BYTES = 20 * 1024 * 1024  # 20MB
MAX_DATA_IMAGE_BYTES = 10 * 1024 * 1024  # 10MB
MIN_OCR_BYTES = 30 * 1024  # Skip tiny icons/logos


@dataclass
class DownloadResult:
    status: str
    http_status: Optional[int]
    content_type: Optional[str]
    local_files: List[str]
    error: Optional[str]
    notes: Optional[str]


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts: List[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "noscript"}:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript"} and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._skip_depth == 0:
            text = data.strip()
            if text:
                self._parts.append(text)

    def get_text(self) -> str:
        return "\n".join(self._parts)


class ImageExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.images: List[str] = []
        self.base_href: Optional[str] = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = {k: v for k, v in attrs}
        if tag == "base" and attrs_dict.get("href"):
            self.base_href = attrs_dict["href"]
        if tag in {"img", "source"}:
            src = (
                attrs_dict.get("data-src")
                or attrs_dict.get("data-original")
                or attrs_dict.get("data-lazy")
                or attrs_dict.get("src")
            )
            if not src:
                srcset = attrs_dict.get("srcset") or attrs_dict.get("data-srcset")
                if srcset:
                    src = srcset.split(",")[0].strip().split(" ")[0]
            if src:
                self.images.append(src)

def unwrap_google_search(url: str) -> Optional[str]:
    parsed = urlparse(url)
    if parsed.netloc in {"www.google.com", "google.com"} and parsed.path == "/search":
        params = parse_qs(parsed.query)
        q = params.get("q", [None])[0]
        if q and q.startswith("http"):
            return q
    return None


def normalize_url(url: str) -> str:
    url = url.replace("\\&", "&")
    unwrapped = unwrap_google_search(url)
    if unwrapped:
        url = unwrapped
    return url.rstrip(").,;")


def encode_url(url: str) -> str:
    parsed = urlparse(url)
    path = quote(parsed.path, safe="/%")
    query = quote(parsed.query, safe="=&%")
    fragment = quote(parsed.fragment, safe="")
    rebuilt = f"{parsed.scheme}://{parsed.netloc}{path}"
    if query:
        rebuilt += f"?{query}"
    if fragment:
        rebuilt += f"#{fragment}"
    return rebuilt


def classify_url(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    if host in {"github.com", "gitlab.com", "bitbucket.org"}:
        return "repo"
    if re.search(r"\.pdf($|[?#])", url.lower()) or ".pdf" in path:
        return "pdf"
    return "website"


def safe_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        f.write(data)


def build_headers() -> Dict[str, str]:
    headers = {"User-Agent": USER_AGENT}
    headers.update(EXTRA_HEADERS)
    return headers


def build_opener_with_context(insecure: bool) -> Optional[object]:
    handlers = []
    if COOKIE_JAR is not None:
        handlers.append(HTTPCookieProcessor(COOKIE_JAR))
    if insecure:
        handlers.append(HTTPSHandler(context=ssl._create_unverified_context()))
    if handlers:
        return build_opener(*handlers)
    return None


def fetch_url(url: str, timeout: int = 30) -> Tuple[Optional[bytes], Optional[int], Optional[str], Optional[str]]:
    safe_url = encode_url(url)
    req = Request(safe_url, headers=build_headers())
    try:
        parsed = urlparse(safe_url)
        insecure = parsed.netloc.lower() in INSECURE_SSL_HOSTS and safe_url.startswith("https://")
        opener = build_opener_with_context(insecure)
        if opener is not None:
            resp = opener.open(req, timeout=timeout)
        else:
            resp = urlopen(req, timeout=timeout)
        with resp:
            content_type = resp.headers.get("Content-Type", "")
            data = resp.read()
            return data, resp.status, content_type, None
    except HTTPError as e:
        return None, e.code, None, f"HTTPError {e.code}"
    except URLError as e:
        return None, None, None, f"URLError {e.reason}"
    except Exception as e:
        return None, None, None, f"Error {e}"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def extract_html_text(html_bytes: bytes) -> str:
    extractor = TextExtractor()
    try:
        extractor.feed(html_bytes.decode("utf-8", errors="ignore"))
    except Exception:
        # Fallback: best-effort decode
        extractor.feed(html_bytes.decode("latin-1", errors="ignore"))
    text = extractor.get_text()
    # Collapse excessive blank lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def extract_html_images(html_bytes: bytes) -> Tuple[List[str], Optional[str]]:
    extractor = ImageExtractor()
    try:
        extractor.feed(html_bytes.decode("utf-8", errors="ignore"))
    except Exception:
        extractor.feed(html_bytes.decode("latin-1", errors="ignore"))
    return extractor.images, extractor.base_href


def guess_extension(url: str, content_type: Optional[str]) -> str:
    path_ext = Path(urlparse(url).path).suffix.lower()
    if path_ext in IMAGE_EXTENSIONS:
        return path_ext
    if content_type:
        ctype = content_type.split(";")[0].strip().lower()
        ext = mimetypes.guess_extension(ctype)
        if ext:
            return ext
    return ".bin"


def decode_data_url(data_url: str) -> Optional[Tuple[bytes, str]]:
    if not data_url.startswith("data:"):
        return None
    header, _, data = data_url.partition(",")
    if not data:
        return None
    header = header[5:]
    is_base64 = ";base64" in header
    mime = header.split(";")[0] if header else "application/octet-stream"
    try:
        if is_base64:
            raw = base64.b64decode(data)
        else:
            raw = unquote_to_bytes(data)
    except Exception:
        return None
    if len(raw) > MAX_DATA_IMAGE_BYTES:
        return None
    ext = mimetypes.guess_extension(mime) or ".bin"
    return raw, ext


def is_tesseract_available() -> bool:
    return shutil.which("tesseract") is not None


def run_tesseract(image_path: Path, txt_path: Path) -> Tuple[bool, Optional[str]]:
    try:
        subprocess.run(
            ["tesseract", str(image_path), str(txt_path.with_suffix("")), "-l", "eng"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True, None
    except subprocess.CalledProcessError as e:
        return False, e.stderr.decode("utf-8", errors="ignore")


def write_manifest(path: Path, entries: List[Dict[str, object]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(entries, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    return path

def has_pdf_header(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            head = f.read(1024)
        # Some PDFs include whitespace or BOM before the header.
        return b"%PDF" in head
    except Exception:
        return False


def extract_pdf_images(root: Path, item_id: str, pdf_path: Path) -> Tuple[List[str], Optional[str]]:
    if shutil.which("pdfimages") is None:
        return [], "pdfimages not available"

    out_dir = root / "sources" / "pdf_images" / item_id
    out_dir.mkdir(parents=True, exist_ok=True)

    if not any(out_dir.iterdir()):
        prefix = out_dir / "img"
        try:
            subprocess.run(
                ["pdfimages", "-all", str(pdf_path), str(prefix)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except subprocess.CalledProcessError as e:
            return [], e.stderr.decode("utf-8", errors="ignore")

    images = [p for p in out_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS]
    entries: List[Dict[str, object]] = []
    for img in images:
        entries.append({"file": img.name, "bytes": img.stat().st_size})

    local_files: List[str] = []
    if entries:
        manifest_path = write_manifest(out_dir / "manifest.json", entries)
        local_files.append(str(manifest_path.relative_to(root)))

    if is_tesseract_available() and entries:
        ocr_dir = root / "sources" / "pdf_image_text" / item_id
        ocr_dir.mkdir(parents=True, exist_ok=True)
        ocr_entries: List[Dict[str, object]] = []
        for img in images:
            if img.suffix.lower() not in OCR_EXTENSIONS:
                continue
            size = img.stat().st_size
            if size > MAX_IMAGE_BYTES or size < MIN_OCR_BYTES:
                continue
            txt_path = ocr_dir / f"{img.stem}.txt"
            if not txt_path.exists():
                ok, err = run_tesseract(img, txt_path)
                if not ok and err:
                    return local_files, f"tesseract failed: {err}"
            if txt_path.exists():
                ocr_entries.append({"file": txt_path.name, "bytes": txt_path.stat().st_size})
        if ocr_entries:
            ocr_manifest = write_manifest(ocr_dir / "manifest.json", ocr_entries)
            local_files.append(str(ocr_manifest.relative_to(root)))

    return local_files, None


def run_pdftotext(pdf_path: Path, txt_path: Path) -> Tuple[bool, Optional[str]]:
    if shutil.which("pdftotext") is None:
        return False, "pdftotext not available"
    try:
        subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), str(txt_path)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True, None
    except subprocess.CalledProcessError as e:
        return False, e.stderr.decode("utf-8", errors="ignore")


def clone_repo(url: str, dest: Path) -> Tuple[bool, Optional[str]]:
    if dest.exists():
        if (dest / ".git").exists():
            return True, None
        return False, "Destination exists but is not a git repo; remove to retry"
    try:
        result = subprocess.run(
            ["git", "clone", "--depth", "1", url, str(dest)],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode != 0:
            return False, result.stderr.decode("utf-8", errors="ignore")
        return True, None
    except Exception as e:
        return False, str(e)


def get_repo_commit(dest: Path) -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(dest), "rev-parse", "HEAD"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.stdout.decode("utf-8", errors="ignore").strip()
    except Exception:
        return None


def load_sources(csv_path: Path) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("url"):
                continue
            row["url"] = normalize_url(row["url"])
            rows.append(row)
    return rows


def write_index_files(root: Path, rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    index_csv = root / "index.csv"
    index_jsonl = root / "index.jsonl"

    enriched: List[Dict[str, str]] = []
    for i, row in enumerate(rows, 1):
        item = dict(row)
        item["id"] = f"CC{i:03d}"
        if not item.get("type"):
            item["type"] = classify_url(item["url"])
        enriched.append(item)

    # CSV
    with index_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "url", "type", "sources"])
        for item in enriched:
            writer.writerow([item["id"], item["url"], item.get("type", ""), item.get("sources", "")])

    # JSONL
    with index_jsonl.open("w", encoding="utf-8") as f:
        for item in enriched:
            f.write(json.dumps(item, ensure_ascii=True) + "\n")

    return enriched


def extract_title_from_line(line: str) -> Optional[str]:
    cleaned = line.strip()
    if not cleaned:
        return None
    # Remove URLs and markdown noise.
    cleaned = URL_RE.sub("", cleaned)
    cleaned = re.sub(r"^[-*•\d\.\)\s]+", "", cleaned)
    cleaned = cleaned.replace("URL:", "").replace("Pdf:", "").replace("PDF:", "")
    cleaned = cleaned.replace("**", "").replace("__", "")
    cleaned = cleaned.strip()
    if not cleaned:
        return None
    quoted = re.findall(r"[\"“](.+?)[\"”]", cleaned)
    if quoted:
        return max(quoted, key=len).strip()
    cleaned = cleaned.strip(" -–—:")
    if len(cleaned) < 5:
        return None
    return cleaned


def title_tokens(title: str) -> List[str]:
    cleaned = re.sub(r"[^a-z0-9 ]", " ", title.lower())
    tokens = [t for t in cleaned.split() if t and t not in TITLE_STOPWORDS]
    return tokens


def titles_match(a: str, b: str) -> bool:
    if not a or not b:
        return False
    a_clean = re.sub(r"[^a-z0-9 ]", " ", a.lower()).strip()
    b_clean = re.sub(r"[^a-z0-9 ]", " ", b.lower()).strip()
    if a_clean in b_clean or b_clean in a_clean:
        return True
    a_tokens = set(title_tokens(a))
    b_tokens = set(title_tokens(b))
    if not a_tokens or not b_tokens:
        return False
    overlap = len(a_tokens & b_tokens) / max(len(a_tokens), len(b_tokens))
    return overlap >= 0.6


def is_bad_title(title: Optional[str]) -> bool:
    if not title:
        return True
    if re.fullmatch(r"\\[\\^\\d+\\]", title.strip()):
        return True
    tokens = title_tokens(title)
    return len(tokens) < 2


def build_title_index(source_paths: List[Path]) -> Dict[str, str]:
    title_index: Dict[str, str] = {}
    for path in source_paths:
        if not path.exists():
            continue
        prev_line = ""
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            urls = URL_RE.findall(line)
            if urls:
                for raw_url in urls:
                    url = normalize_url(raw_url)
                    title = extract_title_from_line(line) or extract_title_from_line(prev_line)
                    if not title:
                        continue
                    if url not in title_index:
                        title_index[url] = title
                    else:
                        existing = title_index[url]
                        if is_bad_title(existing) and not is_bad_title(title):
                            title_index[url] = title
            if line.strip():
                prev_line = line.strip()
    return title_index


def extract_doi(url: str) -> Optional[str]:
    parsed = urlparse(url)
    match = re.search(r"/doi/(10\.[^/]+/.+)$", parsed.path)
    if match:
        return match.group(1)
    return None


def extract_pii(url: str) -> Optional[str]:
    match = re.search(r"/pii/([A-Za-z0-9]+)", url)
    if match:
        return match.group(1)
    return None


def s2_get_json(url: str) -> Optional[dict]:
    if url in S2_CACHE:
        return S2_CACHE[url]
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            S2_CACHE[url] = data
            return data
    except Exception:
        S2_CACHE[url] = None
        return None


def openalex_get_json(url: str) -> Optional[dict]:
    if url in OPENALEX_CACHE:
        return OPENALEX_CACHE[url]
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            OPENALEX_CACHE[url] = data
            return data
    except Exception:
        OPENALEX_CACHE[url] = None
        return None


def wayback_get_json(url: str) -> Optional[dict]:
    if url in WAYBACK_CACHE:
        return WAYBACK_CACHE[url]
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            WAYBACK_CACHE[url] = data
            return data
    except Exception:
        WAYBACK_CACHE[url] = None
        return None


def wayback_snapshot_url(url: str) -> Optional[str]:
    api = "https://archive.org/wayback/available?url=" + quote(url)
    data = wayback_get_json(api)
    if not data:
        return None
    closest = (data.get("archived_snapshots") or {}).get("closest") or {}
    return closest.get("url")


def load_extra_headers(headers_path: Optional[Path]) -> None:
    global EXTRA_HEADERS
    if headers_path is None or not headers_path.exists():
        return
    try:
        data = json.loads(headers_path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            EXTRA_HEADERS.update({str(k): str(v) for k, v in data.items()})
    except Exception:
        return


def load_cookiejar(cookie_path: Optional[Path]) -> None:
    global COOKIE_JAR
    if cookie_path is None or not cookie_path.exists():
        return
    jar = http.cookiejar.MozillaCookieJar()
    try:
        jar.load(cookie_path, ignore_discard=True, ignore_expires=True)
        COOKIE_JAR = jar
    except Exception:
        COOKIE_JAR = None


def openalex_oa_by_doi(doi: str) -> Optional[str]:
    api = "https://api.openalex.org/works/https://doi.org/" + quote(doi)
    data = openalex_get_json(api)
    if not data:
        return None
    best = data.get("best_oa_location") or {}
    if best.get("url"):
        return best["url"]
    for loc in data.get("oa_locations") or []:
        if loc.get("url"):
            return loc["url"]
    return None


def openalex_oa_by_title(title: str) -> Optional[str]:
    if is_bad_title(title):
        return None
    api = "https://api.openalex.org/works?search=" + quote(title) + "&per-page=5"
    data = openalex_get_json(api)
    if not data:
        return None
    for item in data.get("results") or []:
        item_title = item.get("title") or ""
        if not titles_match(title, item_title):
            continue
        best = item.get("best_oa_location") or {}
        if best.get("url"):
            return best["url"]
        for loc in item.get("oa_locations") or []:
            if loc.get("url"):
                return loc["url"]
    return None


def semantic_scholar_open_access_by_doi(doi: str) -> Optional[str]:
    api = (
        "https://api.semanticscholar.org/graph/v1/paper/DOI:"
        + quote(doi)
        + "?fields=title,openAccessPdf"
    )
    data = s2_get_json(api)
    if not data:
        return None
    oa = data.get("openAccessPdf") or {}
    return oa.get("url") or None


def semantic_scholar_open_access_by_title(title: str) -> Optional[str]:
    if is_bad_title(title):
        return None
    if title in S2_TITLE_CACHE:
        return S2_TITLE_CACHE[title]
    api = (
        "https://api.semanticscholar.org/graph/v1/paper/search?query="
        + quote(title)
        + "&limit=5&fields=title,openAccessPdf"
    )
    data = s2_get_json(api)
    if not data:
        S2_TITLE_CACHE[title] = None
        return None
    for item in data.get("data") or []:
        item_title = item.get("title") or ""
        if not titles_match(title, item_title):
            continue
        oa = item.get("openAccessPdf") or {}
        if oa.get("url"):
            S2_TITLE_CACHE[title] = oa["url"]
            return oa["url"]
    S2_TITLE_CACHE[title] = None
    return None


def semantic_scholar_title_by_doi(doi: str) -> Optional[str]:
    api = (
        "https://api.semanticscholar.org/graph/v1/paper/DOI:"
        + quote(doi)
        + "?fields=title"
    )
    data = s2_get_json(api)
    if not data:
        return None
    return data.get("title")


def normalize_to_pdf_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc.lower() == "arxiv.org" and parsed.path.startswith("/abs/"):
        paper_id = parsed.path.replace("/abs/", "").strip("/")
        return f"https://arxiv.org/pdf/{paper_id}.pdf"
    return url


def local_mirror_candidates(title: str, title_index: Dict[str, str]) -> List[str]:
    candidates: List[str] = []
    if is_bad_title(title):
        return candidates
    for url, hint in title_index.items():
        if titles_match(title, hint):
            normalized = normalize_to_pdf_url(url)
            if not normalized.lower().endswith(".pdf"):
                continue
            host = urlparse(normalized).netloc.lower()
            if host in PAYWALLED_DOMAINS:
                continue
            candidates.append(normalized)
    return candidates


def pii_mirror_candidates(pii: str, all_urls: List[str]) -> List[str]:
    candidates: List[str] = []
    for url in all_urls:
        if pii in url and url.lower().endswith(".pdf"):
            candidates.append(url)
    return candidates


def load_overrides(overrides_path: Optional[Path]) -> Dict[str, List[str]]:
    overrides: Dict[str, List[str]] = {}
    if overrides_path is None or not overrides_path.exists():
        return overrides
    try:
        with overrides_path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = normalize_url(row.get("url", "").strip())
                mirror = normalize_url(row.get("mirror_url", "").strip())
                if url and mirror:
                    overrides.setdefault(url, []).append(mirror)
    except Exception:
        return overrides
    return overrides


def jina_mirror(url: str) -> Optional[str]:
    if url.startswith("https://"):
        return "https://r.jina.ai/https://" + url[len("https://") :]
    if url.startswith("http://"):
        return "https://r.jina.ai/http://" + url[len("http://") :]
    return None


def mirror_candidates(
    url: str,
    title_hint: Optional[str],
    title_index: Dict[str, str],
    all_urls: List[str],
    overrides: Dict[str, List[str]],
) -> List[str]:
    candidates: List[str] = []
    if url in overrides:
        candidates.extend(overrides[url])
    unwrapped = unwrap_google_search(url)
    if unwrapped and unwrapped != url:
        candidates.append(unwrapped)

    doi = extract_doi(url)
    if doi:
        oa = semantic_scholar_open_access_by_doi(doi)
        if oa:
            candidates.append(normalize_to_pdf_url(oa))
        oa = openalex_oa_by_doi(doi)
        if oa:
            candidates.append(normalize_to_pdf_url(oa))
        doi_title = semantic_scholar_title_by_doi(doi)
        if doi_title:
            candidates.extend(local_mirror_candidates(doi_title, title_index))

    pii = extract_pii(url)
    if pii:
        candidates.extend(pii_mirror_candidates(pii, all_urls))

    if title_hint and not is_bad_title(title_hint) and urlparse(url).netloc.lower() in TITLE_OA_DOMAINS:
        oa = semantic_scholar_open_access_by_title(title_hint)
        if oa:
            candidates.append(normalize_to_pdf_url(oa))
        oa = openalex_oa_by_title(title_hint)
        if oa:
            candidates.append(normalize_to_pdf_url(oa))
        candidates.extend(local_mirror_candidates(title_hint, title_index))

    if url.startswith("https://www.cs.nmt.edu"):
        candidates.append(url.replace("https://", "http://", 1))
    if url.startswith("https://www.codemr.co.uk"):
        candidates.append(url.replace("https://", "http://", 1))
        candidates.append(url.replace("https://www.", "https://", 1))
    if url == "https://www.explorviz.net/":
        candidates.append("https://explorviz.dev/1-about/")
    if "https://www.inf.usi.ch/lanza/Downloads/" in url:
        filename = urlparse(url).path.split("/")[-1]
        candidates.append(f"https://wettel.github.io/download/{filename}")
        if filename.lower() == "wett2007a.pdf":
            candidates.append("https://wettel.github.io/download/Wettel07a-icpc.pdf")
    if url.endswith("/software-visualization.html") and "inf.usi.ch" in url:
        candidates.append("https://www.inf.usi.ch/en/faculty/lanza/software-visualization.html")
        candidates.append("https://www.inf.usi.ch/en/organization/faculty/lanza/software-visualization.html")

    jina = jina_mirror(url)
    if jina:
        candidates.append(jina)

    wb = wayback_snapshot_url(url)
    if wb:
        candidates.append(wb)

    # De-duplicate while preserving order
    seen = set()
    unique: List[str] = []
    for c in candidates:
        if not c or c == url:
            continue
        if c not in seen:
            seen.add(c)
            unique.append(c)
    return unique


def is_pdf_payload(data: bytes, url: str, content_type: Optional[str]) -> bool:
    if content_type and "pdf" in content_type.lower():
        return True
    if url.lower().endswith(".pdf"):
        return True
    return b"%PDF" in data[:1024]


def looks_like_block_page(text: str) -> bool:
    lowered = text.lower()
    if len(lowered) > 5000:
        return False
    return any(pat in lowered for pat in BLOCK_PATTERNS)


def repo_clone_url(url: str) -> Optional[str]:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    if host not in {"github.com", "gitlab.com", "bitbucket.org"}:
        return None
    segments = [seg for seg in parsed.path.split("/") if seg]
    if len(segments) < 2:
        return None
    return f"{parsed.scheme}://{parsed.netloc}/{segments[0]}/{segments[1]}"


def ensure_sha(path: Path) -> Optional[Path]:
    if not path.exists():
        return None
    sha_path = path.with_suffix(path.suffix + ".sha256")
    if sha_path.exists():
        return sha_path
    data = path.read_bytes()
    sha_path.write_text(sha256_bytes(data) + "\n", encoding="utf-8")
    return sha_path


def download_web(
    root: Path,
    item_id: str,
    url: str,
    title_hint: Optional[str],
    title_index: Dict[str, str],
    all_urls: List[str],
    overrides: Dict[str, List[str]],
) -> DownloadResult:
    html_path = root / "sources" / "web" / "html" / f"{item_id}.html"
    text_path = root / "sources" / "web" / "text" / f"{item_id}.txt"
    local_files: List[str] = []

    if not html_path.exists():
        data, status, content_type, error = fetch_url(url)
        if data is None:
            mirror_result = attempt_mirror_download(
                root, item_id, url, title_hint, title_index, all_urls, overrides
            )
            if mirror_result:
                return mirror_result
            return DownloadResult("error", status, content_type, [], error, None)
        safe_write(html_path, data)
        local_files.append(str(html_path.relative_to(root)))
        sha_path = ensure_sha(html_path)
        if sha_path is not None:
            local_files.append(str(sha_path.relative_to(root)))
    else:
        status = None
        content_type = None
        error = None
        local_files.append(str(html_path.relative_to(root)))
        sha_path = ensure_sha(html_path)
        if sha_path is not None:
            local_files.append(str(sha_path.relative_to(root)))

    html_bytes: Optional[bytes] = None
    if html_path.exists():
        try:
            html_bytes = html_path.read_bytes()
            if not text_path.exists():
                text = extract_html_text(html_bytes)
                text_path.write_text(text + "\n", encoding="utf-8")
                local_files.append(str(text_path.relative_to(root)))
        except Exception as e:
            error = (error or "") + f"; text_extract_failed: {e}"
    if text_path.exists():
        local_files.append(str(text_path.relative_to(root)))

    if html_bytes:
        if not SKIP_IMAGES:
            img_files, img_err = download_web_images(root, item_id, url, html_bytes)
            local_files.extend(img_files)
            if img_err:
                error = (error or "") + f"; web_image_extract_failed: {img_err}"

    ok = html_path.exists() and html_path.stat().st_size > 0
    status_str = "ok" if ok else "suspect"
    notes = None if ok else "HTML missing or empty"
    return DownloadResult(status_str, status, content_type, local_files, error, notes)


def attempt_mirror_download(
    root: Path,
    item_id: str,
    url: str,
    title_hint: Optional[str],
    title_index: Dict[str, str],
    all_urls: List[str],
    overrides: Dict[str, List[str]],
) -> Optional[DownloadResult]:
    require_pdf = urlparse(url).netloc.lower() in PAYWALLED_DOMAINS or extract_doi(url) is not None
    for mirror_url in mirror_candidates(url, title_hint, title_index, all_urls, overrides):
        data, status, content_type, error = fetch_url(mirror_url)
        if data is None:
            continue

        if is_pdf_payload(data, mirror_url, content_type):
            pdf_path = root / "sources" / "pdf" / f"{item_id}_mirror.pdf"
            safe_write(pdf_path, data)
            local_files = [str(pdf_path.relative_to(root))]
            sha_path = ensure_sha(pdf_path)
            if sha_path is not None:
                local_files.append(str(sha_path.relative_to(root)))

            txt_path = root / "sources" / "pdf_text" / f"{item_id}_mirror.txt"
            ok_text, err = run_pdftotext(pdf_path, txt_path)
            if ok_text and txt_path.exists():
                local_files.append(str(txt_path.relative_to(root)))
            elif err:
                error = (error or "") + f"; text_extract_failed: {err}"

            if not SKIP_IMAGES:
                img_files, img_err = extract_pdf_images(root, f"{item_id}_mirror", pdf_path)
                local_files.extend(img_files)
                if img_err:
                    error = (error or "") + f"; pdf_image_extract_failed: {img_err}"

            note = f"Mirrored from {mirror_url}"
            return DownloadResult("ok", status, content_type, local_files, error, note)

        if require_pdf and "web.archive.org" not in mirror_url:
            continue

        text = extract_html_text(data)
        if looks_like_block_page(text):
            continue

        html_path = root / "sources" / "web" / "html" / f"{item_id}_mirror.html"
        safe_write(html_path, data)
        local_files = [str(html_path.relative_to(root))]
        sha_path = ensure_sha(html_path)
        if sha_path is not None:
            local_files.append(str(sha_path.relative_to(root)))

        text_path = root / "sources" / "web" / "text" / f"{item_id}_mirror.txt"
        try:
            text_path.write_text(text + "\n", encoding="utf-8")
            local_files.append(str(text_path.relative_to(root)))
        except Exception as e:
            error = (error or "") + f"; text_extract_failed: {e}"

        if not SKIP_IMAGES:
            img_files, img_err = download_web_images(root, f"{item_id}_mirror", mirror_url, data)
            local_files.extend(img_files)
            if img_err:
                error = (error or "") + f"; web_image_extract_failed: {img_err}"

        note = f"Mirrored from {mirror_url}"
        return DownloadResult("ok", status, content_type, local_files, error, note)

    return None


def download_web_images(
    root: Path,
    item_id: str,
    page_url: str,
    html_bytes: bytes,
) -> Tuple[List[str], Optional[str]]:
    images, base_href = extract_html_images(html_bytes)
    if not images:
        return [], None

    base_url = base_href or page_url
    out_dir = root / "sources" / "web" / "images" / item_id
    out_dir.mkdir(parents=True, exist_ok=True)
    entries: List[Dict[str, object]] = []
    errors: List[str] = []
    seen: set = set()

    for idx, src in enumerate(images, 1):
        if not src or src in seen:
            continue
        seen.add(src)

        if src.startswith("data:"):
            decoded = decode_data_url(src)
            if not decoded:
                continue
            data, ext = decoded
            if len(data) > MAX_IMAGE_BYTES:
                continue
            filename = f"img_{idx:04d}{ext}"
            img_path = out_dir / filename
            if not img_path.exists():
                safe_write(img_path, data)
            entries.append({"file": filename, "source": "data:url"})
            continue

        full_url = urljoin(base_url, src)
        parsed = urlparse(full_url)
        if parsed.scheme not in {"http", "https"}:
            continue
        data, status, content_type, error = fetch_url(full_url)
        if data is None:
            if error:
                errors.append(error)
            continue
        if len(data) > MAX_IMAGE_BYTES:
            continue
        ext = guess_extension(full_url, content_type)
        filename = f"img_{idx:04d}{ext}"
        img_path = out_dir / filename
        if not img_path.exists():
            safe_write(img_path, data)
        entries.append({"file": filename, "source": full_url})

    local_files: List[str] = []
    if entries:
        manifest_path = write_manifest(out_dir / "manifest.json", entries)
        local_files.append(str(manifest_path.relative_to(root)))

    if is_tesseract_available() and entries:
        ocr_dir = root / "sources" / "web" / "image_text" / item_id
        ocr_dir.mkdir(parents=True, exist_ok=True)
        ocr_entries: List[Dict[str, object]] = []
        for entry in entries:
            file_name = entry["file"]
            img_path = out_dir / file_name
            if img_path.suffix.lower() not in OCR_EXTENSIONS:
                continue
            size = img_path.stat().st_size
            if size > MAX_IMAGE_BYTES or size < MIN_OCR_BYTES:
                continue
            txt_path = ocr_dir / f"{img_path.stem}.txt"
            if not txt_path.exists():
                ok, err = run_tesseract(img_path, txt_path)
                if not ok and err:
                    errors.append(err)
                    continue
            if txt_path.exists():
                ocr_entries.append({"file": txt_path.name, "bytes": txt_path.stat().st_size})
        if ocr_entries:
            ocr_manifest = write_manifest(ocr_dir / "manifest.json", ocr_entries)
            local_files.append(str(ocr_manifest.relative_to(root)))

    if errors:
        return local_files, "; ".join(errors[:3])
    return local_files, None


def scan_repo_images(root: Path, item_id: str, repo_path: Path) -> Tuple[List[str], Optional[str]]:
    if not repo_path.exists():
        return [], "repo path missing"

    skip_dirs = {
        ".git",
        "node_modules",
        "vendor",
        "dist",
        "build",
        ".next",
        ".cache",
    }
    images: List[Path] = []
    for root_dir, dirnames, filenames in os.walk(repo_path):
        # Prune heavy directories
        dirnames[:] = [d for d in dirnames if d not in skip_dirs and d != ".git"]
        for filename in filenames:
            if Path(filename).suffix.lower() in IMAGE_EXTENSIONS:
                path = Path(root_dir) / filename
                images.append(path)

    if not images:
        return [], None

    entries: List[Dict[str, object]] = []
    for img in images:
        try:
            rel = img.relative_to(repo_path).as_posix()
        except Exception:
            rel = str(img)
        entries.append({"file": rel, "bytes": img.stat().st_size})

    manifest_path = repo_path / "_images.json"
    write_manifest(manifest_path, entries)

    local_files = [str(manifest_path.relative_to(root))]

    if is_tesseract_available():
        ocr_dir = root / "sources" / "repo_image_text" / item_id
        ocr_dir.mkdir(parents=True, exist_ok=True)
        ocr_entries: List[Dict[str, object]] = []
        for img in images:
            if img.suffix.lower() not in OCR_EXTENSIONS:
                continue
            size = img.stat().st_size
            if size > MAX_IMAGE_BYTES or size < MIN_OCR_BYTES:
                continue
            txt_path = ocr_dir / (img.stem + ".txt")
            if not txt_path.exists():
                ok, err = run_tesseract(img, txt_path)
                if not ok and err:
                    return local_files, f"tesseract failed: {err}"
            if txt_path.exists():
                ocr_entries.append({"file": txt_path.name, "bytes": txt_path.stat().st_size})
        if ocr_entries:
            ocr_manifest = write_manifest(ocr_dir / "manifest.json", ocr_entries)
            local_files.append(str(ocr_manifest.relative_to(root)))

    return local_files, None


def download_item(
    root: Path,
    item: Dict[str, str],
    title_index: Dict[str, str],
    all_urls: List[str],
    overrides: Dict[str, List[str]],
) -> DownloadResult:
    url = item["url"]
    item_type = item.get("type") or classify_url(url)
    item_id = item["id"]
    title_hint = title_index.get(url)

    local_files: List[str] = []

    if item_type == "pdf":
        pdf_path = root / "sources" / "pdf" / f"{item_id}.pdf"
        if not pdf_path.exists():
            data, status, content_type, error = fetch_url(url)
            if data is None:
                mirror_result = attempt_mirror_download(
                    root, item_id, url, title_hint, title_index, all_urls, overrides
                )
                if mirror_result:
                    return mirror_result
                return DownloadResult("error", status, content_type, [], error, None)
            safe_write(pdf_path, data)
            local_files.append(str(pdf_path.relative_to(root)))
            sha_path = ensure_sha(pdf_path)
            if sha_path is not None:
                local_files.append(str(sha_path.relative_to(root)))
        else:
            status = None
            content_type = None
            error = None
            local_files.append(str(pdf_path.relative_to(root)))
            sha_path = ensure_sha(pdf_path)
            if sha_path is not None:
                local_files.append(str(sha_path.relative_to(root)))
        # Validate
        ok = pdf_path.exists() and pdf_path.stat().st_size > 0 and has_pdf_header(pdf_path)
        # Extract text
        txt_path = root / "sources" / "pdf_text" / f"{item_id}.txt"
        if not txt_path.exists() and pdf_path.exists():
            ok_text, err = run_pdftotext(pdf_path, txt_path)
            if ok_text:
                local_files.append(str(txt_path.relative_to(root)))
            else:
                if err:
                    error = (error or "") + f"; text_extract_failed: {err}"
        if txt_path.exists():
            local_files.append(str(txt_path.relative_to(root)))
        if ok:
            if not SKIP_IMAGES:
                img_files, img_err = extract_pdf_images(root, item_id, pdf_path)
                local_files.extend(img_files)
                if img_err:
                    error = (error or "") + f"; pdf_image_extract_failed: {img_err}"
        if not ok:
            mirror_result = attempt_mirror_download(
                root, item_id, url, title_hint, title_index, all_urls, overrides
            )
            if mirror_result:
                return mirror_result
        status_str = "ok" if ok else "suspect"
        notes = None
        if not ok:
            notes = "PDF header missing or file empty"
        return DownloadResult(status_str, status, content_type, local_files, error, notes)

    if item_type == "repo":
        clone_url = repo_clone_url(url)
        if clone_url is None:
            web_result = download_web(
                root, item_id, url, title_hint, title_index, all_urls, overrides
            )
            note = "Not a cloneable repo URL; saved HTML snapshot instead"
            status_str = "suspect" if web_result.status == "ok" else web_result.status
            return DownloadResult(
                status_str,
                web_result.http_status,
                web_result.content_type,
                web_result.local_files,
                web_result.error,
                note,
            )

        repo_path = root / "sources" / "repo" / item_id
        ok, err = clone_repo(clone_url, repo_path)
        local_files.append(str(repo_path.relative_to(root)))
        commit = get_repo_commit(repo_path) if ok else None
        if commit:
            commit_path = repo_path / "_commit.txt"
            commit_path.write_text(commit + "\n", encoding="utf-8")
            local_files.append(str(commit_path.relative_to(root)))
        if not SKIP_IMAGES:
            img_files, img_err = scan_repo_images(root, item_id, repo_path)
            local_files.extend(img_files)
            if img_err:
                err = (err or "") + f"; repo_image_scan_failed: {img_err}"
        status_str = "ok" if ok and commit else "suspect"
        notes = None if status_str == "ok" else "Repo clone failed or commit missing"
        if clone_url != url:
            notes = (notes or "") + "; cloned base repo URL"
        if err and "git-lfs" in err.lower():
            notes = (notes or "") + "; git-lfs required for full checkout"
        return DownloadResult(status_str, None, None, local_files, err, notes)

    # website
    return download_web(root, item_id, url, title_hint, title_index, all_urls, overrides)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default=None,
        help="Path to CodeCity_sources.csv (default: repo root/CodeCity_sources.csv)",
    )
    parser.add_argument(
        "--root",
        default=None,
        help="Library root directory (default: bibliography)",
    )
    parser.add_argument(
        "--cookie-file",
        default=None,
        help="Path to Netscape cookie file for authenticated downloads",
    )
    parser.add_argument(
        "--headers-file",
        default=None,
        help="Path to JSON file of extra HTTP headers",
    )
    parser.add_argument(
        "--overrides",
        default=None,
        help="Path to overrides CSV (url,mirror_url)",
    )
    parser.add_argument("--sleep", type=float, default=0.2, help="Seconds to sleep between HTTP fetches")
    parser.add_argument(
        "--skip-images",
        action="store_true",
        help="Skip downloading/extracting images and OCR (saves disk and time).",
    )
    args = parser.parse_args()

    global SKIP_IMAGES
    SKIP_IMAGES = bool(args.skip_images)

    script_path = Path(__file__).resolve()
    default_root = script_path.parents[1]
    default_input = script_path.parents[2] / "CodeCity_sources.csv"

    root = Path(args.root) if args.root else default_root
    input_csv = Path(args.input) if args.input else default_input
    overrides_path = Path(args.overrides) if args.overrides else (root / "overrides.csv")
    headers_path = Path(args.headers_file) if args.headers_file else (root / "headers.json")
    cookie_path = Path(args.cookie_file) if args.cookie_file else (root / "cookies.txt")

    root.mkdir(parents=True, exist_ok=True)

    load_extra_headers(headers_path)
    load_cookiejar(cookie_path)

    rows = load_sources(input_csv)
    items = write_index_files(root, rows)
    all_urls = [item["url"] for item in items]
    source_root = script_path.parents[2]
    title_index = build_title_index(
        [source_root / f"CodeCity_{i}.md" for i in range(1, 5)]
    )
    overrides = load_overrides(overrides_path)

    report_path = root / "reports" / "download_report.jsonl"
    report_md_path = root / "reports" / "download_report.md"

    ok_count = 0
    suspect_count = 0
    error_count = 0

    report_lines = []
    report_lines.append("# Download report")
    report_lines.append("")
    report_lines.append(f"Input: {input_csv}")
    report_lines.append(f"Total items: {len(items)}")
    report_lines.append("")
    report_lines.append("| ID | Type | Status | URL | Notes |")
    report_lines.append("|---|---|---|---|---|")

    with report_path.open("w", encoding="utf-8") as rf:
        for idx, item in enumerate(items, 1):
            result = download_item(root, item, title_index, all_urls, overrides)
            record = {
                "id": item["id"],
                "url": item["url"],
                "type": item.get("type"),
                "status": result.status,
                "http_status": result.http_status,
                "content_type": result.content_type,
                "local_files": result.local_files,
                "error": result.error,
                "notes": result.notes,
            }
            rf.write(json.dumps(record, ensure_ascii=True) + "\n")

            if result.status == "ok":
                ok_count += 1
            elif result.status == "suspect":
                suspect_count += 1
            else:
                error_count += 1

            note = result.notes or result.error or ""
            report_lines.append(
                f"| {item['id']} | {item.get('type')} | {result.status} | {item['url']} | {note.replace('|',' ')} |"
            )

            # polite delay only for HTTP/HTTPS items (pdf/web)
            if item.get("type") != "repo":
                time.sleep(args.sleep)

    report_lines.append("")
    report_lines.append(f"OK: {ok_count} | Suspect: {suspect_count} | Error: {error_count}")

    report_md_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"Done. OK={ok_count} Suspect={suspect_count} Error={error_count}")
    print(f"Report: {report_md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
