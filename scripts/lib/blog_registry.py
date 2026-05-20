"""Read/write blog post registry and publish content."""

from __future__ import annotations

import json
from pathlib import Path

from .paths import BLOG_POSTS_JSON, CONTENT_BLOGS


def load_registry() -> dict:
    if BLOG_POSTS_JSON.exists():
        return json.loads(BLOG_POSTS_JSON.read_text(encoding="utf-8"))
    return {"posts": []}


def save_registry(data: dict) -> None:
    BLOG_POSTS_JSON.parent.mkdir(parents=True, exist_ok=True)
    BLOG_POSTS_JSON.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def upsert_post(meta: dict, article_html: str) -> None:
    """Write article content and update registry metadata."""
    CONTENT_BLOGS.mkdir(parents=True, exist_ok=True)
    content_path = CONTENT_BLOGS / meta["file"]
    content_path.write_text(article_html.strip() + "\n", encoding="utf-8")

    data = load_registry()
    posts = data.get("posts", [])
    slug = Path(meta["file"]).stem
    entry = {
        "slug": slug,
        "file": meta["file"],
        "title": meta["title_page"],
        "description": meta["meta"],
        "keywords": meta.get("keywords", "Babulal Tamang"),
        "breadcrumb": meta["crumb"],
        "content_file": meta["file"],
    }
    posts = [p for p in posts if p.get("file") != meta["file"]]
    posts.append(entry)
    data["posts"] = sorted(posts, key=lambda p: p["file"])
    save_registry(data)
