"""Simple {{PLACEHOLDER}} template rendering."""

from pathlib import Path


def render_template(template_path: Path, **values: str) -> str:
    text = template_path.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text


def _indent_block(html: str, spaces: int = 4) -> str:
    """Align article block with layout (only the root tag needs extra indent)."""
    lines = html.strip().splitlines()
    if not lines:
        return ""
    pad = " " * spaces
    if lines[0] and not lines[0].startswith(" "):
        lines[0] = pad + lines[0]
    return "\n".join(lines)


def render_blog_page(layout_path: Path, article_html: str, meta: dict) -> str:
    return render_template(
        layout_path,
        PAGE_TITLE=meta["title"],
        META_DESCRIPTION=meta["description"],
        META_KEYWORDS=meta.get("keywords", "Babulal Tamang"),
        BREADCRUMB=meta["breadcrumb"],
        ARTICLE=_indent_block(article_html.strip()),
    )
