---
id: F053
title: Orientation (Twist) Mapping
category: mapping
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC075
implementations: [Langelier Quality Visualization Framework]
related_features: [F006, F005]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [cohesion]
last_updated: 2026-01-05
updated_from: [CC075]
---

# Orientation (Twist) Mapping

## Problem & Motivation

This capability helps make important properties visible at a glance without relying on separate numeric views. A property mapping where a building’s **rotation/orientation** (visual “twist”) encodes a metric value, providing an additional dimension beyond size and color. Without it, metric signals remain harder to perceive and often require separate tables or charts.

## Definition

A property mapping where a building’s **rotation/orientation** (visual “twist”) encodes a metric value, providing an additional dimension beyond size and color.

## Mechanism (Solution)

**Input**: Numeric metric value (e.g., cohesion).

**Process**:
1. Normalize the metric value to a range (e.g., 0–90°).
2. Rotate the building around its vertical axis by the corresponding angle.

**Output**: Cohesive classes appear upright/straight, while low-cohesion classes appear visually twisted.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Adds an at-a-glance quantitative cue. | Outliers can dominate perception without scaling/binning. |
| Supports quick comparison across many entities. | Multiple encodings can increase visual clutter. |

## Sources

- [CC075] Langelier et al. (ASE 2005) — maps LCOM5 (cohesion) to box twist

## See Also

- [[color-mapping]] — coupling encoded as hue in the same framework
- [[height-mapping]] — size/complexity encoded as height in the same framework
