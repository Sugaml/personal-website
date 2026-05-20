"""Repository path constants."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
BLOGS_OUT = ROOT / "blogs"
CONTENT_BLOGS = ROOT / "content" / "blogs"
DATA = ROOT / "data"
BLOG_POSTS_JSON = DATA / "blog-posts.json"
BLOG_LAYOUT = ROOT / "templates" / "blog" / "layout.html"
SCRIPTS = ROOT / "scripts"
GENERATORS = SCRIPTS / "generators"
MAINTENANCE = SCRIPTS / "maintenance"
