---
id: F056
title: IDE-Synchronized Navigation
category: interaction
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC103
implementations: [CodeMetropolis]
related_features: [F026, F022]
supersedes: []
taxonomy:
  granularity: [file, class]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC103]
---

# IDE-Synchronized Navigation

## Problem & Motivation

This capability helps enable efficient details-on-demand and focused exploration in dense scenes. An interaction that synchronizes an IDE context (e.g., the active file or class) with the city, automatically moving the viewpoint or player to the corresponding location in the visualization. Without it, exploration becomes slower and more error-prone because users cannot inspect and act in-context.

## Definition

An interaction that synchronizes an IDE context (e.g., the active file or class) with the city, automatically moving the viewpoint or player to the corresponding location in the visualization.

## Mechanism (Solution)

**Input**: Active file/class in the IDE.

**Process**:
1. The IDE plug-in maps the active file/class to its city entity.
2. A navigation command is sent to the visualization runtime.
3. The player is moved to the corresponding building/district position.
4. In "follow" mode, this update happens continuously as the active file changes.

**Output**: The city view stays aligned with the developer's current IDE focus.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Enables details-on-demand workflows. | Adds UI/interaction complexity. |
| Reduces cognitive load by filtering/focusing. | Can create mode errors if state is unclear. |

## Variations

| Implementation | Mode | Notes |
|----------------|------|-------|
| CodeMetropolis | Jump + Follow | Manual jump to active file building; optional automatic follow that continuously repositions the player. |

## Sources

- [CC103] Balogh et al. (2015) - Eclipse plug-in adds jump/follow navigation synchronized with active file

## See Also

- [[navigation-modes]] - movement styles (walk/fly) that complement synchronized jumps
- [[selection]] - selection-based focus in the visualization
