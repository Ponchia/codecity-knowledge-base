---
id: F071
title: Code Ownership Segmentation (Git Blame Hunks)
category: analysis
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC136
implementations: [CoderCity]
related_features: [F015, F006, F038]
supersedes: []
taxonomy:
  granularity: [file]
  visual_element: [building]
  metric_category: [evolution]
last_updated: 2026-01-05
updated_from: [CC136]
---

# Code Ownership Segmentation (Git Blame Hunks)

## Problem & Motivation

This capability helps connect analysis results to the system’s structural and spatial context. A visualization technique that encodes **code ownership** by subdividing a file’s building into segments derived from version-control blame hunks and coloring each segment by the responsible author, making authorship distribution visible within a file. Without it, findings stay detached from structural context, reducing explainability and prioritization.

## Definition

A visualization technique that encodes **code ownership** by subdividing a file’s building into segments derived from version-control blame hunks and coloring each segment by the responsible author, making authorship distribution visible within a file.

## Mechanism (Solution)

**Input**:
- Per-file line count.
- `git blame` (or equivalent) hunks containing author identity and line ranges.

**Process**:
1. Render each file as a building (height proportional to line count).
2. For each blame hunk, create a vertical building segment spanning the hunk’s line-range portion of the building.
3. Assign each segment a color mapped from the hunk’s author (with optional author/commit filters).

**Output**: Buildings visually reveal authorship distribution and ownership concentration within each file.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Makes ownership concentration and authorship distribution visible inside files (useful for bus-factor and review planning). | `git blame` is an imperfect proxy for ownership (rebases, formatting commits, generated code) and can mislead. |
| Supports team communication about “who touched what” in spatial context. | Author/color overlays can raise privacy concerns and can conflict with other color-based encodings. |

## Sources

- [CC136] CoderCity repository — file buildings segmented by git-blame hunks and colored by author to visualize code ownership

## See Also

- [[evolution-visualization]] — broader class of VCS-derived signals
- [[file-as-building]] — typical granularity for ownership segmentation
- [[color-mapping]] — author palettes are a color-mapping specialization
