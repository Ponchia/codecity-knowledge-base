---
id: F051
title: Database Access Visualization
category: analysis
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC079
implementations: [m3triCity]
related_features: [F015, F032, F029]
supersedes: []
taxonomy:
  granularity: [database, table, class]
  visual_element: [building, edge]
  metric_category: [size, coupling]
last_updated: 2026-01-05
updated_from: [CC079]
---

# Database Access Visualization

## Problem & Motivation

This capability helps connect analysis results to the system’s structural and spatial context. A city extension that visualizes an application’s **database** and **tables** together with the source-code city, and shows which classes access which tables. Without it, findings stay detached from structural context, reducing explainability and prioritization.

## Definition

A city extension that visualizes an application’s **database** and **tables** together with the source-code city, and shows which classes access which tables.

## Mechanism (Solution)

**Input**: Source code with database accesses (embedded queries) plus repository history.

**Process**:
1. Infer a database schema from the codebase (CC079 uses SQLInspect to extract embedded SQL and infer tables and accesses).
2. Compute table-level metrics (e.g., number of columns; number of accessing classes).
3. Render the database as a separate layer using unused 3D space:
   - **City with Clouds**: database above the city (sky).
   - **City with Underground**: database below the city (underground).
4. Connect classes to the tables they access using edges; render the database with light transparency to emphasize its inferred nature.
5. Keep database-related entities stable across evolution using the history-resistant layout.

**Output**: A combined view that supports understanding both code structure and how it interacts with persisted data over time.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Surfaces quality/evolution signals in context. | Overlays can overwhelm the base metaphor. |
| Supports prioritization (hotspots, anomalies). | Signals may be noisy or metric-dependent. |

## Implementation Notes

### Limitations (from CC079)

- Requires schema access or reliable schema inference; schema-less NoSQL and entity-version linking (e.g., rename detection) remain challenging.
- Multiple databases raise additional placement and scaling questions.

## Sources

- [CC079] Ardigò et al. (2021) — m3triCity 2 database visualization (sky/underground) + table-access edges + SQLInspect inference

## See Also

- [[time-travel]] — evolution navigation relying on stable placement over time
- [[bundled-edge-relations]] — edge-based relation visualization in cities (distinct use case)
