---
id: F068
title: Island Metaphor (Module Islands)
category: metaphor
status: variant
introduced_by: CC070
implementations: [IslandViz, SoftVis3D]
related_features: [F001, F017, F002]
taxonomy:
  granularity: [module, package, class]
  visual_element: [island, district, building]
  metric_category: [coupling, size]
last_updated: 2026-01-04
updated_from: [CC070, CC076, CC078, CC114]
---

# Island Metaphor (Module Islands)

## Definition

A visualization metaphor that represents a modular software system as an **archipelago**: modules/bundles become islands, packages become regions on each island, and classes become buildings. The metaphor emphasizes decoupling between modules (separate islands) while keeping internal structure readable through nested regions and buildings.

## Mechanism (from CC070)

**Input**: Module/package/class structure plus dependency relationships (e.g., imports/exports and service connections).

**Process**:
1. Create one island per module/bundle.
2. Subdivide each island into package regions sized to accommodate contained classes (often using a space-filling tiling strategy).
3. Place buildings for class types on top of regions and map a size metric (e.g., LOC) to building height/storeys.
4. Render inter-module dependencies between islands (e.g., via ports and arced arrows) and optionally show additional dependency layers (e.g., services).

**Output**: A navigable archipelago that supports module-level overview and package/class drill-down.

## Variations (from CC114)

CC114 adapts the island metaphor to architectural modules defined by a reflexion model: each architecture module becomes an island, with nested package platforms and class/file buildings within each island. Inter-module dependencies are rendered as arrows between islands and can be filtered to show only architectural violations.

## Sources

- [CC070] Schreiber et al. (IEEE 2019) — IslandViz island metaphor for OSGi-based architectures in VR and AR
- [CC076] Heidrich & Schreiber (MuC 2019) — IslandViz demo: OSGi modules as islands on a virtual table
- [CC078] Misiak et al. (IEEE VR 2018) — island metaphor for OSGi bundles on a virtual table with module/service dependencies
- [CC114] Mohsen (2025) — island-based architecture-module layout for integrating reflexion modeling into SoftVis3D

## See Also

- [[city-metaphor]] — related “built environment” metaphor for OO structure
- [[treemap-layout]] — alternative space-filling approach for hierarchical overviews
