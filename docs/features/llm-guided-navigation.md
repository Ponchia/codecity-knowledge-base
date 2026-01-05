---
id: F075
title: LLM-Guided Navigation
category: interaction
status: experimental
maturity: research
bounded_context: [universal]
introduced_by: CC155
implementations: []
related_features: [F026, F037, F022]
supersedes: []
taxonomy:
  granularity: [file, class, method, function]
  visual_element: [building, district]
  metric_category: []
last_updated: 2026-01-05
updated_from: [CC155]
---

# LLM-Guided Navigation

## Problem & Motivation

Navigating large-scale software visualizations (thousands of buildings/districts) requires users to know WHERE to look. Traditional navigation relies on manual exploration, search queries, or predefined filters. Users often don't know the right search terms or which part of the codebase to explore for their task.

- **Challenge**: How do you help users find relevant code elements when they can only describe their intent in natural language?
- **Insight**: LLMs can interpret developer intent from natural language queries and map them to structural code elements
- **Without this**: Users must manually explore or guess search terms, missing relevant code

## Definition

A navigation enhancement that uses Large Language Models to interpret natural language developer queries and guide exploration to relevant code elements in the visualization, combining AI semantic understanding with deterministic structural views.

## Mechanism (Solution)

**Input**: Natural language query describing developer intent (e.g., "show me the authentication logic" or "where is user input validated?")

**Process**:
1. LLM interprets query to identify relevant code concepts, patterns, or structures
2. System maps LLM output to actual code elements in the codebase
3. Navigation is guided to highlight/focus relevant buildings/districts
4. Historical context tracks exploration path for coherent workflow

**Output**: Visualization navigates to and highlights relevant code elements; user can refine queries iteratively

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Enables intent-based exploration without knowing exact code structure | Depends on LLM accuracy and latency |
| Reduces time to find relevant code for unfamiliar codebases | May hallucinate non-existent code locations |
| Bridges natural language to structural visualization | Requires LLM integration infrastructure |
| Supports exploratory program comprehension | Privacy concerns with code sent to external LLMs |

**Complexity**: High - requires LLM integration, code indexing, and mapping logic
**Performance**: Variable - depends on LLM response time (typically 1-5 seconds)
**Cognitive Load**: Low for users - natural language is intuitive

## Open Questions

- Optimal prompt engineering for code navigation queries
- How to handle ambiguous queries with multiple valid interpretations
- Local vs cloud LLM trade-offs for code privacy
- Integration with existing navigation modes (complement vs replace)

## Sources

- [CC155] Alebachew 2025 - hybrid LLM + UML system for large-scale codebase exploration

## See Also

- [[navigation-modes]] — traditional navigation methods this could enhance
- [[hover-inspection]] — could be enhanced with LLM-generated explanations
- [[selection]] — LLM could guide what to select next
