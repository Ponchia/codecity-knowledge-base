---
id: F047
title: Dependency Path Expansion
category: analysis
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC043
implementations: [SoftViz3D, SoftVis3D]
related_features: [F030, F048]
supersedes: []
taxonomy:
  granularity: [file, package]
  visual_element: [edge, building]
  metric_category: [coupling]
last_updated: 2026-01-05
updated_from: [CC043, CC129]
---

# Dependency Path Expansion

## Problem & Motivation

This capability helps connect analysis results to the system’s structural and spatial context. A hierarchy-aware transformation that converts “flat” dependencies between leaf nodes into a set of dependency edges that follow the containment hierarchy, optionally introducing boundary/interface nodes so dependencies can be rendered with less clutter at multiple abstraction levels. Without it, findings stay detached from structural context, reducing explainability and prioritization.

## Definition

A hierarchy-aware transformation that converts “flat” dependencies between leaf nodes into a set of dependency edges that follow the containment hierarchy, optionally introducing boundary/interface nodes so dependencies can be rendered with less clutter at multiple abstraction levels.

## Mechanism (Solution)

**Input**: A containment hierarchy (tree) plus dependency edges between leaf elements.

**Process**:
1. For each dependency between two leaf nodes, find their common ancestor in the hierarchy.
2. Walk upward from the deeper node(s) toward the common ancestor, creating intermediate dependency edges at each step.
3. Introduce a synthetic “interface” leaf for a subsystem boundary when needed, and connect the original node to that interface node.
4. Aggregate multiple original dependencies that map onto the same path edge by incrementing a counter on that path edge.

**Output**: A set of “path” dependency edges (and interface nodes) that can be visualized per hierarchy layer, supporting both detailed and aggregated dependency views.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Surfaces quality/evolution signals in context. | Overlays can overwhelm the base metaphor. |
| Supports prioritization (hotspots, anomalies). | Signals may be noisy or metric-dependent. |

## Variations

| Implementation | Variation |
|----------------|-----------|
| SoftViz3D (CC043) | Distinguishes “flat” input dependencies from generated “path” dependencies; offers a detail mode that includes more edges and a metric-focused mode that emphasizes path edges (often with weights). |
| SoftVis3D (CC129) | Generates “path” edges labeled `depPath_<id>` and inserts synthetic interface leaf nodes (`interface_<parentId>`). Each path edge aggregates multiple underlying dependency IDs (later used for weighting/thickness). |

## Sources

- [CC043] SoftViz3D repository — dependency-path generation with interface nodes and aggregation counters
- [CC129] sonar-softvis3d-plugin repository — dependency expansion implementation (`DependencyExpander`) with interface nodes and aggregated “depPath” edges

## See Also

- [[contextual-dependency-view]] — focused dependency visualization scoped to a context
- [[edge-thickness-mapping]] — common way to encode aggregated dependency counts
