#!/usr/bin/env python3
"""Build blog HTML pages from templates, metadata, and article content."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.paths import (  # noqa: E402
    BLOG_LAYOUT,
    BLOG_POSTS_JSON,
    BLOGS_OUT,
    CONTENT_BLOGS,
)
from lib.render import render_blog_page  # noqa: E402


def load_posts() -> list[dict]:
    if not BLOG_POSTS_JSON.exists():
        raise SystemExit(
            f"Missing {BLOG_POSTS_JSON}. Run: python3 scripts/extract_blog_content.py"
        )
    data = json.loads(BLOG_POSTS_JSON.read_text(encoding="utf-8"))
    return data["posts"]


def build_blogs() -> int:
    posts = load_posts()
    built = 0
    for post in posts:
        content_path = CONTENT_BLOGS / post["content_file"]
        if not content_path.exists():
            print(f"  SKIP missing content: {content_path.name}")
            continue
        article = content_path.read_text(encoding="utf-8")
        html = render_blog_page(BLOG_LAYOUT, article, post)
        out_path = BLOGS_OUT / post["file"]
        out_path.write_text(html, encoding="utf-8")
        built += 1
    return built


def main() -> None:
    BLOGS_OUT.mkdir(parents=True, exist_ok=True)
    count = build_blogs()
    print(f"Built {count} blog pages → {BLOGS_OUT.relative_to(BLOGS_OUT.parent)}/")


if __name__ == "__main__":
    main()
