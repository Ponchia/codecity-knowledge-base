---
id: F025
title: Visual Tagging (Color & Transparency)
category: interaction
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC023
implementations: [CodeCity, CodeCharta, Code2City, Code2CityVR, SoftVis3D, m3triCity]
related_features: [F006, F022]
supersedes: []
taxonomy:
  granularity: [class, package]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC009, CC023, CC035, CC059, CC091, CC085, CC114, CC040, CC069, CC117]
---

# Visual Tagging (Color & Transparency)

## Problem & Motivation

Exploration sessions often involve returning to previously noticed artifacts and tracking progress. CC023 introduces tagging (color/transparency) to mark selections, while CC035 and CC085 describe marking visited territories to support habitability during longer comprehension tasks.

## Definition

An interaction that assigns colors and/or transparency to selected elements to bookmark, emphasize, or deemphasize parts of a city during exploration.

## Context & Applicability

**Use when:**
- You need to bookmark findings (suspected smells/hotspots) or mark explored vs unexplored areas during incremental exploration (CC023, CC085).
- You want lightweight, reversible emphasis without changing the underlying model or data (CC035).

**Avoid when:**
- Color is already reserved for metric encodings or overlays (e.g., disharmony maps, vulnerability severity) and tagging would conflict without a separate mode/legend (CC117, CC069).
- You need durable, shareable annotations beyond view-state; consider external tracking systems instead (uncertain).

**Prerequisites:** Selection support and an available visual channel (color and/or transparency) plus reset/clear actions; ideally persistence via view configuration/custom views (CC023, CC091).
**Alternatives:** [[query-filtering]] to focus subsets, or persistent presets/state via [[view-configuration]] and shareable view links (CC040).

## Forces

| Force | Pull |
|-------|------|
| Emphasis vs. semantic collision | Tagging helps focus, but can collide with color/opacity already used for metric or issue overlays. |
| Transient exploration vs. persistent annotation | Quick tags support exploration, but teams often want durable, shareable “marks” across sessions. |
| Multiple sets vs. user confusion | Multiple colors/levels enable richer workflows, but too many tags reduce interpretability. |

## Mechanism (Solution)

**Input**: A user-defined set (usually the current selection) plus a tagging action (assign color, set transparency, clear/reset).

**Process**:
1. Apply the chosen color (and/or adjust opacity) to the tagged entities (CC023).
2. Optionally de-emphasize non-tagged entities (e.g., increase transparency) so context remains but distraction is reduced (CC023).
3. Persist/reapply tagging state as part of a view configuration when supported (CC091, CC040).

**Output**: Tagged artifacts remain visually distinct across subsequent navigation and analysis.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Low-friction way to bookmark findings and track exploration progress. | Competes with other color-based encodings; misinterpretation risk without clear legends/modes. |
| Enables “keep context, highlight subset” workflows without changing layout. | Tag sets can accumulate and become hard to manage without good UI support and discipline. |

**Complexity**: Medium
**Performance**: Depends on picking/raycasting and UI update costs.
**Cognitive Load**: Medium (requires learning controls and feedback).

## Variations

### Variations (Code2City / Code2CityVR, from CC009)

CC009 describes color-based emphasis as part of interaction:
- Selected objects are highlighted (yellow).
- Search matches are highlighted (red).

### Variations (CodeCharta, from CC091)

CodeCharta supports persisting user-driven emphasis/de-emphasis state (e.g., marked packages and blacklisted/hidden items) as part of downloadable “Custom Views”, enabling sharing and reapplying such tagging without modifying the underlying map file.

### Variations (m3triCity, from CC059)

CC059 describes a “Colorization” setting that lets users assign specific colors to objects based on tags extracted from file names, regular expressions, or manual selection.

### Variations (SoftVis3D reflexion-model prototype, from CC114)

CC114 describes a “Highlight houses” feature that colors the buildings (classes/files) participating in a selected dependency relationship (e.g., purple) so users can quickly identify the concrete implementation elements responsible for an inter-module dependency.

## Implementation Notes

- Reserve a small, consistent palette for tagging distinct sets; keep it separate from metric scale legends (CC035).
- Provide quick actions: clear tags, reset to defaults, and manage tag sets (add/remove/invert selection) (CC023).
- Persist tagging in view-state (e.g., CodeCharta custom views; SoftVis3D share links) when collaboration/reproducibility matters (CC091, CC040).

## Evidence

### Evidence (from CC023)

CC023 describes tagging as assigning a particular color to a selection (and optionally applying transparency to the rest) so important structures remain easy to rediscover.

### Evidence (from CC035)

CC035 describes this as **marking**, using color and transparency during longer explorations (e.g., highlight starting points or fade uninteresting artifacts).

CC085 describes using color and transparency to mark already-explored “territories” at city scale, helping users keep track of progress during incremental exploration.

## Known Limitations

- Tagging can become confusing if too many sets/colors accumulate; UI support and discipline are needed (CC035).
- If color encodes both metrics and tags, users may misinterpret values; separate modes/legends help (CC035, CC117).
- Heavy translucency can reduce depth perception and readability depending on renderer/material settings.

## Open Questions

- How should tagging state be persisted and shared (view configs, deep links, external notes) without coupling it too tightly to paths/IDs?
- What are good UX patterns for managing multiple tag sets (named sets, legend, “clear by color”) in dense cities?
- Can tools reserve or multiplex the color channel so tagging stays usable even with strong overlays (smells, vulnerabilities)?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — tagging via color and transparency
- [CC035] Wettel PhD thesis — “Mark” interaction and usage examples
- [CC091] CodeCharta docs — Custom Views capturing marked/blacklisted state
- [CC009] Romano et al. (2019) — selection/search highlighting in Code2City/Code2CityVR
- [CC059] Pfahler et al. (2020) — colorization via tags/regex/manual selection in m3triCity
- [CC085] Wettel & Lanza (ICPC 2007) — marking explored areas using color and transparency
- [CC114] Mohsen (2025) — dependency-participant highlighting (“highlight houses”) using purple building recoloring
- [CC040] SoftVis3D repository — shareable view-state links (incl. selection/filters) that can persist emphasis/tagging-like state
- [CC069] Wueppelmann & Yigitbas (2025) — vulnerability-severity overlays competing for color semantics (SecCityVR)
- [CC117] Wettel & Lanza (SoftVis 2008) — disharmony-map overlays using vivid colors (color-channel conflicts with tagging)

## See Also

- [[selection]] — tagging is usually applied to the current selection
- [[query-filtering]] — compute taggable sets at scale
- [[disharmony-maps]] — example of a vivid color overlay that can conflict with tagging
- [[vulnerability-overlay]] — example of severity-based color overlays that compete with tag semantics
