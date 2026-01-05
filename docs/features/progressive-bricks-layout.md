---
id: F028
title: Progressive Bricks Layout
category: layout
status: variant
introduced_by: CC035
implementations: [CodeCity]
related_features: [F027, F005, F007]
taxonomy:
  granularity: [method]
  visual_element: [brick]
  metric_category: [size]
last_updated: 2026-01-02
updated_from: [CC035]
---

# Progressive Bricks Layout

## Definition

A self-adapting layout for method bricks that keeps cities readable when some classes have extremely high method counts, by distributing bricks around the building’s “walls” so height stays within a reasonable range.

## Mechanism (from CC035)

**Input**: Method bricks for a class (and their count).

**Process**:
1. Choose a side-capacity (bricks per wall) based on the total brick count.
2. Place bricks along the building’s perimeter in multiple layers, expanding wall width as needed.
3. Encode functionality magnitude primarily via building volume rather than extreme height.

**Output**: A city where very large classes still stand out by volume without dominating skyline height.

## Sources

- [CC035] Wettel PhD thesis — “Progressive Bricks” adaptive layout

