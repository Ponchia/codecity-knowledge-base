---
id: F048
title: Edge Thickness Mapping
category: mapping
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC043
implementations: [SoftViz3D, SoftVis3D]
related_features: [F030, F047]
supersedes: []
taxonomy:
  granularity: [file, package]
  visual_element: [edge]
  metric_category: [coupling]
last_updated: 2026-01-05
updated_from: [CC043, CC129]
---

# Edge Thickness Mapping

## Problem & Motivation

This capability helps make important properties visible at a glance without relying on separate numeric views. A property mapping where the thickness (line width) of an edge encodes a numeric value (e.g., dependency count or coupling strength), making “stronger” relations visually heavier. Without it, metric signals remain harder to perceive and often require separate tables or charts.

## Definition

A property mapping where the thickness (line width) of an edge encodes a numeric value (e.g., dependency count or coupling strength), making “stronger” relations visually heavier.

## Mechanism (Solution)

**Input**: A set of relations (edges) each with an associated numeric weight.

**Process**:
1. Normalize each edge weight against a reference (e.g., maximum weight in the scope).
2. Convert the normalized weight into a line width (often with a minimum width for visibility).
3. Render edges using that width (optionally with direction cues like arrowheads).

**Output**: A dependency graph where edge thickness communicates relative relation strength.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Adds an at-a-glance quantitative cue. | Outliers can dominate perception without scaling/binning. |
| Supports quick comparison across many entities. | Multiple encodings can increase visual clutter. |

## Variations

| Implementation | Variation |
|----------------|-----------|
| SoftViz3D (CC043) | Computes edge width from a per-edge counter scaled by the maximum counter in the project, and passes it to GraphViz as a `setlinewidth(...)` style. |
| SoftVis3D (CC129) | Sets Graphviz `penwidth` directly from the number of dependency IDs aggregated into each edge (with additional “edge radius” derived from the same count). |

## Sources

- [CC043] SoftViz3D repository — edge-width encoding derived from dependency counters
- [CC129] sonar-softvis3d-plugin repository — dependency edges labeled with `penwidth` based on aggregated dependency counts

## See Also

- [[dependency-path-expansion]] — produces aggregated edges that are natural candidates for thickness encoding
- [[contextual-dependency-view]] — reduces clutter so edge encodings remain readable
