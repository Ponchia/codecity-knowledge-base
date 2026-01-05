---
id: F004
title: Component-as-Building Mapping
category: mapping
status: variant
maturity: emerging
bounded_context: [city-metaphor]
introduced_by: CC015
implementations: [Component City]
related_features: [F001]
supersedes: []
taxonomy:
  granularity: [component]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC015]
---

# Component-as-Building Mapping

## Problem & Motivation

This capability helps make important properties visible at a glance without relying on separate numeric views. A concept mapping where each “component” (coarser than class/function) is rendered as a building, emphasizing higher-level system structure. Without it, metric signals remain harder to perceive and often require separate tables or charts.

## Definition

A concept mapping where each “component” (coarser than class/function) is rendered as a building, emphasizing higher-level system structure.

## Mechanism (Solution)

**Input**: A system decomposition into components (as defined by the tool/model).

**Process**:
1. Create one building per component.
2. Map component attributes/metrics to building properties.
3. Arrange buildings into a city layout.

**Output**: A city with component granularity.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Adds an at-a-glance quantitative cue. | Outliers can dominate perception without scaling/binning. |
| Supports quick comparison across many entities. | Multiple encodings can increase visual clutter. |

## Variations

- Component City uses XML/XSLT to generate VRML scenes; CC015 reports component buildings and function-attribute-related static properties.

## Sources

- [CC015] Jeffery survey — Component City overview and Table 1

## See Also

- [[city-metaphor]] — overarching metaphor
- [[class-as-building]] — more common alternative in surveyed tools
