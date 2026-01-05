---
id: I035
name: City Blocks
origin: cjayawickrema (open-source)
year_introduced: 2025
status: research
source_refs: [CC147]
repo_url: https://github.com/cjayawickrema/city-blocks
demo_url: null
primary_language: JavaScript (Node.js + Three.js)
features_implemented: [F001, F005, F006, F007, F008, F017, F021, F023, F026, F038]
last_updated: 2026-01-04
updated_from: [CC147]
---

# City Blocks

## Overview

City Blocks is an open-source 3D visualization for Git repositories that maps directories and files into a block-and-building “city” to highlight code size and churn.

## Key Mappings (from CC147)

- **Blocks**: directories (nested directories stack into a stepped pyramid with darker shades at higher levels)
- **Buildings**: files
- **Height**: influenced by commit count (churn)
- **Volume / footprint**: derived from lines of code (LOC) (described as LOC³ in the article)
- **Color (“heat”)**: relative commit count vs the maximum commit count in the repo

## Pipeline / Implementation Notes (from CC147)

- Uses a script to compute per-file statistics (e.g., commits and LOC) and emit a `data.csv`.
- Uses a Node.js server to serve the visualization.
- Builds a nested object graph, then renders it with Three.js/WebGL.
- Uses DFS traversal plus a bin-packing placement step to reduce empty space.

## Filtering (from CC147)

- Supports excluding files via a glob-style exclusion file to reduce clutter.

## Sources

- [CC147] City Blocks Medium post — overview, mappings, and implementation sketch (points to GitHub for code)
