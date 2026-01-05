---
id: F029
title: Bundled Edge Relations
category: analysis
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC035
implementations: [CodeCity, m3triCity]
related_features: [F030, F023, F026]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [edge]
  metric_category: [coupling]
last_updated: 2026-01-05
updated_from: [CC035, CC059]
---

# Bundled Edge Relations

## Problem & Motivation

This capability helps connect analysis results to the system’s structural and spatial context. A relation-visualization technique that renders large numbers of dependencies (e.g., invocations, accesses, inheritance) as bundled edges to reduce clutter and reveal structural “routes” through the system. Without it, findings stay detached from structural context, reducing explainability and prioritization.

## Definition

A relation-visualization technique that renders large numbers of dependencies (e.g., invocations, accesses, inheritance) as bundled edges to reduce clutter and reveal structural “routes” through the system.

## Mechanism (Solution)

**Input**: Relationship graph between entities (classes/methods) with relation types.

**Process**:
1. Route edges through shared paths so similar relations form bundles (edge bundling).
2. Render bundles in 3D and rely on interactive navigation to inspect structure from multiple perspectives (e.g., skyline/top/aerial).

**Output**: A city augmented with bundled dependency structures.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Reduces edge clutter and can reveal “routes” of dependency flow through shared bundles. | Bundling hides individual edges and can create false visual proximity if users over-trust the bundles. |
| Makes dependency rendering more feasible than drawing all raw edges. | Still prone to occlusion in 3D and often needs interactive filtering and contextual scoping. |

## Variations

CC059 uses **3D edge bundling** to depict structural refactorings: arcs are drawn from an entity’s original position to its new position, making relocations visible during evolution playback (rather than bundling dependency edges).

## Known Limitations

CC035 notes that even bundled edges can overload views for large systems, motivating on-demand techniques such as [[contextual-dependency-view]] and query-driven selection.

## Sources

- [CC035] Wettel PhD thesis — 3D bundled-edge dependency visualization in code cities
- [CC059] Pfahler et al. (2020) — 3D edge bundling used to visualize refactoring moves as arcs

## See Also

- [[contextual-dependency-view]] — on-demand alternative when even bundling is too cluttered
- [[dependency-path-expansion]] — hierarchy-aware aggregation for dependency edges
- [[edge-thickness-mapping]] — encode relation strength when bundling/aggregation is used
