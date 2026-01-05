---
id: F030
title: Contextual Dependency View
category: interaction
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC035
implementations: [CodeCity, SoftViz3D, SoftVis3D, SecCityVR, DynaCity]
related_features: [F022, F023, F029, F047, F048, F057]
supersedes: []
taxonomy:
  granularity: [file, class, package]
  visual_element: [edge]
  metric_category: [coupling]
last_updated: 2026-01-05
updated_from: [CC035, CC043, CC086, CC069, CC114, CC129, CC133, CC137, CC023, CC053, CC106]
---

# Contextual Dependency View

## Problem & Motivation

Rendering all dependencies in a city can lead to visual occlusion and reduced realism. CC023 notes that global edge rendering is not feasible at scale, motivating on-demand/context-scoped dependency visualization; CC035 formalizes this as a contextual dependency interaction.

## Definition

An interaction that visualizes dependencies only for the current selection (or a reduced scope), avoiding the clutter of rendering all relations globally.

## Context & Applicability

**Use when:**
- You want to understand dependencies of a selected entity/package without cluttering the entire city (CC035, CC114).
- You need interactive drill-down from coarse to fine dependency representations on demand (CC114, CC129).

**Avoid when:**
- The task requires a global dependency graph overview across the whole system; a dedicated graph view may be more appropriate.
- Dependency data is incomplete/ambiguous for the language (dynamic dispatch/reflection); interpret edges cautiously (uncertain).

**Prerequisites:** A dependency model (calls/accesses/imports), a selection scope, and edge rendering/filtering controls (CC035, CC043).
**Alternatives:** [[bundled-edge-relations]] / [[dependency-path-expansion]] for aggregation, or [[query-filtering]] to find related artifacts without drawing all edges.

## Forces

| Force | Pull |
|-------|------|
| Global overview vs. readability | Show enough relations to answer dependency questions, but avoid hairballs and occlusion. |
| Detail-on-demand vs. discoverability | Keep the default view clean, but ensure users can easily discover how to reveal the right dependencies. |
| Structural context vs. edge emphasis | Preserve containment landmarks, but make edges legible (routing, bundling, weighting) within the local scope. |

## Mechanism (Solution)

**Input**: Selection scope + dependency types (inheritance, invocation, access) and direction (incoming/outgoing).

**Process**:
1. Treat the current selection as the context boundary (e.g., package selection expands scope to its classes).
2. Query dependencies for the context.
3. Render only those dependency edges, with user-controlled colors and filters.

**Output**: A focused dependency overlay tied to the selection context.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Makes dependency exploration feasible by avoiding global edge clutter. | Users can miss important long-range dependencies if scope rules are unclear or too narrow. |
| Supports progressive disclosure (module → class → method) in context. | Adds interaction modes and UI state that must be communicated clearly to avoid confusion. |

**Complexity**: Medium
**Performance**: Depends on picking/raycasting and UI update costs.
**Cognitive Load**: Medium (requires learning controls and feedback).

## Variations

### Variations (SoftViz3D, from CC043)

CC043 implements a dedicated “dependency view” that renders dependency edges within the current hierarchical scope (layer) rather than visualizing all dependencies globally. It supports a detail-oriented mode that shows more dependency edges and a metric-oriented mode that focuses on aggregated path edges; edges are weighted (thicker) based on an underlying dependency count.

### Variations (SoftVis3D, from CC129)

CC129 (deprecated Sonar plugin) also provides a dedicated dependency view scoped to the current hierarchy layer. It expands leaf dependencies into hierarchy-following “path” edges and aggregates multiple dependencies onto shared edges, using Graphviz attributes (e.g., `penwidth`) to visually weight edges by the aggregated count.

### Variations (SecCityVR, from CC069)

SecCityVR lets users toggle call-graph edges for vulnerable methods only; arcs are colored blue-white and activated on demand to reduce clutter while inspecting security issue propagation.

### Variations (DynaCity, from CC133)

DynaCity overlays dynamic dependency arcs and uses selection as the context boundary: clicking a component hides all dependency lines except those associated with the selected component, and releasing restores all lines.

CC137 shows the same interaction pattern in the Holoware/DynaCity codebase (selection-scoped arc filtering). It also includes a questionnaire spreadsheet about whether reduced dependency views and use-case filters help common software tasks, providing evidence that “show only relevant dependencies” is a motivated interaction design.

### Variations (SoftVis3D reflexion-model prototype, from CC114)

CC114 describes a SoftVis3D-based prototype that initially shows only module-to-module dependency arrows. Selecting a module-level dependency reveals the underlying class-to-class arrows for that relationship on demand, avoiding the clutter of rendering all dependencies at once. It also provides a “show only violations” filter to focus on architecture-violating dependencies.

## Implementation Notes

CC086 describes CodeCity offering selection-relative queries such as “classes which invoke methods of the selected ones”, reinforcing the idea of scoping dependency exploration to the current context instead of rendering global relations.

## Known Limitations

- Even within scope, dense dependency neighborhoods can clutter; aggregation/bundling helps (CC043, CC129).
- Context scoping can hide long-range dependencies unless users intentionally expand scope.
- Static dependency extraction may miss runtime behavior; complement with [[dynamic-visualization]] when needed (CC053, CC106).

## Evidence

- CC035 frames “view contextual dependencies” as a way to avoid global edge rendering while still supporting dependency understanding during exploration.
- CC114 and CC129 describe drill-down patterns (module-level arrows first; reveal class-level arrows on demand) that preserve readability by deferring detail.
- CC069 applies the same contextual principle to security: toggle call-graph edges for vulnerable methods only, on demand.

## Open Questions

- What are the best default scope rules (entity vs package vs component) for contextual dependencies to minimize user effort and surprise?
- Which edge-routing/aggregation techniques remain readable in 3D without harming the underlying city realism?
- How should tools communicate “hidden edges” so users do not draw false conclusions from an incomplete view?

## Sources

- [CC035] Wettel PhD thesis — “view contextual dependencies” interaction in CodeCity
- [CC023] Wettel & Lanza (VISSOFT 2007) — motivation to avoid global dependency edges; on-demand/context-scoped exploration
- [CC086] Wettel & Lanza (2008) — selection-relative dependency queries (invocation-based context)
- [CC043] SoftViz3D repository — dependency view scoped to hierarchy layers (detail vs metric)
- [CC129] sonar-softvis3d-plugin repository — dependency view scoped to hierarchy layers with dependency aggregation and edge weighting
- [CC069] Wueppelmann & Yigitbas (2025) — SecCityVR toggles call-graph edges for vulnerable methods on demand
- [CC133] DynaCity repository — selection-scoped dependency-line visualization for dynamic dependencies
- [CC137] Holoware software-city repository — selection-scoped dependency filtering and filter-preference questionnaire data
- [CC114] Mohsen (2025) — on-demand drill-down from module-to-module to class-to-class dependency arrows in a SoftVis3D-based prototype
- [CC053] Hasselbring et al. (Software Impacts 2020) — ExplorViz dynamic trace visualization context for runtime dependencies
- [CC106] Vincúr et al. (QRS-C 2017) — VR City trace mode for dynamic behavior that static dependencies may miss

## See Also

- [[dependency-path-expansion]] — hierarchy-aware aggregation for dependency edges
- [[edge-thickness-mapping]] — visual encoding for relation strength
- [[vulnerability-overlay]] — contextual call-graph edges used to explore security issue propagation (SecCityVR)
