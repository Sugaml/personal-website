#!/usr/bin/env python3
"""Generate interview aptitude blog HTML (expandable question bank)."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from interview_aptitude_question_bank import all_questions  # noqa: E402

CONTENT_OUT = Path(__file__).resolve().parents[1] / "content" / "blogs" / "interview-aptitude-logical-questions.html"
PUBLISHED = "2026-05-20"


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "section"


def collect_flat() -> list[tuple[str, dict]]:
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


def render_options(options: dict[str, str]) -> str:
    lines = ['<ul class="aptitude-options list-unstyled mb-3">']
    for key in sorted(options):
        lines.append(
            f'<li class="mb-1"><strong>{html.escape(key)})</strong> {html.escape(options[key])}</li>'
        )
    lines.append("</ul>")
    return "\n".join(lines)


def render_accordion_item(qnum: int, category_slug: str, item: dict) -> str:
    aid = f"q-{category_slug}-{qnum}"
    ans = item["answer"]
    ans_label = ", ".join(ans) if isinstance(ans, list) else ans
    stem = html.escape(item["stem"])
    why = html.escape(item["why"])
    options_html = render_options(item["options"])

    return f"""<div class="accordion-item aptitude-question">
  <h3 class="accordion-header" id="heading-{aid}">
    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
      data-bs-target="#collapse-{aid}" aria-expanded="false" aria-controls="collapse-{aid}">
      <span class="aptitude-qnum me-2 text-muted">Q{qnum}</span>
      <span class="aptitude-stem">{stem}</span>
    </button>
  </h3>
  <div id="collapse-{aid}" class="accordion-collapse collapse" aria-labelledby="heading-{aid}"
    data-bs-parent="#accordion-{category_slug}">
    <div class="accordion-body">
      {options_html}
      <p class="mb-2"><strong>Answer:</strong> <span class="text-success fw-semibold">{html.escape(ans_label)}</span></p>
      <p class="mb-0 small"><strong>Explanation:</strong> {why}</p>
    </div>
  </div>
</div>"""


def render_sections(flat: list[tuple[str, dict]]) -> tuple[str, int]:
    parts: list[str] = []
    current_cat = ""
    category_slug = ""
    qnum = 0
    section_items: list[str] = []

    def flush_section() -> None:
        nonlocal section_items, category_slug, current_cat
        if not section_items:
            return
        parts.append(
            f'<h2 class="h4 mt-5 aptitude-category" id="cat-{category_slug}">{html.escape(current_cat)}</h2>'
        )
        parts.append(
            f'<div class="accordion aptitude-accordion mb-4" id="accordion-{category_slug}">'
        )
        parts.extend(section_items)
        parts.append("</div>")
        section_items = []

    for category, item in flat:
        if category != current_cat:
            flush_section()
            current_cat = category
            category_slug = slugify(category)
        qnum += 1
        section_items.append(render_accordion_item(qnum, category_slug, item))

    flush_section()
    return "\n".join(parts), qnum


def render_article(flat: list[tuple[str, dict]]) -> str:
    sections_html, total = render_sections(flat)
  # fix render_accordion - still has motion typo
    sections_html = sections_html.replace("<div ", "<div ").replace("</div>", "</div>")
    sections_html = sections_html.replace("<div ", "<div ").replace("</div>", "</div>")

    return f"""<article class="inner-page blog-article pb-5 aptitude-bank">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-10 col-xl-9">
            <header class="mb-4 pb-3 border-bottom" data-aos="fade-up">
              <div class="blog-article-meta mb-3">
                <p class="text-muted small mb-2">Interview prep · <time datetime="{PUBLISHED}">20 May 2026</time> · <span class="blog-meta-label">Practice bank</span> · By <a href="../index.html#about" class="blog-author text-reset fw-semibold" rel="author">Babulal Tamang</a></p>
              <ul class="blog-tags list-unstyled d-flex flex-wrap gap-1 mb-0" aria-label="Tags">
                <li><span class="badge rounded-pill text-bg-light border text-muted">Aptitude</span></li>
                <li><span class="badge rounded-pill text-bg-light border text-muted">Logical reasoning</span></li>
                <li><span class="badge rounded-pill text-bg-light border text-muted">Interview</span></li>
              </ul>
              </div>
              <h1 class="h2 mb-3">Interview Aptitude: Logical Reasoning Question Bank</h1>
              <p class="lead mb-3">{total} multiple-choice questions for technical interview aptitude rounds. Tap a question to expand options and reveal the answer.</p>
              <div class="border-start border-primary border-4 ps-3 py-3 bg-light rounded mb-3" role="note">
                <p class="small text-uppercase text-muted mb-1 fw-semibold">How to use</p>
                <p class="mb-0">Try each question under time pressure (about 60–90 seconds), then expand to check your work.</p>
              </div>
              <div class="d-flex flex-wrap gap-2 aptitude-toolbar mb-0">
                <button type="button" class="btn btn-sm btn-outline-primary" id="aptitude-expand-all">Expand all</button>
                <button type="button" class="btn btn-sm btn-outline-secondary" id="aptitude-collapse-all">Collapse all</button>
              </div>
            </header>

            <div class="blog-prose aptitude-prose" data-aos="fade-up" data-aos-delay="50">

{sections_html}

              <h2 class="h4 mt-5">Practice tips</h2>
              <ul>
                <li>Write difference tables for number series before looking at options.</li>
                <li>For syllogisms, sketch quick Venn diagrams.</li>
                <li>Aptitude screens complement—not replace—system design and coding depth.</li>
              </ul>
              <p class="small text-muted mt-4 mb-2"><a href="../index.html#blog">Blog index</a> · <a href="devops-professional-nature.html">DevOps professionalism</a></p>
            </div>
          </div>
        </div>
      </div>
      <script>
      (function () {{
        function setAll(open) {{
          document.querySelectorAll('.aptitude-accordion .accordion-collapse').forEach(function (el) {{
            var btn = document.querySelector('[data-bs-target="#' + el.id + '"]');
            var c = bootstrap.Collapse.getOrCreateInstance(el, {{ toggle: false }});
            open ? c.show() : c.hide();
            if (btn) {{
              btn.classList.toggle('collapsed', !open);
              btn.setAttribute('aria-expanded', open ? 'true' : 'false');
            }}
          }});
        }}
        document.getElementById('aptitude-expand-all')?.addEventListener('click', function () {{ setAll(true); }});
        document.getElementById('aptitude-collapse-all')?.addEventListener('click', function () {{ setAll(false); }});
      }})();
      </script>
    </article>"""


def main() -> None:
    flat = collect_flat()
    CONTENT_OUT.parent.mkdir(parents=True, exist_ok=True)
    CONTENT_OUT.write_text(render_article(flat), encoding="utf-8")
    print(f"Wrote {len(flat)} questions → {CONTENT_OUT}")


if __name__ == "__main__":
    main()
