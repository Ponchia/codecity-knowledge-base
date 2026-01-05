---
id: F074
title: Clothing-Attribute Metric Mapping
category: mapping
status: variant
introduced_by: CC041
implementations: [CodeVestimenta]
related_features: [F072, F073]
taxonomy:
  granularity: [class]
  visual_element: [clothing]
  metric_category: [size, coupling, quality]
last_updated: 2026-01-05
updated_from: [CC041]
---

# Clothing-Attribute Metric Mapping

## Definition

A property-mapping strategy that encodes software quality metrics as **garment attributes** (size, sleeves, color, garment type, collar/belt, stripes) to communicate class complexity and coupling at a glance.

## Mechanism (from CC041)

**Input**: Per-class metrics computed from OO code (LOC, class members, class methods, NOC, RFC, DIT, CBO).

**Process**:
1. Map **Lines of Code** to overall garment size.
2. Map **Number of Class Members** to left sleeve length and **Number of Class Methods** to right sleeve length.
3. Map **Number of Child Classes (NOC)** to color (pale → dark scale).
4. Map **Response for Class (RFC)** to garment type using thresholds (t-shirt < 50, shirt 50–100, pants > 100).
5. Map **Depth of Inheritance Tree (DIT)** to a collar (or belt for pants) if DIT > 6.
6. Map **Coupling Between Objects (CBO)** to stripe patterns (none = uncoupled, one stripe = low coupling, two stripes = high coupling).

**Output**: Clothing items whose visual attributes summarize multiple metrics without requiring the user to read raw tables.

## Variations

| Implementation | Variation |
|----------------|-----------|
| CodeVestimenta | Combines continuous (size, color) and threshold-based (RFC, CBO, DIT) encodings in a single garment. |

## Evidence

CC041 reports improved task performance on harder comprehension questions when participants used the clothing encodings.

## Sources

- [CC041] Defines the metric-to-garment mapping and evaluates it in a controlled study.

## See Also

- [[F072]] clothing-metaphor — overall metaphor.
- [[F073]] class-as-clothing-item — class representation choice.
