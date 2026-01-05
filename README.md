# CodeCity Knowledge Base

A structured knowledge base for the **CodeCity** software visualization domain, extracted from 154 academic papers, tool repositories, and web resources.

## What is CodeCity?

CodeCity is a software visualization paradigm that represents codebases as 3D cities:
- **Classes/files** → Buildings (height = complexity, base = size)
- **Packages/folders** → Districts
- **Metrics** → Visual properties (color, texture, position)

This repository contains a comprehensive extraction of the domain's vocabulary, features, implementations, and research findings.

## Repository Structure

```
docs/
├── glossary.md              # Domain vocabulary (70+ terms)
├── taxonomy.md              # Classification dimensions
├── features/                # 40+ atomic feature cards
│   ├── _index.md
│   ├── height-mapping.md
│   ├── treemap-layout.md
│   └── ...
├── implementations/         # 20+ tool profiles
│   ├── _index.md
│   ├── codecity.md
│   ├── codecharta.md
│   └── ...
└── sources/
    ├── _index.md            # Bibliography with processing status
    └── annotations/         # Per-source extraction YAML (76 processed)

bibliography/
├── index.csv                # Source registry (154 sources)
├── llm_index.jsonl          # Download status + paths
├── processing_status.csv    # Extraction tracking
└── scripts/                 # Download/processing tools
```

## Processing Summary

| Status | Count | Description |
|--------|-------|-------------|
| Complete | 76 | Fully processed with knowledge extracted |
| Skipped | 78 | Duplicates, out-of-scope, or metadata-only |

## What's Tracked vs Generated

**Tracked in git (~1.8 MB):**
- `docs/` — Extracted knowledge base
- `bibliography/*.csv`, `*.jsonl` — Source indexes and tracking
- `bibliography/scripts/` — Build/download scripts
- `PLAN.md`, `LLM_INSTRUCTIONS.md` — Methodology documentation

**Ignored (regenerable, ~5.8 GB):**
- `bibliography/sources/` — Downloaded PDFs, HTML, repo clones
- `bibliography/_backup/` — Local backups

## Regenerate Source Materials

To re-download the source materials:

```bash
# Requires Python 3.9+
pip install requests beautifulsoup4 PyPDF2 gitpython

# Download all sources
python bibliography/scripts/build_codecity_library.py
```

This repopulates `bibliography/sources/` from the URLs in `bibliography/index.csv`.

## Key Documents

- [PLAN.md](PLAN.md) — Extraction methodology and architecture
- [LLM_INSTRUCTIONS.md](LLM_INSTRUCTIONS.md) — Processing instructions for LLM agents
- [docs/glossary.md](docs/glossary.md) — Domain vocabulary
- [docs/features/_index.md](docs/features/_index.md) — Feature catalog
- [docs/implementations/_index.md](docs/implementations/_index.md) — Tool comparison matrix

## Sources

Primary sources include:
- **Wettel PhD Thesis (2010)** — Canonical CodeCity definition
- **Jeffery Survey** — Implementation comparison across 15+ tools
- **Moreno-Lumbreras 2024** — Systematic mapping of 406 publications
- **Tool repositories** — CodeCharta, GoCity, JSCity, ExplorViz, etc.

## License

Knowledge extraction and documentation: MIT

Note: Original sources retain their respective licenses (academic papers, tool repositories).
