#!/usr/bin/env python3
"""One-time migration: split blogs/*.html into content + metadata."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.paths import BLOG_POSTS_JSON, BLOGS_OUT, CONTENT_BLOGS, DATA  # noqa: E402


def parse_post(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    article = re.search(r"<article[^>]*>.*?</article>", text, re.S)
    if not article:
        print(f"  SKIP (no article): {path.name}")
        return None

    title_m = re.search(r"<title>(.*?)</title>", text, re.S)
    desc_m = re.search(r'<meta content="([^"]*)" name="description">', text)
    kw_m = re.search(r'<meta name="keywords" content="([^"]*)">', text)
    crumb_m = re.search(
        r'<li><a href="\.\./index\.html#blog">Blog</a></li>\s*<li>(.*?)</li>',
        text,
        re.S,
    )

    slug = path.stem
    return {
        "slug": slug,
        "file": path.name,
        "title": title_m.group(1).strip() if title_m else path.stem,
        "description": desc_m.group(1) if desc_m else "",
        "keywords": kw_m.group(1) if kw_m else "Babulal Tamang",
        "breadcrumb": crumb_m.group(1).strip() if crumb_m else slug,
        "content_file": path.name,
        "article": article.group(0),
    }


def main() -> None:
    CONTENT_BLOGS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)

    posts: list[dict] = []
    for path in sorted(BLOGS_OUT.glob("*.html")):
        parsed = parse_post(path)
        if not parsed:
            continue
        article = parsed.pop("article")
        (CONTENT_BLOGS / parsed["content_file"]).write_text(article, encoding="utf-8")
        posts.append(parsed)
        print(f"  OK {path.name}")

    payload = {"posts": posts}
    BLOG_POSTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {len(posts)} posts to {CONTENT_BLOGS.relative_to(DATA.parent.parent)}")
    print(f"Metadata: {BLOG_POSTS_JSON.relative_to(DATA.parent.parent)}")


if __name__ == "__main__":
    main()
