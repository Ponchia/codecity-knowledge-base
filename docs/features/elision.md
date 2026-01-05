---
id: F049
title: Elision
category: interaction
status: variant
introduced_by: CC085
implementations: [CodeCity, m3triCity]
related_features: [F022, F023]
taxonomy:
  granularity: [class, package]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-04
updated_from: [CC059, CC085]
---

# Elision

## Definition

An interaction that temporarily removes selected artifacts from the view to reduce occlusion and keep the remaining city readable.

## Mechanism (from CC059)

**Input**: A user selection of artifacts (e.g., a large building obstructing the view).

**Process**:
1. Select one or more objects in the city.
2. Remove the selected objects from the rendered view (without changing the underlying model).

**Output**: A simplified view with obstructing artifacts elided.

## Notes (CodeCity, from CC085)

CC085 describes CodeCity supporting “eliding” as part of its interaction set, alongside selection- and query-driven operations, to help keep views readable during exploration.

## Sources

- [CC085] Wettel & Lanza (ICPC 2007) — CodeCity interaction set includes eliding
- [CC059] Pfahler et al. (2020) — elision to remove selected obstructing objects from view

## See Also

- [[query-filtering]] — hide/exclude artifacts via criteria (e.g., regex)
- [[selection]] — provides the target set for elision
