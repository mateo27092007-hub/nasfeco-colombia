# -*- coding: utf-8 -*-
"""Datos de Nasfeco Colombia que usa el generador (_build/build_co.py).

WhatsApp, precios, códigos y fecha de la oferta NO se editan aquí: se leen del objeto WD al inicio de js/co.js,
que es el único lugar donde se cambian. Lo que está entre {{ }} es un dato pendiente de confirmar:
se ve tal cual en la web para que nadie lo publique sin revisar (busca "{{" en todo el proyecto)."""
import os, re
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = "4"
# Vista previa (GitHub Pages): los buscadores no indexan el borrador. Ponlo en False el día del lanzamiento.
PREVIEW = True                                   # súbelo cada vez que cambies css/co.css o js/co.js

# ------------------------------------------------------------------ EMPRESA
DOMAIN = "nasfeco.com.co"                  # {{confirmar dominio}}: canonical, sitemap y Open Graph
SITE = f"https://{DOMAIN}/"
COMPANY = "Nasfeco S.A.S."                 # {{confirmar razón social}}
NIT = "{{NIT}}"
EMAIL = "{{correo}}"
ADDRESS = "{{dirección de la sede}}"
WA_SHOW = "{{+57 3XX XXX XXXX}}"           # teléfono tal como se muestra en la web

# Mientras no esté confirmada la exclusividad, NO se dice "exclusivo" en ningún lado.
# Si Waterdrop lo confirma por escrito, cambia a "distribuidor exclusivo oficial".
DIST = "distribuidor oficial"
DIST_C = DIST[0].upper() + DIST[1:]

# ------------------------------------------------------------------ CIUDADES CON INSTALACIÓN
HQ_CITY, HQ_REGION = "Bogotá", "Bogotá D.C."
CITIES = [("bogota", "Bogotá", "Bogotá D.C."), ("medellin", "Medellín", "Antioquia"),
          ("cali", "Cali", "Valle del Cauca"), ("barranquilla", "Barranquilla", "Atlántico")]
CITY_NAMES = [c[1] for c in CITIES]
CITY_LIST = ", ".join(CITY_NAMES[:-1]) + " y " + CITY_NAMES[-1]
PRIVACY_URL = "politica-cookies#datos-personales"

# ------------------------------------------------------------------ hreflang (Ecuador ↔ Colombia)
# Solo tiene efecto si la web de Ecuador también enlaza de vuelta a estas páginas con es-CO.
HREFLANG_ON = True
EC_SITE = "https://nasfeco.com/"
HREFLANG = {"": "", "nasfeco": "nasfeco", "product-x12": "product-x12", "product-g5p700a": "product-g5p700a",
            "product-g2p600": "product-g2p600", "product-uf": "product-uf", "product-smart": "product-smart", "politica-cookies": "politica-cookies"}

def hreflang(path):
    if not HREFLANG_ON or path not in HREFLANG:
        return ""
    return (f'<link rel="alternate" hreflang="es-CO" href="{SITE}{path}"><link rel="alternate" hreflang="es-EC" href="{EC_SITE}{HREFLANG[path]}">'
            f'<link rel="alternate" hreflang="x-default" href="{EC_SITE}{HREFLANG[path]}">')

# ------------------------------------------------------------------ DATOS DE js/co.js
def _load_wd():
    js = open(os.path.join(ROOT, "js", "co.js"), encoding="utf-8").read()
    wd = {"whatsapp": re.search(r"whatsapp:\s*'([^']+)'", js).group(1),
          "promo_end": re.search(r"end:\s*'([^']+)'", js).group(1), "products": {}}
    for m in re.finditer(r"^\s*'?([\w-]+)'?:\s*\{\s*name:\s*'([^']*)',\s*price:\s*([\d.]+),\s*was:\s*([\d.]+)(?:,\s*code:\s*'([^']*)')?", js, re.M):
        wd["products"][m.group(1)] = {"name": m.group(2), "price": float(m.group(3)), "was": float(m.group(4)), "code": m.group(5)}
    return wd

WD = _load_wd()
WA_NUM = WD["whatsapp"]
PROMO_END = WD["promo_end"][:10]

def price(pid): return WD["products"][pid]["price"]
def was(pid): return WD["products"][pid]["was"]

def cop(n):
    """Pesos colombianos: $1.999.000 (punto de miles, sin decimales)."""
    return "$" + f"{round(n):,}".replace(",", ".")

def wa(text):
    return f"https://wa.me/{WA_NUM}?text=" + quote(text)

def price_list():
    names = [("smart", "Dispensador ED01"), ("uf", "Ultrafiltración UF"), ("g2", "G2P600"), ("g5", "G5P700A"), ("x12", "X12")]
    return ", ".join(f"{n} {cop(price(p))}" for p, n in names[:-1]) + f" y {names[-1][1]} {cop(price(names[-1][0]))}"

# ------------------------------------------------------------------ AL ESCRIBIR CADA PÁGINA
# En el código del generador se escriben estos marcadores (así no chocan con las llaves de los f-strings):
#   §WA§  número de WhatsApp (de js/co.js)    §TEL§  teléfono visible    §MAIL§  correo
#   ⟦texto⟧  dato pendiente: sale en la web como {{texto}}
def finish(html):
    for a, b in (("§WA§", WA_NUM), ("§TEL§", WA_SHOW), ("§MAIL§", EMAIL), ("⟦", "{{"), ("⟧", "}}"),
                 ("distribuidor oficial", DIST), ("Distribuidor oficial", DIST_C)):
        html = html.replace(a, b)
    return html

def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(finish(html))
    print("ok", name)
