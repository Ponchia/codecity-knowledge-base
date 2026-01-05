---
id: I031
name: Trend Maps (UE4 prototype)
origin: Würfel et al. (CGVC 2015)
year_introduced: 2015
status: research
source_refs: [CC054]
repo_url: null
demo_url: null
primary_language: C++ (Unreal Engine 4)
features_implemented: [F005, F006, F007, F008, F015, F016, F018, F066]
last_updated: 2026-01-04
updated_from: [CC054]
---

# Trend Maps (UE4 prototype)

## Overview

Research prototype that visualizes software-metric trends over a revision range by augmenting a 2.5D treemap-based software map with natural-phenomena-inspired effects. CC054 implements the technique in Unreal Engine 4 (UE4) using shader-based surface materials (item-based metaphors) and particle systems (context-based metaphors).

## Key Capabilities (from CC054)

- **Revision-range trend computation**: computes per-entity metric time series and trend values (slope via linear regression), then discretizes trends into five levels.
- **Item-based effects**: maps trend levels to UE4 material parameters (roughness/metallic/specular/emissive) including multi-texturing (rust) and tessellation + displacement for roughness.
- **Context-based effects**: uses particle systems (e.g., fire/rain) over regions-of-interest; spawns multiple particle emitters within a bounding box using Poisson disk sampling to avoid clustering.
- **Underlying metric map**: combines structural layout with standard mappings (e.g., LOC→area, mean nesting level→height, file-change count→color).

## Sources

- [CC054] Würfel et al. (2015) — Trend maps with natural phenomena metaphors in UE4
