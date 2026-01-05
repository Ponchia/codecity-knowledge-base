---
id: F027
title: Method-as-Bricks Representation
category: mapping
status: variant
maturity: emerging
bounded_context: [city-metaphor]
introduced_by: CC035
implementations: [CodeCity, Getaviz]
related_features: [F002, F028, F031, F033]
supersedes: []
taxonomy:
  granularity: [method]
  visual_element: [brick]
  metric_category: [evolution, size]
last_updated: 2026-01-05
updated_from: [CC035, CC131]
---

# Method-as-Bricks Representation

## Problem & Motivation

This capability helps make important properties visible at a glance without relying on separate numeric views. A fine-grained representation where methods are shown as small cuboids (“bricks”) associated with their class, enabling method-level evolution and composition to be inspected within the city metaphor. Without it, metric signals remain harder to perceive and often require separate tables or charts.

## Definition

A fine-grained representation where methods are shown as small cuboids (“bricks”) associated with their class, enabling method-level evolution and composition to be inspected within the city metaphor.

## Mechanism (Solution)

**Input**: Methods of a class, plus method creation order/time (from the versioning repository).

**Process**:
1. Render the class as a platform/base.
2. Render each method as a brick and stack bricks in layers.
3. Order bricks by creation time (older below, newer above).

**Output**: A city where classes expose method-level structure and evolution cues.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Enables method-level composition/evolution cues while preserving class-level context. | Very high element counts can overwhelm performance and readability in large systems. |
| Supports fine-grained evolution views (age maps, timelines) inside a familiar city substrate. | Dense bricks can be hard to select/inspect without dedicated layouts, filtering, and tool support. |

## Implementation Notes

CC035 observes that extremely tall classes can compromise overview at this granularity, motivating the [[progressive-bricks-layout]] variant.

CC131 (Getaviz) provides a “City Bricks” visualization variant that renders method-level bricks inside class buildings.

## Sources

- [CC035] Wettel PhD thesis — fine-grained “method bricks” representation
- [CC131] Getaviz repository — “City Bricks” example output with method-level bricks

## See Also

- [[class-as-building]] — coarse-grained container that bricks refine
- [[progressive-bricks-layout]] — layout variant to keep brick-based cities readable at scale
- [[age-map]] — fine-grained age maps often apply to method bricks
- [[timeline-visualization]] — brick-based timelines for method “generations”
