---
id: F004
title: Component-as-Building Mapping
category: mapping
status: variant
introduced_by: CC015
implementations: [Component City]
related_features: [F001]
taxonomy:
  granularity: [component]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-02
updated_from: [CC015]
---

# Component-as-Building Mapping

## Definition

A concept mapping where each “component” (coarser than class/function) is rendered as a building, emphasizing higher-level system structure.

## Mechanism

**Input**: A system decomposition into components (as defined by the tool/model).

**Process**:
1. Create one building per component.
2. Map component attributes/metrics to building properties.
3. Arrange buildings into a city layout.

**Output**: A city with component granularity.

## Variations (from CC015)

- Component City uses XML/XSLT to generate VRML scenes; CC015 reports component buildings and function-attribute-related static properties.

## Sources

- [CC015] Jeffery survey — Component City overview and Table 1

## See Also

- [[city-metaphor]] — overarching metaphor
- [[class-as-building]] — more common alternative in surveyed tools

