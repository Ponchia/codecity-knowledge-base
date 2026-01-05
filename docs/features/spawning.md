---
id: F024
title: Spawning (Isolated Views)
category: interaction
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC023
implementations: [CodeCity]
related_features: [F022]
supersedes: []
taxonomy:
  granularity: [class, package]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC020, CC023, CC035, CC085]
---

# Spawning (Isolated Views)

## Problem & Motivation

Even with selection, the surrounding city can occlude the region of interest. CC023 introduces spawning a complementary view containing only the selected elements so users can focus on a district/subset without losing the ability to continue exploration.

## Definition

An interaction that creates a new, complementary view containing only a selected subset of entities, enabling focused exploration without visual clutter.

## Context & Applicability

**Use when:**
- You want to examine a selected district/subset without interference from the rest of the city (CC023, CC020, CC085).
- You need side-by-side comparison between an overview and a focused subset (CC035).

**Avoid when:**
- Users would lose necessary context; prefer dimming/non-destructive focus (visual tagging) or contextual dependency overlays instead (CC023).
- Spawning many views would overwhelm window/tab management and fragment attention.

**Prerequisites:** A selection mechanism plus view management (create/close, naming, and camera defaults; optionally sync between views) (CC023, CC035).
**Alternatives:** [[query-filtering]] (hide/exclude), [[visual-tagging]] (fade non-relevant elements), or [[elision]] (remove selected elements from the current view).

## Forces

| Force | Pull |
|-------|------|
| Focus vs. context | Isolate a subset to reduce clutter, but preserve a link back to the full city so users do not get lost. |
| Parallel views vs. attention fragmentation | Multiple simultaneous views enable comparison, but can overload window/tab management. |
| Reproducibility vs. ad-hoc exploration | Spawned views support exploration, but need naming/persistence to be shareable and repeatable. |

## Mechanism (Solution)

1. Select a set of entities.
2. Spawn a new view that isolates the selection.
3. Continue exploration within the isolated subset.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Reduces occlusion and visual clutter for a selected district/subset. | Easy to lose global context; requires clear “return to overview” affordances. |
| Enables side-by-side comparison (overview vs focused view). | View proliferation can fragment attention and increase render/memory cost. |

**Complexity**: Medium
**Performance**: Depends on picking/raycasting and UI update costs.
**Cognitive Load**: Medium (requires learning controls and feedback).

## Implementation Notes

- Carry over the same mapping/layout parameters to the spawned view so the subset remains interpretable (CC023).
- Provide a clear link back to the originating context (breadcrumbs, parent district name, or synchronized camera jumps) (CC020, CC085).
- Keep lifecycle management simple (close all spawned views, return-to-overview) to avoid fragmentation (CC035).

## Evidence

CC020 describes using spawned windows to focus on a specific district (package) when exploring the city overview.

CC085 describes spawning a new view containing only a selected district to reduce occlusion from unrelated classes during focused exploration.

## Variations

| Pattern | Variation | Notes |
|---------|-----------|------|
| Separate window/view | Spawn a complementary view containing only the selected district/subset | Canonical CodeCity behavior described as a “complementary view” (CC023, CC035). |
| In-place isolation | Temporarily hide/dim non-selected elements in the same view | Often overlaps with tagging/filtering patterns; treat as a lighter-weight alternative when multiple windows are undesirable (uncertain). |

## Known Limitations

- Spawning can fragment attention and reduce global context if overused (CC023).
- Divergent configurations between views can confuse interpretation unless synchronized or clearly labeled.
- Multiple views increase rendering/memory cost.

## Open Questions

- How should tools synchronize spawned views (camera linking, shared selection, shared filters) without creating confusing coupled state?
- What UI patterns keep “where did this view come from?” clear (breadcrumbs, origin links, automatic naming)?
- When is spawning preferable to query/filtering or visual tagging for the same user goal?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — spawning isolated districts/views
- [CC035] Wettel PhD thesis — spawning as “complementary view” for focused analysis
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — spawning separate windows for district-focused exploration
- [CC085] Wettel & Lanza (ICPC 2007) — district-only spawned view used to avoid occlusion

## See Also

- [[selection]] — primary input to spawning
- [[query-filtering]] — compute the subset to spawn
- [[visual-tagging]] — lighter-weight alternative for focus without new views
- [[elision]] — remove selected objects to reduce clutter in the current view
