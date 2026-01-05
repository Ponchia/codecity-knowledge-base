---
id: F013
title: Source Code Display
category: interaction
status: variant
introduced_by: CC023
implementations: [CodeCity, GoCity, CityVR, VR City, Code Park, SoftVis3D, SynchroVis / ExplorViz]
related_features: [F001, F006]
taxonomy:
  granularity: [file, class]
  visual_element: [building]
  metric_category: [size, behavior]
last_updated: 2026-01-04
updated_from: [CC015, CC023, CC035, CC040, CC025, CC106, CC080, CC104, CC057, CC126]
---

# Source Code Display

## Definition

An interaction feature that presents actual source code in-context within the city (e.g., on building walls) or via overlays (e.g., a translucent HUD), enabling navigation from spatial structures to concrete code.

## Mechanism

**Input**: Source code text linked to city entities.

**Process**:
1. Select a building/entity.
2. Retrieve and render the associated source code.
3. Provide navigation affordances (definitions/usages, scrolling, etc.).

**Output**: A city visualization that doubles as a code navigation interface.

## Examples (from CC015 / CC023)

- CodeCity: context menu can access the represented source code.
- CityVR: source code shown in a translucent 2D heads-up display.
- Code Park: source code rendered as syntax-aware “wallpaper” on the walls of a class “room”, with IDE-like navigation (e.g., go-to-definition) that uses animated transitions to preserve orientation. (CC126)

CC035 further notes that CodeCity allows viewing the source code of any visualized class (as part of the baseline/tool comparison in the controlled experiment design). CC025 describes this as unidirectional linking from a city artifact to the represented source code.

CC057 notes that immersive VR environments can allow users to access external information such as source code without leaving the visualization context (e.g., using a palmtop or laptop inside the VR environment).

## Evidence (from CC080)

CC080 shows ExplorViz exposing a context-menu action (“Inspect source code”) that opens a CodeMirror-based viewer and fetches code via a server-side CodeViewer service.

## Evidence (from CC104)

CC104 reports GoCity providing a button that opens the selected directory, file, or struct directly on GitHub.

## Variations (SoftVis3D, from CC040)

CC040 shows SoftVis3D providing source-code access by opening SonarQube’s code view for the selected file in a new browser window/tab (linking out from the city to the platform’s code viewer rather than rendering code directly in the 3D scene).

## Evidence (from CC106)

CC106 describes VR City providing in-VR source-code browsing via “code labels”:
- Clicking a method floor creates a label showing class information (e.g., modifiers and qualified name) and method header.
- The label can be extended to include the method body.
- Labels remain linked to the corresponding floor and can be freely moved in 3D space using controllers, enabling a user-created spatial workspace.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — CodeCity context-menu access to source code
- [CC035] Wettel PhD thesis — explicit “view the source code of any visualized class” capability
- [CC025] Wettel & Lanza (ICSE 2011) — CodeCity unidirectional linking from visualization to source code
- [CC015] Jeffery survey — CityVR and Code Park descriptions; Table 1 (“Src” column)
- [CC106] Vincúr et al. (QRS-C 2017) — VR City code labels in VR (headers, bodies, movable workspace)
- [CC040] SoftVis3D repository — selected-file “Open file” action opens SonarQube code view
- [CC080] ExplorViz archived repo — CodeMirror code viewer and “Inspect source code” context menu
- [CC104] GoCity SANER 2019 — GitHub “open file” action for selected elements
- [CC057] Maletic et al. (ICSE 2001) — in-VR access to external information (e.g., source code) discussed as a VE advantage
- [CC126] Khaloo et al. (VISSOFT 2017) — Code Park: source-code-on-walls “wallpaper” and code navigation in a 3D environment

## See Also

- [[color-mapping]] — translucence/brightness often used for overlays
