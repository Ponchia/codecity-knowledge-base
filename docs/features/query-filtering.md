---
id: F023
title: Query-Based Filtering
category: interaction
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC023
implementations: [CodeCity, CodeCharta, Code2City, Code2CityVR, SoftVis3D, m3triCity, Langelier Quality Visualization Framework]
related_features: [F022, F049]
supersedes: []
taxonomy:
  granularity: [file, class, package]
  visual_element: [building, district]
  metric_category: [size, coupling]
last_updated: 2026-01-05
updated_from: [CC009, CC020, CC023, CC024, CC035, CC038, CC040, CC059, CC075, CC086, CC091, CC085, CC098]
---

# Query-Based Filtering

## Problem & Motivation

Manual selection is slow when cities contain thousands of entities. CC023 notes that manual selection can be cumbersome and introduces a query engine to search/filter by name, type, category, or relations to the current selection; later tools add regex/pattern UIs (CC038, CC091).

## Definition

A query mechanism that automatically selects or filters entities based on criteria (name/type/category/relationships), reducing manual selection effort in large cities.

## Context & Applicability

**Use when:**
- You need to find entities by name/type/category or by relationships to the current selection (CC023, CC035).
- You want to reduce clutter by hiding/excluding non-relevant entities or focusing on a computed subset (CC091, CC038).

**Avoid when:**
- Query criteria are poorly defined (inconsistent naming/metadata) and would produce noisy results.
- Users are not comfortable with regex/pattern syntaxes; prefer predefined queries and menu-driven filters (CC024, CC098).

**Prerequisites:** An indexed model (names, types, relationships) and a query/filter UI (predefined queries, generic query language, or regex/pattern input) (CC023, CC024, CC098).
**Alternatives:** [[selection]] for manual focus, [[hover-inspection]] for quick checks, or persistent presets via [[view-configuration]] / CodeCharta “Custom Views” (CC091).

## Forces

| Force | Pull |
|-------|------|
| Power vs. learnability | Expressive queries scale to large models, but regex/query languages can intimidate users without good presets and feedback. |
| Focus vs. context preservation | Aggressive filtering reduces clutter, but can hide context needed for interpretation unless the UI makes state obvious. |
| Interactivity vs. cost | Relation queries (calls, subclasses, dependencies) provide high value, but can be expensive without indexing and caching. |

## Mechanism (Solution)

**Input**: Query criteria (name/type/category), optional relation scope (relative to current selection), and a filter action (highlight, hide/exclude, spawn).

**Process**:
1. Interpret the criteria (string match / regex / predefined query).
2. Execute against the model (including relation queries like subclasses, invocations, and accesses) (CC023).
3. Apply the result to the visualization (select/highlight, hide/exclude, or spawn an isolated view).

**Output**: A computed focus set (and optionally a reduced visible set) that can drive further interactions.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Scales exploration beyond manual clicking by computing focus sets (names, types, relations). | Hidden/excluded state can confuse users if the tool does not clearly show “what’s filtered out”. |
| Enables repeatable workflows via predefined queries and saved filters. | Query errors (bad regex, unexpected matches) can derail exploration without previews and error feedback. |

**Complexity**: Medium
**Performance**: Depends on picking/raycasting and UI update costs.
**Cognitive Load**: Medium (requires learning controls and feedback).

## Variations

### Variations (CodeCharta, from CC091)

CodeCharta’s Web Studio provides a search/filter UI over buildings using `.gitignore`-style patterns. It supports hiding or excluding matched buildings (hidden buildings are flattened; excluded buildings are removed from view) and provides UI panels to inspect and restore hidden/excluded items.

### Variations (Code2City / Code2CityVR, from CC009)

CC009 describes Code2City and Code2CityVR offering search:
- **By name** (e.g., types matching a string).
- **By callers** (types that call methods of a specified type).

Matches are highlighted in the city (red).

### Variations (SoftVis3D, from CC038)

CC038 describes include/exclude options where the file name is checked against a user-provided regular expression (JavaScript `RegExp` semantics). The captured `visualizationStatus` configuration also shows separate `includeClasses` and `excludeClasses` filter values and an option to exclude test classes.

CC040 confirms this is implemented as distinct include/exclude filters that match file names using JavaScript `String.match(...)` semantics.

### Variations (m3triCity, from CC059)

CC059 describes a settings option to hide objects matching a regular expression.

### Variations (Langelier framework, from CC075)

CC075 implements two filtering modes:
- **Metric-distribution filters** that highlight extreme values (e.g., via boxplot-based thresholds).
- **Structural filters** that keep only classes related by a chosen UML relation (associations, aggregations, generalizations) to a selected class.

## Implementation Notes

CC024 groups specialized queries into:
- **Absolute** queries (e.g., interfaces, root classes)
- **Relative** queries based on the current selection (e.g., classes that invoke methods of the selected ones)

CC086 reiterates the same split (absolute vs selection-relative), framing the query mechanism as a way to indirectly interact with city artifacts alongside contextual menus.

CC085 gives a concrete example of selection-relative querying in CodeCity by selecting a class and triggering a “select subclass hierarchy” operation via menus, then applying further selection-driven actions (e.g., recoloring or changing transparency of non-selected elements).

CC098 describes the same split in slightly different terms (“general” vs “selection-related” queries) and notes CodeCity offers both a generic query language and predefined query actions.

## Evidence

### Evidence (from CC023)

CC023 describes criteria including:
- Name matching (e.g., classes containing “UML”)
- Type-based selection (e.g., all classes in a “GUI” district)
- Category-based selection (e.g., root classes)
- Relations to current selection (e.g., subclasses/superclasses; invocation/access relationships)

### Evidence (from CC035)

CC035 further describes CodeCity queries as supporting:
- Searching by string and type (e.g., all packages)
- Vocabulary/term-oriented searches
- Queries relative to the current selection (e.g., dependency context and related artifacts)

It also notes a query engine and a “generic query” mechanism that supports prototyping new queries via short code snippets.

## Known Limitations

- Queries can return very large result sets; additional filtering/aggregation may be needed (CC023).
- Regex/pattern matching can be confusing; UIs should preview results and provide error feedback (CC038, CC091).
- Relation-based queries depend on the quality of the dependency model; dynamic behavior may not be captured (uncertain).

## Open Questions

- What is the best mix of predefined queries vs free-form query languages for typical developer workflows?
- How should tools preview and explain query results (why did this match?) to reduce trust issues and mistakes?
- Can query/filter state be made reliably shareable/reproducible across machines and tool versions (schema evolution, path differences)?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — filtering + query engine
- [CC035] Wettel PhD thesis — query criteria and query-engine prototyping support
- [CC091] CodeCharta docs — search/filter UI with hide/exclude behavior
- [CC009] Romano et al. (2019) — name/caller search in Code2City/Code2CityVR
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — query mechanism for interacting with entities
- [CC024] Wettel & Lanza (WASDeTT 2008) — absolute vs selection-relative query categories
- [CC086] Wettel & Lanza (2008) — query mechanism + examples of absolute vs selection-relative queries
- [CC085] Wettel & Lanza (ICPC 2007) — query-based selection operations (e.g., subclass hierarchy selection)
- [CC038] SoftVis3D website — regex-based include/exclude filters (incl. test-class variant)
- [CC040] SoftVis3D repository — include/exclude filter implementation (regex-like `match`)
- [CC059] Pfahler et al. (2020) — regex-based hiding of city objects in m3triCity
- [CC075] Langelier et al. (ASE 2005) — extreme-value and relation-based filtering for quality analysis
- [CC098] Wettel & Lanza (2008 tech report) — generic query language + predefined queries (general vs selection-related)

## See Also

- [[selection]] — baseline interaction that queries often produce/modify
- [[spawning]] — isolate query results into a separate view
- [[visual-tagging]] — emphasize/deemphasize sets found via queries
- [[view-configuration]] — persist filters/queries as part of a reusable view
