---
id: F010
title: Coupling Layout
category: layout
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC106
implementations: [VR City, Viseagull]
related_features: [F001]
supersedes: []
taxonomy:
  granularity: [class, file]
  visual_element: [building]
  metric_category: [coupling]
last_updated: 2026-01-05
updated_from: [CC015, CC106, CC148]
---

# Coupling Layout

## Problem & Motivation

This capability helps keep spatial organization interpretable and memorable as the city grows. A layout where spatial proximity (and sometimes geometric contact) between buildings encodes coupling: more-coupled entities are placed nearer to each other to make dependency structure visible in the city’s geometry. Without it, navigation and spatial memory degrade because placement feels arbitrary or unstable.

## Definition

A layout where spatial proximity (and sometimes geometric contact) between buildings encodes coupling: more-coupled entities are placed nearer to each other to make dependency structure visible in the city’s geometry.

## Mechanism (Solution)

**Input**: A weighted coupling graph of classes (nodes) and dependencies (edges, weighted by dependency count), plus a per-method metric (e.g., LOC) for fine-grained building floors.

**Process**:
1. Compute a **spectral ordering** of classes using the graph’s **Fiedler vector**.
2. For each class (in that ordering), compute a descending list of per-method metric values; treat the list as the building’s floors.
3. Place floor “blocks” along a **Hilbert curve** (space-filling curve) and merge blocks belonging to the same class to form a building footprint.
4. Leave space between buildings to form streets.

**Output**: A city where proximity/contact is meaningful as coupling.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Makes large structures navigable via spatial organization. | May hide non-hierarchical relationships. |
| Can improve stability/orientation if positions are consistent. | Computing layout can be expensive at scale. |

## Variations

| Source | Notes |
|--------|-------|
| CC015 | Summarizes VR City’s layout as “organic/jigsaw-like”, describing coupling encoded via building contacts. |
| CC106 | Provides a concrete coupling-driven algorithm (spectral ordering + Hilbert-curve placement) that positions buildings with respect to coupling. |
| CC148 | Describes a coupling-driven, cluster-level layout for files: t-SNE projects the coupling distance matrix into 2D positions (used to place cluster centroids), then a spring-layout-like overlap-removal step avoids city overlap while preserving distances. |

## Sources

- [CC106] Vincúr et al. (QRS-C 2017) — coupling-graph layout algorithm (spectral ordering + Hilbert curve)
- [CC015] Jeffery survey — VR City description and Table 1 (survey summary)
- [CC148] Géry (2021) — Viseagull Medium post describing file-coupling clustering and t-SNE + spring-like layout for “cities + roads”

## See Also

- [[street-layout]] — layout based on streets/directories
