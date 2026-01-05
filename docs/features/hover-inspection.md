---
id: F037
title: Hover Inspection (Examine)
category: interaction
status: canonical
introduced_by: CC035
implementations: [CodeCity, GoCity, CodeCharta, JSCity, m3triCity, BabiaXR-CodeCity, VariCity / VariMetrics]
related_features: [F022, F013]
taxonomy:
  granularity: [package, class, method, file, function, module]
  visual_element: [district, building, brick]
  metric_category: [size, complexity, coupling, evolution, quality]
last_updated: 2026-01-04
updated_from: [CC035, CC059, CC091, CC094, CC104, CC096, CC134, CC045]
---

# Hover Inspection (Examine)

## Definition

A details-on-demand interaction that lets users inspect an artifact by hovering over it, revealing the underlying model entity and the values mapped onto its visual properties.

## Mechanism (from CC035)

**Input**: Cursor hover target (district/building/brick).

**Process**:
1. Identify the hovered artifact.
2. Show contextual information (entity identity/type and metric values corresponding to visual encodings).

**Output**: Fast, low-friction inspection without changing selection or view state.

## Evidence (from CC094)

CC094 (JSCity repository) implements hover inspection by raycasting into the 3D scene and, when a block is hovered, displaying the block’s `tooltip`/name (including mapped metric values like LOC) as a details-on-demand label.

## Evidence (from CC059)

CC059 describes m3triCity showing a tooltip with additional information when hovering on elements; the settings panel also includes options for hover labels (e.g., filename and/or author name).

## Evidence (from CC104)

CC104 reports GoCity showing a hover window with LOC, number of methods, and number of attributes for directories, files, and structs.

## Evidence (from CC045)

CC045 describes VariCity using hover to reveal additional relationship links (e.g., additional usage relationships as underground streets and inheritance links) so the default view stays readable while still supporting details-on-demand exploration.

## Evidence (BabiaXR-CodeCity, from CC096)

CC096 describes BabiaXR-CodeCity providing tooltip-based inspection:
- On-screen: hovering the cursor over a building opens a tooltip with the file name and mapped metric values.
- In VR: the same tooltip behavior is triggered via controller raycasting (e.g., Oculus Quest 2 pointing).

## Evidence (BabiaXR repository, from CC134)

CC134 implements hover-based legends in the city components by handling `mouseenter`/`mouseleave` events on buildings to show/hide a label entity (and optionally a highlight box) containing the artifact `id` and mapped metric values.

## Sources

- [CC035] Wettel PhD thesis — “Examine” interaction in CodeCity
- [CC059] Pfahler et al. (2020) — hover tooltips and configurable hover labels in m3triCity
- [CC091] CodeCharta docs — hover a building to see name/metric; click for details
- [CC094] JSCity repository — raycast-based hover tooltip for blocks
- [CC104] GoCity SANER 2019 — hover window with LOC/NOM/NOA for code elements
- [CC096] Moreno-Lumbreras et al. (2022) — hover tooltips on-screen and controller raycasting in VR (BabiaXR-CodeCity)
- [CC134] BabiaXR repository — A-Frame hover events create/remove legend entities for buildings
- [CC045] Mortara et al. (JSS 2024 preprint) — hover reveals additional relationship links in VariCity to reduce clutter
