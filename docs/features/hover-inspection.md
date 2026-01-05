---
id: F037
title: Hover Inspection (Examine)
category: interaction
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC035
implementations: [CodeCity, GoCity, CodeCharta, JSCity, m3triCity, BabiaXR-CodeCity, VariCity / VariMetrics]
related_features: [F022, F013]
supersedes: []
taxonomy:
  granularity: [package, class, method, file, function, module]
  visual_element: [district, building, brick]
  metric_category: [size, complexity, coupling, evolution, quality]
last_updated: 2026-01-05
updated_from: [CC035, CC059, CC091, CC094, CC104, CC096, CC134, CC045]
---

# Hover Inspection (Examine)

## Problem & Motivation

Many encodings (height/footprint/color) are only interpretable with the underlying metric values. Hover inspection provides fast details-on-demand so users can verify what an artifact represents without committing to selection or opening separate panels (CC035).

## Definition

A details-on-demand interaction that lets users inspect an artifact by hovering over it, revealing the underlying model entity and the values mapped onto its visual properties.

## Context & Applicability

**Use when:**
- Users need quick checks of names and mapped metric values while navigating (CC094, CC104).
- You want to keep the main view uncluttered while still offering details-on-demand (CC045).

**Avoid when:**
- The input modality has no reliable hover state (touch devices) or hover conflicts with drag/selection interactions.
- Targets are very small/occluded and hover would flicker; prefer click selection with a stable details pane (CC091).

**Prerequisites:** Hit-testing/raycasting to detect hovered entities, a tooltip/label UI, and debouncing to avoid flicker (CC094, CC134).
**Alternatives:** [[selection]] for persistent focus/actions, or [[source-code-display]] when code context is required.

## Forces

| Force | Pull |
|-------|------|
| Low friction vs. UI noise | Instant tooltips support fast checks, but too many labels can clutter and occlude the scene. |
| Responsiveness vs. stability | Real-time hover feedback feels fluid, but requires debouncing to avoid flicker in dense layouts. |
| Modality affordances vs. consistency | Desktop hover is natural, but VR/AR needs raycasting equivalents that remain discoverable and comfortable. |

## Mechanism (Solution)

**Input**: Cursor hover target (district/building/brick).

**Process**:
1. Identify the hovered artifact.
2. Show contextual information (entity identity/type and metric values corresponding to visual encodings).

**Output**: Fast, low-friction inspection without changing selection or view state.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Fast “details-on-demand” without committing to selection. | Tooltips can flicker/occlude and may be undiscoverable without onboarding cues. |
| Helps users interpret visual encodings by exposing mapped metric values. | Hover is not available on all devices; VR/AR equivalents vary and can add cognitive overhead. |

**Complexity**: Medium
**Performance**: Depends on picking/raycasting and UI update costs.
**Cognitive Load**: Medium (requires learning controls and feedback).

## Variations

| Implementation | Hover variation | Notes |
|----------------|------------------|------|
| JSCity / GoCity | raycast + tooltip label | Hover reveals name and mapped metric values (CC094, CC104). |
| m3triCity | configurable hover labels | Tooltip content can be configured (e.g., filename, author) (CC059). |
| BabiaXR-CodeCity | mouse hover / VR ray hover | Same concept across on-screen and VR via controller raycasting (CC096, CC134). |
| VariCity | hover reveals additional relations | Hover is used to reveal extra links while keeping defaults uncluttered (CC045). |

## Implementation Notes

- Debounce hover events and keep the tooltip stable (anchor near cursor/entity) to reduce flicker in dense scenes (CC094, CC134).
- Include identity (name/path) and mapped metric values so encodings are explainable (CC104, CC096).
- In VR, reuse controller raycasting for hover and show labels in-world or as HUD panels (CC096).

## Evidence

### Evidence (from CC094)

CC094 (JSCity repository) implements hover inspection by raycasting into the 3D scene and, when a block is hovered, displaying the block’s `tooltip`/name (including mapped metric values like LOC) as a details-on-demand label.

### Evidence (from CC059)

CC059 describes m3triCity showing a tooltip with additional information when hovering on elements; the settings panel also includes options for hover labels (e.g., filename and/or author name).

### Evidence (from CC104)

CC104 reports GoCity showing a hover window with LOC, number of methods, and number of attributes for directories, files, and structs.

### Evidence (from CC045)

CC045 describes VariCity using hover to reveal additional relationship links (e.g., additional usage relationships as underground streets and inheritance links) so the default view stays readable while still supporting details-on-demand exploration.

### Evidence (BabiaXR-CodeCity, from CC096)

CC096 describes BabiaXR-CodeCity providing tooltip-based inspection:
- On-screen: hovering the cursor over a building opens a tooltip with the file name and mapped metric values.
- In VR: the same tooltip behavior is triggered via controller raycasting (e.g., Oculus Quest 2 pointing).

### Evidence (BabiaXR repository, from CC134)

CC134 implements hover-based legends in the city components by handling `mouseenter`/`mouseleave` events on buildings to show/hide a label entity (and optionally a highlight box) containing the artifact `id` and mapped metric values.

## Known Limitations

- Tooltips can occlude the scene and may flicker in dense layouts without debouncing (CC134).
- Hover is not available on all devices; in VR/AR it depends on raycasting metaphors and comfort (CC096).
- Users may not discover hover interactions; provide legends/help or alternative inspection paths.

## Open Questions

- What tooltip placement/behavior best reduces occlusion (screen-space vs world-space labels, anchoring, fade rules)?
- How can tools make hover discoverable without constantly displaying help text (progressive hints, “?” overlays)?
- In VR/AR, which inspection pattern works best at scale: hover labels, click panels, or “inspect mode” tools?

## Sources

- [CC035] Wettel PhD thesis — “Examine” interaction in CodeCity
- [CC059] Pfahler et al. (2020) — hover tooltips and configurable hover labels in m3triCity
- [CC091] CodeCharta docs — hover a building to see name/metric; click for details
- [CC094] JSCity repository — raycast-based hover tooltip for blocks
- [CC104] GoCity SANER 2019 — hover window with LOC/NOM/NOA for code elements
- [CC096] Moreno-Lumbreras et al. (2022) — hover tooltips on-screen and controller raycasting in VR (BabiaXR-CodeCity)
- [CC134] BabiaXR repository — A-Frame hover events create/remove legend entities for buildings
- [CC045] Mortara et al. (JSS 2024 preprint) — hover reveals additional relationship links in VariCity to reduce clutter

## See Also

- [[selection]] — persistent focus/actions (vs transient hover)
- [[source-code-display]] — deeper inspection once an entity is identified
- [[visual-tagging]] — emphasize entities after inspecting them
