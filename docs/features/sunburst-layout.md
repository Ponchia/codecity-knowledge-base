---
id: F052
title: Sunburst Layout
category: layout
status: variant
introduced_by: CC075
implementations: [Langelier Quality Visualization Framework]
related_features: [F008, F001]
taxonomy:
  granularity: [class]
  visual_element: [district, building]
  metric_category: [size]
last_updated: 2026-01-03
updated_from: [CC075]
---

# Sunburst Layout

## Definition

A radial, space-filling layout that assigns hierarchical groups (e.g., packages) to angular slices and places entities along concentric arcs, enabling an overview of package structure in a circular “map”.

## Mechanism (from CC075)

**Input**: Package hierarchy with class counts per package.

**Process**:
1. Allocate an angular slice to each package proportional to the number of contained classes.
2. Place class glyphs along the arc for the package; use increasing radius for deeper hierarchy levels.
3. Draw radial separators between sibling packages and arc separators between levels.
4. Enforce minimum spacing between class glyphs (discrete boxes), which can introduce empty “holes” in some layouts.

**Output**: A circular, hierarchy-preserving city map with classes arranged radially.

## Evidence / Notes

CC075 reports that Sunburst supports many analysis tasks effectively but can make orientation-based cues (e.g., box twist for cohesion) harder to perceive than in treemap layouts.

## Sources

- [CC075] Langelier et al. (ASE 2005) — adapted Sunburst for class-level software maps

## See Also

- [[treemap-layout]] — alternative space-filling layout for software hierarchies
