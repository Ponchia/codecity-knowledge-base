---
id: F073
title: Class-as-Clothing-Item Mapping
category: mapping
status: variant
maturity: emerging
bounded_context: [clothing-metaphor]
introduced_by: CC041
implementations: [CodeVestimenta]
related_features: [F072, F074]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [clothing]
  metric_category: [size, coupling, quality]
last_updated: 2026-01-05
updated_from: [CC041]
---

# Class-as-Clothing-Item Mapping

## Problem & Motivation

This capability helps make important properties visible at a glance without relying on separate numeric views. A mapping where each software **class** is rendered as a distinct clothing item, enabling quick visual comparison of class-level metric profiles in a wardrobe-style display. Without it, metric signals remain harder to perceive and often require separate tables or charts.

## Definition

A mapping where each software **class** is rendered as a distinct clothing item, enabling quick visual comparison of class-level metric profiles in a wardrobe-style display.

## Mechanism (Solution)

**Input**: Class list plus computed metrics (LOC, members/methods, inheritance, coupling).

**Process**:
1. Select a garment type per class (e.g., t-shirt, shirt, pants).
2. Render the garment with metric-driven attributes (size, sleeves, color, collar/belt, stripes).
3. Pair the view with a legend so garments can be traced back to class names.

**Output**: A grid of garments representing the classes in a system, useful for scanning outliers.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Adds an at-a-glance quantitative cue. | Outliers can dominate perception without scaling/binning. |
| Supports quick comparison across many entities. | Multiple encodings can increase visual clutter. |

## Variations

| Implementation | Variation |
|----------------|-----------|
| CodeVestimenta | Garment type is driven by RFC thresholds (t-shirt < 50, shirt 50–100, pants > 100). |

## Evidence

CC041’s study reports improved comprehension for dependency and design-quality tasks when the visual mapping is available.

## Sources

- [CC041] Defines the class-to-garment mapping and uses it in a controlled study.

## See Also

- [[clothing-metaphor]] — the umbrella metaphor.
- [[clothing-attribute-mapping]] — how metrics map to garment properties.
