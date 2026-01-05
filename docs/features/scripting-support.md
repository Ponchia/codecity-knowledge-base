---
id: F036
title: Scripting Support for Ad-hoc Visualizations
category: platform
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC035
implementations: [CodeCity]
related_features: [F035]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [size, coupling, evolution, quality]
last_updated: 2026-01-05
updated_from: [CC024, CC035, CC086, CC098, CC120]
---

# Scripting Support for Ad-hoc Visualizations

## Problem & Motivation

This capability helps enable rapid ad-hoc exploration and creation of custom queries/views. A scripting mechanism that enables rapid prototyping of new visualizations on top of the underlying model, beyond the fixed set of pre-defined city views. Without it, users are limited to built-in interactions and cannot quickly prototype task-specific analyses.

## Definition

A scripting mechanism that enables rapid prototyping of new visualizations on top of the underlying model, beyond the fixed set of pre-defined city views.

## Mechanism (Solution)

**Input**: A model (e.g., FAMIX/Hismo entities) and a script defining how to build a view.

**Process**:
1. Write a short script to build a visualization (inspired by Mondrian).
2. Execute the script to generate an ad-hoc visualization.
3. Use the script to validate feasibility before fully integrating/optimizing the visualization in the tool.

**Output**: Quickly iterated prototypes of new city-style (or other) views.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Enables rapid prototyping of new views/queries and “one-off” analyses without extending the GUI. | Requires scripting expertise; can exclude users and increase support burden. |
| Scripts can be versioned/reused, improving reproducibility of ad-hoc analyses. | Scripts can become brittle as the underlying model/API evolves, and may raise security/sandboxing concerns. |

## Implementation Notes

CC024 describes implementing a basic scripting language (inspired by Mondrian) to build **ad-hoc visualizations** by replacing the view-construction part, enabling feasibility experiments before fully integrating a visualization into the GUI. It also notes that CodeCity’s built-in view construction remained optimized (domain-knowledge based) for performance rather than being script-driven.

CC086’s module-level architecture explicitly includes a “Scripting” component and presents mappers as scriptable objects (mappers provide an `asScript` representation), reinforcing scripting as a first-class extension mechanism in CodeCity.

CC098 shows CodeCity scripting in practice and frames it as a way to build **ad-hoc views** (a script plus the resulting city view).

CC120 describes a scripting interface inspired by Mondrian’s Easel (variable list + code editor + generated visualization) and positions scripting as a way to experiment with new visualizations without continuously extending the GUI.

## Sources

- [CC035] Wettel PhD thesis — scripting support for prototyping ad-hoc visualizations
- [CC024] Wettel & Lanza (WASDeTT 2008) — scripting language inspired by Mondrian for ad-hoc views
- [CC086] Wettel & Lanza (2008) — CodeCity architecture includes scripting and scriptable mappers (`asScript`)
- [CC098] Wettel & Lanza (2008 tech report) — CodeCity scripting example and resulting ad-hoc city view
- [CC120] Wettel (2008) — experience report on adding scripting to CodeCity, including a scripting UI and prototyping rationale

## See Also

- [[view-configuration]] — GUI-driven configuration vs script-driven extension
- [[query-filtering]] — common target for scripting new queries
