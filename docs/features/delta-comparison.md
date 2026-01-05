---
id: F039
title: Delta Comparison View
category: analysis
status: variant
introduced_by: CC091
implementations: [CodeCharta]
related_features: [F015, F006, F005, F007]
taxonomy:
  granularity: [file]
  visual_element: [building, district]
  metric_category: [evolution]
last_updated: 2026-01-02
updated_from: [CC091, CC014]
---

# Delta Comparison View

## Definition

An evolution-analysis view that compares two city maps (two snapshots) and visualizes **what changed** (added/removed entities and metric deltas), enabling quick “before vs after” inspection.

## Mechanism (from CC091)

**Input**: Two city maps (e.g., `cc.json` snapshots built from different commits/branches).

**Process**:
1. Load two maps as reference and comparison.
2. Align entities (typically by path in the hierarchy).
3. Compute per-entity deltas (added/removed/changed metrics).
4. Encode changes visually (e.g., default red=removed, green=added).

**Output**: A “delta map” that highlights changes between two points in time.

## Sources

- [CC091] CodeCharta docs — Delta View (compare two maps; default red removed / green added)
- [CC014] CodeCharta website — “Track your changes” via comparing older maps
