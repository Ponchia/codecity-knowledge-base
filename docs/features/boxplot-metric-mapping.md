---
id: F019
title: Boxplot-Based Metric Mapping
category: mapping
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC023
implementations: [CodeCity]
related_features: [F018]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC023, CC024, CC035, CC085]
---

# Boxplot-Based Metric Mapping

## Problem & Motivation

This capability helps make important properties visible at a glance without relying on separate numeric views. A discretized mapping strategy that derives category boundaries from the distribution of metric values in the analyzed system (using a boxplot technique). Without it, metric signals remain harder to perceive and often require separate tables or charts.

## Definition

A discretized mapping strategy that derives category boundaries from the distribution of metric values in the analyzed system (using a boxplot technique).

## Mechanism (Solution)

CC035 describes computing quartiles and outlier limits (via IQR) and using those boundaries to split the input range into five contiguous categories, which are then mapped to discrete building-dimension presets.

CC085 provides the same five-level split framing explicitly in terms of building types, using the lower/upper extreme limits and quartiles as boundaries to produce a “balanced” distribution of building archetypes.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Adapts bin boundaries to the current system’s distribution, improving within-system overview readability. | Not comparable across systems: “high” in one system may map to a different visual level in another. |
| Handles outliers by assigning them to explicit extreme categories. | Bin boundaries can shift when the dataset changes (and can introduce threshold “jumps” near quartiles). |

## Implementation Notes

CC024 describes this as a **BoxplotMapper** that computes boundaries for five categories (extremely low, low, average, high, extremely high). It also provides an example of mapping building length to a discrete set of outputs `{1, 2, 4, 8, 12}` based on the class’s attribute-count cluster.

## Evidence

- Produces “balanced” cities because boundaries are relative to the values present in the current system.
- Not suitable for comparisons across systems, since a “low” value in one system may be “high” in another.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — boxplot-based mapping discussion
- [CC035] Wettel PhD thesis — quartile/IQR-based boundary construction and mapping to building types
- [CC024] Wettel & Lanza (WASDeTT 2008) — BoxplotMapper categories and example discrete outputs
- [CC085] Wettel & Lanza (ICPC 2007) — boxplot-based mapping used to assign CodeCity building archetypes

## See Also

- [[discretized-metric-mapping]] — parent pattern for binning-based encodings
- [[threshold-metric-mapping]] — absolute-threshold alternative for cross-system comparability
- [[height-mapping]] — common target property for boxplot binning
