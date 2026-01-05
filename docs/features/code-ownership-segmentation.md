---
id: F071
title: Code Ownership Segmentation (Git Blame Hunks)
category: analysis
status: variant
introduced_by: CC136
implementations: [CoderCity]
related_features: [F015, F006, F038]
taxonomy:
  granularity: [file]
  visual_element: [building]
  metric_category: [evolution]
last_updated: 2026-01-04
updated_from: [CC136]
---

# Code Ownership Segmentation (Git Blame Hunks)

## Definition

A visualization technique that encodes **code ownership** by subdividing a file’s building into segments derived from version-control blame hunks and coloring each segment by the responsible author, making authorship distribution visible within a file.

## Mechanism (from CC136)

**Input**:
- Per-file line count.
- `git blame` (or equivalent) hunks containing author identity and line ranges.

**Process**:
1. Render each file as a building (height proportional to line count).
2. For each blame hunk, create a vertical building segment spanning the hunk’s line-range portion of the building.
3. Assign each segment a color mapped from the hunk’s author (with optional author/commit filters).

**Output**: Buildings visually reveal authorship distribution and ownership concentration within each file.

## Sources

- [CC136] CoderCity repository — file buildings segmented by git-blame hunks and colored by author to visualize code ownership
