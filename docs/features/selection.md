---
id: F022
title: Selection
category: interaction
status: canonical
introduced_by: CC023
implementations: [CodeCity, Code2City, Code2CityVR, VR City, SoftVis3D, SoftViz3D, m3triCity, DynaCity, BabiaXR-CodeCity, IslandViz]
related_features: [F024, F025, F023, F049, F056]
taxonomy:
  granularity: [file, class, package, module]
  visual_element: [building, district, floor, island]
  metric_category: [size]
last_updated: 2026-01-04
updated_from: [CC009, CC023, CC024, CC035, CC040, CC043, CC059, CC106, CC103, CC133, CC134, CC137, CC070]
---

# Selection

## Definition

An interaction that lets the user select one or more entities (buildings or districts) to inspect, modify, or use as input for other operations.

## Mechanism (from CC023)

CC023 describes selection as:
- Manual clicking on elements.
- Programmatic selection via a query mechanism.

Common operations include adding/removing elements, clearing, and inverting the selection.

## Variations (from CC009)

CC009 describes selection in Code2City and Code2CityVR as:
- **Code2City**: choose an object (building/district) via a viewfinder; selection is highlighted and a details panel is shown.
- **Code2CityVR**: gaze at an object and press a controller button to select it.

CC106 describes VR City selection as pointing at an object with a controller pointer and triggering interactions via the controller’s trigger/grip controls (e.g., selecting, grabbing).

## Variations (IslandViz, from CC070)

CC070 describes selection in IslandViz across XR modalities:
- **VR (Oculus Rift / HTC Vive)**: users select islands/bundles and other elements on a virtual table using controller-based pointing and interaction.
- **AR (HoloLens)**: bundles can be selected with an Air-Tap gesture; the selected bundle is highlighted with a wireframe.

## Notes (from CC024)

CC024 describes interacting with city artifacts via contextual menus and a query mechanism; the visualization window includes an information panel that shows details for the currently focused element.

## Variations (SoftVis3D, from CC040)

CC040 shows SoftVis3D supporting click-based selection via raycasting into the 3D scene. The UI exposes selected-entity actions (e.g., opening SonarQube’s code view or measures view for the selected file) and includes the selection in shareable links by serializing `selectedObjectKey` into the `visualizationStatus` URL parameter.

## Variations (SoftViz3D, from CC043)

CC043 implements click-based selection in an X3DOM-rendered scene: selecting a layer or leaf changes its material color (focus highlight) and updates a sidebar details panel via AJAX.

## Variations (m3triCity, from CC059)

CC059 describes selection being used to drive other evolution UI components: when users select an object, the evolution timeline highlights all commits involving the entity. CC059 also uses selection as the input for [[elision]] (removing selected objects from the view).

## Variations (DynaCity, from CC133)

CC133 implements click-based selection in Unity: pressing the mouse on a building shows a label with the component name and triggers a selection-scoped dependency overlay; releasing the mouse clears the label and restores the full dependency view.

CC137 contains the same selection-driven dependency filtering pattern in the Holoware/DynaCity codebase (via click and release events).

## Variations (BabiaXR, from CC134)

CC134 implements selection in A-Frame by attaching click handlers to buildings and “quarters” and tagging selectable entities with a CSS class (`babiaxraycasterclass`) used by the scene’s raycaster configuration. Selection toggles details-on-demand legends/highlights for the chosen entity.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — selection interaction
- [CC035] Wettel PhD thesis — selection operations and use as context for other interactions
- [CC009] Romano et al. (2019) — viewfinder and gaze-based selection (Code2City/Code2CityVR)
- [CC024] Wettel & Lanza (WASDeTT 2008) — contextual menus + information panel for focused element
- [CC106] Vincúr et al. (QRS-C 2017) — VR City controller-based pointing and selection
- [CC040] SoftVis3D repository — click/raycast selection + selected-file actions + selection in share links
- [CC043] SoftViz3D repository — click selection with focus highlighting + sidebar details
- [CC059] Pfahler et al. (2020) — selection-linked timeline highlights and selection-driven elision
- [CC133] DynaCity repository — Unity click selection with label and selection-scoped dependency overlay
- [CC134] BabiaXR repository — click selection on buildings/quarters with raycaster-targeted entities and toggleable legends
- [CC137] Holoware software-city repository — Unity selection events used to drive dependency filtering
- [CC070] Schreiber et al. (IEEE 2019) — IslandViz selection in VR and HoloLens AR (Air-Tap)

## See Also

- [[ide-synchronized-navigation]] — IDE-driven “jump/follow” navigation to the current code context
