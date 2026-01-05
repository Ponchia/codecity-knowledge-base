---
id: F025
title: Visual Tagging (Color & Transparency)
category: interaction
status: canonical
introduced_by: CC023
implementations: [CodeCity, CodeCharta, Code2City, Code2CityVR, SoftVis3D, m3triCity]
related_features: [F006, F022]
taxonomy:
  granularity: [class, package]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-04
updated_from: [CC009, CC023, CC035, CC059, CC091, CC085, CC114]
---

# Visual Tagging (Color & Transparency)

## Definition

An interaction that assigns colors and/or transparency to selected elements to bookmark, emphasize, or deemphasize parts of a city during exploration.

## Evidence (from CC023)

CC023 describes tagging as assigning a particular color to a selection (and optionally applying transparency to the rest) so important structures remain easy to rediscover.

## Evidence (from CC035)

CC035 describes this as **marking**, using color and transparency during longer explorations (e.g., highlight starting points or fade uninteresting artifacts).

CC085 describes using color and transparency to mark already-explored “territories” at city scale, helping users keep track of progress during incremental exploration.

## Variations (Code2City / Code2CityVR, from CC009)

CC009 describes color-based emphasis as part of interaction:
- Selected objects are highlighted (yellow).
- Search matches are highlighted (red).

## Variations (CodeCharta, from CC091)

CodeCharta supports persisting user-driven emphasis/de-emphasis state (e.g., marked packages and blacklisted/hidden items) as part of downloadable “Custom Views”, enabling sharing and reapplying such tagging without modifying the underlying map file.

## Variations (m3triCity, from CC059)

CC059 describes a “Colorization” setting that lets users assign specific colors to objects based on tags extracted from file names, regular expressions, or manual selection.

## Variations (SoftVis3D reflexion-model prototype, from CC114)

CC114 describes a “Highlight houses” feature that colors the buildings (classes/files) participating in a selected dependency relationship (e.g., purple) so users can quickly identify the concrete implementation elements responsible for an inter-module dependency.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — tagging via color and transparency
- [CC035] Wettel PhD thesis — “Mark” interaction and usage examples
- [CC091] CodeCharta docs — Custom Views capturing marked/blacklisted state
- [CC009] Romano et al. (2019) — selection/search highlighting in Code2City/Code2CityVR
- [CC059] Pfahler et al. (2020) — colorization via tags/regex/manual selection in m3triCity
- [CC085] Wettel & Lanza (ICPC 2007) — marking explored areas using color and transparency
- [CC114] Mohsen (2025) — dependency-participant highlighting (“highlight houses”) using purple building recoloring
