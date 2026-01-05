# Local CodeCity Bibliography Library

This folder hosts a local, LLM-friendly bibliography built from `CodeCity_sources.csv`.

## Layout

- `index.csv` / `index.jsonl`: canonical list of sources with stable IDs
- `sources/pdf/`: downloaded PDFs
- `sources/pdf_text/`: extracted text (if `pdftotext` is available)
- `sources/pdf_images/`: extracted images from PDFs (if `pdfimages` is available)
- `sources/pdf_image_text/`: OCR text from PDF images (if `tesseract` is available)
- `sources/web/html/`: raw HTML snapshots
- `sources/web/text/`: extracted text from HTML
- `sources/web/images/`: downloaded images from HTML
- `sources/web/image_text/`: OCR text from web images
- `sources/repo/`: shallow clones of repositories
- `sources/repo_image_text/`: OCR text from repo images
- `reports/`: download and validation reports
- `scripts/`: build scripts

## Build

Run:

```bash
python bibliography/scripts/build_codecity_library.py
```

It will download artifacts, extract text, and write a report to `reports/download_report.md`.
