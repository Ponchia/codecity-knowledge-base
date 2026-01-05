---
id: I015
name: CodeCharta
origin: MaibornWolff (open-source)
year_introduced: 2017
status: active
source_refs: [CC091, CC014]
repo_url: https://github.com/MaibornWolff/codecharta
demo_url: https://codecharta.com/visualization/app/index.html
primary_language: Kotlin/Java (analysis) + TypeScript/Angular/Three.js (visualization)
features_implemented: [F001, F038, F017, F005, F007, F006, F008, F009, F022, F023, F025, F035, F037, F015, F039, F040]
last_updated: 2026-01-02
updated_from: [CC091, CC014]
---

# CodeCharta

## Overview

CodeCharta is an open-source “software city/map” toolchain with two parts: a CLI (“CodeCharta Shell”, `ccsh`) that produces `cc.json` maps from multiple analyzers/importers, and a Web Studio (web + Electron desktop) that renders the maps as an interactive 3D city/treemap.

## Notes (from CC014)

- The project positions CodeCharta as **local-only** analysis/visualization, emphasizing that code and metrics stay on the user’s machine unless explicitly shared.
- The website frames CodeCharta’s primary use as making hotspots and technical debt visible for communication and refactoring prioritization.

## Key Mappings (from CC091)

- **Buildings**: files
- **Districts**: folders
- **Metrics → visuals**: user-selectable metrics mapped to building area/height/color

## Layout / Views

- **Treemap layouts**: squarified treemap (and variants)
- **Street layouts**: street-like layouts and hybrid treemap/street variants
- **Delta view**: compare two maps to show changes (added/removed and metric deltas)
- **Custom views**: save/share UI configurations (metrics, filters, marked/blacklisted items) without modifying the original `cc.json`

## Data Format (`cc.json`)

`cc.json` is CodeCharta’s interchange format describing a project as a file/folder tree with per-node attributes (metrics) and optional relations:
- `nodes`: hierarchical folder/file nodes with `attributes` (metrics)
- optional `edges`: relations between nodes/buildings (with edge attributes)
- optional `attributeDescriptors`: metric metadata (title/description/link/direction, analyzers)
- optional `fixedPosition`: layout constraints for top-level folders

## Sources

- [CC091] CodeCharta repository — README, docs site (gh-pages), schema changelog, and changelogs
