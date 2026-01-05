---
id: F021
title: Stacked-Platform Topology
category: layout
status: canonical
maturity: established
bounded_context: [city-metaphor]
introduced_by: CC023
implementations: [CodeCity]
related_features: [F008, F017]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [platform, district, building]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC023, CC020, CC035]
---

# Stacked-Platform Topology

## Problem & Motivation

Nested package hierarchies are hard to read in a purely planar layout. CC023 introduces “topology” via stacked platforms so nesting depth becomes visible through altitude, improving orientation in large systems.

## Definition

A topology technique that represents nested packages as stacked platforms, placing buildings at different altitudes to make package nesting visible and improve orientation.

## Context & Applicability

**Use when:**
- The hierarchy is deep enough that nested districts need an additional cue beyond borders and color (CC023).
- You want altitude to act as a quick proxy for nesting depth during navigation (CC023).

**Avoid when:**
- The hierarchy is shallow or altitude would add unnecessary visual complexity (CC023).
- Users must interpret building height precisely and altitude could be confused with metric height without clear legends and camera defaults.

**Prerequisites:** A nested hierarchy plus a consistent altitude-step policy and navigation controls to change altitude/angle (CC023).
**Alternatives:** Encode nesting via district shading (CC020, CC035) or use a hierarchical layout like [[sunburst-layout]] instead of altitude.

## Forces

| Force | Pull |
|-------|------|
| Nesting clarity vs. visual complexity | Altitude makes nesting obvious, but adds 3D structure that can increase clutter and navigation effort. |
| Altitude semantics vs. metric-height semantics | Use altitude for containment depth, but prevent confusion with height-as-metric encodings. |
| Orientation vs. occlusion | Vertical separation can improve orientation, but stacked layers can occlude each other depending on camera defaults. |

## Mechanism (Solution)

**Input**: Nested package hierarchy.

**Process**:
1. Layout each package/district separately.
2. For nested packages, stack their districts as platforms at increasing altitudes.
3. Place buildings on the platform corresponding to their package.

**Output**: A city where altitude conveys package nesting.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Makes deep containment hierarchies readable by turning “depth” into a spatial cue (altitude). | Increases occlusion and can make navigation harder in dense, deeply nested systems. |
| Provides an additional orientation landmark (which level you are on). | Can be misread as a metric signal unless the UI clearly separates “platform height” from “building height”. |

**Complexity**: Medium
**Performance**: Layout computation can be a bottleneck for large graphs/hierarchies.
**Cognitive Load**: Medium (users must learn layout semantics).

## Implementation Notes

- Choose an altitude step that separates platforms without making navigation cumbersome; align with camera controls (CC023).
- Render platform edges/borders clearly to indicate containment and keep buildings anchored to the correct level (CC023).
- Provide quick focus operations (selection, spawn) to move between levels without disorientation (CC023).

## Evidence

CC023 introduces stacked platforms as the way CodeCity makes deep package nesting visible (“topology”); CC035 reiterates the technique as part of the city’s habitability/orientation design. No controlled user study isolating the benefit of altitude-based nesting cues is reported in these sources.

## Variations

| Approach | Nesting cue | Notes |
|----------|-------------|------|
| Stacked platforms | Altitude steps per nesting level | Canonical CodeCity “topology” approach (CC023). |
| District shading | Color/lightness per nesting level | Alternative nesting cue used alongside/without altitude (CC020, CC035). |

## Known Limitations

- Additional vertical structure can increase occlusion and navigation effort in dense hierarchies (CC023).
- Altitude cues can be misread as metric height unless legends/tooltips are clear.
- Very deep nesting can create many thin layers; benefits diminish when most layers are sparse.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — “topology” via stacked platforms
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — district shading as a nesting cue (alternative to altitude)
- [CC035] Wettel PhD thesis — package-nesting cues (altitude vs shading) in the CodeCity approach

## Open Questions

- When should tools prefer shading/borders over altitude (or vice versa) based on hierarchy depth and user task?
- What are good defaults for altitude step size and camera constraints to reduce occlusion while keeping nesting obvious?
- How can stacked platforms coexist with other vertical encodings (height mapping, layered overlays) without confusing users?

## See Also

- [[package-as-district]] — containment hierarchy that platforms visualize
- [[treemap-layout]] — common packing strategy within each platform
- [[navigation-modes]] — vertical vs horizontal navigation is often needed to exploit altitude cues
