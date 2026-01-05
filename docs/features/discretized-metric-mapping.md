---
id: F018
title: Discretized Metric Mapping
category: mapping
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC023
implementations: [CodeCity, Trend Maps (UE4 prototype)]
related_features: [F005, F007, F019, F020]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC023, CC024, CC035, CC085, CC054]
---

# Discretized Metric Mapping

## Problem & Motivation

Linear metric mappings can be dominated by outliers, forcing most buildings into a visually indistinguishable range. CC023 introduces discretized mappings to keep overviews readable, and CC085 ties discrete “building archetypes” to habitability so users can interpret cityscapes without being overwhelmed by extreme ranges.

## Definition

A metric-to-visual mapping strategy that limits a visual property (e.g., height) to a small set of discrete categories to improve readability and reduce “extreme range” effects in overviews.

## Context & Applicability

**Use when:**
- You need an overview where typical entities remain distinguishable despite outliers (CC023).
- You want categorical “size classes” (e.g., house→skyscraper) for quick scanning and discussion (CC085, CC035).

**Avoid when:**
- Analysts need precise quantitative differences or small changes within a bin (discretization hides detail) (CC035).
- You lack reliable thresholds/distribution statistics for choosing bins (CC024, CC035).

**Prerequisites:** A binning strategy (boxplot/distribution-based or threshold-based), a small number of categories, and a legend describing category meaning (CC024, CC085).
**Alternatives:** Continuous mapping via [[height-mapping]] / [[base-mapping]], or a specific binning strategy like [[boxplot-metric-mapping]] or [[threshold-metric-mapping]].

## Forces

| Force | Pull |
|-------|------|
| Overview legibility vs. numeric precision | Use a small set of categories so typical entities remain distinguishable, but accept loss of fine-grained differences within bins. |
| Cross-system comparability vs. distribution fit | Thresholds enable comparing different systems, but may not match each system’s distribution; boxplot bins fit the data but are less comparable. |
| “Habitability” vs. analytical transparency | Archetypes and stylized categories improve readability, but can introduce artificial structure that obscures real distributions. |

## Mechanism (Solution)

**Input**: Metric values for a set of entities.

**Process**:
1. Choose an ordered set of categories (CC023 uses 5 levels: very small, small, average, tall, very tall).
2. Compute boundaries between categories using a strategy (e.g., boxplot-based or threshold-based).
3. Map each entity’s metric to a category, and render using the corresponding visual level.

**Output**: Cities where “average” buildings remain legible even when outliers exist.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Preserves overview readability under heavy-tailed metrics by preventing extreme range domination. | Hides within-bin variation; small changes near thresholds can appear as sudden “jumps”. |
| Supports communicable “size classes” (e.g., house→skyscraper) for discussion and scanning. | Requires careful bin/threshold choice; poor thresholds can mislead or reduce comparability. |

**Complexity**: Low
**Performance**: Typically cheap; depends on recomputation frequency.
**Cognitive Load**: Low–Medium (depends on legend/scale).

## Implementation Notes

### Notes (from CC035)

CC035 describes mapping discrete categories to **building archetypes** (e.g., house → mansion → apartment block → office building → skyscraper) with fixed dimension presets. It also critiques “artificial habitability” introduced by distribution-based binning when the goal is accurate representation; in the thesis’ later examples, identity mapping is used as the default.

CC085 introduces the same “building types” framing and explicitly ties these archetypes to boxplot-based and threshold-based strategies for mapping metric values to a small set of discrete size categories.

### Notes (from CC024)

CC024 describes CodeCity’s discretization support in terms of concrete mapper implementations:
- **Boxplot-based** clustering into five categories (extremely low → extremely high) derived from the current system’s metric distribution.
- **Threshold-based** clustering using manual thresholds (often informed by typical metric ranges) to enable cross-system comparability.

### Notes (from CC054)

CC054 discretizes **trend values** into five categories (strong increase, increase, stagnation, decrease, strong decrease) and uses these discrete levels to parameterize and select visual effects (surface materials and particle systems) for a trend-map view.

### Notes (from CC023)

CC023 contrasts this with linear mapping, where outliers can force most buildings to appear insignificantly small in overview, requiring zooming out so far that details disappear.

## Evidence

- CC023 and CC085 motivate discretization primarily as a readability/habitability strategy in overview exploration (no controlled isolation of discretization effects is reported in these sources).
- CC054 shows discretization used as a practical step to drive discrete visual-effect selection/parameterization for trend communication.

## Variations

| Strategy | How bins are chosen | Notes |
|----------|----------------------|------|
| Boxplot-based | Derived from the current system’s metric distribution | Improves within-system legibility but hinders cross-system comparison (CC024, CC085). |
| Threshold-based | Manual thresholds (often guided by typical ranges) | Enables cross-system comparability but requires validated thresholds (CC024). |
| Effect-driven discretization | Discretize a derived value (e.g., trend slope) into a small ordinal set | Used to select discrete visual effects/levels (CC054). |

## Known Limitations

- Discretization reduces precision and can create boundary effects (entities near a threshold look more different than they are) (CC035).
- Distribution-based bins hinder cross-system comparability; threshold-based bins require validated thresholds (CC024, CC035).
- Over-stylized archetypes can create “artificial habitability” that obscures true distributions (CC035).

## Open Questions

- What is the “right” number of bins for common city tasks (hotspot detection vs comparison) and common metric distributions?
- How should tools communicate uncertainty and boundary effects near thresholds (e.g., jitter bands, tooltips with raw values)?
- Can discretization be made stable across versions (so entities don’t “jump bins” constantly) without hiding meaningful changes?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — category-based mapping and tradeoffs
- [CC035] Wettel PhD thesis — building-type presets + discussion of identity vs binned strategies
- [CC024] Wettel & Lanza (WASDeTT 2008) — mapper hierarchy (boxplot/threshold) and example binning for Java metrics
- [CC085] Wettel & Lanza (ICPC 2007) — building archetypes and discretized mappings motivated by habitability
- [CC054] Würfel et al. (CGVC 2015) — five-level discretization of metric-trend slopes for effect parameterization in trend maps

## See Also

- [[height-mapping]] — common continuous alternative
- [[base-mapping]] — second continuous geometric channel often discretized
- [[boxplot-metric-mapping]] — distribution-based discretization strategy
- [[threshold-metric-mapping]] — manual-threshold discretization strategy
