---
id: F026
title: Navigation Modes (Vertical & Horizontal)
category: interaction
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC023
implementations: [CodeCity, CodeMetropolis, Code2City, Code2CityVR, Code Park, JSCity, SecCityVR, VR City]
related_features: [F001, F056, F064]
supersedes: []
taxonomy:
  granularity: [class, function]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC009, CC020, CC023, CC024, CC035, CC086, CC094, CC102, CC069, CC030, CC126, CC106]
---

# Navigation Modes (Vertical & Horizontal)

## Problem & Motivation

Free-form 3D navigation can cause disorientation. CC023 constrains navigation to videogame-like modes and distinguishes vertical (orbit/fly) from horizontal (in-city driving) navigation so users can build survey knowledge and route knowledge without “God-mode” movement.

## Definition

A navigation model that distinguishes between “vertical” navigation (orbit/fly around the city) and “horizontal” navigation (move within the city at street/building level), with physical constraints to preserve orientation.

## Context & Applicability

**Use when:**
- Users need both an overview (survey) and an in-context street/building-level inspection mode (CC023, CC030).
- You want to preserve locality by constraining movement (collisions, ground) and offering predictable camera behaviors (CC023, CC086).

**Avoid when:**
- Mode switching would confuse the target users; prefer smooth animated transitions between viewpoints instead (CC126).
- The visualization is effectively 2D/top-down and separate modes add little value.

**Prerequisites:** Camera controls for orbit/pan/zoom plus a first-person or constrained walk/fly mode, collision/ground constraints, and clear mode indicators (CC023, CC094).
**Alternatives:** [[metaphor-aware-navigation]] for assisted metaphor-specific navigation, or [[ide-synchronized-navigation]] for IDE-driven jumps without manual travel.

## Forces

| Force | Pull |
|-------|------|
| Scalability | Favor simple, compressive representations at large scale. |
| Fidelity | Favor detailed representations that preserve nuance. |

## Mechanism (Solution)

**Input**: User navigation intent (overview vs in-city) and input modality (mouse/keyboard, VR controller).

**Process**:
1. **Vertical mode**: orbit/pan/zoom and adjust altitude for a bird’s-eye overview (CC023, CC086).
2. **Horizontal mode**: move within the city at street/building level with collisions and a ground constraint (no passing through buildings; no below-ground movement) (CC023).
3. Support explicit mode switching and/or animated transitions to preserve spatial awareness (CC126, CC094).

**Output**: Two complementary navigation modes balancing overview comprehension with local inspection.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Enables details-on-demand workflows. | Adds UI/interaction complexity. |
| Reduces cognitive load by filtering/focusing. | Can create mode errors if state is unclear. |

**Complexity**: Medium
**Performance**: Depends on picking/raycasting and UI update costs.
**Cognitive Load**: Medium (requires learning controls and feedback).

## Variations

| Implementation | Navigation variation | Notes |
|----------------|----------------------|------|
| CodeCity | explicit vertical vs horizontal modes | Overview flying/orbit vs in-city driving with collisions/ground constraint (CC023). |
| SecCityVR | teleport “walking” + flying | Ground teleport for comfort plus flying for overview; includes regrouping teleport (CC069). |
| VR City | room-scale + teleportation | Natural walking where possible, teleportation for distant movement (CC106). |
| Code Park | exocentric/egocentric with animated transitions | Two viewpoints with transitions to preserve spatial awareness (CC126). |

## Implementation Notes

CC024 reiterates desktop navigation as combining panning/moving forward/backward with orbiting movements on both the vertical and horizontal plane to maintain a good city overview perspective.

### Additional Navigation Controls (from CC020)

CC020 lists common navigation actions in CodeCity’s desktop 3D environment, including orbiting, rotation, panning, and moving back and forth.

## Evidence

### Evidence (from CC023)

CC023 describes:
- Vertical navigation: orbiting, flying around, moving forward/backward, changing altitude.
- Horizontal navigation: “driving around” among buildings, constrained by collisions and ground (no passing through buildings; no going below ground).
- The two navigation types are modal (only one active at a time).

### Evidence (from CC009)

CC009 describes Code2CityVR supporting both overhead and in-city navigation:
- Fly over the city (bird’s-eye view).
- Walk around the city and climb buildings (street/building-level exploration).
- Adjust movement speed.

### Evidence (from CC069)

CC069 describes SecCityVR providing two locomotion modes: ground-level teleport “walking” on streets and a flying mode for overview navigation. It also includes a regrouping control where one user can teleport to another user’s position.

### Evidence (from CC094)

CC094 (JSCity repository) implements two explicit control modes:
- **Orbital**: orbit/pan/zoom navigation around the city (overview-oriented).
- **First-person**: “walk/fly through” navigation using keyboard/mouse controls with adjustable movement speed.

### Evidence (from CC102)

CC102 describes CodeMetropolis supporting both bird’s-eye exploration (flight in Minecraft’s creative mode) and street-level walking to inspect method-level detail.

### Evidence (from CC030)

CC030 argues that metaphor-dependent navigation can be necessary to preserve spatial knowledge in 3D worlds. It illustrates city-metaphor navigation as (a) walking at street level for **route knowledge** and (b) flying at district level for **survey knowledge**, and recommends using different navigation schemes at different metaphor-hierarchy levels.

### Evidence (from CC126)

CC126 (Code Park) uses two viewpoints for navigating code structures:
- **Exocentric (bird’s-eye) view** for overview navigation.
- **Egocentric (first-person) view** for “inside the class” inspection.

It also uses animated transitions (e.g., “go to definition” moves from the current class to bird’s-eye view and then to the destination class) to preserve spatial awareness during navigation.

### Evidence (from CC086)

CC086 describes CodeCity navigation as combining:
- Basic movements like panning and moving forward/backward.
- Orbiting movements on both the vertical and horizontal plane to maintain good perspective.

## Known Limitations

- Mode errors: users may not realize which mode is active, leading to control confusion; strong cues help (CC023).
- Constrained horizontal travel can be slow for long distances; shortcuts (jump-to/search) are often needed (CC126).
- VR locomotion can induce discomfort; comfort settings/teleport may be required (CC009).

## Open Questions

- What transition designs best preserve spatial orientation when switching modes (animated camera paths, minimaps, breadcrumbs)?
- How should tools balance “travel time” vs realism (teleport shortcuts, jump-to-definition, search-based warps) without losing locality benefits?
- Which navigation defaults work best for different platforms (desktop vs VR) and user goals (overview vs detail inspection)?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — navigation model and “no God-mode”
- [CC035] Wettel PhD thesis — navigation framed as videogame-like movement constraints
- [CC009] Romano et al. (2019) — VR navigation actions and speed control (Code2CityVR)
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — desktop navigation actions (orbit/rotate/pan/move)
- [CC024] Wettel & Lanza (WASDeTT 2008) — desktop navigation emphasizing vertical/horizontal orbiting
- [CC086] Wettel & Lanza (2008) — CodeCity navigation (keyboard/mouse; panning + orbiting planes)
- [CC094] JSCity repository — orbital vs first-person controls and speed adjustment
- [CC102] Balogh & Beszedes (2013) — CodeMetropolis fly/walk navigation for overview vs detail
- [CC030] Russo dos Santos (2002 thesis) — metaphor-aware navigation concepts and city-metaphor walk/fly navigation levels
- [CC126] Khaloo et al. (VISSOFT 2017) — Code Park exocentric/egocentric modes and orientation-preserving animated transitions
- [CC069] Wueppelmann & Yigitbas (2025) — SecCityVR VR locomotion (teleport “walking” + flying) in a code-city environment
- [CC106] Vincúr et al. (QRS-C 2017) — VR City navigation (room-scale walking + teleportation)

## See Also

- [[ide-synchronized-navigation]] - jump/follow navigation aligned with IDE context
- [[metaphor-aware-navigation]] - assisted navigation adapted to metaphor components
