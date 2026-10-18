# -*- coding: utf-8 -*-
"""Genera sitemap.xml y robots.txt con URLs limpias (sin .html) y la fecha de hoy como lastmod."""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import co as C

TODAY = datetime.date.today().isoformat()
PAGES = [("", "1.0"), ("nasfeco", "0.8"),
         ("product-x12", "0.8"), ("product-g5p700a", "0.8"), ("product-g2p600", "0.8"), ("product-uf", "0.8"), ("product-smart", "0.8")] + \
        [(f"purificadores-agua-{slug}", "0.9") for slug, _, _ in C.CITIES] + [("politica-cookies", "0.3")]

for path, _ in PAGES:   # no publicar en el sitemap una página que no existe
    assert os.path.exists(os.path.join(C.ROOT, (path or "index") + ".html")), path

urls = "\n".join(f"  <url><loc>{C.SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>" for p, pr in PAGES)
open(os.path.join(C.ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
open(os.path.join(C.ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n").write(
    f"User-agent: *\nAllow: /\n\nSitemap: {C.SITE}sitemap.xml\n")
print("ok sitemap.xml", len(PAGES), "URLs · robots.txt")
