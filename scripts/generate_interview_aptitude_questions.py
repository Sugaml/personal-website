#!/usr/bin/env python3
"""Generate interview aptitude / logical reasoning practice questions."""

from __future__ import annotations

from pathlib import Path

from interview_aptitude_question_bank import all_questions, q

OUTPUT = Path(__file__).resolve().parents[1] / "study" / "interview-aptitude-logical-questions.md"


def collect_flat() -> list[tuple[str, dict]]:
    """Return (category, question) pairs preserving section order."""
    flat: list[tuple[str, dict]] = []
    seen: set[str] = set()
    for category, items in all_questions().items():
        for item in items:
            key = item["stem"][:100]
            if key in seen:
                continue
            seen.add(key)
            flat.append((category, item))
    return flat


def render_markdown(flat: list[tuple[str, dict]]) -> str:
    lines = [
        "# Interview Aptitude: Logical Reasoning Question Bank",
        f"## Practice questions ({len(flat)} unique questions)",
        "",
        "> **Purpose:** Logical and quantitative aptitude items common in technical and graduate "
        "interview screens (online assessments, HR aptitude rounds, and problem-solving warm-ups). "
        "Each item includes a worked explanation.",
        "",
        "| Section | Focus |",
        "|---------|--------|",
        "| Number series | Patterns, primes, squares, alternating rules |",
        "| Letter and word patterns | Alphabets, codes, odd-one-out |",
        "| Analogies and classification | Verbal and technical analogies |",
        "| Syllogisms and deductive logic | Valid conclusions, fallacies |",
        "| Coding-decoding | Symbol substitution, binary/hex |",
        "| Blood relations | Family trees |",
        "| Direction and distance | Compass, Pythagoras |",
        "| Seating and ordering | Queues, schedules |",
        "| Puzzles and constraints | Boxes, weighings, ordering |",
        "| Data interpretation logic | Percentages, medians, charts |",
        "| Tech-flavored reasoning | SRE, capacity, availability trade-offs |",
        "",
        "---",
        "",
    ]

    current_category = ""
    qnum = 0
    for category, item in flat:
        if category != current_category:
            current_category = category
            lines.extend(["", f"## {category}", ""])
        qnum += 1
        lines.append(f"### Question {qnum}")
        lines.append("")
        lines.append(item["stem"])
        lines.append("")
        for key in sorted(item["options"]):
            lines.append(f"- **{key})** {item['options'][key]}")
        lines.append("")
        ans = item["answer"]
        if isinstance(ans, list):
            lines.append(f"**Correct answer(s):** {', '.join(ans)}")
        else:
            lines.append(f"**Correct answer:** {ans}")
        lines.append("")
        lines.append("**Explanation:**")
        lines.append("")
        lines.append(item["why"])
        lines.append("")
        correct = ans if isinstance(ans, list) else [ans]
        lines.append("**Why other options are wrong:**")
        for key in sorted(item["options"]):
            if key in correct:
                continue
            lines.append(
                f"- **{key})** {item['options'][key]} — Does not follow from the pattern or logic described above."
            )
        lines.append("")
        lines.append("---")

    lines.extend(
        [
            "",
            "## How to practice",
            "",
            "1. Time yourself: 45–90 seconds per question in assessment conditions.",
            "2. After each mistake, write the rule you missed (difference table, letter shift, etc.).",
            "3. For syllogisms, sketch Venn diagrams; for series, write differences on paper.",
            "4. Pair with system-design and coding prep—aptitude rounds rarely replace technical depth.",
            "",
            "*Unofficial practice material for interview preparation.*",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    flat = collect_flat()
    if len(flat) < 50:
        raise SystemExit(f"Expected 50+ unique questions, got {len(flat)}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render_markdown(flat), encoding="utf-8")
    print(f"Wrote {len(flat)} unique questions to {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
