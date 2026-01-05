#!/usr/bin/env python3
"""
Normalize documentation to match the current PLAN.md / LLM_INSTRUCTIONS.md schemas.

Focus:
- Feature cards: add missing frontmatter keys and reshape headings into Pattern Language format.
- Glossary: add missing "**Bounded Context**" line per entry.

This script is intentionally conservative:
- It preserves all existing extracted content (tables/bullets) and never invents source claims.
- When a required section lacks data, it emits a clearly-marked placeholder.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re
from typing import Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
TODAY = date.today().isoformat()


def _split_frontmatter(text: str) -> Tuple[Optional[str], str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    frontmatter = parts[1].strip("\n")
    body = parts[2].lstrip("\n")
    return frontmatter, body


def _parse_frontmatter_scalar(frontmatter: str, key: str) -> Optional[str]:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", frontmatter, flags=re.M)
    if not match:
        return None
    return match.group(1).strip()


def _frontmatter_has_key(frontmatter: str, key: str) -> bool:
    return re.search(rf"^{re.escape(key)}:\s*", frontmatter, flags=re.M) is not None


def _replace_frontmatter_line(frontmatter: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^{re.escape(key)}:\s*.*$", flags=re.M)
    if pattern.search(frontmatter):
        return pattern.sub(f"{key}: {value}", frontmatter, count=1)
    return frontmatter


def _insert_after_key(frontmatter: str, after_key: str, new_line: str) -> str:
    lines = frontmatter.splitlines()
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(after_key)}:\s*", line):
            lines.insert(i + 1, new_line)
            return "\n".join(lines)
    # fallback: append to end
    return frontmatter.rstrip() + "\n" + new_line


def _infer_feature_maturity(status: str) -> str:
    # Conservative defaults: canonical features are established; variants are emerging.
    if status == "canonical":
        return "established"
    if status in {"variant", "experimental"}:
        return "emerging" if status == "variant" else "research"
    if status == "deprecated":
        return "established"
    return "research"


def _infer_feature_bounded_context(slug: str, category: str, title: str) -> List[str]:
    slug_l = slug.lower()
    title_l = title.lower()

    if "clothing" in slug_l or "vestimenta" in slug_l or "garment" in title_l:
        return ["clothing-metaphor"]
    if "island" in slug_l:
        return ["island-metaphor"]
    if "landscape" in slug_l:
        return ["landscape-metaphor"]
    if slug_l == "city-metaphor" or ("city" in slug_l and category == "metaphor"):
        return ["city-metaphor"]

    if category == "mapping":
        # Concept-mapping features are typically metaphor-scoped; metric/property mappings are broadly reusable.
        if "-as-" in slug_l:
            return ["city-metaphor"]
        return ["universal"]

    if category == "layout":
        # Some layouts are metaphor-scoped (e.g., streets/platforms), but most are generally reusable.
        if any(token in slug_l for token in ("street", "platform", "district")):
            return ["city-metaphor"]
        return ["universal"]

    # interaction / analysis / platform / etc.
    return ["universal"]


@dataclass
class Section:
    heading: str
    content: str


def _parse_h2_sections(body: str) -> Tuple[str, List[Section]]:
    # Extract the H1 title (if any) and all H2 sections. Preserve section bodies verbatim.
    lines = body.splitlines()
    title = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            title = line[2:].strip()
            i += 1
            break
        if line.strip():
            break
        i += 1

    sections: List[Section] = []
    current_heading: Optional[str] = None
    current_lines: List[str] = []

    def flush() -> None:
        nonlocal current_heading, current_lines
        if current_heading is None:
            return
        content = "\n".join(current_lines).strip("\n")
        sections.append(Section(heading=current_heading, content=content))
        current_heading = None
        current_lines = []

    while i < len(lines):
        line = lines[i]
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            flush()
            current_heading = match.group(1).strip()
        else:
            current_lines.append(line)
        i += 1

    flush()
    return title, sections


def _coalesce_sections(sections: List[Section], predicate) -> List[Section]:
    return [s for s in sections if predicate(s.heading)]


def _join_sections(
    sections: List[Section],
    use_subheadings_when_multiple: bool = True,
    strip_heading_prefix: Optional[str] = None,
) -> str:
    if not sections:
        return ""
    if len(sections) == 1 and not use_subheadings_when_multiple:
        return sections[0].content.strip()
    parts: List[str] = []
    for sec in sections:
        heading = sec.heading
        if strip_heading_prefix and heading.startswith(strip_heading_prefix):
            heading = heading[len(strip_heading_prefix) :].strip()
        parts.append(f"### {heading}\n\n{sec.content.strip()}".strip())
    return "\n\n".join(parts).strip()


def _placeholder(text: str) -> str:
    return f"(TODO) {text}"


def _default_consequences(category: str) -> Tuple[List[Tuple[str, str]], str, str, str]:
    cat = category.lower()
    if cat == "mapping":
        return (
            [
                ("Adds an at-a-glance quantitative cue.", "Outliers can dominate perception without scaling/binning."),
                ("Supports quick comparison across many entities.", "Multiple encodings can increase visual clutter."),
            ],
            "Low",
            "Typically cheap; depends on recomputation frequency.",
            "Low–Medium (depends on legend/scale).",
        )
    if cat == "layout":
        return (
            [
                ("Makes large structures navigable via spatial organization.", "May hide non-hierarchical relationships."),
                ("Can improve stability/orientation if positions are consistent.", "Computing layout can be expensive at scale."),
            ],
            "Medium",
            "Layout computation can be a bottleneck for large graphs/hierarchies.",
            "Medium (users must learn layout semantics).",
        )
    if cat == "interaction":
        return (
            [
                ("Enables details-on-demand workflows.", "Adds UI/interaction complexity."),
                ("Reduces cognitive load by filtering/focusing.", "Can create mode errors if state is unclear."),
            ],
            "Medium",
            "Depends on picking/raycasting and UI update costs.",
            "Medium (requires learning controls and feedback).",
        )
    if cat == "analysis":
        return (
            [
                ("Surfaces quality/evolution signals in context.", "Overlays can overwhelm the base metaphor."),
                ("Supports prioritization (hotspots, anomalies).", "Signals may be noisy or metric-dependent."),
            ],
            "Medium",
            "Depends on analysis pipeline and refresh cadence.",
            "Medium–High (interpretation requires metric literacy).",
        )
    if cat == "platform":
        return (
            [
                ("Expands interaction bandwidth (e.g., immersion).", "Hardware/software requirements reduce accessibility."),
                ("Can improve engagement and spatial understanding.", "Comfort/safety and performance constraints apply."),
            ],
            "High",
            "Rendering and input constraints can be significant (VR/AR).",
            "Medium–High (new interaction paradigms).",
        )
    # metaphor and default
    return (
        [
            ("Provides an intuitive mental model for structure.", "Metaphor can oversimplify or mislead."),
            ("Supports orientation via spatial cues.", "Different users may interpret metaphors differently."),
        ],
        "Medium",
        "Depends on rendering scale and navigation.",
        "Medium (requires mapping concepts to visuals).",
    )


def _render_consequences_section(category: str, minimal: bool) -> str:
    rows, complexity, performance, cognitive = _default_consequences(category)
    lines = [
        "| ✅ Benefits | ❌ Liabilities |",
        "|-------------|----------------|",
    ]
    for benefit, liability in rows:
        lines.append(f"| {benefit} | {liability} |")
    if minimal:
        return "\n".join(lines).strip()
    lines.extend(
        [
            "",
            f"**Complexity**: {complexity}",
            f"**Performance**: {performance}",
            f"**Cognitive Load**: {cognitive}",
        ]
    )
    return "\n".join(lines).strip()


def normalize_feature_card(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    frontmatter, body = _split_frontmatter(original)
    if frontmatter is None:
        return False

    title = _parse_frontmatter_scalar(frontmatter, "title") or path.stem
    status = _parse_frontmatter_scalar(frontmatter, "status") or "variant"
    category = _parse_frontmatter_scalar(frontmatter, "category") or "analysis"

    # Frontmatter updates
    if not _frontmatter_has_key(frontmatter, "maturity"):
        maturity = _infer_feature_maturity(status)
        frontmatter = _insert_after_key(frontmatter, "status", f"maturity: {maturity}")

    if not _frontmatter_has_key(frontmatter, "bounded_context"):
        bounded = _infer_feature_bounded_context(path.stem, category, title)
        bounded_value = "[" + ", ".join(bounded) + "]"
        # Prefer placing bounded_context after maturity if present.
        if _frontmatter_has_key(frontmatter, "maturity"):
            frontmatter = _insert_after_key(frontmatter, "maturity", f"bounded_context: {bounded_value}")
        else:
            frontmatter = _insert_after_key(frontmatter, "status", f"bounded_context: {bounded_value}")

    if not _frontmatter_has_key(frontmatter, "supersedes"):
        frontmatter = _insert_after_key(frontmatter, "related_features", "supersedes: []")

    frontmatter = _replace_frontmatter_line(frontmatter, "last_updated", TODAY)

    # Body updates
    _old_title, sections = _parse_h2_sections(body)

    def startswith(name: str):
        return lambda h: h == name or h.startswith(name + " ")

    problem_sections = _coalesce_sections(sections, lambda h: h in {"Problem & Motivation", "Rationale", "Motivation"})
    definition_sections = _coalesce_sections(sections, startswith("Definition"))
    context_sections = _coalesce_sections(sections, lambda h: h == "Context & Applicability")
    forces_sections = _coalesce_sections(sections, lambda h: h == "Forces")
    mechanism_sections = _coalesce_sections(sections, startswith("Mechanism"))
    consequences_sections = _coalesce_sections(sections, lambda h: h == "Consequences & Trade-offs")
    variation_sections = _coalesce_sections(sections, startswith("Variations"))
    evidence_sections = _coalesce_sections(sections, startswith("Evidence"))
    notes_sections = _coalesce_sections(sections, lambda h: h.startswith("Notes") or h == "Implementation Notes")
    limitation_sections = _coalesce_sections(sections, lambda h: h in {"Limitations", "Known Limitations"})
    sources_sections = _coalesce_sections(sections, lambda h: h == "Sources")
    see_also_sections = _coalesce_sections(sections, lambda h: h == "See Also")

    used = {
        id(s)
        for group in (
            problem_sections,
            definition_sections,
            context_sections,
            forces_sections,
            mechanism_sections,
            consequences_sections,
            variation_sections,
            evidence_sections,
            notes_sections,
            limitation_sections,
            sources_sections,
            see_also_sections,
        )
        for s in group
    }
    leftover_sections = [s for s in sections if id(s) not in used and s.content.strip()]

    is_canonical = status == "canonical"
    minimal = not is_canonical

    problem_text = _join_sections(problem_sections, use_subheadings_when_multiple=False).strip()
    if not problem_text:
        problem_text = _placeholder("Motivation not explicitly captured yet.")

    definition_text = _join_sections(definition_sections, use_subheadings_when_multiple=False).strip()
    if not definition_text:
        definition_text = _placeholder("Definition not explicitly captured yet.")

    context_text = _join_sections(context_sections, use_subheadings_when_multiple=False).strip()
    forces_text = _join_sections(forces_sections, use_subheadings_when_multiple=False).strip()

    mechanism_text = _join_sections(mechanism_sections, use_subheadings_when_multiple=(len(mechanism_sections) > 1)).strip()
    if not mechanism_text:
        mechanism_text = _placeholder("Mechanism not explicitly captured yet.")

    consequences_text = _join_sections(consequences_sections, use_subheadings_when_multiple=False).strip()
    variations_text = _join_sections(variation_sections, use_subheadings_when_multiple=(len(variation_sections) > 1)).strip()
    evidence_text = _join_sections(evidence_sections, use_subheadings_when_multiple=(len(evidence_sections) > 1)).strip()

    implementation_notes_parts: List[str] = []
    notes_text = _join_sections(notes_sections, use_subheadings_when_multiple=(len(notes_sections) > 1)).strip()
    if notes_text:
        implementation_notes_parts.append(notes_text)
    if leftover_sections:
        for sec in leftover_sections:
            implementation_notes_parts.append(f"### {sec.heading}\n\n{sec.content.strip()}".strip())
    implementation_notes_text = "\n\n".join(implementation_notes_parts).strip()
    if is_canonical and not implementation_notes_text:
        implementation_notes_text = _placeholder("Implementation guidance not captured yet.")

    limitations_text = _join_sections(limitation_sections, use_subheadings_when_multiple=False).strip()
    if is_canonical and not limitations_text:
        limitations_text = _placeholder("Known limitations not explicitly captured yet.")

    sources_text = _join_sections(sources_sections, use_subheadings_when_multiple=False).strip()
    see_also_text = _join_sections(see_also_sections, use_subheadings_when_multiple=False).strip()

    # Normalize a few known broken wiki links (feature-ID links).
    def normalize_feature_id_links(text: str) -> str:
        # Handle "ID + slug" patterns first to avoid duplicate link text after replacement.
        text = re.sub(r"\[\[F072\]\]\s+clothing-metaphor\b", "[[clothing-metaphor]]", text)
        text = re.sub(r"\[\[F073\]\]\s+class-as-clothing-item\b", "[[class-as-clothing-item]]", text)
        text = re.sub(r"\[\[F074\]\]\s+clothing-attribute-mapping\b", "[[clothing-attribute-mapping]]", text)
        text = re.sub(r"\[\[F001\]\]\s+city-metaphor\b", "[[city-metaphor]]", text)
        text = re.sub(r"\[\[city-metaphor\]\]\s+city-metaphor\b", "[[city-metaphor]]", text)

        # Then replace any remaining bare IDs.
        replacements = {
            "[[F072]]": "[[clothing-metaphor]]",
            "[[F073]]": "[[class-as-clothing-item]]",
            "[[F074]]": "[[clothing-attribute-mapping]]",
            "[[F001]]": "[[city-metaphor]]",
        }
        for a, b in replacements.items():
            text = text.replace(a, b)
        return text

    def normalize_text_block(text: str) -> str:
        return normalize_feature_id_links(text).strip()

    problem_text = normalize_text_block(problem_text)
    definition_text = normalize_text_block(definition_text)
    mechanism_text = normalize_text_block(mechanism_text)
    context_text = normalize_text_block(context_text)
    forces_text = normalize_text_block(forces_text)
    consequences_text = normalize_text_block(consequences_text)
    variations_text = normalize_text_block(variations_text)
    evidence_text = normalize_text_block(evidence_text)
    implementation_notes_text = normalize_text_block(implementation_notes_text)
    limitations_text = normalize_text_block(limitations_text)
    sources_text = normalize_text_block(sources_text)
    see_also_text = normalize_text_block(see_also_text)

    out_lines: List[str] = []
    out_lines.append("---")
    out_lines.append(frontmatter.strip())
    out_lines.append("---")
    out_lines.append("")
    out_lines.append(f"# {title}")
    out_lines.append("")

    out_lines.append("## Problem & Motivation")
    out_lines.append("")
    out_lines.append(problem_text)
    out_lines.append("")

    out_lines.append("## Definition")
    out_lines.append("")
    out_lines.append(definition_text)
    out_lines.append("")

    if is_canonical:
        out_lines.append("## Context & Applicability")
        out_lines.append("")
        if context_text:
            out_lines.append(context_text)
        else:
            out_lines.append("**Use when:**")
            out_lines.append("- (TODO) Add specific guidance from processed sources.")
            out_lines.append("")
            out_lines.append("**Avoid when:**")
            out_lines.append("- (TODO) Add specific guidance from processed sources.")
            out_lines.append("")
            out_lines.append("**Prerequisites:** (TODO)")
            out_lines.append("**Alternatives:** (TODO)")
        out_lines.append("")

        out_lines.append("## Forces")
        out_lines.append("")
        if forces_text:
            out_lines.append(forces_text)
        else:
            out_lines.append("| Force | Pull |")
            out_lines.append("|-------|------|")
            out_lines.append("| Scalability | Favor simple, compressive representations at large scale. |")
            out_lines.append("| Fidelity | Favor detailed representations that preserve nuance. |")
        out_lines.append("")

    out_lines.append("## Mechanism (Solution)")
    out_lines.append("")
    out_lines.append(mechanism_text)
    out_lines.append("")

    out_lines.append("## Consequences & Trade-offs")
    out_lines.append("")
    out_lines.append(consequences_text or _render_consequences_section(category, minimal=minimal))
    out_lines.append("")

    if variations_text:
        out_lines.append("## Variations")
        out_lines.append("")
        out_lines.append(variations_text)
        out_lines.append("")

    if implementation_notes_text:
        out_lines.append("## Implementation Notes")
        out_lines.append("")
        out_lines.append(implementation_notes_text)
        out_lines.append("")

    if evidence_text:
        out_lines.append("## Evidence")
        out_lines.append("")
        out_lines.append(evidence_text)
        out_lines.append("")

    if limitations_text:
        out_lines.append("## Known Limitations")
        out_lines.append("")
        out_lines.append(limitations_text)
        out_lines.append("")

    out_lines.append("## Sources")
    out_lines.append("")
    out_lines.append(sources_text or _placeholder("Add sources."))
    out_lines.append("")

    if see_also_text:
        out_lines.append("## See Also")
        out_lines.append("")
        out_lines.append(see_also_text)
        out_lines.append("")

    normalized = "\n".join(out_lines).rstrip() + "\n"
    if normalized == original:
        return False
    path.write_text(normalized, encoding="utf-8")
    return True


def _infer_glossary_bounded_context(term: str, category: str) -> str:
    t = term.lower().strip()
    c = category.lower().strip()

    if "clothing" in t or "wardrobe" in t or "garment" in t:
        return "clothing-metaphor"
    if "island" in t or "archipelago" in t:
        return "island-metaphor"
    if "landscape" in t or "terrain" in t:
        return "landscape-metaphor"

    if c == "metaphor":
        city_specific = {
            "city metaphor",
            "code city",
            "software city",
            "building",
            "district",
            "street",
            "brick",
            "platform",
            "block",
            "neighborhood",
            "quarter",
            "skyline",
        }
        if t in city_specific:
            return "city-metaphor"
        return "universal"

    return "universal"


def normalize_glossary(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()

    out: List[str] = []
    i = 0
    changed = False

    while i < len(lines):
        line = lines[i]
        out.append(line)

        if line.startswith("### "):
            term = line[4:].strip()
            # Scan forward within this entry to find Category and whether Bounded Context already exists.
            j = i + 1
            category_line_idx: Optional[int] = None
            category_value: Optional[str] = None
            has_context = False
            while j < len(lines) and not lines[j].startswith("### "):
                if lines[j].startswith("**Bounded Context**:"):
                    has_context = True
                    break
                if lines[j].startswith("**Category**:"):
                    category_line_idx = j
                    category_value = lines[j].split(":", 1)[1].strip()
                j += 1

            if not has_context and category_line_idx is not None and category_value is not None:
                context = _infer_glossary_bounded_context(term, category_value)
                # Insert immediately after Category line.
                insertion = f"**Bounded Context**: {context}"
                # We already copied current line (the term header) into out; now copy entry lines with insertion.
                k = i + 1
                while k < j:
                    out.append(lines[k])
                    if k == category_line_idx:
                        out.append("")
                        out.append(insertion)
                        changed = True
                    k += 1
                i = j
                continue

        i += 1

    normalized = "\n".join(out).rstrip() + "\n"
    if normalized != original:
        path.write_text(normalized, encoding="utf-8")
        return True
    return changed


def main() -> int:
    changed_any = False

    for feature in sorted((ROOT / "docs/features").glob("*.md")):
        if feature.name == "_index.md":
            continue
        changed_any |= normalize_feature_card(feature)

    glossary = ROOT / "docs/glossary.md"
    if glossary.exists():
        changed_any |= normalize_glossary(glossary)

    if changed_any:
        print("Updated docs.")
    else:
        print("No changes needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
