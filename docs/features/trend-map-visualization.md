---
id: F066
title: Trend Maps (Natural-Phenomena Trend Encoding)
category: analysis
status: variant
introduced_by: CC054
implementations: [Trend Maps (UE4 prototype)]
related_features: [F015, F016, F018, F062]
taxonomy:
  granularity: [file]
  visual_element: [building, district]
  metric_category: [evolution, size, complexity, quality]
last_updated: 2026-01-04
updated_from: [CC054]
---

# Trend Maps (Natural-Phenomena Trend Encoding)

## Definition

An evolution-visualization technique that extends a software map (2.5D treemap) of a selected revision by encoding **metric trends** over a revision range using natural-phenomena-inspired visual effects (surface materials and particle systems), enabling a single-view overview of changes without animation.

## Mechanism (from CC054)

**Input**: Version-control history over a revision range, per-entity metric time series, and a selected “reference” revision within the range.

**Process**:
1. Compute software metrics per entity for each revision in the selected range.
2. Aggregate metrics bottom-up in the hierarchy to enable group-level trend effects (e.g., directories/packages).
3. Compute a trend value per entity/group (CC054 uses linear-regression slope) and discretize it into five levels (strong increase → strong decrease).
4. Map trend levels to effect-parameter ranges and render:
   - **Item-based effects**: change surface/material properties (e.g., rough↔shiny, rust↔glow).
   - **Context-based effects**: spawn particle effects around regions-of-interest (e.g., fire/rain).

**Output**: A software map augmented with visually distinctive trend encodings for quick hotspot overview.

## Notes / Limitations (from CC054)

- Trend maps show trends only for entities present at the chosen revision within the range; added/removed entities are not fully represented.
- Strong visual effects (e.g., emissive glow) can interfere with other encodings such as color mapping.
- Context-based effects can introduce clutter or occlusion on large regions-of-interest.

## Sources

- [CC054] Würfel et al. (CGVC 2015) — “Natural Phenomena as Metaphors for Visualization of Trend Data in Interactive Software Maps”

## See Also

- [[evolution-visualization]] — broader category that trend maps instantiate
- [[discretized-metric-mapping]] — five-level discretization used for trend categories
- [[texture-mapping]] — item-based surface/material mappings used for trend encoding
- [[production-cost-overlay]] — related use of “effects” (e.g., fire) as attention-guiding overlays
