---
id: F063
title: Configurable Grouping (Arbitrary Districts)
category: analysis
status: variant
introduced_by: CC026
implementations: [Code Arcades]
related_features: [F035]
taxonomy:
  granularity: [class, package]
  visual_element: [district, building]
  metric_category: [coupling]
last_updated: 2026-01-04
updated_from: [CC026]
---

# Configurable Grouping (Arbitrary Districts)

## Definition

A city-visualization capability that supports grouping code entities into districts/blocks using an alternative grouping relation (not only the declared package/namespace hierarchy), enabling views based on recovered architecture components or other ad-hoc groupings.

## Mechanism (from CC026)

**Input**: A grouping assignment for classes (e.g., namespace membership or recovered architecture component membership derived from dependency analysis).

**Process**:
1. Select the grouping relation to use for the view.
2. Assign each class to a district/block according to the selected grouping.
3. Layout districts and place classes within each district, optionally sorting by additional project/evolution signals.

**Output**: A city that can be reorganized around different modular decompositions.

## Sources

- [CC026] Savidis & Vasilopoulos (ICSEng 2025 preprint) — configurable grouping mechanism for arranging classes by namespaces or recovered architecture components.

## See Also

- [[view-configuration]] — broader mechanism for configuring mappings and visual properties

