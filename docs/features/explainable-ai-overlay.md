---
id: F087
title: Explainable AI Overlay
category: analysis
status: experimental
maturity: research
bounded_context: [universal]
introduced_by: CC169
implementations: []
related_features: [F057, F058, F075]
supersedes: []
taxonomy:
  granularity: [file, class, method]
  visual_element: [building]
  metric_category: [quality, security]
last_updated: 2026-01-05
updated_from: [CC169]
---

# Explainable AI Overlay

## Problem & Motivation

AI/ML models increasingly power software analysis—defect prediction, vulnerability detection, code smell identification. These models output predictions but not explanations. Developers see "this file is likely buggy" but not WHY, making it hard to trust or act on predictions.

- **Challenge**: How do you make AI-driven code analysis actionable and trustworthy?
- **Insight**: XAI techniques can explain predictions at file and line level, showing which factors drove the prediction
- **Without this**: AI predictions are black boxes; developers ignore or distrust them

## Definition

An analysis overlay that visualizes not just AI model predictions (defect probability, vulnerability risk) but also the explanations for those predictions—highlighting which code characteristics, metrics, or patterns drove the AI's assessment at file and line level.

## Context & Applicability

**Use when:**
- AI/ML models are used for code analysis (defect prediction, security, quality)
- Developers need to understand and act on AI predictions
- Building trust in AI-assisted workflows
- Quality improvement planning based on ML insights

**Avoid when:**
- No AI/ML models in the analysis pipeline
- Simple rule-based analysis where explanations are trivial
- Real-time requirements where XAI adds latency

**Prerequisites:** ML model with XAI support (SHAP, LIME, etc.); prediction pipeline

**Alternatives:** [[vulnerability-overlay]] for rule-based security; [[disharmony-maps]] for metric-based smells

## Mechanism (Solution)

**Input**: ML model predictions + XAI explanations; code model

**Process**:
1. Run ML model (defect prediction, etc.) on codebase
2. Generate XAI explanations for each prediction:
   - Feature importance (which metrics mattered most)
   - Line-level attribution (which lines contributed to prediction)
3. Visualize predictions as building color/height overlay
4. On inspection, show explanation breakdown:
   - Top contributing factors
   - Highlighted risky lines
   - Comparison to similar files
5. Provide actionable guidance based on explanation

**Output**: City with AI risk overlay; clicking buildings shows explanation of why AI flagged them; line-level highlighting in code view

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Makes AI predictions actionable | XAI computation adds latency |
| Builds trust through transparency | Explanations may be complex to interpret |
| Enables data-driven quality improvement | Depends on quality of underlying ML model |
| Identifies specific improvement targets | May surface unexpected/uncomfortable patterns |

**Complexity**: High - requires XAI pipeline integration; explanation visualization
**Performance**: Variable - XAI computation can be expensive
**Cognitive Load**: Medium - understanding explanations requires some ML literacy

## Implementation Notes

- **Key algorithms**: SHAP, LIME for feature importance; attention maps for line attribution
- **Common pitfalls**: Overwhelming users with too much explanation detail; explanations that are themselves confusing
- **Integration points**: ML prediction pipeline; XAI libraries; code navigation
- **Recommended defaults**: Top-3 factors per prediction; optional line-level detail

## Open Questions

- Optimal level of explanation detail for different users
- How to visualize uncertainty in predictions
- Integration with existing code review workflows
- Whether to explain false positives/negatives

## Sources

- [CC169] Tantithamthavorn & Jiarpakdee - XAI for SE book/resource (Monash University)

## See Also

- [[vulnerability-overlay]] — security overlay (could be XAI-enhanced)
- [[heat-map-overlay]] — generic overlay mechanism
- [[llm-guided-navigation]] — another AI integration approach
- [[disharmony-maps]] — traditional metric-based smell detection

