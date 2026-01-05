---
id: F061
title: Levelized Layout (LSM Rows)
category: layout
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC137
implementations: [DynaCity]
related_features: [F008, F017]
supersedes: []
taxonomy:
  granularity: [package, class]
  visual_element: [district, building]
  metric_category: [coupling]
last_updated: 2026-01-05
updated_from: [CC137]
---

# Levelized Layout (LSM Rows)

## Problem & Motivation

This capability helps keep spatial organization interpretable and memorable as the city grows. A layout strategy that arranges districts/buildings into horizontal rows (“levels”) based on an architectural layering model (e.g., an LSM level derived from the dependency graph), making layer boundaries and dependency direction easier to interpret than space-filling packings. Without it, navigation and spatial memory degrade because placement feels arbitrary or unstable.

## Definition

A layout strategy that arranges districts/buildings into horizontal rows (“levels”) based on an architectural layering model (e.g., an LSM level derived from the dependency graph), making layer boundaries and dependency direction easier to interpret than space-filling packings.

## Mechanism (Solution)

**Input**: A hierarchy of packages/classes with an assigned integer `level` per node (from a Layered Structure Model), plus per-element footprints.

**Process**:
1. Group child elements by `level` to form ordered rows.
2. Within each row, place elements left-to-right with fixed spacing and center the row within the available width.
3. Stack successive rows front-to-back (depth direction), again with fixed spacing.

**Output**: A city where architectural levels appear as visible rows; deeper or higher-level components can be visually separated even when they belong to the same container.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Makes large structures navigable via spatial organization. | May hide non-hierarchical relationships. |
| Can improve stability/orientation if positions are consistent. | Computing layout can be expensive at scale. |

## Implementation Notes

CC137 also contains an alternative bin-packing layout implementation (used as a comparison condition in the bundled evaluation spreadsheets), but the default city construction path builds an LSM and lays out elements by level.

## Sources

- [CC137] Holoware software-city repository — level-based row layout (`lsmNode.GetLevel()` grouping) for packages and classes

## See Also

- [[treemap-layout]] — common space-filling alternative
- [[package-as-district]] — typical hierarchy grouping used by levelized layouts
