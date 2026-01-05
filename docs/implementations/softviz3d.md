---
id: I020
name: SoftViz3D
origin: Stefan Rinderle (NICTA master thesis; open-source)
year_introduced: 2015
status: archived
source_refs: [CC043]
repo_url: https://github.com/stefanrinderle/SoftViz3D
demo_url: http://rinderle.info/3dArch
primary_language: PHP (Yii) + JavaScript (X3DOM) + GraphViz
features_implemented: [F005, F007, F022, F030, F047, F048]
last_updated: 2026-01-03
updated_from: [CC043]
---

# SoftViz3D

## Overview

SoftViz3D is a deprecated web-based tool that visualizes software structure and dependencies as a layered 3D scene rendered via X3DOM. It combines a hierarchy view with a dedicated dependency view that routes and weights dependency edges, aiming to provide a clear overview even for large projects.

## Architecture / Stack (from CC043)

- **Web app**: PHP application using the Yii framework with a MySQL backend.
- **3D rendering**: X3DOM (X3D in HTML) in the browser.
- **Layout and edge routing**: GraphViz (`neato` for structure layouts; `dot` for dependency layouts and edge routing).
- **Deployment**: requires Apache + MySQL; GraphViz `dot` binary; PEAR Image_GraphViz (per README).

## Views

- **Structure view**: hierarchical layers rendered as platforms containing leaf “buildings”.
- **Dependency view**: renders dependency edges within a hierarchy layer; supports a detail mode and a metric/aggregated mode (path edges + weights).

## Sources

- [CC043] SoftViz3D repository — README (thesis context + deprecation) and implementation (GraphViz + X3DOM dependency view)
