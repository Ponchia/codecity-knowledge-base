---
id: F079
title: Sonification Navigation
category: interaction
status: experimental
maturity: research
bounded_context: [universal]
introduced_by: CC158
implementations: []
related_features: [F078, F026, F005, F006]
supersedes: []
taxonomy:
  granularity: [file, class, method]
  visual_element: [building]
  metric_category: [size, complexity, coupling]
last_updated: 2026-01-05
updated_from: [CC158, CC159]
---

# Sonification Navigation

## Problem & Motivation

Visual encodings (height, color, base) cannot be perceived by blind users and may be missed by sighted users focused elsewhere. Audio provides a parallel channel that can convey metric information without visual attention.

- **Challenge**: How do you convey metric values without requiring visual attention?
- **Insight**: Audio parameters (pitch, volume, duration, timbre) can encode numeric values
- **Without this**: Metric perception requires visual focus; BLV users excluded entirely

## Definition

An interaction feature that encodes software metrics as non-speech audio (sonification), enabling users to perceive metric values through sound while navigating the visualization—particularly valuable for accessibility and eyes-free exploration.

## Mechanism (Solution)

**Input**: Metric values (LOC, complexity, etc.) for code elements being navigated

**Process**:
1. Map metric to audio parameter:
   - Height/size → pitch (higher = taller building)
   - Complexity → duration or density of tones
   - Coverage → volume or brightness
2. Trigger audio when element receives focus (keyboard navigation or gaze)
3. Allow fast-stepping through elements with continuous audio stream
4. Provide audio landmarks for orientation (district entry/exit sounds)

**Output**: Users hear metric values as they navigate; can identify outliers by audio alone

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Enables BLV user participation | Learning curve for audio interpretation |
| Provides parallel information channel | May be disruptive in shared spaces |
| Enables eyes-free exploration | Precision limited compared to visual |
| Can highlight outliers even when not visible | Requires careful audio design |

**Complexity**: Medium - audio generation is straightforward; mapping design is nuanced
**Performance**: Minimal - audio generation is lightweight
**Cognitive Load**: Medium initially; decreases with practice

## Implementation Notes

- **Key algorithms**: Linear mapping of metric range to pitch range (e.g., 200-800 Hz)
- **Common pitfalls**: Too-wide pitch ranges become unpleasant; too-narrow indistinguishable
- **Recommended defaults**: Pitch for primary metric; volume for secondary; duration for selection feedback

## Sources

- [CC158] Chart Reader CHI 2023 - sonification for data visualization accessibility
- [CC159] MIT Umwelt 2024 - sonification as one of three modalities for data representation

## See Also

- [[accessibility-mode]] — parent feature this belongs to
- [[height-mapping]] — visual encoding this parallels in audio
- [[color-mapping]] — another visual encoding that could be sonified
