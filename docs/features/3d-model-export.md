---
id: F040
title: 3D Model Export (3D Printing)
category: interaction
status: variant
introduced_by: CC091
implementations: [CodeCharta, SynchroVis / ExplorViz]
related_features: [F001]
taxonomy:
  granularity: [file, class]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-03
updated_from: [CC091, CC014, CC080]
---

# 3D Model Export (3D Printing)

## Definition

An export capability that generates a printable 3D model of the current city/map so the visualization can be shared as a **physical artifact** (e.g., for demos or communication).

## Mechanism (from CC091)

**Input**: Current city geometry and selected rendering settings.

**Process**:
1. Open the export/print dialog from the visualization UI.
2. Configure scale and presentation elements (e.g., labels, optional QR code, optional logo).
3. Export the model as a 3D-printing file format (e.g., STL or 3MF).

**Output**: A downloadable 3D model file representing the city.

## Variations (ExplorViz, from CC080)

CC080 shows ExplorViz exporting application models to **OpenSCAD** source files, with options for labels, lids, and puzzle-style cuts to support 3D printing and assembly.

## Sources

- [CC091] CodeCharta docs — 3D printing export (STL/3MF) and configuration options
- [CC014] CodeCharta website — highlights printing a 3D model of the codebase
- [CC080] ExplorViz archived repo — OpenSCAD export pipeline for printable application models
