---
id: F050
title: Data File Visualization
category: analysis
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC079
implementations: [m3triCity]
related_features: [F001, F035, F038]
supersedes: []
taxonomy:
  granularity: [file]
  visual_element: [building]
  metric_category: [size, complexity]
last_updated: 2026-01-05
updated_from: [CC079]
---

# Data File Visualization

## Problem & Motivation

This capability helps connect analysis results to the system’s structural and spatial context. A city extension that visualizes **data files** (e.g., XML/JSON) alongside source-code entities, using data-structure metrics to encode properties of the rendered data-file artifacts. Without it, findings stay detached from structural context, reducing explainability and prioritization.

## Definition

A city extension that visualizes **data files** (e.g., XML/JSON) alongside source-code entities, using data-structure metrics to encode properties of the rendered data-file artifacts.

## Mechanism (Solution)

**Input**: Repository snapshots containing data files (e.g., XML, JSON).

**Process**:
1. Identify data files in the repository.
2. Compute simple data metrics (e.g., number of entities/entity types, maximum nesting level, maximum number of properties).
3. Render data files using distinct meshes (glyphs) and map the metrics to their geometry.

**Output**: Data files appear in the city as separate, visually distinguishable artifacts whose shape reflects data characteristics.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Surfaces quality/evolution signals in context. | Overlays can overwhelm the base metaphor. |
| Supports prioritization (hotspots, anomalies). | Signals may be noisy or metric-dependent. |

## Sources

- [CC079] Ardigò et al. (2021) — m3triCity 2 adds data-file entities, metrics, and dedicated meshes

## See Also

- [[file-as-building]] — file-granularity cities where files are the primary buildings
- [[view-configuration]] — selecting metrics and glyph options for a visualization
