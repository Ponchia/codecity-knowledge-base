---
id: F020
title: Threshold-Based Metric Mapping
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

# Threshold-Based Metric Mapping

## Definition

A discretized mapping strategy that uses empirically established absolute thresholds for a metric to define category boundaries, enabling cross-system comparisons.

## Evidence / Tradeoff (from CC023)

- Enables comparisons among cities because the boundaries are absolute.
- Requires reliable thresholds per metric; effectiveness depends on their existence and quality.

## Example Thresholds (from CC035)

CC035 provides an example of cross-system thresholds for Java NOM used to form five bins: `[0,2)`, `[2,4)`, `[4,10)`, `[10,15)`, `[15,∞)`, derived from prior statistics on measured systems.

## Notes (from CC024)

CC024 frames this as a **ThresholdMapper** where users manually specify thresholds, often informed by statistical data about typical metric values. It also provides an example set of input clusters for Java NOM: `[0,4)`, `[4,7)`, `[7,10)`, `[10,15)`, `[15,∞)`. (CC035 and CC024 use different example thresholds; treat them as alternative threshold sets rather than a single canonical one.)

CC085 cites Java NOM threshold values `4 / 7 / 10 / 15` (from prior system measurements) and uses them as categorical boundaries for mapping class heights to CodeCity building types.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — threshold-based mapping discussion (thresholds cited from [13])
- [CC035] Wettel PhD thesis — concrete threshold example + discussion of comparability vs data availability
- [CC024] Wettel & Lanza (WASDeTT 2008) — ThresholdMapper concept and example Java NOM thresholds
- [CC085] Wettel & Lanza (ICPC 2007) — threshold values for Java NOM and mapping to building archetypes
