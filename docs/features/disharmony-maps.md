---
id: F034
title: Disharmony Maps
category: analysis
status: canonical
introduced_by: CC117
implementations: [CodeCity, Code2City, Code2CityVR]
related_features: [F006, F025, F037]
taxonomy:
  granularity: [class, method]
  visual_element: [building, brick]
  metric_category: [quality]
last_updated: 2026-01-04
updated_from: [CC025, CC035, CC086, CC117, CC055, CC064]
---

# Disharmony Maps

## Definition

A design-quality visualization that overlays the software city with colors indicating detected design disharmonies (“code smells”), enabling an overview of the proportion, distribution, and dominant types of design problems while preserving structural context.

## Mechanism (from CC035)

**Input**: Detection-strategy results per entity (boolean/label per disharmony type), plus the city’s usual structural metric mappings.

**Process**:
1. Assign a vivid color per disharmony type.
2. Color affected entities with the disharmony color; render unaffected entities in neutral gray.
3. Keep structural metrics on geometry (e.g., height/footprint) while color encodes disharmony.

**Output**: A “map” of design problems embedded in the system’s spatial structure.

## Evidence (from CC086)

CC086 describes disharmony maps as being inspired by disease maps: use vivid colors to highlight detected “harmony breakers” while rendering unaffected entities in neutral grays to keep context present but non-distracting.

## Evidence (from CC117)

CC117 introduces disharmony maps as a way to localize detection-strategy results in context:
- Encode disharmony types in color while keeping structural metrics mapped to geometry (e.g., NOA/NOM).
- Support overview questions like **distribution** across packages and **dominant disharmony types**.
- Avoid the context loss of long textual result lists, and make it more feasible to correlate multiple disharmony types.

## Evidence (from CC055)

CC055 describes Code2City supporting smell-based coloring to help identify design problems, including distinct colors for brain classes, data classes, and god classes while keeping the city’s structural context.

## Sources

- [CC117] Wettel & Lanza (SoftVis 2008) — introduces disharmony maps for visual localization of design problems
- [CC035] Wettel PhD thesis — disharmony maps inspired by disease maps + multiple case studies
- [CC025] Wettel & Lanza (ICSE 2011) — disharmony-map example and design-problem tasks in controlled experiment context
- [CC086] Wettel & Lanza (2008) — disharmony-map explanation and example (vivid colors vs neutral context)
- [CC055] Code2City project report — smell-based coloring for brain/data/god classes in a UE4-based software city
- [CC064] Romano et al. (IST 2019) — controlled experiment paper documenting Code2City’s smell highlighting (brain/data/god classes)
