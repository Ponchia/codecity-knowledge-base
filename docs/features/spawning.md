---
id: F024
title: Spawning (Isolated Views)
category: interaction
status: canonical
introduced_by: CC023
implementations: [CodeCity]
related_features: [F022]
taxonomy:
  granularity: [class, package]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-04
updated_from: [CC020, CC023, CC035, CC085]
---

# Spawning (Isolated Views)

## Definition

An interaction that creates a new, complementary view containing only a selected subset of entities, enabling focused exploration without visual clutter.

## Mechanism (from CC023)

1. Select a set of entities.
2. Spawn a new view that isolates the selection.
3. Continue exploration within the isolated subset.

## Evidence (from CC020)

CC020 describes using spawned windows to focus on a specific district (package) when exploring the city overview.

CC085 describes spawning a new view containing only a selected district to reduce occlusion from unrelated classes during focused exploration.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — spawning isolated districts/views
- [CC035] Wettel PhD thesis — spawning as “complementary view” for focused analysis
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — spawning separate windows for district-focused exploration
- [CC085] Wettel & Lanza (ICPC 2007) — district-only spawned view used to avoid occlusion
