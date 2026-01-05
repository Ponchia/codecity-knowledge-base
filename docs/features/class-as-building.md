---
id: F002
title: Class-as-Building Mapping
category: mapping
status: canonical
maturity: established
bounded_context: [city-metaphor]
introduced_by: CC023
implementations: [CodeCity, SkyscrapAR, VizzAspectJ-3D, EvoStreets, SynchroVis / ExplorViz, CityVR, VR City, Code Park, Code2City, Code2CityVR, m3triCity, Langelier Quality Visualization Framework, SecCityVR, VariCity / VariMetrics]
related_features: [F001, F017, F003, F004, F005]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [size, evolution, behavior, variability]
last_updated: 2026-01-05
updated_from: [CC009, CC015, CC017, CC020, CC023, CC024, CC035, CC059, CC075, CC069, CC045, CC036, CC085, CC091]
---

# Class-as-Building Mapping

## Problem & Motivation

CC023 argues that classes (together with their packages) are a primary orientation point for developers, and that using class granularity preserves realism and scalability.

Compared to method-as-building (F003), this approach trades fine-grained detail for scalability.

## Definition

A concept mapping where each object-oriented class is represented as a single building in the software city. Building dimensions encode class-level metrics (methods, attributes, LOC), enabling visualization of systems with thousands of classes.

## Context & Applicability

**Use when:**
- You need a scalable overview at object-oriented granularity where classes are a primary comprehension unit (CC023, CC015, CC035).
- You want stable orientation points for package/district navigation and for layering quality/evolution overlays (CC023, CC035).

**Avoid when:**
- You need fine-grained details inside classes by default (use method-level features or drill-down views) (CC035).
- The system is not naturally class-oriented; prefer file/function/module mappings instead (CC036, CC091).

**Prerequisites:** An OO model with classes and their containment (packages/namespaces) plus class-level metrics (e.g., NOM/NOA/LOC) and a mapping strategy for height/footprint/color.
**Alternatives:** [[file-as-building]], [[function-as-building]], [[component-as-building]], or finer-grained internals via [[method-as-bricks]] / [[method-as-floors]].

## Forces

| Force | Pull |
|-------|------|
| Overview scalability vs. internal detail | One building per class makes large systems tractable, but hides within-class structure unless complemented by finer-grained views. |
| OO realism vs. language generality | Classes are a natural “building” unit in OO systems, but the mapping becomes awkward for non-class-centric languages. |
| Stable landmarks vs. split/merge accuracy | Treat a class as one landmark to support navigation and overlays, but refactorings and multi-responsibility classes can blur meaning. |

## Mechanism (Solution)

**Input**: Class from object-oriented system

**Process**:
1. Extract class from source/model
2. Calculate metrics (NOM, NOA, LOC)
3. Map metrics to building dimensions
4. Position within package/district

**Output**: 3D building representing the class

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Scales well: thousands of classes become navigable landmarks. | Hides intra-class structure unless paired with method-level representations or drill-down. |
| Aligns with common developer mental models (classes/packages). | Biases the visualization toward OO and can mislead when “class” is not the main modular unit. |

**Complexity**: Low
**Performance**: Typically cheap; depends on recomputation frequency.
**Cognitive Load**: Low–Medium (depends on legend/scale).

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
| SecCityVR | Buildings contain method floors colored by vulnerability severity; methods slightly wider than building footprint to emphasize issues. (CC069) |
| VariCity / VariMetrics | CC045 maps variability-related OO-mechanism metrics to class-building dimensions (e.g., method variants as height and constructor variants as width) to surface variability hotspots. |

## Implementation Notes

- Use stable identifiers (e.g., fully-qualified names or FAMIX entities) so selection/overlays map reliably across views (CC023, CC024, CC035).
- Start with simple cuboid glyphs and magnitude mappings (e.g., NOM height, NOA footprint, LOC color) and offer discretized mapping for habitability when needed (CC023, CC035, CC085).
- Keep detail on demand: show fine-grained elements (methods/relations) via drill-down, selection-scoped queries, or separate views (CC023, CC035).

## Evidence

CC023 demonstrates the mapping at scale; CC015 later reports class granularity as the dominant choice across surveyed implementations.

## Known Limitations

- Class granularity hides intra-class structure unless complemented with drill-down or fine-grained representations (CC023, CC035).
- Very large systems can slow interactivity/navigation without optimization (CC023).
- The mapping is OO-centric; usefulness depends on how well classes align with conceptual modules in the given codebase (CC015).

## Open Questions

- When should a “class building” be split into multiple sub-buildings (e.g., by inner classes, responsibilities, or architectural roles)?
- How should class-level buildings represent cross-cutting structures (aspects, mixins, traits) without confusing the mapping?
- What are good defaults for non-OO systems (files, functions, modules) that preserve the same “landmark” benefits?

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
- [CC036] Viana et al. (arXiv 2017) — counterexample adaptation: function-level buildings for JavaScript systems (JSCity)
- [CC091] CodeCharta docs — file-as-building alternative mapping used in practice
- [CC085] Wettel & Lanza (ICPC 2007) — habitability framing and discretized building archetypes/mapping strategies
- [CC069] Wueppelmann & Yigitbas (2025) — SecCityVR uses class buildings (with method-level overlays) in VR

## See Also

- [[function-as-building]] — finer granularity alternative
- [[height-mapping]] — how building height encodes metrics
