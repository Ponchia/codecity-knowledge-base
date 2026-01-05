---
id: F083
title: Mini-Map Navigation
category: interaction
status: experimental
maturity: emerging
bounded_context: [universal]
introduced_by: CC164
implementations: [ExplorViz]
related_features: [F026, F082, F041]
supersedes: []
taxonomy:
  granularity: [system]
  visual_element: [district, landscape]
  metric_category: []
last_updated: 2026-01-05
updated_from: [CC164]
---

# Mini-Map Navigation

## Problem & Motivation

In large 3D software cities, users easily become disoriented—"lost in the city." The immersive view provides detail but lacks global context. Users cannot see where they are relative to the whole system, making systematic exploration difficult.

- **Challenge**: How do you provide navigation context without leaving the 3D immersive view?
- **Insight**: A secondary 2D overview (mini-map) provides orientation while the main view shows detail
- **Without this**: Users repeatedly zoom out to orient, losing their place, or explore randomly

## Definition

A miniature two-dimensional top-view projection displayed alongside the 3D visualization, providing navigational context and allowing users to quickly orient themselves and jump to different areas of the software city.

## Context & Applicability

**Use when:**
- Software city is large enough that users can get lost
- Systematic exploration of multiple areas is needed
- Users need to maintain mental map of overall structure
- Collaborative exploration where users share locations

**Avoid when:**
- Small codebases where everything is visible at once
- Purely immersive VR where 2D overlays break presence

**Prerequisites:** 2D rendering capability; top-down view of hierarchy

**Alternatives:** [[software-landscape-view]] for separate full overview; [[navigation-modes]] with breadcrumbs

## Mechanism (Solution)

**Input**: Current camera position/orientation; complete city layout

**Process**:
1. Render top-down 2D projection of entire city layout
2. Display current viewport as highlighted rectangle on mini-map
3. Allow click/tap on mini-map to teleport camera to that location
4. Optionally highlight points of interest, search results, or collaborator positions
5. Update in real-time as camera moves

**Output**: Persistent corner overlay showing city overview with current position; click-to-navigate functionality

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Provides constant orientation context | Consumes screen real estate |
| Enables quick navigation across city | May distract from 3D view |
| Supports systematic exploration | Flattens 3D structure to 2D |
| Familiar pattern from games/maps | Requires additional rendering pass |

**Complexity**: Low - standard overview+detail pattern
**Performance**: Minimal - 2D rendering is fast
**Cognitive Load**: Low - users familiar with mini-maps from games

## Implementation Notes

- **Key algorithms**: Top-down orthographic projection; viewport frustum visualization
- **Common pitfalls**: Cluttered mini-map for large cities; unclear viewport indicator
- **Integration points**: Camera controller; overlay UI layer
- **Recommended defaults**: Corner placement; ~150-200px size; adjustable opacity

## Sources

- [CC164] Hansen et al. VISSOFT 2025 - mini-map augmentation in ExplorViz with user study

## See Also

- [[navigation-modes]] — camera controls the mini-map visualizes
- [[semantic-zoom]] — often paired with mini-map for overview+detail
- [[software-landscape-view]] — full-screen overview alternative
- [[collaborative-multi-user-vr]] — can show collaborator positions on mini-map

