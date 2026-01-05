---
id: F012
title: AR Overlay
category: platform
status: variant
introduced_by: CC015
implementations: [SkyscrapAR, SynchroVis / ExplorViz, IslandViz]
related_features: [F001, F015]
taxonomy:
  granularity: [class, module, package]
  visual_element: [building, district, island]
  metric_category: [size, behavior, evolution]
last_updated: 2026-01-04
updated_from: [CC015, CC018, CC071, CC077, CC070]
---

# AR Overlay

## Definition

An augmented reality variant of the software city where the 3D city is overlaid onto the physical world (e.g., projected onto a marker card or viewed through AR devices).

## Mechanism

**Input**: A city model + an AR anchoring/tracking mechanism (e.g., marker tracking or device-based spatial tracking).

**Process**:
1. Establish an anchor in physical space (marker, plane, or world-anchor).
2. Render the city aligned to the anchor.
3. Allow direct manipulation (rotate/scale/translate) via gestures or controllers.

**Output**: A manipulable city overlayed on a physical surface.

## Evidence (from CC015)

CC015 describes SkyscrapAR projecting the city onto a physical marker card for direct manipulation; it also notes follow-on exploration on HoloLens.

CC018’s systematic mapping study reports that most identified city-metaphor tools do not use extended reality (85% non-XR), suggesting AR remains underexplored relative to non-XR platforms despite a growing XR trend.

CC071 and CC077 indicate that ExplorViz provides an AR environment (via web/XR technology) where the city visualization is available, including the heat-map overlay described in CC071.

CC070 describes IslandViz providing an AR mode on Microsoft HoloLens for an island-metaphor visualization, using gesture, gaze, and voice input (including Air-Tap selection and Tap-and-Hold-based zoom/pan on a virtual tabletop).

## Sources

- [CC015] Jeffery survey — SkyscrapAR description
- [CC018] Moreno-Lumbreras et al. (JSS 2024) — systematic mapping highlighting XR adoption trends and gaps
- [CC071] Krause et al. (2021) — ExplorViz heat-map overlay is also available in the AR environment
- [CC077] ExplorViz “About” page — web-based tool highlighting WebXR-based AR/VR support
- [CC070] Schreiber et al. (IEEE 2019) — IslandViz AR mode on HoloLens with gesture/gaze/voice interaction

## See Also

- [[vr-immersion]] — VR counterpart
- [[evolution-visualization]] — churn-based encodings used in AR examples
