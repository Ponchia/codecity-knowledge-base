---
id: F043
title: Nested Functions as Stacked Buildings
category: mapping
status: variant
maturity: emerging
bounded_context: [city-metaphor]
introduced_by: CC036
implementations: [JSCity, GoCity]
related_features: [F003, F005, F007]
supersedes: []
taxonomy:
  granularity: [function, class, file]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC036, CC093, CC104]
---

# Nested Functions as Stacked Buildings

## Problem & Motivation

This capability helps make important properties visible at a glance without relying on separate numeric views. A representation strategy for nested functions where an inner function is rendered as a smaller building placed on top of the building representing its enclosing function, making nesting depth visible while preserving a “city” metaphor. Without it, metric signals remain harder to perceive and often require separate tables or charts.

## Definition

A representation strategy for nested functions where an inner function is rendered as a smaller building placed on top of the building representing its enclosing function, making nesting depth visible while preserving a “city” metaphor.

## Mechanism (Solution)

**Input**: Functions with nesting relationships and per-function metrics (e.g., LOC and number of variables).

**Process**:
1. Render each top-level function as a building.
2. For each nested function, render an additional building placed on top of its enclosing function’s building.
3. Aggregate parent dimensions so the base is widest at the bottom and narrower at higher levels (e.g., parent width sums variables across nested children; parent height sums LOC across nested children).

**Output**: A city where nesting appears as building “stacks” rather than only by spatial grouping.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Makes nesting depth visible while keeping inner functions tied to their enclosing context. | Stacking increases occlusion and can make tall “function towers” harder to interpret without camera/legend support. |
| Supports aggregation (parent height/width derived from children) for overview cues. | Aggregation choices can hide within-stack variation; selection/inspection becomes more complex. |

## Variations

| Implementation | Nested Entity | Container |
|----------------|---------------|-----------|
| JSCity | nested functions | enclosing function building |
| GoCity | structs | file building (structs stacked on top) |

## Sources

- [CC036] Viana et al. (arXiv 2017) — JSCity nested-function visualization
- [CC093] GoCity repository — structs stacked on top of file buildings
- [CC104] GoCity SANER 2019 — structs positioned on top of file buildings

## See Also

- [[function-as-building]] — base granularity for function-level cities
- [[file-as-building]] — container granularity used by GoCity (structs stacked on files)
- [[height-mapping]] — stacking/aggregation often interacts with height encodings
