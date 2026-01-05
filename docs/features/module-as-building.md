---
id: F044
title: Module-as-Building Mapping
category: mapping
status: variant
introduced_by: CC094
implementations: [JSCity]
related_features: [F003, F017]
taxonomy:
  granularity: [module]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-02
updated_from: [CC094]
---

# Module-as-Building Mapping

## Definition

A concept mapping where a software module (e.g., a JavaScript AMD/Angular module declaration) is represented as a dedicated building, making module structure visible in the same spatial metaphor as functions and districts.

## Mechanism (from CC094)

**Input**: A parsed program representation (AST) with module-declaration nodes and source locations.

**Process**:
1. Detect module-declaration call expressions (e.g., AMD `define(...)` and `angular.module(...)`).
2. Create a building record named `Module` (optionally including the module name when present).
3. Render the module as a building (with its own color/style) and attach it into the building hierarchy for hover/inspection and nested content.

**Output**: “Module” buildings that appear alongside function buildings within file/district context.

## Variations

CC094’s generator uses a fixed height for module buildings (instead of mapping a size metric to height). Other systems could map module-level metrics (size/coupling) using the same height/base mapping mechanisms used for other buildings.

## Sources

- [CC094] JSCity repository — UI help legend lists “AMD Module [Building]” and the generator detects module declarations

## See Also

- [[function-as-building]] — finer-grained building mapping often coexisting with modules
- [[package-as-district]] — common grouping dimension for module/function buildings
