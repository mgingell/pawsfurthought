"""Builds the Paws Fur Thought website from src/ into site/.

    python build.py          build once
    python build.py --watch  rebuild whenever something in src/ changes

Only the Python standard library is used. Upload the contents of site/ to any static host.
"""
import datetime
import html
import json
import os
import re
import shutil
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "site")

# Menu order. The slug is the page file name in src/pages/ (without .html).
NAV = [("index", "Home"), ("apply", "Apply"), ("faq", "FAQ"), ("resources", "Resources"),
       ("gallery", "Gallery"), ("contact", "Contact Us"), ("donate", "Donate")]

# Old WordPress addresses -> new pages, so existing links and bookmarks keep working
REDIRECTS = {
    "/application-process/in-take/": "/apply/",
    "/application-process/": "/apply/",
    "/about/": "/",
    "/who-we-are/": "/",
    "/home-2/": "/",
}


def read(*parts):
    with open(os.path.join(*parts), encoding="utf-8") as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def href(slug):
    return "/" if slug == "index" else f"/{slug}/"


def nav_html(current):
    items = []
    for slug, label in NAV:
        cur = ' aria-current="page"' if slug == current else ""
        cls = ' class="donate"' if slug == "donate" else ""
        items.append(f'\t\t\t\t<li{cls}><a href="{href(slug)}"{cur}>{label}</a></li>')
    return "\n".join(items)


def gallery_html():
    photos = json.loads(read(SRC, "gallery.json"))
    if not photos:
        return '\t\t\t\t<p class="gallery-empty">New photos are on the way. Please check back soon.</p>'
    missing = [p["file"] for p in photos if not p.get("alt") or p["alt"] == "DESCRIBE THIS PHOTO"]
    if missing:
        print(f"  WARNING gallery.json: {len(missing)} photo(s) still need a description: {', '.join(missing)}")
    folder = os.path.join(SRC, "static", "img", "gallery")
    listed = {p["file"] for p in photos}
    unused = sorted(f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f not in listed)
    if unused:
        print(f"  NOTE: {len(unused)} photo(s) in img/gallery/ aren't in gallery.json (still uploaded, not shown)")
    tiles = []
    for photo in photos:
        f = photo["file"]
        full = f"/img/gallery/{f}"
        thumb = f"/img/gallery/thumbs/{f}" if os.path.exists(os.path.join(SRC, "static", "img", "gallery", "thumbs", f)) else full
        tiles.append(f'\t\t\t\t<button type="button" data-full="{full}"><img src="{thumb}" alt="{html.escape(photo["alt"])}" loading="lazy"></button>')
    return "\n".join(tiles)


def intake_parts(cfg):
    url, email = cfg["intake_form_url"], cfg["email"]
    if url:
        status = (f'<div class="callout"><p><strong>Applications are open.</strong> Start with our short online intake screening form. '
                  f'For questions about successor dogs or general inquiries, email <a href="mailto:{email}">{email}</a>.</p>'
                  f'<p><a class="btn" href="{html.escape(url)}" target="_blank" rel="noopener">Start the Intake Screening Form</a></p></div>')
        button = f'<a class="btn" href="{html.escape(url)}" target="_blank" rel="noopener">Start the Intake Screening Form</a>'
    else:
        status = (f'<div class="callout"><p><strong>Our online intake form will be available in late October 2026.</strong> Please check back soon. '
                  f'For questions about successor dogs or general inquiries, email <a href="mailto:{email}">{email}</a>.</p></div>')
        button = ('<span class="btn" aria-disabled="true">Start the Intake Form</span>'
                  '<span class="small">This button goes live when the intake form is ready.</span>')
    return status, button


def parse_page(text):
    m = re.match(r"\s*<!--(.*?)-->\s*", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).strip().splitlines():
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()
        text = text[m.end():]
    return meta, text


def build():
    cfg = json.loads(read(SRC, "site.json"))
    site_url = cfg["site_url"].rstrip("/")
    layout = read(SRC, "layout.html")
    intake_status, intake_button = intake_parts(cfg)

    # Empty site/ but keep the folder itself (the local web server is watching it)
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        p = os.path.join(OUT, name)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    shutil.copytree(os.path.join(SRC, "static"), OUT, dirs_exist_ok=True)

    values = {
        "email": cfg["email"],
        "site_url": site_url,
        "contact_form_endpoint": html.escape(cfg["contact_form_endpoint"]),
        # Lets the form post directly to the service if JavaScript is off
        "contact_form_action": f'action="{html.escape(cfg["contact_form_endpoint"])}" method="POST" ' if cfg["contact_form_endpoint"] else "",
        "intake_status": intake_status,
        "intake_button": intake_button,
        "year": str(datetime.date.today().year),
    }
    sitemap = []
    for file in sorted(os.listdir(os.path.join(SRC, "pages"))):
        slug = file[:-5]
        meta, body = parse_page(read(SRC, "pages", file))
        body = re.sub(r"\{\{partial:(\w+)\}\}", lambda m: read(SRC, "partials", m.group(1) + ".html").rstrip(), body)
        if "{{gallery}}" in body:
            body = body.replace("{{gallery}}", gallery_html())
        page = (layout.replace("{{content}}", body.rstrip())
                      .replace("{{nav}}", nav_html(slug))
                      .replace("{{title}}", html.escape(meta.get("title", "Paws Fur Thought")))
                      .replace("{{description}}", html.escape(meta.get("description", "")))
                      .replace("{{canonical}}", site_url + ("/404.html" if slug == "404" else href(slug))))
        for key, val in values.items():
            page = page.replace("{{" + key + "}}", val)
        leftover = set(re.findall(r"\{\{[^}]*\}\}", page))
        if leftover:
            print(f"  WARNING {file}: unfilled placeholders {sorted(leftover)}")
        out = os.path.join(OUT, "404.html" if slug == "404" else ("index.html" if slug == "index" else os.path.join(slug, "index.html")))
        write(out, page)
        if slug != "404":
            sitemap.append(site_url + href(slug))

    for old, new in REDIRECTS.items():
        write(os.path.join(OUT, old.strip("/"), "index.html"),
              f'<!doctype html><meta charset="utf-8"><title>Moved</title><link rel="canonical" href="{site_url}{new}">'
              f'<meta http-equiv="refresh" content="0; url={new}"><p>This page has moved to <a href="{new}">{site_url}{new}</a>.</p>\n')
    # Real 301 redirects on hosts that read a _redirects file (Netlify, Cloudflare Pages)
    write(os.path.join(OUT, "_redirects"), "".join(f"{old} {new} 301\n{old.rstrip('/')} {new} 301\n" for old, new in REDIRECTS.items()))

    write(os.path.join(OUT, "robots.txt"), f"User-agent: *\nAllow: /\nSitemap: {site_url}/sitemap.xml\n")
    write(os.path.join(OUT, "sitemap.xml"),
          '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{u}</loc></url>\n" for u in sitemap) + "</urlset>\n")
    print(f"Built {len(sitemap)} pages into site/ at {time.strftime('%H:%M:%S')}")


def snapshot():
    state = {}
    for folder, _, files in os.walk(SRC):
        for f in files:
            p = os.path.join(folder, f)
            state[p] = os.path.getmtime(p)
    return state


if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)
    build()
    if "--watch" in sys.argv:
        print("Watching src/ for changes (Ctrl+C to stop)...")
        last = snapshot()
        while True:
            time.sleep(1)
            now = snapshot()
            if now != last:
                last = now
                try:
                    build()
                except Exception as e:  # keep watching after a typo in a page or JSON file
                    print(f"  BUILD FAILED: {e}")
