---
id: F054
title: Class-as-District Mapping
category: mapping
status: variant
maturity: emerging
bounded_context: [city-metaphor]
introduced_by: CC102
implementations: [CodeMetropolis]
related_features: [F002, F017, F045]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [district]
  metric_category: [size, complexity]
last_updated: 2026-01-05
updated_from: [CC102]
---

# Class-as-District Mapping

## Problem & Motivation

This capability helps make important properties visible at a glance without relying on separate numeric views. A concept mapping where each class is rendered as a **district/plate** (a fenced area) rather than a building, providing a bounded region that contains the class’s internal elements (e.g., method floors). Without it, metric signals remain harder to perceive and often require separate tables or charts.

## Definition

A concept mapping where each class is rendered as a **district/plate** (a fenced area) rather than a building, providing a bounded region that contains the class’s internal elements (e.g., method floors).

## Mechanism (Solution)

**Input**: Classes and their contained methods (with per-method metrics).

**Process**:
1. Create a district (grass plate with fences) for each class.
2. Place a building container inside the district and stack method floors within it.
3. Use per-method metrics to size the floors (e.g., width/length from complexity, height from logical LOC).

**Output**: A city where class boundaries are represented as districts, with method-level detail inside.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Adds an at-a-glance quantitative cue. | Outliers can dominate perception without scaling/binning. |
| Supports quick comparison across many entities. | Multiple encodings can increase visual clutter. |

## Sources

- [CC102] Balogh & Beszedes (2013) — CodeMetropolis uses districts to represent classes

## See Also

- [[class-as-building]] — more common class representation
- [[method-as-floors]] — method-level structure inside a class
- [[package-as-district]] — higher-level containment mapping
