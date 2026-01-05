---
id: F050
title: Data File Visualization
category: analysis
status: variant
introduced_by: CC079
implementations: [m3triCity]
related_features: [F001, F035, F038]
taxonomy:
  granularity: [file]
  visual_element: [building]
  metric_category: [size, complexity]
last_updated: 2026-01-03
updated_from: [CC079]
---

# Data File Visualization

## Definition

A city extension that visualizes **data files** (e.g., XML/JSON) alongside source-code entities, using data-structure metrics to encode properties of the rendered data-file artifacts.

## Mechanism (from CC079)

**Input**: Repository snapshots containing data files (e.g., XML, JSON).

**Process**:
1. Identify data files in the repository.
2. Compute simple data metrics (e.g., number of entities/entity types, maximum nesting level, maximum number of properties).
3. Render data files using distinct meshes (glyphs) and map the metrics to their geometry.

**Output**: Data files appear in the city as separate, visually distinguishable artifacts whose shape reflects data characteristics.

## Sources

- [CC079] Ardigò et al. (2021) — m3triCity 2 adds data-file entities, metrics, and dedicated meshes

## See Also

- [[file-as-building]] — file-granularity cities where files are the primary buildings
- [[view-configuration]] — selecting metrics and glyph options for a visualization

