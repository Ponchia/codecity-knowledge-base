---
id: F080
title: Gaze-Based Interaction
category: interaction
status: experimental
maturity: research
bounded_context: [universal]
introduced_by: CC161
implementations: []
related_features: [F011, F037, F026]
supersedes: []
taxonomy:
  granularity: [file, class, method]
  visual_element: [building, district]
  metric_category: []
last_updated: 2026-01-05
updated_from: [CC161]
---

# Gaze-Based Interaction

## Problem & Motivation

In VR software cities, controller-based interaction requires holding devices and explicit button presses. This is fatiguing for extended exploration and occupies hands that could be used for other tasks. Eye tracking hardware is increasingly available in VR headsets.

- **Challenge**: How do you enable hands-free interaction in VR software cities?
- **Insight**: Eye tracking can infer user intent from gaze direction and dwell time
- **Without this**: Users must hold controllers and press buttons for all interactions

## Definition

An interaction mode that uses eye tracking to enable hands-free navigation and selection in VR software cities, inferring user intent from gaze direction, dwell time, and gaze patterns.

## Context & Applicability

**Use when:**
- VR headset has integrated eye tracking (Quest Pro, Vive Pro Eye, etc.)
- Extended exploration sessions where controller fatigue is concern
- Hands-free operation needed (e.g., during discussion, presenting)

**Avoid when:**
- Eye tracking hardware not available
- User has eye tracking difficulties (nystagmus, etc.)
- High-precision selection required (gaze is imprecise)

**Prerequisites:** VR headset with eye tracking; calibration procedure

**Alternatives:** [[navigation-modes]] with controller input

## Mechanism (Solution)

**Input**: Eye tracking data (gaze ray, pupil position, blink detection)

**Process**:
1. **Gaze highlighting**: Element under gaze receives visual feedback
2. **Dwell selection**: Sustained gaze (e.g., 500ms) triggers selection
3. **Gaze navigation**: Look at navigation targets (arrows, minimap) to move
4. **Attention mapping**: Track gaze patterns to understand user focus
5. **Gaze + gesture**: Combine gaze target with hand gesture for precise action

**Output**: Hands-free selection, inspection, and navigation; attention heatmaps for analysis

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Hands-free operation | Hardware dependency (eye tracking) |
| Natural interaction (look at what interests you) | Gaze is imprecise (Midas touch problem) |
| Reduces controller fatigue | Calibration required per session/user |
| Enables attention analysis | Privacy concerns with gaze data |

**Complexity**: Medium - eye tracking APIs are mature; interaction design is nuanced
**Performance**: Minimal overhead; eye tracking runs at high frequency
**Cognitive Load**: Low - looking is natural; avoiding accidental activation is learned

## Open Questions

- Optimal dwell time for selection without false positives
- Combining gaze with other modalities (voice, gesture) for disambiguation
- Privacy implications of gaze data collection
- Effectiveness compared to controller-based interaction

## Sources

- [CC161] Eye-tracking in VR survey (Springer 2024) - comprehensive review of techniques and applications

## See Also

- [[vr-immersion]] — VR platform this enhances
- [[hover-inspection]] — similar concept adapted from desktop (mouse hover)
- [[navigation-modes]] — standard navigation this extends with gaze mode
