---
id: F027
title: Method-as-Bricks Representation
category: mapping
status: variant
introduced_by: CC035
implementations: [CodeCity, Getaviz]
related_features: [F002, F028, F031, F033]
taxonomy:
  granularity: [method]
  visual_element: [brick]
  metric_category: [evolution, size]
last_updated: 2026-01-04
updated_from: [CC035, CC131]
---

# Method-as-Bricks Representation

## Definition

A fine-grained representation where methods are shown as small cuboids (“bricks”) associated with their class, enabling method-level evolution and composition to be inspected within the city metaphor.

## Mechanism (from CC035)

**Input**: Methods of a class, plus method creation order/time (from the versioning repository).

**Process**:
1. Render the class as a platform/base.
2. Render each method as a brick and stack bricks in layers.
3. Order bricks by creation time (older below, newer above).

**Output**: A city where classes expose method-level structure and evolution cues.

## Notes

CC035 observes that extremely tall classes can compromise overview at this granularity, motivating the [[progressive-bricks-layout]] variant.

CC131 (Getaviz) provides a “City Bricks” visualization variant that renders method-level bricks inside class buildings.

## Sources

- [CC035] Wettel PhD thesis — fine-grained “method bricks” representation
- [CC131] Getaviz repository — “City Bricks” example output with method-level bricks
