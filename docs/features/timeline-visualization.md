---
id: F033
title: Timeline Visualization
category: analysis
status: canonical
introduced_by: CC116
implementations: [CodeCity, m3triCity]
related_features: [F015, F031, F027]
taxonomy:
  granularity: [class, method, system]
  visual_element: [platform, brick]
  metric_category: [evolution]
last_updated: 2026-01-04
updated_from: [CC035, CC059, CC116]
---

# Timeline Visualization

## Definition

An evolution visualization component that places versions along a time axis and provides a compact per-version representation, enabling both navigation (“jump to version”) and understanding of when entities appear/disappear or when changes concentrate.

## Mechanism (from CC035)

**Input**: Version history for a class/package, including per-version method sets.

**Process**:
1. Render successive versions as platforms positioned along a left→right timeline.
2. Render methods as bricks on each platform.
3. Optionally combine with [[age-map]] coloring to highlight “generations” of methods introduced in the same version.

**Output**: A compact timeline view that supports comparing evolution across versions.

## Evidence (from CC116)

CC116 uses a fine-grained timeline to show method “generations” across versions (methods as bricks on successive version platforms), including a worked example timeline for a single class.

## Variations (m3triCity, from CC059)

CC059 describes an interactive timeline below the main visualization that summarizes per-version change intensity for multiple metric categories (e.g., fields, methods, for-loops, LOC). Users can jump to a moment by clicking on the timeline; when a city object is selected, the timeline highlights all commits involving that entity.

## Sources

- [CC035] Wettel PhD thesis — fine-grained timeline technique
- [CC059] Pfahler et al. (2020) — interactive evolution timeline (change categories + jump-to-version + selection-linked highlights)
- [CC116] Wettel & Lanza (WCRE 2008) — fine-grained timeline technique (methods as bricks across versions)
