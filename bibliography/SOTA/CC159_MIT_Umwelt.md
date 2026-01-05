# CC159: Umwelt: Accessible Data Visualization Tool

**Source URL**: https://news.mit.edu/2024/umwelt-enables-interactive-accessible-charts-creation-blind-low-vision-users-0327
**Institution**: MIT & University College London
**Year**: 2024
**Gap Category**: Accessibility

## Overview

Umwelt is software that enables blind and low-vision users to create customized, interactive data representations without requiring an initial visual chart.

## Key Features

### Three Modalities for Data Representation
1. **Visualization** - Traditional chart formats like scatterplots and line graphs
2. **Textual Description** - Structured text organizing data by relevant fields
3. **Sonification** - Converting data into non-speech audio tones

### User Experience
- Seamless switching between modalities depending on analytical needs
- Automatic heuristics generate default representations across all three formats
- Helps users overcome the "blank-slate effect"

## Accessibility Philosophy

Rather than converting existing visual charts, Umwelt "de-centers" visualization by treating it as one component of a multisensory experience.

> "Enabling the full participation of blind and low-vision people in data analysis involves seeing visualization as just one piece of this bigger, multisensory puzzle." - Jonathan Zong, lead researcher

## Research Team
- **Jonathan Zong** - EECS graduate student, lead author
- **Daniel Hajas** - UCL researcher, blind at age 16
- **Arvind Satyanarayan** - MIT associate professor, senior author

## User Study Findings
Five expert screen-reader users found the tool:
- "Useful for creating, exploring, and discussing data representations"
- Valuable for facilitating communication with sighted colleagues

## Relevance to CodeCity Knowledge Base
- **Primary**: Informs "multimodal accessibility" feature for software cities
- **Bounded Context**: universal
- **Feature Category**: platform/interaction
- **Key Techniques**:
  - Multi-modality (visual + text + audio)
  - Sonification of code metrics
  - De-centering visual-first design
- **Related Features**: Could inform F026 (navigation-modes) accessibility extensions
