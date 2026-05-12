babulal.com.np

Design notes:
- Hero (theme v2): Decorative floating skill/tool labels live in .hero-skills-bg (aria-hidden). CSS drift animation with per-tag custom properties; prefers-reduced-motion disables motion. On narrow viewports, labels after the 25th child are hidden to reduce clutter.