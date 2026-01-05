---
id: F003
title: Function-as-Building Mapping
category: mapping
status: variant
introduced_by: CC015
implementations: [Software World, Vizz3D, High-Rise, JSCity]
related_features: [F001, F002, F005, F044]
taxonomy:
  granularity: [function]
  visual_element: [building]
  metric_category: [size, behavior]
last_updated: 2026-01-02
updated_from: [CC015, CC036, CC094]
---

# Function-as-Building Mapping

## Definition

A concept mapping where each function/method is represented as a building. This supports fine-grained inspection but can reduce scalability on large systems.

## Mechanism

**Input**: A program model with functions/methods and (optionally) their containing classes.

**Process**:
1. Create one building per function/method.
2. Group buildings by containing unit (e.g., methods inside a class district/area).
3. Map one or more metrics to visual properties (commonly height/color/texture).

**Output**: A city where the primary visual unit is a function/method.

## Variations (from CC015)

| Tool | Notable mapping details |
|------|--------------------------|
| Software World | Methods are buildings; parameters depicted as exterior doors; color indicates public/private; height uses a LOC-derived scale. |
| Vizz3D | Member functions are buildings placed on a class “platform”; wall texture encodes LOC. |
| High-Rise | Table 1 lists “function” granularity; CC015’s description discusses near real-time timing with building height proportional to time consumed in a recent window. |
| JSCity | Functions are buildings in a browser-based city; height uses LOC and footprint uses number of variables; nested functions are rendered as stacked buildings (and the repo also renders some module declarations as buildings). |

## Evidence

CC015 positions function-level buildings as trading off scalability for detail; no controlled evaluation is described for Software World / Component City.

## Sources

- [CC015] Jeffery survey — overview and comparison (Table 1)
- [CC036] Viana et al. (arXiv 2017) — JSCity (functions as buildings in a web-based city)
- [CC094] JSCity repository — implementation details for function buildings and related building types

## See Also

- [[city-metaphor]] — overarching metaphor
- [[class-as-building]] — coarser-grained alternative
- [[height-mapping]] — common encoding for function-level buildings
- [[module-as-building]] — module declarations rendered as buildings (variant)
