---
id: F043
title: Nested Functions as Stacked Buildings
category: mapping
status: variant
introduced_by: CC036
implementations: [JSCity, GoCity]
related_features: [F003, F005, F007]
taxonomy:
  granularity: [function, class, file]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-03
updated_from: [CC036, CC093, CC104]
---

# Nested Functions as Stacked Buildings

## Definition

A representation strategy for nested functions where an inner function is rendered as a smaller building placed on top of the building representing its enclosing function, making nesting depth visible while preserving a “city” metaphor.

## Mechanism (from CC036)

**Input**: Functions with nesting relationships and per-function metrics (e.g., LOC and number of variables).

**Process**:
1. Render each top-level function as a building.
2. For each nested function, render an additional building placed on top of its enclosing function’s building.
3. Aggregate parent dimensions so the base is widest at the bottom and narrower at higher levels (e.g., parent width sums variables across nested children; parent height sums LOC across nested children).

**Output**: A city where nesting appears as building “stacks” rather than only by spatial grouping.

## Variations

| Implementation | Nested Entity | Container |
|----------------|---------------|-----------|
| JSCity | nested functions | enclosing function building |
| GoCity | structs | file building (structs stacked on top) |

## Sources

- [CC036] Viana et al. (arXiv 2017) — JSCity nested-function visualization
- [CC093] GoCity repository — structs stacked on top of file buildings
- [CC104] GoCity SANER 2019 — structs positioned on top of file buildings
