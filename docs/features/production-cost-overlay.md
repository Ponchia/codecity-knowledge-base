---
id: F062
title: Production-Cost Overlay (Business Indicators)
category: analysis
status: variant
introduced_by: CC006
implementations: [Panas et al. 3D City prototype]
related_features: [F057, F058]
taxonomy:
  granularity: [package, class]
  visual_element: [district, building]
  metric_category: [evolution, behavior, quality]
last_updated: 2026-01-04
updated_from: [CC006]
---

# Production-Cost Overlay (Business Indicators)

## Definition

An analysis overlay that superimposes production- and maintenance-cost signals (e.g., work distribution, hot execution, frequent modifications, obsolete code) onto a software city to help stakeholders quickly identify high-cost or high-risk areas without changing the underlying structural mapping.

## Mechanism (from CC006)

**Input**: Static and dynamic analysis signals plus production context (e.g., execution frequency, modification frequency, ownership/work assignment, aspect tags).

**Process**:
1. Render a base software city showing structural entities (e.g., packages and classes) as city elements.
2. Compute or import cost-related indicators per entity.
3. Overlay indicators using visual annotations (colors and icon-like effects), such as:
   - work distribution (yellow + staff names),
   - “recycling”/obsolete parts (brown),
   - hot execution spots (fire),
   - aspects/cross-cutting concerns (colored markers),
   - high costs from frequent modifications (flashes).

**Output**: A city augmented with business/production annotations indicating where maintenance and operational effort concentrates.

## Sources

- [CC006] Panas et al. (IV 2003) — proposes a software-city overlay focused on production and maintenance-cost information.

## See Also

- [[vulnerability-overlay]] — security-focused overlay variant using SAST findings
- [[heat-map-overlay]] — heat-map overlay for runtime metrics

