---
id: I028
name: DynaCity
origin: QAware (open-source)
year_introduced: 2022
status: research
source_refs: [CC133, CC137]
repo_url: https://github.com/qaware/dynacity
demo_url: null
primary_language: C# (Unity)
features_implemented: [F001, F017, F002, F007, F005, F014, F030, F022, F026, F061]
last_updated: 2026-01-04
updated_from: [CC133, CC137]
---

# DynaCity

## Overview

DynaCity is a Unity-based software-city visualization that combines a static dependency graph with dynamic runtime traces. It builds a package/class city from a `.dot` dependency graph, then overlays dynamic dependencies and component load aggregated from ElasticSearch-exported span/transaction JSON files, allowing time-sliced exploration and selection-driven dependency focus. The related Holoware repository (CC137) contains additional view variants and evaluation artifacts for this codebase.

## Technical Details (from CC133)

**Inputs**:
- Static dependencies: `.dot` file parsed into a dependency graph.
- Dynamic behavior: ElasticSearch APM-style `spans*.json` plus `transaction*.json`, aggregated into time buckets.

**Mappings**:
- **Packages**: rendered as “basement” platforms (LSM package elements).
- **Classes**: rendered as neon towers; footprint uses fan-out and height uses fan-in (from the dependency graph).
- **Dynamic load**: building color and dependency-arc color encode aggregated call/load by HTTP status category (success/client error/server error) and intensity scaled by min/max load.

**Interaction**:
- **Time navigation**: left/right arrow keys step through time buckets.
- **Selection focus**: click a component to show only its dependency arcs; release to show all arcs again.
- **Navigation**: free-fly camera controls (mouse look + WASD/QE movement with adjustable speed).

## Additional Details (from CC137)

**Levelized layout**: The Holoware codebase constructs a Layered Structure Model (LSM) from the `.dot` dependency graph and can lay out packages/classes in rows by LSM level (a “levelized” layout), as an alternative to bin-packing-style layouts.

**View variants**:
- **Day view**: focuses on static structure and can draw dependency-cycle arcs.
- **Night view**: visualizes “use cases” from trace-span JSON files as arcs between components and supports stepping through use cases / points of interest.
- **ErrorCodes view**: loads ElasticSearch-exported traces, aggregates them into time frames, recolors buildings and arcs by HTTP status categories, and supports next/previous time-frame navigation.

**Evaluation artifacts**: CC137 includes raw spreadsheet data comparing bin-packing vs levelized layouts on correctness/time for comprehension tasks, plus a questionnaire about dependency/use-case filtering preferences.

## Sources

- [CC133] DynaCity repository — Unity implementation combining DOT-based static dependencies with ElasticSearch span aggregation and interactive time-sliced dependency overlays
- [CC137] Holoware software-city repository — layered (LSM) city construction, trace/use-case views, and bundled evaluation spreadsheets
