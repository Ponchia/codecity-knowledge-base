---
id: F016
title: Texture Mapping
category: mapping
status: variant
introduced_by: CC015
implementations: [Vizz3D, CodeMetropolis, VariCity / VariMetrics, Trend Maps (UE4 prototype)]
related_features: [F001]
taxonomy:
  granularity: [function, method]
  visual_element: [building, floor]
  metric_category: [size, quality]
last_updated: 2026-01-04
updated_from: [CC015, CC103, CC130, CC045, CC054]
---

# Texture Mapping

## Definition

A property mapping where surface texture (patterning of a building’s exterior) encodes information about the represented entity, providing a channel beyond height/base/color.

## Mechanism

**Input**: A numeric property (or binned ranges) per entity.

**Process**:
1. Choose a texture scale or discrete texture set.
2. Map values to texture selection or intensity.
3. Render the texture on building surfaces.

**Output**: A city where texture conveys a metric without changing geometry.

## Evidence (from CC015)

CC015 describes Vizz3D indicating lines of code for a member function via the texture of its exterior walls.

## Variations (from CC103)

CodeMetropolis maps the **number of statements** to Minecraft block materials for method floors (e.g., glass -> sandstone -> stone -> obsidian), making wall material a discrete texture channel for a size metric.

CC130 documents the current mapping-file format and examples that quantize metrics (e.g., McCC) into specific Minecraft block IDs for both internal and external materials of floors (e.g., `minecraft:glass`, `minecraft:stone`, `minecraft:obsidian`).

CC045 describes VariMetrics (an extension to VariCity) supporting texture-based strategies such as a **crackled texture** to encode software-quality metrics intended to surface technical-debt-critical areas.

CC054 (Trend Maps) implements multiple surface-appearance effects in UE4 materials, including multi-texturing (e.g., rust distribution via Perlin noise) and geometry/normal/displacement-based roughness, to encode discretized trend categories.

## Sources

- [CC015] Jeffery survey — Vizz3D description
- [CC103] Balogh et al. (2015) - CodeMetropolis maps statements to floor material
- [CC130] CodeMetropolis repository — mapping XML examples quantize metrics into Minecraft block materials
- [CC045] Mortara et al. (JSS 2024 preprint) — VariMetrics supports crackled-texture strategies for quality/technical-debt overlays
- [CC054] Würfel et al. (CGVC 2015) — UE4 surface-material effects (rust/roughness/shininess/glow) used as trend encodings in software maps
