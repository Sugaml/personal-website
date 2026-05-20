# babulal.com.np — personal website

Static portfolio and blog site (HTML, CSS, Bootstrap). Deployed via GitHub Pages; optional Docker/nginx for local preview.

## Project structure

```
├── index.html              # Home page (sections: about, skills, blog, contact, …)
├── portfolio-details.html  # Portfolio detail template page
├── assets/                 # CSS, JS, images, vendor libraries
├── blogs/                  # Built blog pages (deployed URLs — run `make build`)
├── content/blogs/          # Article HTML only (edit posts here)
├── data/
│   └── blog-posts.json     # Per-post title, description, breadcrumb, keywords
├── templates/blog/
│   └── layout.html         # Shared chrome (header, nav, footer, scripts)
└── scripts/
    ├── build_site.py       # Assemble blogs/ from content + template + data
    ├── extract_blog_content.py
    ├── gen-*.py            # Series generators (Kubernetes hands-on, FinOps/GreenOps)
    └── lib/                # Shared paths, render, registry helpers
```

## Workflow

**Edit a blog post**

1. Change the article in `content/blogs/<slug>.html`.
2. Update metadata in `data/blog-posts.json` if title, description, or breadcrumb changed.
3. Run `make build` to regenerate `blogs/*.html`.

**Add a new post**

1. Add `content/blogs/my-new-post.html` (wrap body in `<article class="inner-page blog-article pb-5">…</article>`).
2. Add an entry to `data/blog-posts.json`.
3. Add a card on `index.html` under the right blog section.
4. Run `make build`.

**Generate series posts**

```bash
python3 scripts/gen-kubernetes-hands-on-blogs.py
python3 scripts/gen-finops-greenops-blogs.py
```

Each generator updates `content/` + `data/blog-posts.json` and runs the site build.

## Commands

| Command | Description |
|---------|-------------|
| `make build` | Build all blog pages |
| `make extract` | Re-split `blogs/` into `content/` + `data/` (migration) |
| `make serve` | Local server at http://localhost:8080 |
| `make docker-build` | Build nginx image |
| `make docker-run` | Run container on port 80 |

## Design notes

See `DEVELOPMENT-NOTES.md` for content changelog and `Readme.txt` for hero/theme notes.
