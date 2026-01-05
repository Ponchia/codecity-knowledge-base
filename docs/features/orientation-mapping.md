---
id: F053
title: Orientation (Twist) Mapping
category: mapping
status: variant
introduced_by: CC075
implementations: [Langelier Quality Visualization Framework]
related_features: [F006, F005]
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [cohesion]
last_updated: 2026-01-03
updated_from: [CC075]
---

# Orientation (Twist) Mapping

## Definition

A property mapping where a building’s **rotation/orientation** (visual “twist”) encodes a metric value, providing an additional dimension beyond size and color.

## Mechanism (from CC075)

**Input**: Numeric metric value (e.g., cohesion).

**Process**:
1. Normalize the metric value to a range (e.g., 0–90°).
2. Rotate the building around its vertical axis by the corresponding angle.

**Output**: Cohesive classes appear upright/straight, while low-cohesion classes appear visually twisted.

## Sources

- [CC075] Langelier et al. (ASE 2005) — maps LCOM5 (cohesion) to box twist

## See Also

- [[color-mapping]] — coupling encoded as hue in the same framework
- [[height-mapping]] — size/complexity encoded as height in the same framework
