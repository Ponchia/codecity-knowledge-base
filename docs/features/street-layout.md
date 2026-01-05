---
id: F009
title: Street Layout
category: layout
status: variant
introduced_by: CC015
implementations: [EvoStreets, CrocoCosmos, CodeCharta, SoftVis3D]
related_features: [F001, F015]
taxonomy:
  granularity: [file, class]
  visual_element: [street, building]
  metric_category: [size, evolution]
last_updated: 2026-01-05
updated_from: [CC015, CC038, CC040, CC091, CC128, CC101]
---

# Street Layout

## Definition

A layout approach that organizes buildings around streets, using street structure to represent packages/directories and improve navigability and spatial orientation.

## Mechanism

**Input**: Hierarchy (directories/packages) and entities (e.g., classes).

**Process**:
1. Create streets corresponding to groupings (directories/packages).
2. Place buildings (entities) along/around streets.
3. Optionally use map-like cues (elevation/topography) for temporal attributes.
4. Preserve layout consistency over evolution by appending new elements at street ends and keeping removed elements faintly visible.

**Output**: A city where streets are first-class organizing elements.

## Evidence (from CC015)

CC015 describes EvoStreets laying out classes around streets corresponding to directories or packages, with origin date conveyed via topographic elevation.

CC091 documents CodeCharta offering street-like layouts where directories are represented as streets and file nodes as buildings (including hybrid street/treemap variants).

CC038 describes an “Evostreet” layout as a stable layout for evolving software systems. The embedded `visualizationStatus` configuration further describes each street as representing a subsystem (folder/package), with branching streets indicating containment.

CC128 (the `codecity-visualizer` library used by SoftVis3D) implements an Evostreet illustrator focused on long-term consistency. It exposes configuration options for street/highway geometry, house sizes/margins, and layout constraints (e.g., preventing “snails” — winding streets without houses), and it documents a `StreetContainer` that supports configurable distribution and segmentation of houses/branches along the road.

CC101 specifies the EvoStreets construction: inner nodes are rendered as straight lines (streets) and leaf nodes as square rectangles attached to their parent street. Rectangle size typically encodes coupling. For consistency across versions, new nodes are attached to the far end of their parent street, removed nodes remain (e.g., transparent), and sibling order/side placement is preserved over time.

## Sources

- [CC015] Jeffery survey — EvoStreets description and Table 1
- [CC091] CodeCharta repo/docs — StreetMap and hybrid street/treemap layouts
- [CC038] SoftVis3D website — “Evostreet” stable layout option + subsystem-as-street description
- [CC040] SoftVis3D repository — uses an Evostreet illustrator with street/subsystem containment semantics
- [CC128] codecity-visualizer repository — Evostreet illustrator configuration and StreetContainer placement options
- [CC101] Steinbrückner dissertation — EvoStreets layout construction and evolution-consistency rules

## See Also

- [[treemap-layout]] — space-filling alternative
- [[evolution-visualization]] — temporal properties shown via date/elevation
