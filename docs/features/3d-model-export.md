---
id: F040
title: 3D Model Export (3D Printing)
category: interaction
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC091
implementations: [CodeCharta, SynchroVis / ExplorViz]
related_features: [F001]
supersedes: []
taxonomy:
  granularity: [file, class]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC091, CC014, CC080]
---

# 3D Model Export (3D Printing)

## Problem & Motivation

This capability helps share and reuse a city representation outside the tool (reports, demos, 3D printing). An export capability that generates a printable 3D model of the current city/map so the visualization can be shared as a **physical artifact** (e.g., for demos or communication). Without it, sharing/archiving requires screenshots or re-running the tool, and physical/standalone reuse is harder.

## Definition

An export capability that generates a printable 3D model of the current city/map so the visualization can be shared as a **physical artifact** (e.g., for demos or communication).

## Mechanism (Solution)

**Input**: Current city geometry and selected rendering settings.

**Process**:
1. Open the export/print dialog from the visualization UI.
2. Configure scale and presentation elements (e.g., labels, optional QR code, optional logo).
3. Export the model as a 3D-printing file format (e.g., STL or 3MF).

**Output**: A downloadable 3D model file representing the city.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Enables sharing and archival as a standalone artifact (including physical 3D prints). | Loses interaction/animation; printed models may oversimplify or require geometry cleanup. |
| Useful for communication and demos outside the visualization tool. | Requires scaling/label decisions and can be sensitive to printer/format constraints. |

## Variations

CC080 shows ExplorViz exporting application models to **OpenSCAD** source files, with options for labels, lids, and puzzle-style cuts to support 3D printing and assembly.

## Sources

- [CC091] CodeCharta docs — 3D printing export (STL/3MF) and configuration options
- [CC014] CodeCharta website — highlights printing a 3D model of the codebase
- [CC080] ExplorViz archived repo — OpenSCAD export pipeline for printable application models

## See Also

- [[view-configuration]] — exported models typically depend on the active view/mappings
- [[city-metaphor]] — exported artifact is usually a city/map view
