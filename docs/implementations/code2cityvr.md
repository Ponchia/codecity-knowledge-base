---
id: I017
name: Code2CityVR
origin: Romano et al. (Roma2019b)
year_introduced: 2019
status: research
source_refs: [CC009, CC055, CC064]
repo_url: null
demo_url: http://graphics.unibas.it/Code2City/index.md.html
primary_language: C++ / Blueprints (Unreal Engine 4)
features_implemented: [F001, F002, F005, F006, F007, F008, F011, F017, F022, F023, F025, F026, F034]
last_updated: 2026-01-04
updated_from: [CC009, CC055, CC064]
---

# Code2CityVR

## Overview

VR-based version of Code2City that keeps the same city-metaphor feature set but changes interaction to an immersive head-mounted display setup. CC009 describes Code2CityVR as using Oculus Rift and a controller for gaze-based selection and city navigation.

## VR Interaction (from CC009)

- **Select** by looking at an object and pressing a controller button.
- **Scale**: the rendered scene is proportional to the user to strengthen the “being in a real city” feeling.
- **Navigation**: fly over the city (bird’s-eye view), climb buildings, look from tall buildings, and walk around at street level.
- **Search input**: a virtual keyboard is shown; includes text completion.
- **Movement speed**: user-adjustable.

## Additional VR Notes (from CC055)

- **Hardware**: Oculus Rift HMD with an Xbox One wireless controller (also mentions an earlier HTC Vive variant).
- **Selection**: gaze-based pointing (head direction) plus controller button to select.
- **Search input**: virtual keyboard can be toggled; includes text completion.

## Empirical Note (from CC009)

CC009 reports that Code2CityVR significantly improves **positive affects** compared to Eclipse, but most participants reported at least one VR side effect (e.g., headache, nausea, visual annoyance).

## Empirical Evidence (from CC064)

CC064 reports a controlled experiment comparing Eclipse vs Code2City vs Code2CityVR (FindBugs; 42 participants in experimental sessions). Key outcomes:

- **Correctness**: both city-metaphor treatments outperform Eclipse (ANOVA p=0.005; Tukey HSD p=0.006 and p=0.035).
- **Time**: Code2CityVR is significantly faster than both Code2City and Eclipse (ANOVA p<0.001; post-hoc p=0.001 and p<0.001).
- **Side effects**: only 3/17 Code2CityVR participants reported no side effects; headache, nausea, and visual annoyance were common.

## Sources

- [CC009] Romano et al. — tool description + controlled experiment on feelings/emotions/thinking
- [CC055] Code2City project report — UE4 implementation details and concrete VR interaction/controller mapping
- [CC064] Romano et al. (IST 2019) — controlled experiment comparing on-screen vs VR city-metaphor use (plus Eclipse baseline)
