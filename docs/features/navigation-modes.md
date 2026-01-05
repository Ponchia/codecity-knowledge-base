---
id: F026
title: Navigation Modes (Vertical & Horizontal)
category: interaction
status: canonical
introduced_by: CC023
implementations: [CodeCity, CodeMetropolis, Code2City, Code2CityVR, Code Park, JSCity, SecCityVR]
related_features: [F001, F056, F064]
taxonomy:
  granularity: [class, function]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-04
updated_from: [CC009, CC020, CC023, CC024, CC035, CC086, CC094, CC102, CC069, CC030, CC126]
---

# Navigation Modes (Vertical & Horizontal)

## Definition

A navigation model that distinguishes between “vertical” navigation (orbit/fly around the city) and “horizontal” navigation (move within the city at street/building level), with physical constraints to preserve orientation.

## Evidence (from CC023)

CC023 describes:
- Vertical navigation: orbiting, flying around, moving forward/backward, changing altitude.
- Horizontal navigation: “driving around” among buildings, constrained by collisions and ground (no passing through buildings; no going below ground).
- The two navigation types are modal (only one active at a time).

## Evidence (from CC009)

CC009 describes Code2CityVR supporting both overhead and in-city navigation:
- Fly over the city (bird’s-eye view).
- Walk around the city and climb buildings (street/building-level exploration).
- Adjust movement speed.

## Evidence (from CC094)

CC094 (JSCity repository) implements two explicit control modes:
- **Orbital**: orbit/pan/zoom navigation around the city (overview-oriented).
- **First-person**: “walk/fly through” navigation using keyboard/mouse controls with adjustable movement speed.

## Evidence (from CC102)

CC102 describes CodeMetropolis supporting both bird’s-eye exploration (flight in Minecraft’s creative mode) and street-level walking to inspect method-level detail.

## Evidence (from CC030)

CC030 argues that metaphor-dependent navigation can be necessary to preserve spatial knowledge in 3D worlds. It illustrates city-metaphor navigation as (a) walking at street level for **route knowledge** and (b) flying at district level for **survey knowledge**, and recommends using different navigation schemes at different metaphor-hierarchy levels.

## Evidence (from CC126)

CC126 (Code Park) uses two viewpoints for navigating code structures:
- **Exocentric (bird’s-eye) view** for overview navigation.
- **Egocentric (first-person) view** for “inside the class” inspection.

It also uses animated transitions (e.g., “go to definition” moves from the current class to bird’s-eye view and then to the destination class) to preserve spatial awareness during navigation.

## Evidence (from CC086)

CC086 describes CodeCity navigation as combining:
- Basic movements like panning and moving forward/backward.
- Orbiting movements on both the vertical and horizontal plane to maintain good perspective.

## Additional Navigation Controls (from CC020)

CC020 lists common navigation actions in CodeCity’s desktop 3D environment, including orbiting, rotation, panning, and moving back and forth.

## Notes (from CC024)

CC024 reiterates desktop navigation as combining panning/moving forward/backward with orbiting movements on both the vertical and horizontal plane to maintain a good city overview perspective.

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

## See Also

- [[ide-synchronized-navigation]] - jump/follow navigation aligned with IDE context
- [[metaphor-aware-navigation]] - assisted navigation adapted to metaphor components
