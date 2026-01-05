---
id: F002
title: Class-as-Building Mapping
category: mapping
status: canonical
introduced_by: CC023
implementations: [CodeCity, SkyscrapAR, VizzAspectJ-3D, EvoStreets, SynchroVis / ExplorViz, CityVR, VR City, Code Park, Code2City, Code2CityVR, m3triCity, Langelier Quality Visualization Framework, SecCityVR, VariCity / VariMetrics]
related_features: [F001, F017, F003, F004, F005]
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [size, evolution, behavior, variability]
last_updated: 2026-01-04
updated_from: [CC009, CC015, CC017, CC020, CC023, CC024, CC035, CC059, CC075, CC069, CC045]
---

# Class-as-Building Mapping

## Definition

A concept mapping where each object-oriented class is represented as a single building in the software city. Building dimensions encode class-level metrics (methods, attributes, LOC), enabling visualization of systems with thousands of classes.

## Mechanism

**Input**: Class from object-oriented system

**Process**:
1. Extract class from source/model
2. Calculate metrics (NOM, NOA, LOC)
3. Map metrics to building dimensions
4. Position within package/district

**Output**: 3D building representing the class

## Rationale

CC023 argues that classes (together with their packages) are a primary orientation point for developers, and that using class granularity preserves realism and scalability.

Compared to method-as-building (F003), this approach trades fine-grained detail for scalability.

## Variations

| Implementation | Notable details (from CC015) |
|----------------|------------------------------|
| CodeCity | Height proportional to number of methods; footprint proportional to number of member variables; treemap layout with terrain elevation for package nesting. |
| SkyscrapAR | Similar to CodeCity but uses churn for building height; projected onto a physical marker card for AR manipulation. |
| VizzAspectJ-3D | Extends CodeCity to represent both classes and aspects as buildings; aspect height uses number of pointcuts/advice; includes multiple color-coded views. |
| CityVR | VR (HTC Vive) implementation generated from CodeCity; brightness indicates LOC; source code can be shown in a translucent HUD. |
| VR City | Uses coupling-driven organic layout; supports revision-log highlighting (e.g., author commits) and call-trace overlays. |
| SynchroVis / ExplorViz | Visualizes runtime: per-instance depiction via “storeys”; threads shown with colored arrows; supports VR interaction (translation/rotation/scale). |
| m3triCity | Evolution-first web city; refactorings are shown as explicit movements with arcs (history-resistant layout keeps positions stable). |
| Langelier Quality Visualization Framework | Represents each class as a simple 3D box to support large-scale quality analysis. |
| SecCityVR | Buildings contain method floors colored by vulnerability severity; methods slightly wider than building footprint to emphasize issues. |
| VariCity / VariMetrics | CC045 maps variability-related OO-mechanism metrics to class-building dimensions (e.g., method variants as height and constructor variants as width) to surface variability hotspots. |

## Evidence

CC023 demonstrates the mapping at scale; CC015 later reports class granularity as the dominant choice across surveyed implementations.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — packages as districts; classes as buildings; NOM/NOA mappings
- [CC035] Wettel PhD thesis — concept mapping rationale + magnitude mapping (NOM/NOA/LOC)
- [CC015] Jeffery survey — later survey reporting class-level granularity dominance
- [CC017] Wettel CodeCity homepage — classes represented as buildings
- [CC009] Romano et al. (2019) — Code2City/Code2CityVR tool description using types (classes/interfaces) as buildings
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — classes depicted as buildings (CodeCity)
- [CC024] Wettel & Lanza (WASDeTT 2008) — CodeCity nutshell mapping (classes as buildings)
- [CC059] Pfahler et al. (2020) — classes depicted as buildings in an evolving web-based city (m3triCity)
- [CC075] Langelier et al. (ASE 2005) — class-level 3D box representation for quality analysis
- [CC045] Mortara et al. (JSS 2024 preprint) — uses class buildings to encode variability metrics for hotspot detection (VariCity)

## See Also

- [[function-as-building]] — finer granularity alternative
- [[height-mapping]] — how building height encodes metrics
