---
id: F008
title: Treemap Layout
category: layout
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC023
implementations: [CodeCity, CodeMetropolis, CodeCharta, m3triCity, Langelier Quality Visualization Framework, SecCityVR, BabiaXR-CodeCity, Code2City, Code2CityVR, Trend Maps (UE4 prototype)]
related_features: [F001, F002, F017, F021]
supersedes: []
taxonomy:
  granularity: [file, class]
  visual_element: [district, building]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC015, CC020, CC023, CC024, CC035, CC059, CC075, CC086, CC091, CC102, CC069, CC130, CC134, CC137, CC054, CC055]
---

# Treemap Layout

## Problem & Motivation

City metaphors need a deterministic way to place many nested districts and buildings in limited space. CC023 uses a modified treemap/rectangle-packing approach so packages occupy contiguous regions and classes fill those regions, producing dense but navigable overviews.

## Definition

A space-filling layout that places buildings using a treemap so hierarchical groupings (e.g., packages) form nested regions that fully partition the available area.

## Context & Applicability

**Use when:**
- The primary structure is a containment hierarchy (packages/folders) and you want a space-filling overview (CC023, CC035).
- You need to render thousands of entities with minimal wasted space while preserving district boundaries (CC023).

**Avoid when:**
- Spatial stability across versions is critical but hierarchy/metrics change frequently (repacking can cause “layout jumps”) (CC059).
- Cross-cutting dependencies are the primary target and global edge rendering would dominate the view; use contextual/aggregated dependency techniques instead (CC023).

**Prerequisites:** A hierarchy with per-node sizes (for rectangle areas), a deterministic ordering rule, and a rectangle-packing/squarified-treemap algorithm (CC023, CC035).
**Alternatives:** [[street-layout]] (EvoStreets) for evolution-stable layouts, [[spiral-layout]] for deterministic ordering, [[sunburst-layout]] for radial space-filling, or [[levelized-layout]] for architecture-level rows.

## Forces

| Force | Pull |
|-------|------|
| Space utilization vs. temporal stability | Dense space-filling improves scalability, but repacking under metric/hierarchy changes causes “layout jumps”. |
| Aspect ratio vs. hierarchy fidelity | Squarer rectangles help readability, but constraints can reduce fidelity to exact area proportions. |
| Determinism vs. optimal packing | Deterministic ordering improves reproducibility, but may waste space compared to more adaptive heuristics. |
| Containment clarity vs. relationship visibility | Emphasize hierarchy boundaries, but accept that cross-cutting relations need separate, contextual techniques. |

## Mechanism (Solution)

### Mechanism

**Input**: Hierarchical structure (e.g., packages containing classes).

**Process (from CC023)**:
1. Recurse over package nesting levels: treat each package as a district and layout its contents.
2. Solve a 2D rectangle-packing problem (buildings have bases on the ground) using a modified treemap approach.
3. Place buildings largest-first; use a binary tree over the available surface to find best-fitting empty nodes and split space as needed.

**Output**: A city whose districts reflect the hierarchy via nested partitioning.

### Mechanism Detail (from CC035)

CC035 refines the algorithmic description as a **rectangle packing** problem using a 2D partition tree (kd-tree): for each rectangle (largest-first), choose a target empty node that either preserves the currently covered bounding rectangle (minimizing waste) or expands it toward a near-square aspect ratio; split the target node to fit; and track margins/gaps as spatial separators.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Space-filling overview that scales to large hierarchies with clear district boundaries. | Sensitive to hierarchy/metric changes; without stabilization, movement can mask real evolution signals. |
| Supports “where is it?” navigation via stable containment semantics (package → district). | Encodes containment, not dependencies; global edges quickly occlude the view. |

**Complexity**: Medium
**Performance**: Layout computation can be a bottleneck for large graphs/hierarchies.
**Cognitive Load**: Medium (users must learn layout semantics).

## Variations

CC134 implements a treemap-like quarter/building layout as an A-Frame component (`babia-city`, also mirrored in `babiaxr-codecity`): the hierarchy is recursively partitioned into nested rectangles (“quarters”) and leaf rectangles (“buildings”) using either:
- a naive split (slice-like subdivision along the longer side), or
- a “pivot” split that chooses a pivot element and distributes remaining elements around it.

This implementation exposes the mapped metric fields as component configuration (`farea`, `fheight`, `fmaxarea`) rather than hard-coding specific software metrics.

CC137 contains a classic “growing” rectangle-packing implementation (`BinPacker`: find/split/grow) used to pack child elements into a parent rectangle with spacing, matching the general treemap/rectangle-packing family used by many city visualizations.

## Implementation Notes

- Use squarifying strategies (or pack largest-first) to keep rectangles near-square for readability (CC023).
- Keep sibling ordering stable (e.g., sort by size/name) to reduce unnecessary movement under small metric changes (CC035).
- Combine with nesting cues (e.g., [[stacked-platform-topology]] or district shading) for deep hierarchies (CC023).

## Evidence

CC023 provides a concrete algorithmic description of the modified treemap/packing strategy; CC015 later summarizes the approach at a high level.

CC020 (the ICSE 2008 tool demo) explicitly describes CodeCity’s layout as a **containment-based layout inspired by rectangle packing**.

CC024 reiterates the same characterization (containment-based layout inspired by rectangle packing) while discussing CodeCity’s tunable visualizations and layout choices inside view configurations.

CC086 reiterates that district size and position are defined by a treemap layout (framing it as the spatial basis for the class/package city overview).

CC091 documents CodeCharta implementing treemap-based layouts (including a squarified treemap) for file/folder hierarchies as an interactive 3D “code map”.

CC054 builds “trend maps” on top of 2.5D treemap-based software maps, using the treemap cuboids as reference geometry for additional (trend) encodings via surface and particle effects.

CC059 describes m3triCity placing packages and classes using a recursive bin-packing algorithm (similar to other city visualizations) and then augmenting it with an evolution-aware, history-resistant stability strategy (pre-allocating final space to reduce “layout jumps”).

CC075 adapts treemaps to **discrete** class boxes by rounding slice sizes to fit a minimum class footprint and expanding slices when needed, then searching for partitions that minimize empty “holes”.

CC102 describes CodeMetropolis organizing namespace hierarchy using “plates” laid out like a treemap, expanding plates to fit contained elements.
CC069 adapts a treemap/bin-packing layout to keep class buildings near-square while placing them within package platforms for SecCityVR.

CC055 describes Code2City reconstructing a package/type tree from exported metrics and positioning packages/types via a recursive “bin-packing” (rectangle-packing) layout that computes dimensions bottom-up.

CC130’s CodeMetropolis “placing” stage implements a recursive rectangle-packing layout that packs child rectangles into their parent with spacing, growing the packing area until all children fit (a containment-based packing strategy consistent with other city-metaphor treemap/bin-packing layouts).

## Known Limitations

- Small metric changes can reorder packing and move many buildings, making evolution comparisons harder (CC059).
- Deep hierarchies can produce tiny districts/buildings that are hard to select/interpret (CC023).
- The layout encodes containment but not cross-cutting relationships; global dependency edges often occlude the scene (CC023).

## Open Questions

- Which stability strategies (preallocation, incremental updates, stable sorting) provide the best “mental map” preservation with acceptable space overhead?
- How should tools expose layout determinism (sorting keys, tie-breaking) so layouts are reproducible across machines/versions?
- When should a tool switch from treemap/bin-packing to alternative layouts (street-based, levelized) based on task or evolution needs?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — layout algorithm description
- [CC035] Wettel PhD thesis — rectangle packing algorithm details (partition tree, boundary preservation/expansion)
- [CC015] Jeffery survey — later description of CodeCity layout
- [CC091] CodeCharta docs — squarified treemap layout for file/folder “code maps”
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — containment-based layout inspired by rectangle packing
- [CC024] Wettel & Lanza (WASDeTT 2008) — view configuration layouts and containment-based rectangle-packing description
- [CC086] Wettel & Lanza (2008) — district placement defined by treemap layout (CodeCity nutshell)
- [CC059] Pfahler et al. (2020) — bin-packing-based city placement + history-resistant stability strategy in m3triCity
- [CC075] Langelier et al. (ASE 2005) — discrete treemap adaptation for 3D class boxes
- [CC102] Balogh & Beszedes (2013) — CodeMetropolis uses treemap-like plates for namespace hierarchy
- [CC069] Wueppelmann & Yigitbas (2025) — SecCityVR uses an adapted treemap/bin-packing layout for packages/classes
- [CC130] CodeMetropolis repository — placing tool uses recursive rectangle packing (“PackLayout”) for containment-based placement
- [CC134] BabiaXR repository — `babia-city` treemap-like splitting (`split: naive|pivot`) for buildings and hierarchical quarters
- [CC137] Holoware software-city repository — `BinPacker` rectangle packing (find/split/grow) as a binpacking layout variant
- [CC054] Würfel et al. (CGVC 2015) — 2.5D treemap reference geometry for trend-map software maps
- [CC055] Code2City project report — recursive “bin-packing” layout for packages/types from a reconstructed hierarchy

## See Also

- [[class-as-building]] — common entity mapping used with treemaps
- [[street-layout]] — alternative layout emphasizing paths/streets
