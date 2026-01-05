---
id: F029
title: Bundled Edge Relations
category: analysis
status: variant
introduced_by: CC035
implementations: [CodeCity, m3triCity]
related_features: [F030, F023, F026]
taxonomy:
  granularity: [class]
  visual_element: [edge]
  metric_category: [coupling]
last_updated: 2026-01-03
updated_from: [CC035, CC059]
---

# Bundled Edge Relations

## Definition

A relation-visualization technique that renders large numbers of dependencies (e.g., invocations, accesses, inheritance) as bundled edges to reduce clutter and reveal structural “routes” through the system.

## Mechanism (from CC035)

**Input**: Relationship graph between entities (classes/methods) with relation types.

**Process**:
1. Route edges through shared paths so similar relations form bundles (edge bundling).
2. Render bundles in 3D and rely on interactive navigation to inspect structure from multiple perspectives (e.g., skyline/top/aerial).

**Output**: A city augmented with bundled dependency structures.

## Variations (m3triCity, from CC059)

CC059 uses **3D edge bundling** to depict structural refactorings: arcs are drawn from an entity’s original position to its new position, making relocations visible during evolution playback (rather than bundling dependency edges).

## Limitations

CC035 notes that even bundled edges can overload views for large systems, motivating on-demand techniques such as [[contextual-dependency-view]] and query-driven selection.

## Sources

- [CC035] Wettel PhD thesis — 3D bundled-edge dependency visualization in code cities
- [CC059] Pfahler et al. (2020) — 3D edge bundling used to visualize refactoring moves as arcs
