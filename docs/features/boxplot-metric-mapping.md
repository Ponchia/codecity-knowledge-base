---
id: F019
title: Boxplot-Based Metric Mapping
category: mapping
status: variant
introduced_by: CC023
implementations: [CodeCity]
related_features: [F018]
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-04
updated_from: [CC023, CC024, CC035, CC085]
---

# Boxplot-Based Metric Mapping

## Definition

A discretized mapping strategy that derives category boundaries from the distribution of metric values in the analyzed system (using a boxplot technique).

## Evidence / Tradeoff (from CC023)

- Produces “balanced” cities because boundaries are relative to the values present in the current system.
- Not suitable for comparisons across systems, since a “low” value in one system may be “high” in another.

## Mechanism Detail (from CC035)

CC035 describes computing quartiles and outlier limits (via IQR) and using those boundaries to split the input range into five contiguous categories, which are then mapped to discrete building-dimension presets.

CC085 provides the same five-level split framing explicitly in terms of building types, using the lower/upper extreme limits and quartiles as boundaries to produce a “balanced” distribution of building archetypes.

## Notes (from CC024)

CC024 describes this as a **BoxplotMapper** that computes boundaries for five categories (extremely low, low, average, high, extremely high). It also provides an example of mapping building length to a discrete set of outputs `{1, 2, 4, 8, 12}` based on the class’s attribute-count cluster.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — boxplot-based mapping discussion
- [CC035] Wettel PhD thesis — quartile/IQR-based boundary construction and mapping to building types
- [CC024] Wettel & Lanza (WASDeTT 2008) — BoxplotMapper categories and example discrete outputs
- [CC085] Wettel & Lanza (ICPC 2007) — boxplot-based mapping used to assign CodeCity building archetypes
