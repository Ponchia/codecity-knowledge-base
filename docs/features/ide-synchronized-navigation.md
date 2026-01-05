---
id: F056
title: IDE-Synchronized Navigation
category: interaction
status: variant
introduced_by: CC103
implementations: [CodeMetropolis]
related_features: [F026, F022]
taxonomy:
  granularity: [file, class]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-03
updated_from: [CC103]
---

# IDE-Synchronized Navigation

## Definition

An interaction that synchronizes an IDE context (e.g., the active file or class) with the city, automatically moving the viewpoint or player to the corresponding location in the visualization.

## Mechanism (from CC103)

**Input**: Active file/class in the IDE.

**Process**:
1. The IDE plug-in maps the active file/class to its city entity.
2. A navigation command is sent to the visualization runtime.
3. The player is moved to the corresponding building/district position.
4. In "follow" mode, this update happens continuously as the active file changes.

**Output**: The city view stays aligned with the developer's current IDE focus.

## Variations

| Implementation | Mode | Notes |
|----------------|------|-------|
| CodeMetropolis | Jump + Follow | Manual jump to active file building; optional automatic follow that continuously repositions the player. |

## Sources

- [CC103] Balogh et al. (2015) - Eclipse plug-in adds jump/follow navigation synchronized with active file

## See Also

- [[navigation-modes]] - movement styles (walk/fly) that complement synchronized jumps
- [[selection]] - selection-based focus in the visualization
