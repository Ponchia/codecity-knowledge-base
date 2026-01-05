---
id: F049
title: Elision
category: interaction
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC085
implementations: [CodeCity, m3triCity]
related_features: [F022, F023]
supersedes: []
taxonomy:
  granularity: [class, package]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC059, CC085]
---

# Elision

## Problem & Motivation

This capability helps enable efficient details-on-demand and focused exploration in dense scenes. An interaction that temporarily removes selected artifacts from the view to reduce occlusion and keep the remaining city readable. Without it, exploration becomes slower and more error-prone because users cannot inspect and act in-context.

## Definition

An interaction that temporarily removes selected artifacts from the view to reduce occlusion and keep the remaining city readable.

## Mechanism (Solution)

**Input**: A user selection of artifacts (e.g., a large building obstructing the view).

**Process**:
1. Select one or more objects in the city.
2. Remove the selected objects from the rendered view (without changing the underlying model).

**Output**: A simplified view with obstructing artifacts elided.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Enables details-on-demand workflows. | Adds UI/interaction complexity. |
| Reduces cognitive load by filtering/focusing. | Can create mode errors if state is unclear. |

## Implementation Notes

CC085 describes CodeCity supporting “eliding” as part of its interaction set, alongside selection- and query-driven operations, to help keep views readable during exploration.

## Sources

- [CC085] Wettel & Lanza (ICPC 2007) — CodeCity interaction set includes eliding
- [CC059] Pfahler et al. (2020) — elision to remove selected obstructing objects from view

## See Also

- [[query-filtering]] — hide/exclude artifacts via criteria (e.g., regex)
- [[selection]] — provides the target set for elision
