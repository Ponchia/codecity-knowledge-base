---
id: F086
title: Developer Knowledge Map
category: analysis
status: experimental
maturity: emerging
bounded_context: [universal]
introduced_by: CC168
implementations: [CodeCompass]
related_features: [F071, F015, F031]
supersedes: []
taxonomy:
  granularity: [file, class, module]
  visual_element: [building, district]
  metric_category: [evolution, quality]
last_updated: 2026-01-05
updated_from: [CC168]
---

# Developer Knowledge Map

## Problem & Motivation

Large software projects accumulate tribal knowledge—certain developers become experts on certain modules. When developers leave or are unavailable, this knowledge is lost. Project managers ask: "Who knows this code?" and "What happens if this person leaves?"

- **Challenge**: How do you visualize developer expertise distribution across a codebase?
- **Insight**: Version control commit history reveals who has worked on what and how much
- **Without this**: Knowledge silos are invisible until a crisis (bus factor events)

## Definition

An analysis overlay that visualizes developer expertise and knowledge distribution across the codebase, calculating competence metrics from version control data (commit frequency, change significance) and identifying "gray zones" where knowledge is dangerously concentrated or scarce.

## Context & Applicability

**Use when:**
- Assessing bus factor risk across the codebase
- Onboarding new developers to unfamiliar areas
- Identifying knowledge silos before they become critical
- Planning team restructuring or knowledge transfer

**Avoid when:**
- Solo developer projects
- Codebases with insufficient version history
- Privacy concerns about individual performance metrics

**Prerequisites:** Version control history with author information

**Alternatives:** [[code-ownership-segmentation]] for file-level ownership; [[age-map]] for temporal analysis

## Mechanism (Solution)

**Input**: Version control history (commits, authors, changed files, timestamps)

**Process**:
1. Calculate per-developer competence scores for each code element:
   - Commit frequency (how often they've touched it)
   - Change significance (how much they've modified)
   - Recency weighting (recent knowledge valued higher)
2. Identify knowledge concentration patterns:
   - Single-expert zones (high bus factor risk)
   - Gray zones (no clear expert)
   - Well-distributed areas (healthy)
3. Visualize as overlay: building color/annotation showing expertise level
4. Aggregate to team/company views for management

**Output**: City where buildings show expertise distribution; "gray zones" highlighted as risk areas

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Makes invisible knowledge visible | May expose individual performance (privacy) |
| Identifies bus factor risks proactively | Commit count != expertise (junior may commit more) |
| Supports onboarding and knowledge transfer | Requires sufficient history to be meaningful |
| Enables data-driven team planning | Historical expertise may be stale |

**Complexity**: Medium - commit history mining; competence scoring
**Performance**: Low - analysis done offline; visualization is lightweight
**Cognitive Load**: Low - color coding is intuitive

## Implementation Notes

- **Key algorithms**: Author attribution from blame/commit history; competence scoring; decay functions for recency
- **Common pitfalls**: Equating commit count with expertise; ignoring code review contributions
- **Integration points**: Version control APIs; user directory for author resolution
- **Recommended defaults**: Red for gray zones; blue spectrum for expertise density

## Sources

- [CC168] Fekete & Porkoláb Acta Cybernetica 2024 - developer knowledge visualization in CodeCompass

## See Also

- [[code-ownership-segmentation]] — per-file ownership visualization
- [[evolution-visualization]] — temporal analysis this builds on
- [[age-map]] — related temporal analysis
- [[bus factor]] — the risk metric this helps assess

