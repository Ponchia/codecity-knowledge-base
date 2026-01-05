---
id: F021
title: Stacked-Platform Topology
category: layout
status: canonical
introduced_by: CC023
implementations: [CodeCity]
related_features: [F008, F017]
taxonomy:
  granularity: [class]
  visual_element: [platform, district, building]
  metric_category: [size]
last_updated: 2026-01-02
updated_from: [CC023]
---

# Stacked-Platform Topology

## Definition

A topology technique that represents nested packages as stacked platforms, placing buildings at different altitudes to make package nesting visible and improve orientation.

## Mechanism (from CC023)

**Input**: Nested package hierarchy.

**Process**:
1. Layout each package/district separately.
2. For nested packages, stack their districts as platforms at increasing altitudes.
3. Place buildings on the platform corresponding to their package.

**Output**: A city where altitude conveys package nesting.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — “topology” via stacked platforms

