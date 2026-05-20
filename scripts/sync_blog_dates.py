#!/usr/bin/env python3
"""Sync publication dates from data/blog-posts.json across content, index, and built blogs."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

from lib.blog_dates import build_published_map, time_element  # noqa: E402
from lib.paths import BLOG_POSTS_JSON, BLOGS_OUT, CONTENT_BLOGS  # noqa: E402

INDEX = ROOT / "index.html"
TIME_RE = re.compile(r'<time datetime="[^"]+">[^<]*</time>')
CARD_HREF_RE = re.compile(
    r'(<article[^>]*class="[^"]*blog-index-card[^"]*"[^>]*>)'
    r"([\s\S]*?)"
    r'href="blogs/([^"]+)"',
    re.IGNORECASE,
)


def load_registry() -> dict:
    return json.loads(BLOG_POSTS_JSON.read_text(encoding="utf-8"))


def dedupe_posts(posts: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for post in posts:
        slug = post["slug"]
        if slug in seen:
            continue
        seen.add(slug)
        out.append(post)
    return out


def sync_registry_dates(posts: list[dict], published_map: dict[str, str]) -> list[dict]:
    for post in posts:
        post["published"] = published_map[post["slug"]]
        post.pop("updated", None)
    return posts


def replace_time_tags(html: str, iso: str) -> str:
    return TIME_RE.sub(time_element(iso), html)


def article_meta_line(post: dict) -> str:
    return time_element(post["published"])


def patch_content_file(post: dict) -> bool:
    path = CONTENT_BLOGS / post["content_file"]
    if not path.exists():
        print(f"  SKIP missing content: {path.name}")
        return False
    text = path.read_text(encoding="utf-8")
    new = replace_time_tags(text, post["published"])
    new = re.sub(r'\s*·\s*<span class="blog-meta-updated">[^<]*</span>', "", new)
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def patch_index_card(article_open: str, body: str, filename: str, post: dict) -> str:
    pub = post["published"]
    meta = article_meta_line(post)
    body = re.sub(r'\s*·\s*<span class="blog-meta-updated">[^<]*</span>', "", body)
    new_body, count = TIME_RE.subn(meta, body, count=1)
    if count == 0:
        return article_open + body + f'href="blogs/{filename}"'

    if 'data-published="' not in article_open:
        article_open = article_open.replace(
            "<article ",
            f'<article data-published="{pub}" ',
            1,
        )
    else:
        article_open = re.sub(
            r'data-published="[^"]*"',
            f'data-published="{pub}"',
            article_open,
            count=1,
        )
    return article_open + new_body + f'href="blogs/{filename}"'


def patch_index(index_html: str, posts_by_file: dict[str, dict]) -> str:
    def repl(match: re.Match[str]) -> str:
        filename = match.group(3)
        post = posts_by_file.get(filename)
        if not post:
            return match.group(0)
        return patch_index_card(match.group(1), match.group(2), filename, post)

    return CARD_HREF_RE.sub(repl, index_html)


def ensure_index_toolbar(html: str) -> str:
    toolbar = """        <div class="blog-index-toolbar d-flex flex-wrap align-items-center justify-content-center gap-2 mb-4" role="group" aria-label="Sort blog cards">
          <span class="text-muted small mb-0"><i class="bi bi-sort-down" aria-hidden="true"></i> Sort</span>
          <button type="button" class="btn btn-sm btn-outline-secondary active" data-blog-sort="newest" aria-pressed="true">Newest first</button>
          <button type="button" class="btn btn-sm btn-outline-secondary" data-blog-sort="oldest" aria-pressed="false">Oldest first</button>
        </div>
"""
    if "blog-index-toolbar" in html:
        return html
    marker = '        <h3 class="h5 text-center mb-3 mt-2">AWS — certification'
    if marker not in html:
        return html
    return html.replace(marker, toolbar + "\n" + marker, 1)


def main() -> None:
    data = load_registry()
    posts = dedupe_posts(data["posts"])
    slugs = [p["slug"] for p in posts]
    published_map = build_published_map(slugs)
    posts = sync_registry_dates(posts, published_map)
    data["posts"] = posts
    BLOG_POSTS_JSON.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    posts_by_file = {p["file"]: p for p in posts}
    content_changed = 0
    for post in posts:
        if patch_content_file(post):
            content_changed += 1

    index_html = INDEX.read_text(encoding="utf-8")
    index_html = ensure_index_toolbar(index_html)
    index_html = patch_index(index_html, posts_by_file)
    INDEX.write_text(index_html, encoding="utf-8")

    subprocess.run([sys.executable, str(SCRIPTS / "build_site.py")], check=True, cwd=ROOT)

    print(f"Registry: {len(posts)} posts with published dates")
    print(f"Content files updated: {content_changed}")
    print(f"Date range: {min(published_map.values())} → {max(published_map.values())}")


if __name__ == "__main__":
    main()
