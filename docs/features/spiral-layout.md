---
id: F059
title: Spiral Layout
category: layout
status: variant
introduced_by: CC096
implementations: [BabiaXR-CodeCity]
related_features: [F008]
taxonomy:
  granularity: [file]
  visual_element: [district, building]
  metric_category: [size, evolution]
last_updated: 2026-01-04
updated_from: [CC096, CC134]
---

# Spiral Layout

## Definition

A layout strategy that places buildings in a center-out spiral order within each hierarchy level (e.g., within a directory), so that new buildings appearing/disappearing in the hierarchy cause less disruptive movement than space-filling rectangle-packing layouts.

## Mechanism (from CC096)

**Input**: A hierarchy of groups (e.g., directories) and elements (e.g., files/buildings).

**Process**:
1. For a given hierarchy level, place the first building at the center.
2. Place subsequent buildings by stepping outward along a spiral path around the center.
3. Apply the same spiral placement recursively to groups of buildings at the same hierarchy level.

**Output**: A city layout where buildings are arranged in spiral patterns per group, intended to preserve a perceivable sense of place when the hierarchy changes between snapshots.

## Mechanism Detail (BabiaXR, from CC134)

CC134’s `babia-boats` component implements a spiral-style placement algorithm by walking around the current bounding rectangle in a repeating right → down → left → up cycle:
1. Place the first element and initialize the current bounds (left/right/up/down) based on its footprint.
2. For each subsequent element, place it adjacent to the active side (right, then down, then left, then up), updating the running bounds when the spiral completes a side.
3. Repeat the cycle, expanding the bounds as needed as new elements are added.

The component applies the same strategy recursively for hierarchical “quarters” (nodes with `children`), producing nested spiral placements.

## Rationale (from CC096)

CC096 argues that space-filling rectangle-packing layouts can cause widespread repositioning when new buildings appear, reducing the perceived relationship to previous positions in evolution scenarios; the spiral approach aims to behave more stably under such changes.

## Sources

- [CC096] Moreno-Lumbreras et al. (2022) — spiral placement for web-based CodeCity (BabiaXR-CodeCity) motivated by evolution stability
- [CC134] BabiaXR repository — `babia-boats` spiral-style placement (right/down/left/up) for buildings and hierarchical quarters
