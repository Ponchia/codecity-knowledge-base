---
id: F011
title: VR Immersion
category: platform
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC015
implementations: [Software World, SynchroVis / ExplorViz, CityVR, VR City, Code2CityVR, SecCityVR, Getaviz, IslandViz]
related_features: [F001, F013]
supersedes: []
taxonomy:
  granularity: [class, function]
  visual_element: [building]
  metric_category: [size, behavior]
last_updated: 2026-01-05
updated_from: [CC009, CC015, CC018, CC053, CC106, CC080, CC069, CC077, CC096, CC131, CC055, CC057, CC064, CC070, CC084]
---

# VR Immersion

## Problem & Motivation

Several implementations extend software cities into VR to leverage embodied navigation and large-scale spatial perception. CC009 reports higher positive affect for a VR city compared to Eclipse, and CC053 explores collaborative VR in ExplorViz for shared comprehension tasks.

## Definition

Rendering and interacting with a software city inside virtual reality (e.g., Oculus Rift, HTC Vive), enabling immersive exploration and natural-scale navigation.

## Context & Applicability

**Use when:**
- Tasks benefit from spatial understanding and navigation (overview vs local inspection), or you want collaborative walkthroughs (CC053, CC009).
- The analysis is primarily structural/visual (low textual density) where immersion can help engagement (CC009).

**Avoid when:**
- Users must read/edit code or long text in the environment; current HMDs are poor for dense text workflows (CC009).
- Sessions are long or users are sensitive to motion sickness/visual strain (CC009).

**Prerequisites:** VR-capable rendering and interaction model (controllers/gaze/raycast selection), strong performance (frame rate), and accessibility/safety considerations (CC009, CC053).
**Alternatives:** [[ar-overlay]] for mixed-reality views, or desktop/Web3D cities when text/UI density matters (e.g., CodeCharta/SoftVis3D).

## Forces

| Force | Pull |
|-------|------|
| Immersion vs. text legibility | VR supports embodied navigation, but dense text (code, long labels) remains hard to read in HMDs. |
| Comfort vs. navigation fidelity | Free movement can increase sickness; teleportation improves comfort but reduces realism and spatial continuity. |
| Hardware constraints vs. accessibility | Immersion requires specialized hardware and strong performance, limiting who can use it. |
| Collaboration vs. cognitive overhead | Multi-user VR can aid shared comprehension, but adds awareness/coordination demands (avatars, pointers, synchronization). |

## Mechanism (Solution)

**Input**: A city model and an interactive camera/controller model.

**Process**:
1. Render the city stereoscopically in VR.
2. Provide interaction modes (translation/rotation/scale; pointing/selection).
3. Optionally integrate source code or runtime traces via overlays.

**Output**: Immersive, interactive software city exploration.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Can improve engagement and support embodied spatial reasoning for large structures. | VR side effects and comfort constraints can limit session length and user adoption. |
| Enables natural-scale walkthroughs and collaborative exploration in a shared space. | Travel time and interaction friction can make some tasks slower than 2D dashboards/IDEs. |

**Complexity**: High
**Performance**: Rendering and input constraints can be significant (VR/AR).
**Cognitive Load**: Medium–High (new interaction paradigms).

## Variations

| Implementation style | Example | Notes |
|----------------------|---------|------|
| In-city immersion | SecCityVR | User is “inside” the city; locomotion includes flying and ground teleportation (CC069). |
| World-in-miniature / tabletop | IslandViz | A virtual-table setup for exploring an artifact as a manipulable object (CC070). |
| Room-scale walking + teleport | VR City | Uses room-scale where possible plus teleportation for long distances (CC106). |
| CAVE / room VR | Imsovision | Targets a CAVE-style immersive environment for stereopsis and physical navigation (CC057). |
| Web-based VR mode | BabiaXR-CodeCity / ExplorViz | Browser/WebXR or WebVR-based VR access paths (CC096, CC077, CC080). |

## Implementation Notes

### Notes (from CC015)

CC015 highlights a practical constraint: current head-mounted displays remain limited for large quantities of text, contributing to a split between “high-text desktop” and “low-text VR” cities.

CC018’s systematic mapping study reports that most identified city-metaphor tools do not use extended reality (85% non-XR), but also highlights a growing trend toward XR usage, indicating an opportunity for further research and broader adoption.

CC053 describes ExplorViz’s VR evolution: after adding a single-user VR mode (as an alternative to screen-based visualization), ExplorViz introduced a first multi-user VR approach in 2019 and a fully collaborative multi-user VR approach in 2020.

CC077’s “About” page highlights a modern web/XR stack for ExplorViz (WebXR), positioning AR/VR as part of its “higher immersion” interaction research.

CC009 describes Code2CityVR (Oculus Rift) as supporting immersive city navigation (fly-over, street-level walking/climbing) and search input via a virtual keyboard with text completion. It also reports that VR improved positive affect compared to Eclipse, but that most participants reported at least one VR side effect (e.g., headache, nausea, visual annoyance).

CC055 adds implementation detail for Code2City’s VR mode, including Oculus Rift + Xbox controller interaction (gaze-based selection) and a reported rendering performance of ~45 FPS in VR on a FindBugs city.

CC057 describes Imsovision targeting the **CAVE** (room-sized stereoscopic VR) and motivates immersive VR for software visualization using stereopsis and physical navigation (walking/crouching) as advantages over conventional 3D desktop views.

CC064 reports a controlled experiment comparing Eclipse vs a city-metaphor tool on-screen vs the same city-metaphor tool in immersive VR (Oculus Rift): both city-metaphor treatments improve correctness vs Eclipse, and the VR treatment is significantly faster than the on-screen city while also reporting frequent VR side effects.

CC096 compares on-screen and immersive VR usage of the same web-based CodeCity implementation (BabiaXR-CodeCity) in two controlled experiments (n=24 and n=26). It reports that VR participants completed tasks significantly faster while maintaining comparable correctness to on-screen participants.

CC069 reports SecCityVR on Meta Quest, focused on VR visualization of security vulnerabilities with call-graph overlays; a user study (n=17) found higher SUS usability and lower temporal demand/frustration than a dashboard, despite longer task times.

CC131’s Getaviz README states that generated visualizations can be explored in VR on both HTC Vive and Oculus Rift.

CC070 describes IslandViz on Oculus Rift / HTC Vive, using a virtual-table setup (“world-in-miniature”) to explore an island metaphor for OSGi-based architectures.

CC084 describes an early gesture-controlled ExplorViz VR approach using an Oculus Rift DK1 and Microsoft Kinect v2, enabling translation/rotation/scale interactions beyond mouse/keyboard.

### Notes (from CC080)

CC080’s archived ExplorViz web client includes a WebVR mode that integrates Oculus rendering with Leap Motion hand tracking (VRControls/VREffect + Leap libraries), and the README highlights experiments with Kinect v2 and Oculus Rift.

### Notes (from CC106)

CC106 describes VR City on HTC Vive, leveraging room-scale tracking for natural navigation by walking and using teleportation to reach distant parts of a city when the physical play area is insufficient. Object interaction is performed with handheld controllers via pointing (selection), triggering actions, and grabbing/moving elements.

## Known Limitations

- Motion/visual side effects (headache, nausea, visual annoyance) are common for some users (CC009).
- Text legibility and data entry are constrained; many workflows still require an IDE on a 2D screen (CC009).
- Rendering large cities at VR frame rates may require aggressive LOD/culling, reducing detail.

## Evidence

- CC009 reports significantly higher positive affect for a VR city compared to Eclipse, but also reports frequent VR side effects.
- CC064 reports both on-screen and VR city conditions improving correctness versus Eclipse, and reports the VR condition being faster than the on-screen city while also noting VR side effects.
- CC096 reports two controlled experiments comparing on-screen vs VR for the same web-based city, finding VR users completed tasks faster with comparable correctness.
- CC069 reports a user study comparing SecCityVR to a dashboard baseline: higher usability and lower temporal demand/frustration in VR, but longer task times attributed largely to travel time in the city.

## Open Questions

- What interaction patterns best support “text-heavy” workflows (code reading, search, editing) without breaking VR comfort constraints?
- How can VR cities reduce travel time while preserving the locality benefits that motivate the city metaphor?
- What are effective multi-user awareness cues (pointers, view frustums, annotations) that improve collaboration without cluttering the scene?

## Sources

- [CC015] Jeffery survey — Table 1 and conclusion
- [CC018] Moreno-Lumbreras et al. (JSS 2024) — systematic mapping highlighting XR adoption trends and gaps
- [CC053] Hasselbring et al. (Software Impacts 2020) — ExplorViz VR timeline and collaborative multi-user VR
- [CC077] ExplorViz “About” page — WebXR-based AR/VR positioning
- [CC009] Romano et al. (2019) — Code2CityVR tool description and controlled experiment on feelings/emotions/thinking
- [CC096] Moreno-Lumbreras et al. (2022) — controlled experiments comparing on-screen vs VR CodeCity (BabiaXR-CodeCity)
- [CC106] Vincúr et al. (QRS-C 2017) — VR City interaction/navigation using HTC Vive (walking + teleportation)
- [CC080] ExplorViz archived repo — WebVR/Leap Motion integration and VR interaction stack
- [CC069] Wueppelmann & Yigitbas (2025) — SecCityVR VR vulnerability visualization with user study vs dashboard
- [CC131] Getaviz repository — VR exploration via HTC Vive and Oculus Rift
- [CC055] Code2City project report — UE4-based Code2City in VR (Oculus Rift + controller interaction)
- [CC057] Maletic et al. (ICSE 2001) — Imsovision in the CAVE and rationale for immersive VR software visualization
- [CC064] Romano et al. (IST 2019) — controlled experiment: Eclipse vs screen city vs VR city (correctness/time + side effects)
- [CC070] Schreiber et al. (IEEE 2019) — IslandViz in Oculus Rift/HTC Vive with a virtual-table interaction model
- [CC084] Fittkau dissertation (2015/2016) — ExplorViz gesture-controlled VR (Oculus Rift DK1 + Kinect v2) and interaction design beyond 2D

## See Also

- [[ar-overlay]] — related mixed-reality variant
- [[source-code-display]] — text-heavy overlays/inside-building code
