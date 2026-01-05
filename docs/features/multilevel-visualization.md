---
id: F055
title: Multilevel Visualization (Distance-Based Detail)
category: interaction
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC102
implementations: [CodeMetropolis, IslandViz]
related_features: [F026, F037]
supersedes: []
taxonomy:
  granularity: [package, class, method, module]
  visual_element: [district, floor, island, building]
  metric_category: [size, complexity]
last_updated: 2026-01-05
updated_from: [CC102, CC070, CC078]
---

# Multilevel Visualization (Distance-Based Detail)

## Problem & Motivation

This capability helps enable efficient details-on-demand and focused exploration in dense scenes. A multi-scale interaction technique where the visible level of detail depends on distance: an overview emphasizes large-scale structure, while close inspection reveals finer-grained entities and metrics. Without it, exploration becomes slower and more error-prone because users cannot inspect and act in-context.

## Definition

A multi-scale interaction technique where the visible level of detail depends on distance: an overview emphasizes large-scale structure, while close inspection reveals finer-grained entities and metrics.

## Mechanism (Solution)

**Input**: A hierarchical city model with multiple levels (namespaces, classes, methods).

**Process**:
1. Provide a bird’s-eye view (flight) for macro structure (namespaces/classes).
2. Allow street-level navigation for micro detail (method-level floors).
3. Let the user change level of detail by moving closer or farther rather than toggling explicit filters.

**Output**: A city that supports both macro and micro comprehension without overwhelming the viewer.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Enables details-on-demand workflows. | Adds UI/interaction complexity. |
| Reduces cognitive load by filtering/focusing. | Can create mode errors if state is unclear. |

## Variations

CC070 uses a related approach for an island-metaphor architecture view: it defines three abstraction layers (island, region, building) and targets implicit transitions based on the relative size of elements in the user’s view frustum. Users can also scale the table visualization (zoom), which changes what detail level is rendered.

## Sources

- [CC102] Balogh & Beszedes (2013) — multilevel data visualization via fly/walk exploration in Minecraft
- [CC070] Schreiber et al. (IEEE 2019) — IslandViz: implicit level transitions across island/region/building based on distance/scale
- [CC078] Misiak et al. (IEEE VR 2018) — IslandViz ties zoom/scale to abstraction-layer transitions in a virtual-table setup

## See Also

- [[navigation-modes]] — movement modes that enable scale changes
- [[hover-inspection]] — details on demand at a given scale
