# 00 — Build a Local (LLM‑Ready) Bibliography From Source Lists

> **Purpose**: turn a set of “source list” files (research notes containing URLs) into a **local, LLM‑friendly bibliography library**: downloaded artifacts + extracted text + extracted images + OCR + a single `llm_index.jsonl` that points to everything.
>
> This is the **ingestion** phase. The **knowledge extraction / documentation** phase happens after this, using the downloaded library as the source of truth.

---

## What You Start With (Inputs)

### 1) “Source list” files (your research context)

Create a folder (name doesn’t matter) and put **all** research notes in it (Markdown recommended):

```
inputs/
  01_notes.md
  02_links.md
  03_papers.md
  04_tools.md
```

Rules:
- These files are treated as **full context** for the bibliography.
- Do **not** delete or rewrite them during ingestion; they are the provenance trail.
- URLs can appear anywhere in the text as `https://…` or `http://…`.

### 2) Canonical URL inventory (generated): `sources.csv`

From the input files we generate a canonical list:

```csv
url,type,sources
https://example.org/paper.pdf,pdf,inputs/01_notes.md;inputs/03_papers.md
https://github.com/org/repo,repo,inputs/04_tools.md
https://example.org/blog,website,inputs/02_links.md
```

Fields:
- `url`: absolute URL (deduped + normalized)
- `type`: `pdf` | `website` | `repo` (heuristic; fixable)
- `sources`: which input files mentioned the URL (keep this!)

---

## What You Produce (Outputs)

Create a **library root** directory for this topic (one library per topic):

```
bibliography_<topic>/
  index.csv
  index.jsonl
  llm_index.jsonl
  overrides.csv
  headers.json
  cookies.txt            # optional
  reports/
    download_report.md
    download_report.jsonl
  sources/
    pdf/
    pdf_text/
    pdf_images/
    pdf_image_text/
    web/
      html/
      text/
      images/
      image_text/
    repo/
    repo_image_text/
```

### The single entrypoint for an LLM

`llm_index.jsonl` (one JSON object per source ID) points to:
- text files to embed / chunk
- image manifests + OCR manifests
- repo locations
- download status (`ok` / `suspect` / `error`)

---

## Step‑By‑Step Pipeline (Repeatable)

### Step 0 — Choose names

Pick:
- `TOPIC_SLUG` (e.g. `software-city-metaphor`)
- `LIB_ROOT` (e.g. `bibliography_software-city-metaphor`)

```bash
export TOPIC_SLUG="your-topic"
export LIB_ROOT="bibliography_${TOPIC_SLUG}"
```

### Step 1 — (Optional) Merge inputs into a single “frozen context” file

This keeps a verbatim, timestampable snapshot of everything you started from.

```bash
python - <<'PY'
from pathlib import Path
import datetime

inputs_dir = Path("inputs")
out = Path("inputs_merged.md")

parts = []
parts.append(f"# Merged input context ({datetime.date.today().isoformat()})\\n")
for p in sorted(inputs_dir.glob("**/*")):
    if p.is_file() and p.suffix.lower() in {".md", ".txt"}:
        parts.append(f"## {p.as_posix()}\\n")
        parts.append(p.read_text(encoding="utf-8", errors="ignore").rstrip() + "\\n")

out.write_text("\\n".join(parts) + "\\n", encoding="utf-8")
print("wrote", out)
PY
```

### Step 2 — Extract + dedupe URLs into `sources.csv`

Run from repo root (edit `INPUTS_DIR` and `OUT`):

```bash
python - <<'PY'
import re, csv
from pathlib import Path
from urllib.parse import urlparse, parse_qs

INPUTS_DIR = Path("inputs")
OUT = Path("sources.csv")
url_re = re.compile(r"https?://[^\\s\\)\\]\"\\'<]+")

def unwrap_google(u: str) -> str:
    p = urlparse(u)
    if p.netloc in {"google.com", "www.google.com"} and p.path == "/search":
        q = parse_qs(p.query).get("q", [None])[0]
        if q and q.startswith("http"):
            return q
    return u

def normalize(u: str) -> str:
    u = u.replace("\\\\&", "&").rstrip(").,;")
    return unwrap_google(u)

def classify(u: str) -> str:
    host = urlparse(u).netloc.lower()
    path = urlparse(u).path.lower()
    if host in {"github.com", "gitlab.com", "bitbucket.org"}:
        return "repo"
    if path.endswith(".pdf") or ".pdf" in path:
        return "pdf"
    return "website"

seen = {}
for p in sorted(INPUTS_DIR.glob("**/*")):
    if not (p.is_file() and p.suffix.lower() in {".md", ".txt"}):
        continue
    text = p.read_text(encoding="utf-8", errors="ignore")
    for raw in url_re.findall(text):
        url = normalize(raw)
        seen.setdefault(url, set()).add(p.as_posix())

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["url", "type", "sources"])
    for url in seen:
        w.writerow([url, classify(url), ";".join(sorted(seen[url]))])

print("wrote", OUT, "unique_urls", len(seen))
PY
```

### Step 3 — Initialize the library root + repair inputs

```bash
mkdir -p "$LIB_ROOT"
printf "url,mirror_url\\n" > "$LIB_ROOT/overrides.csv"
printf "{}\\n" > "$LIB_ROOT/headers.json"
# Optional (only if you have legitimate access): export cookies in Netscape format:
#   $LIB_ROOT/cookies.txt
```

### Step 4 — Install extraction dependencies

To get full fidelity (text + images + OCR), you need:
- `pdftotext` and `pdfimages` (Poppler)
- `tesseract` (OCR)
- `git`

macOS:
```bash
brew install poppler tesseract
```

### Step 5 — Build the bibliography library (download + extract)

Run the build script from your repo. The script should:
- read `sources.csv`
- download PDFs / web pages / repos
- extract text from PDF + HTML
- extract images from PDFs + HTML + repos
- OCR extracted images (best effort)
- write `reports/download_report.md` + `reports/download_report.jsonl`

Example command shape:

```bash
python bibliography/scripts/build_codecity_library.py \
  --input sources.csv \
  --root "$LIB_ROOT"
```

Notes:
- The build script name/path is repo-specific. In a new codebase, keep the same interface: `--input` and `--root`.
- The run is **incremental**: rerunning should reuse existing downloads and only fill missing parts.

---

## Validation: “Did We Download the Right Things?”

This is mandatory. The pipeline must **mark** failures and suspicious downloads.

### Where to look

- `$LIB_ROOT/reports/download_report.md` (human scan)
- `$LIB_ROOT/reports/download_report.jsonl` (machine analysis)

### Required status semantics

Your report must assign exactly one of:

- `ok`: the artifact exists and passes basic sanity checks
- `suspect`: something exists but likely wrong / incomplete (needs repair)
- `error`: download/extraction failed (missing or blocked)

### Sanity checks (minimum)

For each item:

- **PDF**
  - file exists, non-empty
  - PDF header present (`%PDF` within first ~1KB)
  - text extraction exists (or explicitly logged as unavailable)
  - image manifest exists if image extraction is enabled
- **Website**
  - HTML snapshot exists, non-empty
  - extracted text exists
  - not obviously a captcha/“enable javascript” block page
  - image manifest exists if enabled
- **Repo**
  - clone directory exists and has a commit hash recorded
  - image manifest exists if repo image scan is enabled

### Quick summary script (counts + list errors)

```bash
python - <<'PY'
import json
from collections import Counter, defaultdict
from pathlib import Path

LIB_ROOT = Path("bibliography_your-topic")  # change me
report = LIB_ROOT / "reports" / "download_report.jsonl"

status = Counter()
by_type = defaultdict(Counter)
errors = []

for line in report.read_text(encoding="utf-8").splitlines():
    rec = json.loads(line)
    status[rec["status"]] += 1
    by_type[rec.get("type")][rec["status"]] += 1
    if rec["status"] != "ok":
        errors.append(rec)

print("status:", dict(status))
print("by_type:", {k: dict(v) for k, v in by_type.items()})
print("\\nnon-ok:")
for rec in errors:
    print(f\"- {rec['id']} {rec.get('type')} {rec['status']} {rec['url']} | {rec.get('notes') or rec.get('error') or ''}\")\nPY
```

---

## Repair Loop: Make Errors/Suspects Go Away (Without Losing Provenance)

For each `error` or `suspect` row in `download_report`:

1. **Prefer open mirrors**:
   - add rows to `$LIB_ROOT/overrides.csv` (`url,mirror_url`)
2. **Use cookies only when legitimate**:
   - put Netscape cookies in `$LIB_ROOT/cookies.txt`
3. **Fix bad URLs**:
   - if a URL is truncated/escaped, fix it in `sources.csv` (and record which input file caused it)
4. **Rerun the build script**:
   - verify the report improved

Important: do not “paper over” failures by deleting report lines. Failures are part of the provenance.

---

## Build the Single LLM Index (`llm_index.jsonl`)

After a build run, generate **one file** that an LLM/RAG system can use to locate all artifacts.

Requirements for each entry:
- stable `id`
- `url`, `type`, `status`, `notes`, `error`
- `text_paths` (prefer these for retrieval)
- image manifests + OCR manifests
- repo paths (if any)

Generator (edit `LIB_ROOT`):

```bash
python - <<'PY'
import json
from pathlib import Path

LIB_ROOT = Path("bibliography_your-topic")  # change me
report_path = LIB_ROOT / "reports" / "download_report.jsonl"
out_path = LIB_ROOT / "llm_index.jsonl"

def add_if_exists(out, p: Path):
    if p.exists():
        out.append(str(p))

with report_path.open("r", encoding="utf-8") as f, out_path.open("w", encoding="utf-8") as out:
    for line in f:
        rec = json.loads(line)
        item_id = rec["id"]

        text_paths = []
        image_manifest_paths = []
        image_ocr_manifest_paths = []
        repo_paths = []

        add_if_exists(text_paths, LIB_ROOT / "sources" / "pdf_text" / f"{item_id}.txt")
        add_if_exists(text_paths, LIB_ROOT / "sources" / "pdf_text" / f"{item_id}_mirror.txt")
        add_if_exists(text_paths, LIB_ROOT / "sources" / "web" / "text" / f"{item_id}.txt")
        add_if_exists(text_paths, LIB_ROOT / "sources" / "web" / "text" / f"{item_id}_mirror.txt")

        add_if_exists(image_manifest_paths, LIB_ROOT / "sources" / "pdf_images" / item_id / "manifest.json")
        add_if_exists(image_ocr_manifest_paths, LIB_ROOT / "sources" / "pdf_image_text" / item_id / "manifest.json")
        add_if_exists(image_manifest_paths, LIB_ROOT / "sources" / "web" / "images" / item_id / "manifest.json")
        add_if_exists(image_ocr_manifest_paths, LIB_ROOT / "sources" / "web" / "image_text" / item_id / "manifest.json")

        repo_dir = LIB_ROOT / "sources" / "repo" / item_id
        if repo_dir.exists():
            repo_paths.append(str(repo_dir))
            add_if_exists(repo_paths, repo_dir / "_commit.txt")
            add_if_exists(image_manifest_paths, repo_dir / "_images.json")
            add_if_exists(image_ocr_manifest_paths, LIB_ROOT / "sources" / "repo_image_text" / item_id / "manifest.json")

        entry = {
            "id": item_id,
            "url": rec.get("url"),
            "type": rec.get("type"),
            "status": rec.get("status"),
            "notes": rec.get("notes"),
            "error": rec.get("error"),
            "local_files": rec.get("local_files") or [],
            "text_paths": text_paths,
            "image_manifest_paths": image_manifest_paths,
            "image_ocr_manifest_paths": image_ocr_manifest_paths,
            "repo_paths": repo_paths,
        }
        out.write(json.dumps(entry, ensure_ascii=True) + "\\n")

print("wrote", out_path)
PY
```

---

## Portability Checklist (Copy/Paste Into Another Repo)

To reuse this pipeline in a new codebase:

- Copy this file as-is (it’s topic-agnostic).
- Ensure the new repo has a build script that matches the interface:
  - `--input sources.csv`
  - `--root bibliography_<topic>`
  - writes `reports/download_report.{md,jsonl}`
- Keep `inputs/` + `sources.csv` + `overrides.csv` committed so the bibliography is reproducible.
- Decide your ID scheme early; treat IDs as stable once the library is created.

