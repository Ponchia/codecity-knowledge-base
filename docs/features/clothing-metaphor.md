---
id: F072
title: Clothing Metaphor
category: metaphor
status: variant
maturity: emerging
bounded_context: [clothing-metaphor]
introduced_by: CC041
implementations: [CodeVestimenta]
related_features: [F001, F073, F074]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [clothing]
  metric_category: [size, coupling, quality]
last_updated: 2026-01-05
updated_from: [CC041]
---

# Clothing Metaphor

## Problem & Motivation

This capability helps provide a familiar mental model that supports orientation and discussion. A visualization metaphor that represents software classes as **garments** in a wardrobe, using familiar clothing shapes to make class-level metrics easier to interpret during program comprehension. Without it, users lose a consistent metaphor for reasoning about structure and scale.

## Definition

A visualization metaphor that represents software classes as **garments** in a wardrobe, using familiar clothing shapes to make class-level metrics easier to interpret during program comprehension.

## Mechanism (Solution)

**Input**: Object-oriented classes plus software quality metrics (e.g., LOC, NOC, RFC, DIT, CBO).

**Process**:
1. Render one clothing item per class.
2. Encode metrics into garment attributes (size, sleeves, color, garment type, collar/belt, stripes).
3. Present a legend to map garment icons back to class names.

**Output**: A wardrobe-style visualization that highlights classes with unusual metric profiles for quick inspection.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Provides an intuitive mental model for structure. | Metaphor can oversimplify or mislead. |
| Supports orientation via spatial cues. | Different users may interpret metaphors differently. |

## Variations

| Implementation | Variation |
|----------------|-----------|
| CodeVestimenta | Generates static images (batches of ~50 classes) with a legend, rather than an interactive 3D scene. |

## Evidence

CC041 reports a controlled study (41 completed participants) where the clothing metaphor improved performance on harder comprehension tasks, especially dependency and design-quality questions.

## Sources

- [CC041] Introduces CodeVestimenta and the clothing metaphor with empirical validation.

## See Also

- [[class-as-clothing-item]] — class-to-garment mapping.
- [[clothing-attribute-mapping]] — metric encodings on garments.
- [[city-metaphor]] — alternative spatial metaphor.
