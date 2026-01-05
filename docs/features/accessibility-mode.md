---
id: F078
title: Accessibility Mode
category: platform
status: experimental
maturity: research
bounded_context: [universal]
introduced_by: CC158
implementations: []
related_features: [F026, F037, F079]
supersedes: []
taxonomy:
  granularity: [file, class, method]
  visual_element: [building, district]
  metric_category: []
last_updated: 2026-01-05
updated_from: [CC158, CC159]
---

# Accessibility Mode

## Problem & Motivation

Software city visualizations are inherently visual, excluding blind and low-vision (BLV) users from program comprehension benefits. Screen readers cannot interpret 3D scenes, and existing accessibility efforts focus on simple charts, not complex 3D visualizations.

- **Challenge**: How do you make software city visualizations accessible to screen reader users?
- **Insight**: Hierarchical navigation, sonification, and structured descriptions can convey spatial data non-visually
- **Without this**: BLV developers cannot benefit from software visualization tools

## Definition

A platform feature that provides alternative modalities (hierarchical navigation, audio sonification, structured text descriptions) for consuming software city visualizations, enabling blind and low-vision users to explore and understand code structure.

## Context & Applicability

**Use when:**
- Supporting BLV users in the development team
- Compliance with accessibility standards (WCAG, Section 508)
- Multimodal exploration desired (combining visual with audio)

**Avoid when:**
- All users are fully sighted (but consider inclusivity)

**Prerequisites:** Screen reader compatibility; audio output capability

**Alternatives:** None - this is the only approach for BLV accessibility

## Mechanism (Solution)

**Input**: Software city visualization data (buildings, districts, metrics)

**Process**:
1. Organize visualization into hierarchical regions (districts → buildings → details)
2. Generate structured text descriptions for each element
3. Implement keyboard navigation through hierarchy
4. Provide sonification for metric values (pitch = height, volume = base)
5. Enable modality switching (visual ↔ text ↔ audio)

**Output**: BLV users can navigate and understand code structure through non-visual modalities

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Enables BLV participation in software visualization | Significant implementation effort |
| Multimodal approach benefits all users | Audio output may be disruptive in shared spaces |
| Compliance with accessibility standards | May not capture all nuances of 3D spatial layout |
| De-centers vision as primary modality | Learning curve for sonification interpretation |

**Complexity**: High - requires alternative interaction paradigms
**Performance**: Minimal overhead if implemented efficiently
**Cognitive Load**: Variable - depends on user's screen reader expertise

## Evidence

- Thompson et al. (CC158): 10 BLV users in co-design study over 5 months found hierarchical + sonification approach enabled autonomous visualization consumption
- Zong et al. (CC159): 5 expert screen-reader users found multimodal approach useful for creating, exploring, and discussing data

## Sources

- [CC158] Chart Reader CHI 2023 - hierarchical navigation + sonification for screen readers
- [CC159] MIT Umwelt 2024 - multimodal (visual + text + audio) accessibility approach

## See Also

- [[sonification-navigation]] — audio encoding of metric values
- [[navigation-modes]] — standard navigation this extends with accessible modes
- [[hover-inspection]] — could be adapted for keyboard/audio inspection
