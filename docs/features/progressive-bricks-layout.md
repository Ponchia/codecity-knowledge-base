---
id: F028
title: Progressive Bricks Layout
category: layout
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC035
implementations: [CodeCity]
related_features: [F027, F005, F007]
supersedes: []
taxonomy:
  granularity: [method]
  visual_element: [brick]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC035]
---

# Progressive Bricks Layout

## Problem & Motivation

This capability helps keep spatial organization interpretable and memorable as the city grows. A self-adapting layout for method bricks that keeps cities readable when some classes have extremely high method counts, by distributing bricks around the building’s “walls” so height stays within a reasonable range. Without it, navigation and spatial memory degrade because placement feels arbitrary or unstable.

## Definition

A self-adapting layout for method bricks that keeps cities readable when some classes have extremely high method counts, by distributing bricks around the building’s “walls” so height stays within a reasonable range.

## Mechanism (Solution)

**Input**: Method bricks for a class (and their count).

**Process**:
1. Choose a side-capacity (bricks per wall) based on the total brick count.
2. Place bricks along the building’s perimeter in multiple layers, expanding wall width as needed.
3. Encode functionality magnitude primarily via building volume rather than extreme height.

**Output**: A city where very large classes still stand out by volume without dominating skyline height.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Prevents extremely tall “brick towers” for classes with many methods, improving readability. | Layout is less intuitive than simple stacking and may require explanation/legends. |
| Preserves visibility of large classes by using volume/perimeter rather than height alone. | Adds layout complexity and can increase the footprint/space used by very large classes. |

## Sources

- [CC035] Wettel PhD thesis — “Progressive Bricks” adaptive layout

## See Also

- [[method-as-bricks]] — representation that this layout makes scalable
- [[class-as-building]] — coarse structure that bricks refine
- [[height-mapping]] — height-limiting motivation for progressive bricks
