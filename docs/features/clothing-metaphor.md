---
id: F072
title: Clothing Metaphor
category: metaphor
status: variant
introduced_by: CC041
implementations: [CodeVestimenta]
related_features: [F001, F073, F074]
taxonomy:
  granularity: [class]
  visual_element: [clothing]
  metric_category: [size, coupling, quality]
last_updated: 2026-01-05
updated_from: [CC041]
---

# Clothing Metaphor

## Definition

A visualization metaphor that represents software classes as **garments** in a wardrobe, using familiar clothing shapes to make class-level metrics easier to interpret during program comprehension.

## Mechanism (from CC041)

**Input**: Object-oriented classes plus software quality metrics (e.g., LOC, NOC, RFC, DIT, CBO).

**Process**:
1. Render one clothing item per class.
2. Encode metrics into garment attributes (size, sleeves, color, garment type, collar/belt, stripes).
3. Present a legend to map garment icons back to class names.

**Output**: A wardrobe-style visualization that highlights classes with unusual metric profiles for quick inspection.

## Variations

| Implementation | Variation |
|----------------|-----------|
| CodeVestimenta | Generates static images (batches of ~50 classes) with a legend, rather than an interactive 3D scene. |

## Evidence

CC041 reports a controlled study (41 completed participants) where the clothing metaphor improved performance on harder comprehension tasks, especially dependency and design-quality questions.

## Sources

- [CC041] Introduces CodeVestimenta and the clothing metaphor with empirical validation.

## See Also

- [[F073]] class-as-clothing-item — class-to-garment mapping.
- [[F074]] clothing-attribute-mapping — metric encodings on garments.
- [[F001]] city-metaphor — alternative spatial metaphor.
