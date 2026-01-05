---
id: F033
title: Timeline Visualization
category: analysis
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC116
implementations: [CodeCity, m3triCity]
related_features: [F015, F031, F027]
supersedes: []
taxonomy:
  granularity: [class, method, system]
  visual_element: [platform, brick]
  metric_category: [evolution]
last_updated: 2026-01-05
updated_from: [CC035, CC059, CC116]
---

# Timeline Visualization

## Problem & Motivation

Evolution analysis needs both temporal context and navigation. CC116 uses a fine-grained timeline (versions as platforms, methods as bricks) to show method “generations”, while CC059 uses a timeline widget to summarize change intensity and jump to points in history.

## Definition

An evolution visualization component that places versions along a time axis and provides a compact per-version representation, enabling both navigation (“jump to version”) and understanding of when entities appear/disappear or when changes concentrate.

## Context & Applicability

**Use when:**
- You want a quick overview of change concentration and the ability to jump to a specific version/commit (CC059).
- You need fine-grained per-entity evolution (e.g., method generations) across sampled versions (CC116).

**Avoid when:**
- History is very long or very fine-grained without aggregation; timeline becomes dense and unreadable (CC059).
- Users need full diff context across many files; a timeline should complement, not replace, diff tools.

**Prerequisites:** A version/commit sequence (timestamps) and per-version entity sets/metrics; optional bucketing/aggregation and linking to the main city view (CC116, CC059).
**Alternatives:** [[time-travel]] for stable-layout stepping, or [[delta-comparison]] for focused two-version comparisons.

## Forces

| Force | Pull |
|-------|------|
| Overview vs. detail | A compact timeline supports navigation, but detailed per-entity history can overwhelm the display without filtering. |
| Long histories vs. readability | Show full history for context, but provide zoom/bucketing to avoid dense, unreadable timelines. |
| Tight linking vs. independence | Link timeline selection to the city view for fluid exploration, but avoid confusing coupled state across views. |

## Mechanism (Solution)

**Input**: Version history for a class/package, including per-version method sets.

**Process**:
1. Render successive versions as platforms positioned along a left→right timeline.
2. Render methods as bricks on each platform.
3. Optionally combine with [[age-map]] coloring to highlight “generations” of methods introduced in the same version.

**Output**: A compact timeline view that supports comparing evolution across versions.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Provides temporal context (“when?”) and jump-to-version navigation alongside spatial context (“where?”). | Requires aggregation/zoom for long histories; otherwise becomes dense and hard to interpret. |
| Supports identifying change concentration and method “generations” over time. | Depends on stable identity mapping; refactorings can break continuity and mislead. |

**Complexity**: Medium
**Performance**: Depends on analysis pipeline and refresh cadence.
**Cognitive Load**: Medium–High (interpretation requires metric literacy).

## Variations

CC059 describes an interactive timeline below the main visualization that summarizes per-version change intensity for multiple metric categories (e.g., fields, methods, for-loops, LOC). Users can jump to a moment by clicking on the timeline; when a city object is selected, the timeline highlights all commits involving that entity.

## Implementation Notes

- Provide time bucketing (day/week/month/year) and zoom to manage long histories (CC059).
- Link timeline interactions to city state (jump to version; highlight commits for selected entity) (CC059).
- Keep per-version glyphs compact and use consistent color/legend for fine-grained timelines (CC116).

## Evidence

CC116 uses a fine-grained timeline to show method “generations” across versions (methods as bricks on successive version platforms), including a worked example timeline for a single class.

## Known Limitations

- Long histories can overwhelm timelines; aggregation sacrifices detail and can hide short-lived spikes (CC059).
- Fine-grained timelines scale poorly for entities with many methods unless filtered/summarized (CC116).
- Selection-linked highlights require stable identity mapping; refactorings can break continuity (CC059).

## Open Questions

- What aggregation strategies best preserve “spikes” and short-lived events while keeping timelines readable?
- How should timelines represent refactorings (move/rename/split) so continuity and discontinuity are both visible?
- When should timelines be global (system-level) vs local (per-entity), and how should tools bridge the two?

## Sources

- [CC035] Wettel PhD thesis — fine-grained timeline technique
- [CC059] Pfahler et al. (2020) — interactive evolution timeline (change categories + jump-to-version + selection-linked highlights)
- [CC116] Wettel & Lanza (WCRE 2008) — fine-grained timeline technique (methods as bricks across versions)

## See Also

- [[evolution-visualization]] — broader evolution signals and views
- [[time-travel]] — stable-layout stepping through versions
- [[age-map]] — complementary age coloring for entities in a timeline
