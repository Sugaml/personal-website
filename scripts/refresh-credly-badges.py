#!/usr/bin/env python3
"""Write assets/data/credly-badges.json from Credly public badges API (run from repo root)."""
import json
import sys
import urllib.request

PROFILE = "https://www.credly.com/users/babulal-tamang/badges"
API = "https://www.credly.com/users/babulal-tamang/badges.json"
OUT = "assets/data/credly-badges.json"


def main():
    req = urllib.request.Request(API, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = json.load(resp)

    out = []
    for b in raw.get("data", []):
        t = b.get("badge_template") or {}
        issuer = ""
        ents = (b.get("issuer") or {}).get("entities") or []
        if ents and ents[0].get("entity"):
            issuer = ents[0]["entity"].get("name") or ""
        desc = (t.get("description") or "").strip()
        if len(desc) > 240:
            desc = desc[:237].rsplit(" ", 1)[0] + "…"
        bid = b.get("id")
        out.append(
            {
                "id": bid,
                "name": t.get("name") or "Badge",
                "imageUrl": b.get("image_url") or t.get("image_url"),
                "issued": b.get("issued_at_date"),
                "issuer": issuer,
                "description": desc,
                "assertionUrl": f"https://www.credly.com/badges/{bid}",
            }
        )

    payload = {"profileUrl": PROFILE, "badges": out}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")
    print(f"Wrote {len(out)} badges to {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
