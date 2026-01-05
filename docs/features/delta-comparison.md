---
id: F039
title: Delta Comparison View
category: analysis
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC091
implementations: [CodeCharta]
related_features: [F015, F006, F005, F007]
supersedes: []
taxonomy:
  granularity: [file]
  visual_element: [building, district]
  metric_category: [evolution]
last_updated: 2026-01-05
updated_from: [CC091, CC014]
---

# Delta Comparison View

## Problem & Motivation

This capability helps connect analysis results to the system’s structural and spatial context. An evolution-analysis view that compares two city maps (two snapshots) and visualizes **what changed** (added/removed entities and metric deltas), enabling quick “before vs after” inspection. Without it, findings stay detached from structural context, reducing explainability and prioritization.

## Definition

An evolution-analysis view that compares two city maps (two snapshots) and visualizes **what changed** (added/removed entities and metric deltas), enabling quick “before vs after” inspection.

## Mechanism (Solution)

**Input**: Two city maps (e.g., `cc.json` snapshots built from different commits/branches).

**Process**:
1. Load two maps as reference and comparison.
2. Align entities (typically by path in the hierarchy).
3. Compute per-entity deltas (added/removed/changed metrics).
4. Encode changes visually (e.g., default red=removed, green=added).

**Output**: A “delta map” that highlights changes between two points in time.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Provides a fast “before vs after” view of two snapshots (added/removed entities and metric deltas). | Requires reliable entity alignment between maps; renames/moves can appear as deletes+adds without extra logic. |
| Useful for reviews, regressions, and communication of change impacts in spatial context. | Captures only two points in time; does not replace multi-version evolution analysis. |

## Sources

- [CC091] CodeCharta docs — Delta View (compare two maps; default red removed / green added)
- [CC014] CodeCharta website — “Track your changes” via comparing older maps

## See Also

- [[evolution-visualization]] — multi-version evolution context beyond two snapshots
- [[time-travel]] — stable-layout stepping across versions
- [[trend-map-visualization]] — aggregate trend view across a revision range
