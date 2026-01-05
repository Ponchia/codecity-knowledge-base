---
id: I022
name: Langelier Quality Visualization Framework
origin: Université de Montréal (DIRO)
year_introduced: 2005
status: research
source_refs: [CC075]
repo_url: null
demo_url: null
primary_language: Unknown (research prototype)
features_implemented: [F002, F005, F006, F008, F015, F023, F052, F053]
last_updated: 2026-01-03
updated_from: [CC075]
---

# Langelier Quality Visualization Framework

## Overview

A research prototype for visualization-based software quality analysis. It represents classes as simple 3D boxes, maps quality-related metrics to box color/size/orientation, and uses architectural layouts (Treemap/Sunburst) plus filters to enable rapid detection of anomalies and architectural patterns.

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F002]] Class-as-Building | Each class is rendered as a simple 3D box. |
| [[F006]] Color Mapping | Coupling (CBO) mapped to a blue→red color scale. |
| [[F005]] Height Mapping | Size/complexity (WMC) mapped to box height. |
| [[F053]] Orientation Mapping | Cohesion (LCOM5) mapped to box “twist” (rotation). |
| [[F008]] Treemap Layout | Discrete Treemap adapted to fit 3D boxes and package structure. |
| [[F052]] Sunburst Layout | Radial space-filling layout adapted to class boxes. |
| [[F023]] Query-Based Filtering | Filters highlight extreme metric values and UML relation subsets. |
| [[F015]] Evolution Visualization | Multi-version views used for package/program evolution analysis. |

## Technical Details

**Granularity**: class

**Visual Element**: building (3D box)

**Metrics Supported**:
- CBO (coupling)
- LCOM5 (cohesion)
- WMC (size/complexity)
- DIT (inheritance depth; used for filtering/refinement)

**Platform**: desktop 3D visualization prototype (exact stack not specified)

## Sources

- [CC075] Langelier et al. (ASE 2005) — visualization framework, metric mappings, layouts, filters, and experiment results
