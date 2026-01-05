---
id: F081
title: Test Coverage Overlay
category: analysis
status: experimental
maturity: emerging
bounded_context: [universal]
introduced_by: CC163
implementations: []
related_features: [F058, F057, F006]
supersedes: []
taxonomy:
  granularity: [file, class, method]
  visual_element: [building]
  metric_category: [quality]
last_updated: 2026-01-05
updated_from: [CC163]
---

# Test Coverage Overlay

## Problem & Motivation

Developers need to understand which parts of the codebase are well-tested and which lack coverage. Traditional coverage reports are line-level tables that don't show the spatial distribution of coverage across the architecture.

- **Challenge**: How do you visualize test coverage in the context of code structure?
- **Insight**: Coverage can be mapped as a color overlay on software city buildings
- **Without this**: Coverage data is disconnected from architectural context

## Definition

An analysis overlay that visualizes test coverage data (line/branch coverage percentages) on software city buildings, typically using color gradients from red (low coverage) to green (high coverage), enabling identification of untested architectural areas.

## Context & Applicability

**Use when:**
- Test coverage data is available (Cobertura, JaCoCo, lcov)
- Identifying undertested parts of the codebase
- Reviewing coverage impact of changes in merge requests
- Quality gate enforcement visualization

**Avoid when:**
- No test coverage data available
- Coverage metric is inappropriate for the codebase

**Prerequisites:** Coverage report in supported format (Cobertura XML, JaCoCo XML)

**Alternatives:** [[heat-map-overlay]] for generic metric overlays; [[vulnerability-overlay]] for security focus

## Mechanism (Solution)

**Input**: Test coverage report (Cobertura/JaCoCo format) + software city model

**Process**:
1. Parse coverage report to extract per-file/class coverage percentages
2. Map coverage percentage to color gradient:
   - 0-50%: Red spectrum (high risk)
   - 50-80%: Yellow spectrum (moderate)
   - 80-100%: Green spectrum (well-covered)
3. Apply color as building surface/material
4. Optionally show line-level coverage as building floor coloring

**Output**: City where building color indicates test coverage; untested areas visually prominent

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Shows coverage in architectural context | Coverage % may not reflect test quality |
| Identifies untested areas at a glance | Requires coverage data from CI pipeline |
| Integrates with CI/CD workflows | Color can conflict with other color mappings |
| Supports quality gate visualization | May oversimplify (100% coverage != well-tested) |

**Complexity**: Low - straightforward metric-to-color mapping
**Performance**: Minimal - parsing coverage report is fast
**Cognitive Load**: Low - red/green intuitive (but consider colorblindness)

## Implementation Notes

- **Key algorithms**: Parse Cobertura XML; aggregate line coverage to file/class level
- **Common pitfalls**: Handling files not in coverage report (mark as "unknown"); colorblind-safe palettes
- **Integration points**: CI/CD pipeline artifacts; merge request visualization
- **Recommended defaults**: Red-yellow-green gradient; "unknown" as gray

## Sources

- [CC163] GitLab Test Coverage Visualization - CI/CD integration patterns for coverage display

## See Also

- [[heat-map-overlay]] — generic overlay mechanism this specializes
- [[vulnerability-overlay]] — similar overlay for security metrics
- [[color-mapping]] — underlying color encoding mechanism
