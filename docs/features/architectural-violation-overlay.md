---
id: F070
title: Architectural Violation Overlay (Reflexion Model)
category: analysis
status: variant
introduced_by: CC114
implementations: [SoftVis3D]
related_features: [F030, F068]
taxonomy:
  granularity: [module, class]
  visual_element: [edge, island, building]
  metric_category: [coupling]
last_updated: 2026-01-04
updated_from: [CC114]
---

# Architectural Violation Overlay (Reflexion Model)

## Definition

A visualization overlay that distinguishes **architecture-conforming** dependencies from **architecture-violating** dependencies using an explicit architecture plan (e.g., a reflexion model), enabling developers to spot architectural erosion and drill down to the concrete classes responsible.

## Mechanism (from CC114)

**Input**:
- Architecture module definitions + allowed module dependencies (architecture plan).
- Mapping from code entities to modules (e.g., regex-based package mapping).
- Observed implementation dependencies (e.g., class-to-class dependency list).

**Process**:
1. Derive module-to-module dependencies by aggregating entity-level dependencies via the entity→module mapping.
2. Compare derived dependencies against the allowed-dependency plan to label dependencies as **valid** vs **violation**.
3. Render module-level dependency arrows and optionally expose underlying class-to-class dependencies on demand.
4. Provide filters (e.g., show only violations) and highlighting for the participating classes.

**Output**: A dependency overlay where violations are visually emphasized (e.g., red arrows) and can be investigated down to the responsible classes.

## Evidence (from CC114)

CC114’s SoftVis3D-based prototype:
- Colors module-to-module arrows to differentiate valid vs violating dependencies (blue vs red).
- Allows filtering to show only violations and highlights the involved buildings (classes) for a selected dependency.

## Sources

- [CC114] Mohsen (2025) — integrates reflexion-model architecture plans into a 3D “code city”/island visualization; visualizes allowed vs violating dependencies with drill-down.
