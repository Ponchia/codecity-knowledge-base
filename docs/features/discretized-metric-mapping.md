---
id: F018
title: Discretized Metric Mapping
category: mapping
status: canonical
introduced_by: CC023
implementations: [CodeCity, Trend Maps (UE4 prototype)]
related_features: [F005, F007, F019, F020]
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-04
updated_from: [CC023, CC024, CC035, CC085, CC054]
---

# Discretized Metric Mapping

## Definition

A metric-to-visual mapping strategy that limits a visual property (e.g., height) to a small set of discrete categories to improve readability and reduce “extreme range” effects in overviews.

## Mechanism (from CC023)

**Input**: Metric values for a set of entities.

**Process**:
1. Choose an ordered set of categories (CC023 uses 5 levels: very small, small, average, tall, very tall).
2. Compute boundaries between categories using a strategy (e.g., boxplot-based or threshold-based).
3. Map each entity’s metric to a category, and render using the corresponding visual level.

**Output**: Cities where “average” buildings remain legible even when outliers exist.

## Notes (from CC035)

CC035 describes mapping discrete categories to **building archetypes** (e.g., house → mansion → apartment block → office building → skyscraper) with fixed dimension presets. It also critiques “artificial habitability” introduced by distribution-based binning when the goal is accurate representation; in the thesis’ later examples, identity mapping is used as the default.

CC085 introduces the same “building types” framing and explicitly ties these archetypes to boxplot-based and threshold-based strategies for mapping metric values to a small set of discrete size categories.

## Notes (from CC024)

CC024 describes CodeCity’s discretization support in terms of concrete mapper implementations:
- **Boxplot-based** clustering into five categories (extremely low → extremely high) derived from the current system’s metric distribution.
- **Threshold-based** clustering using manual thresholds (often informed by typical metric ranges) to enable cross-system comparability.

## Notes (from CC054)

CC054 discretizes **trend values** into five categories (strong increase, increase, stagnation, decrease, strong decrease) and uses these discrete levels to parameterize and select visual effects (surface materials and particle systems) for a trend-map view.

## Notes (from CC023)

CC023 contrasts this with linear mapping, where outliers can force most buildings to appear insignificantly small in overview, requiring zooming out so far that details disappear.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — category-based mapping and tradeoffs
- [CC035] Wettel PhD thesis — building-type presets + discussion of identity vs binned strategies
- [CC024] Wettel & Lanza (WASDeTT 2008) — mapper hierarchy (boxplot/threshold) and example binning for Java metrics
- [CC085] Wettel & Lanza (ICPC 2007) — building archetypes and discretized mappings motivated by habitability
- [CC054] Würfel et al. (CGVC 2015) — five-level discretization of metric-trend slopes for effect parameterization in trend maps
