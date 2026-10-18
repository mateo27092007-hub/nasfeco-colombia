# -*- coding: utf-8 -*-
"""NASFECO COLOMBIA · Medellín — genera toda la web.

Como las webs de Miami y España: pocos equipos (Waterdrop X12 y Ultrafiltración UF) y todo el servicio Nasfeco,
con identidad propia de Colombia: esmeralda y oro (las esmeraldas y El Dorado), franja tricolor, bandas de tejido wayúu,
las montañas del valle de Aburrá con el Metrocable y voz paisa.

Uso:  python _build/build_co.py   (y después  python _build/build_seo.py)
Escribe: index.html, product-x12.html, product-uf.html y politica-cookies.html.
Datos de la empresa: _build/co.py · WhatsApp, precios, códigos y oferta: js/co.js (objeto WD).
Marcadores: §WA§ §TEL§ §MAIL§ y ⟦pendiente⟧ (ver co.py → finish)."""
import os, re, json, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import co as C

ROOT, SITE, V = C.ROOT, C.SITE, C.VER
WA_PATH = re.sub(r'^<path d="|"$', "", open(os.path.join(HERE, "wa_path.txt"), encoding="utf-8").read().strip())

def a(path):
    """Ruta a un recurso; falla si no existe (así no se publica una imagen rota)."""
    if not os.path.exists(os.path.join(ROOT, path)): raise FileNotFoundError(path)
    return path

def ico(d, w=20, sw=1.6):
    return f'<svg viewBox="0 0 24 24" width="{w}" height="{w}" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{d}"/></svg>'
I_ARR = "M7 17L17 7M9 7h8v8"; I_RIGHT = "M5 12h14M13 6l6 6-6 6"; I_X = "M6 6l12 12M18 6L6 18"; I_MENU = "M4 8h16M4 16h16"; I_PLUS = "M12 5v14M5 12h14"
I_CHAT = "M4 5h16v11H9l-5 4z"; I_HOME = "M3 11l9-7 9 7v9H3zM9 20v-6h6v6"
I_TOOL = "M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.8-3.8a6 6 0 01-7.9 7.9l-6.9 6.9a2.1 2.1 0 01-3-3l6.9-6.9a6 6 0 017.9-7.9z"
I_SHIELD = "M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6zM8.5 12l2.5 2.5 4.5-5"
I_GIFT = "M4 11h16v10H4zM2 7h20v4H2zM12 7v14M12 7c-1.5-3-5-3.5-5-1s3 1 5 1zm0 0c1.5-3 5-3.5 5-1s-3 1-5 1z"
I_SPARK = "M12 3l1.8 5.4L19 10l-5.2 1.6L12 17l-1.8-5.4L5 10l5.2-1.6z"; I_CHECK = "M5 12l5 5 9-10"; I_PIN = "M12 22s7-6.2 7-12a7 7 0 10-14 0c0 5.8 7 12 7 12zM12 12.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"
WA = f'<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="{WA_PATH}"/></svg>'

def em(t): return t.replace("[", "<em>").replace("]", "</em>")
def kick(text, lt=False, c=False): return f'<p class="kick{" lt" if lt else ""}{" c" if c else ""}">{text}</p>'
def btn(text, attrs="", cls="b-gold", href=None, icon=I_ARR):
    inner = f'<span>{text}</span><i>{ico(icon, 15, 1.9)}</i>'
    return f'<a class="btn {cls}" href="{href}" {attrs}>{inner}</a>' if href else f'<button type="button" class="btn {cls}" {attrs}>{inner}</button>'
def wa_btn(text, msg, cls="b-wa"): return f'<a class="btn {cls}" href="{C.wa(msg)}" target="_blank" rel="noopener"><span>{text}</span><i>{WA}</i></a>'

# ------------------------------------------------------------------ marca: logo NASFECO COLOMBIA, sello, motivos colombianos
# Logo oficial NASFECO COLOMBIA (assets/brand): a color para fondos claros, blanco y dorado para fondos oscuros.
def logo(kind="c", h=40, cls=""):
    src = "assets/brand/nasfeco-colombia.png" if kind == "c" else "assets/brand/nasfeco-colombia-blanco.png"
    return f'<img class="logo {cls}" src="{a(src)}" alt="NASFECO Colombia" width="{round(h * 800 / 183)}" height="{h}">'
def mark(w=34, kind="w"):
    src = "assets/brand/simbolo-blanco.png" if kind == "w" else "assets/brand/simbolo.png"
    return f'<img class="mk" src="{a(src)}" alt="" width="{w}" height="{w}">'
def seal():
    """Sello giratorio de distribuidor oficial (como en la web de Ecuador)."""
    return (f'<div class="seal" aria-hidden="true"><svg class="seal-r" viewBox="0 0 200 200"><defs><path id="sealp" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs>'
            f'<text><textPath href="#sealp" textLength="486">NASFECO · DISTRIBUIDOR OFICIAL · WATERDROP · MEDELLÍN · </textPath></text></svg>{mark(46, "w")}</div>')
def stripe(): return '<div class="tri" aria-hidden="true"><i></i><i></i><i></i></div>'
def wayuu(cls=""): return f'<div class="wayuu {cls}" aria-hidden="true"></div>'
def mountains(cls=""):
    """Las montañas del valle de Aburrá con el Metrocable (ilustración propia)."""
    cab = "".join(f'<g transform="translate({x} {y})"><path d="M0 -14V0" stroke="currentColor" stroke-width="1.6"/><rect x="-9" y="0" width="18" height="15" rx="3" fill="var(--oro)"/><rect x="-6" y="3" width="12" height="5" rx="1" fill="rgba(5,40,29,.55)"/></g>' for x, y in ((420, 92), (760, 70), (1080, 52)))
    return (f'<svg class="mtn {cls}" viewBox="0 0 1440 240" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M0 150 C120 110 200 80 300 96 S470 40 560 62 S720 120 820 96 S980 30 1080 48 S1260 104 1340 86 L1440 70 V240 H0Z" fill="var(--m1)"/>'
            '<path d="M0 190 C140 160 240 140 360 156 S540 120 660 140 S860 186 980 166 S1180 120 1300 140 L1440 150 V240 H0Z" fill="var(--m2)"/>'
            f'<path d="M150 150 Q620 60 1300 22" fill="none" stroke="currentColor" stroke-width="1.4" opacity=".7"/>{cab}'
            '<path d="M0 214 C200 200 380 196 560 206 S960 222 1140 210 L1440 204 V240 H0Z" fill="var(--m3)"/></svg>')

# ------------------------------------------------------------------ los dos equipos
X, UF = "assets/x12/", "assets/uf/"
def vid(path, cls=""):
    return f'<video class="{cls}" muted playsinline loop preload="none" data-auto poster="{a(path + "-poster.jpg")}"><source src="{a(path + ".mp4")}" type="video/mp4"></video>'
def media(src, alt=""):
    return vid(src[:-4]) if src.endswith(".mp4") else f'<img src="{a(src)}" alt="{alt}" loading="lazy">'

MODELS = {
  "x12": dict(name="X12", gpd="1200 GPD", tag="Máxima pureza", file="product-x12.html", power=True, art="la", req="assets/req/requisitos-instalacion.jpg",
    photo=X + "ui-wd-x12-new-vis-pr-logo.webp", yt="26BQXx1PgIE",
    card="Ósmosis inversa sin tanque de 11 etapas, minerales alcalinos y llave inteligente. Quita sarro, metales y sales disueltas.",
    bullets=["1200 GPD: una taza en unos 3 segundos", "11 etapas · membrana de 0.0001 μm", "Minerales alcalinos · pH 7.5±", "Llave inteligente con TDS"],
    kick="Ósmosis inversa sin tanque · Serie X", h1="Waterdrop [X12]",
    desc="El equilibrio perfecto para la mayoría de familias: agua pura al instante, minerales alcalinos y una llave inteligente que te muestra cómo está tu agua. Valorada, instalada y acompañada por Nasfeco en Medellín.",
    chips=["1200 GPD", "11 etapas", "3:1", "pH 7.5", "NSF/ANSI 42 · 58 · 372"],
    gallery=[X + f for f in ["ui-wd-x12-main-sello.webp", "ui-wd-x12-b-new-vis-main.webp", "ui-wd-x12-new-vis-pr-logo-white.jpg", "WD_X12_new.webp", "1226-WD-_1016-1200g__2.jpg", "1226-WD-_1016-1200g__3.jpg", "X12_3.jpg", "X12_4.jpg", "1226-WD-_1016-1200g__7.jpg", "X12_8.jpg", "X12-NSF_ANTI-4258372.jpg"]],
    feats=[("assets/clips/x12-tds.mp4", "Una llave que te informa", "Muestra el TDS de tu agua en tiempo real y te avisa cuándo toca cambiar cada filtro."),
           ("assets/clips/x12-pour.mp4", "Una taza en unos 3 segundos", "Sin tanque que llenar: el agua pasa por los filtros directo a tu vaso, con 1200 galones por día."),
           (X + "7f24c79c8deb40ad8173c66aa62464a8.mp4", "Con minerales alcalinos", "Después de purificar, le devuelve calcio y magnesio al agua y la deja con un pH cercano a 7.5."),
           ("assets/x16/38fc560a5a7b46c2b2d5d6b2549e4ceb.mp4", "11 etapas de filtración", "Membrana de 0.0001 μm y protección LED: reduce TDS, cloro, flúor, plomo, PFOA, PFOS y más."),
           ("assets/clips/x12-cabinet.mp4", "Tu mueble, de vuelta", "Delgado y de pie, sin tanque: libera hasta un 70 % del espacio bajo el lavaplatos."),
           ("assets/clips/x12-inside.mp4", "Filtros en segundos", "Tres filtros que se giran y se cambian sin herramientas ni goteos.")],
    specs=[("Modelo", "WD-X12"), ("Capacidad nominal", "1200 GPD"), ("Agua pura / desagüe", "3:1"), ("Filtración", "11 etapas · membrana de 0.0001 μm"), ("Remineralización", "Minerales alcalinos · pH 7.5±"),
           ("Llave", "Inteligente: TDS, volumen programable y aviso de filtros"), ("Certificación", "NSF/ANSI 42, 58 y 372"), ("Medidas", "46 × 16 × 42 cm"), ("Peso", "17.7 kg"),
           ("Electricidad", "Tomacorriente bajo el lavaplatos"), ("Vida de los filtros", "F1A 12 meses · F2 6 meses · X12-F3 24 meses, según el uso")],
    spec_img=X + "X12-Spec.jpg",
    cmp=["Ósmosis inversa + remineralización", "1200 GPD", "11 etapas · 0.0001 μm", "Sí: quita sarro, metales y sales", "Sí, tomacorriente", "Bajo el lavaplatos, sin tanque", "Familias que quieren la máxima pureza"],
    faq=[("¿Por qué la X12 es la más recomendada?", "Tiene caudal de sobra para una familia, 11 etapas de filtración, minerales alcalinos y una llave con volumen programable."),
         ("¿Necesita electricidad?", "Sí: un tomacorriente bajo el lavaplatos para la bomba sin tanque, la llave inteligente y la protección LED. Si no lo tienes, lo revisamos en la valoración."),
         ("¿Quita los minerales del agua?", "La ósmosis inversa retiene casi todo, pero la X12 tiene una etapa que le devuelve calcio y magnesio y deja el pH alrededor de 7.5."),
         ("¿Cada cuánto se cambian los filtros?", "F2 cada 6 meses, F1A cada 12 meses y X12-F3 cada 24 meses, según el uso. La llave te avisa y nosotros te recordamos cuándo toca."),
         ("¿Puedo usar mi propia llave?", "No. La llave de la X12 es parte del sistema: tiene el monitor de calidad, la protección LED y el aviso de cambio de filtros.")]),
  "uf": dict(name="Ultrafiltración UF", gpd="0.01 μm", tag="Sin electricidad", file="product-uf.html", power=False, art="la", req="assets/req/requisitos-instalacion-uf.jpg",
    photo=UF + "10UB-UF-NSF.png", yt="tL_2gSpSn20",
    card="Membrana de 0.01 μm que quita cloro, sedimentos y bacterias y conserva los minerales. Sin luz y sin desperdiciar agua.",
    bullets=["Membrana de ultrafiltración de 0.01 μm", "0 % de desperdicio de agua", "No necesita electricidad", "Llave de acero inoxidable incluida"],
    kick="Bajo el lavaplatos · Sin electricidad", h1="Waterdrop [Ultrafiltración UF]",
    desc="Agua limpia que conserva sus minerales naturales. Sin electricidad, sin desperdicio de agua y con llave de acero inoxidable incluida. Ideal si el agua de tu casa llega en buen estado y lo que quieres es mejor sabor.",
    chips=["0.01 μm", "0 % desperdicio", "Sin electricidad", "Conserva minerales"],
    gallery=[UF + f for f in ["10UB-UF-NSF-feed.jpg", "10UB-UF-NSF.png", "UB-UF_6.jpg", "UB-UF_7.jpg", "UB-UF_4.jpg", "UB-UF_3.jpg", "UB-UF_9.jpg", "UB-UF_8.jpg", "dedicated-faucet-ultrafiltration.png"]],
    feats=[(UF + "wd-undersink-ub-uf-img-1.webp", "Retiene lo que no se ve", "Todo lo que mide más de 0.01 micras se queda en la membrana: óxido, bacterias, quistes y sedimentos."),
           (UF + "UB-UF_6.jpg", "Un filtro para todo el año", "Cada filtro dura hasta 12 meses u 8000 galones, suficiente para una familia."),
           (UF + "UB-UF_7.jpg", "Se cambia en 3 segundos", "Conexión giratoria sin herramientas, sin fugas y sin ensuciar el mueble."),
           (UF + "UB-UF_9.jpg", "Llave de acero inoxidable 304", "Llave dedicada sin plomo, con acabado cepillado, incluida en la caja."),
           (UF + "wd-undersink-ub-uf-img-8.png", "Para tomar, cocinar y lavar alimentos", "Quita lo que no quieres y conserva los minerales."),
           (UF + "wd-product-ubuf-overviews-img3.jpg", "Diseño compacto", "Ocupa muy poco bajo el lavaplatos y no necesita tomacorriente.")],
    specs=[("Modelo", "WD-10UB-UF"), ("Filtración", "Membrana UF de 0.01 μm"), ("Caudal", "2.8 L/min"), ("Desperdicio de agua", "0 %"), ("Vida del filtro", "RF10-UF 12 meses u 8000 galones"),
           ("Medidas", "9 × 10 × 31 cm"), ("Peso", "1.7 kg"), ("Temperatura del agua", "2 a 38 °C"), ("Electricidad", "No necesita"), ("Llave", "Acero inoxidable 304 sin plomo, incluida")],
    spec_img=UF + "10UB-UF-NSF.png",
    cmp=["Membrana de ultrafiltración", "2.8 L/min", "0.01 μm · conserva minerales", "No: conserva las sales y minerales", "No necesita", "Bajo el lavaplatos", "Mejor sabor sin gastar luz"],
    faq=[("¿La UF necesita electricidad?", "No. Funciona con la presión de agua de tu casa, así que no gasta luz y sigue funcionando aunque se vaya la energía."),
         ("¿Cuál es la diferencia con la X12?", "La UF retiene bacterias, óxido y sedimentos y conserva los minerales, pero no reduce las sales disueltas (TDS). Si tu agua tiene mucho sarro o quieres la máxima pureza, te recomendamos la X12."),
         ("¿Cada cuánto se cambia el filtro?", "Hasta 12 meses u 8000 galones, según tu consumo. El indicador te avisa con luz y nosotros te recordamos cuándo toca.")]),
}
ORDER = ["x12", "uf"]
def full(k): return C.WD["products"][k]["name"]

# ------------------------------------------------------------------ cabecera, pie y piezas comunes
def head(title, desc, path, ld, img="assets/home/escena-cocina.jpg"):
    url = SITE + path
    return f'''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{"noindex, nofollow" if C.PREVIEW else "index, follow"}">
<link rel="canonical" href="{url}">{C.hreflang(path)}
<meta name="theme-color" content="#05281D">
<meta property="og:type" content="website"><meta property="og:site_name" content="Nasfeco Colombia"><meta property="og:locale" content="es_CO"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{SITE}{a(img)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="favicon.png"><link rel="apple-touch-icon" href="favicon.png">
<link rel="preload" href="assets/fonts/bricolage-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/co.css?v={V}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Ir al contenido</a>'''

def promo_bar():
    return f'''{stripe()}
<div class="pbar" data-promo role="region" aria-label="Oferta"><div class="pbar-in"><b data-promo-name></b><span>Hasta <strong data-maxoff></strong> de descuento con tu código</span><a href="index.html#equipos">Ver equipos</a><span class="pbar-t">Termina en <i data-cd>…</i></span></div></div>'''

NAV = [("index.html#equipos", "Equipos"), ("index.html#por-que", "Por qué Nasfeco"), ("index.html#bienvenida", "Tu bienvenida"), ("index.html#medellin", "Medellín"), ("index.html#faq", "Preguntas")]

def header(solid=False):
    links = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return promo_bar() + f'''
<header class="hd{" solid" if solid else ""}" id="hd">
  <a class="hd-logo" href="index.html" aria-label="NASFECO Colombia, inicio">{logo("w", 38, "lg-w")}{logo("c", 38, "lg-c")}</a>
  <nav class="hd-nav" aria-label="Principal">{links}</nav>
  <div class="hd-r"><button type="button" class="hd-cta dk" data-book>Agenda tu valoración <i>{ico(I_ARR, 14, 1.9)}</i></button><button type="button" class="hd-menu" data-menu aria-expanded="false" aria-controls="mnav" aria-label="Abrir menú">{ico(I_MENU, 22, 1.6)}</button></div>
</header>
<div class="mnav" id="mnav" hidden><nav aria-label="Menú móvil">{links}<a href="product-x12.html">Waterdrop X12</a><a href="product-uf.html">Ultrafiltración UF</a></nav>{btn("Agenda tu valoración", "data-book", "b-gold")}<small>WhatsApp §TEL§ · Medellín</small></div>'''

def footer():
    return f'''
<footer class="ft">
  {wayuu("w-ft")}
  <div class="wrap ft-g">
    <div class="ft-brand">{logo("w", 40)}<p>Agua. Tecnología. Atención personal. {C.COMPANY}, distribuidor oficial de Waterdrop Filter, desde Medellín.</p>
      <a class="ft-us" href="https://nasfecousa.com/"><img src="{a("assets/brand/nasfeco-us-white.png")}" alt="NASFECO US International" width="70" height="24">Miami, FL ↗</a></div>
    <div><h3 class="ft-h">Equipos</h3><a href="product-x12.html">Waterdrop X12</a><a href="product-uf.html">Ultrafiltración UF</a><button type="button" class="ft-l" data-compare>Comparar los dos</button><button type="button" class="ft-l" data-quiz>¿Cuál es para mí?</button></div>
    <div><h3 class="ft-h">Nasfeco</h3><a href="index.html#por-que">Por qué Nasfeco</a><a href="index.html#bienvenida">Tu bienvenida</a><a href="politica-cookies">Política de cookies</a><a href="{C.PRIVACY_URL}">Tratamiento de datos personales</a><button type="button" class="ft-l" data-cookie-settings>Configurar cookies</button></div>
    <div><h3 class="ft-h">Contacto</h3><a href="{C.wa("¡Hola Nasfeco! Quiero información sobre los purificadores.")}" target="_blank" rel="noopener">WhatsApp §TEL§</a><a href="mailto:§MAIL§">§MAIL§</a><p>Medellín, Antioquia</p><p>Instalamos en las 16 comunas</p></div>
  </div>
  <div class="ft-b"><span>© 2026 Nasfeco · Colombia. {C.COMPANY} · NIT {C.NIT}. Distribuidor oficial de Waterdrop Filter. Waterdrop Filter es una marca registrada de su fabricante.</span><span>Hecho en Medellín · Creado por <strong>Mateo Perez</strong></span></div>
</footer>'''

def yt_box(i, label):
    return (f'<div class="yt-s" data-ytauto="{i}" aria-label="{label}"><img src="{a(f"assets/img/yt/{i}.webp")}" alt="" loading="lazy">'
            f'<div class="yt-gate"><p>Este video está en YouTube, que usa cookies.</p><button type="button" class="btn b-gold" data-consent="yes"><span>Aceptar y ver</span></button></div></div>')

def zone_select(sid):
    og = lambda lab, xs: f'<optgroup label="{lab}">' + "".join(f"<option>{x}</option>" for x in xs) + "</optgroup>"
    return f'<select id="{sid}" aria-label="Tu comuna o municipio"><option value="">Elige tu comuna o municipio</option>{og("Medellín · comunas", C.COMUNAS)}{og("Medellín · corregimientos", C.CORREGIMIENTOS)}{og("Fuera de Medellín", C.OTROS)}</select>'

def checker(sid, lt=True):
    return (f'<form class="zc{" lt" if lt else ""}" data-check><label for="{sid}">{ico(I_PIN, 18, 1.8)}¿Llegamos a tu casa?</label>'
            f'<div class="zc-row">{zone_select(sid)}{btn("Agendar mi valoración", "data-book data-check-go hidden", "b-gold")}</div><p class="zc-out" data-check-out aria-live="polite"></p></form>')

def cmp_table():
    rows = ["Tecnología", "Caudal", "Filtración", "Quita sarro y sales (TDS)", "Electricidad", "Instalación", "Ideal para"]
    th = "".join(f'<th><img src="{a(MODELS[k]["photo"])}" alt=""><br>{full(k).replace("Waterdrop ", "")}</th>' for k in ORDER)
    tb = "".join(f'<tr><th>{r}</th>{"".join(f"<td>{MODELS[k]["cmp"][i]}</td>" for k in ORDER)}</tr>' for i, r in enumerate(rows))
    tb += '<tr><th>Precio final</th>' + "".join(f'<td><b data-price="{k}"></b></td>' for k in ORDER) + "</tr>"
    tb += '<tr><th>Servicio Nasfeco</th>' + "".join('<td>Valoración, instalación, kit y seguimiento</td>' for _ in ORDER) + "</tr>"
    tb += '<tr><th></th>' + "".join(f'<td><button type="button" class="btn b-green" data-book="{k}"><span>Elegir {MODELS[k]["name"].split()[-1]}</span><i>↗</i></button></td>' for k in ORDER) + "</tr>"
    return f'<div class="cmp"><table><thead><tr><th>Compara</th>{th}</tr></thead><tbody>{tb}</tbody></table></div>'

def dialogs(req=None):
    x = f'<button type="button" class="dx" data-close aria-label="Cerrar">{ico(I_X, 20, 1.6)}</button>'
    cfg = {"models": {k: {"img": MODELS[k]["photo"], "gpd": MODELS[k]["gpd"], "install": True, "url": MODELS[k]["file"]} for k in ORDER},
           "zones": {"comunas": C.COMUNAS, "corr": C.CORREGIMIENTOS, "otros": C.OTROS}, "company": C.COMPANY, "privacy": C.PRIVACY_URL}
    reqd = (f'<dialog class="dlg dlg-wide" id="d-req" aria-labelledby="rq-t">{x}{kick("Revisar antes de comprar")}<h2 class="h3" id="rq-t">{em("Requisitos de [instalación.]")}</h2>'
            f'<div class="req-img"><a href="{a(req[0])}" target="_blank" rel="noopener"><img src="{req[0]}" alt="Requisitos para instalar el {req[1]}: tomas de agua visibles debajo del lavaplatos" loading="lazy"></a></div><p class="fine">Toca la imagen para verla en grande. Si tienes dudas, lo revisamos en la valoración.</p></dialog>') if req else ""
    return f'''
<dialog class="dlg dlg-wide" id="d-compare" aria-labelledby="cmp-t">{x}{kick("Elige lo que va contigo")}<h2 class="h3" id="cmp-t">{em("X12 o UF, [lado a lado.]")}</h2>{cmp_table()}
  <p class="fine">Precios finales en pesos colombianos, con IVA. El caudal real depende de la presión de agua de tu casa.</p></dialog>
<dialog class="dlg" id="d-quiz" aria-labelledby="qz-t">{x}{kick("Un minuto para conocerte")}<h2 class="h3" id="qz-t">{em("¿Cuál va [contigo?]")}</h2><div id="qz-body"></div></dialog>
<dialog class="dlg dlg-book" id="d-book" aria-labelledby="bk-title">
  <aside class="bk-side">{mark(44)}<h3>{em("Tu casa.<br>Tu agua.<br>[Tu experiencia.]")}</h3>
    <div class="bk-sum"><img id="bk-img" src="{a(MODELS["x12"]["photo"])}" alt=""><div><b id="bk-model"></b><span id="bk-price"></span><small id="bk-inc"></small></div></div>{wayuu("w-side")}</aside>
  <div class="bk-main">{x}<div class="bk-prog"><span class="on"></span><span></span><span></span><b id="bk-step">01 / 03</b></div>
    <h2 class="h3" id="bk-title"></h2><p class="bk-sub" id="bk-sub"></p>
    <form id="bk-form" novalidate><div id="bk-fields"></div><p class="bk-err" id="bk-err" role="alert"></p>
      <div class="row bk-btns"><button type="button" class="btn b-line" id="bk-back"><span>Atrás</span></button><button type="submit" class="btn b-green" id="bk-next"><span>Continuar</span><i>{ico(I_RIGHT, 15, 1.9)}</i></button></div></form></div>
</dialog>{reqd}
<div class="ck" id="ck" role="dialog" aria-modal="false" aria-labelledby="ck-t" hidden>
  <p id="ck-t"><b>Cookies</b>Solo usamos el almacenamiento imprescindible para que la web funcione. Los videos de YouTube colocan sus propias cookies, así que solo se cargan si aceptas; lo mismo con la medición de anuncios, si la activamos. Puedes cambiar tu elección desde el pie de página. <a class="ul" href="politica-cookies">Política de cookies</a></p>
  <div class="ck-b"><button type="button" class="btn ck-btn" data-consent="no"><span>Rechazar</span></button><button type="button" class="btn ck-btn" data-consent="yes"><span>Aceptar</span></button></div>
</div>
<a class="cc-wa" href="{C.wa("¡Hola Nasfeco! Quiero información sobre los purificadores.")}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">{WA}</a>
<button type="button" class="cc-btn" data-cc aria-expanded="false" aria-controls="cc">{ico(I_SPARK, 18, 1.6)}<span>¿Dudas? Te ayudamos</span></button>
<div class="cc" id="cc" hidden role="dialog" aria-label="Tu asesor Nasfeco">
  <div class="cc-h">{mark(34, "c")}<div><small>Tu asesor · Nasfeco Medellín</small><b>¿Qué más pues? ¿En qué te ayudamos?</b></div><button type="button" class="dx" data-cc-close aria-label="Cerrar">{ico(I_X, 18, 1.6)}</button></div>
  <div class="cc-t">{"".join(f'<button type="button" data-cc-topic="{k}">{t}</button>' for k, t in [("which", "¿X12 o UF?"), ("inc", "Todo lo que incluye"), ("kitchen", "¿Funciona en mi cocina?"), ("care", "Después de instalar"), ("pay", "Precios y pago")])}</div>
  <p class="cc-a" id="cc-a" aria-live="polite"></p>
  <div class="cc-f">{wa_btn("Hablar con una persona por WhatsApp", "¡Hola Nasfeco! Tengo una pregunta sobre los purificadores.")}{btn("Agendar mi valoración", "data-book", "b-line")}<button type="button" class="btn b-line" data-quiz><span>¿Cuál es para mí?</span><i>{ico(I_ARR, 15, 1.9)}</i></button></div>
  <small>Respuestas preparadas. Para todo lo demás, te responde una persona por WhatsApp.</small>
</div>
<script>window.NF_CFG = {json.dumps(cfg, ensure_ascii=False)};</script>
<script src="js/co.js?v={V}"></script>'''

def ribbon(items):
    t = "".join(f"<span>{x}</span>" for x in items * 2)
    return f'<div class="ribbon" aria-hidden="true"><div>{t}</div></div>'
RIBBON = ["Medellín", "La ciudad de la eterna primavera", "Precios en pesos con IVA", "Distribuidor oficial Waterdrop Filter", "Instalación incluida", "Kit de bienvenida", "Chao botellón"]

# ------------------------------------------------------------------ secciones del inicio
def hero_home():
    return f'''
<section class="hero" id="top">
  {wayuu("w-hero")}
  <div class="wrap hero-g">
    <div class="hero-c">
      <p class="auth"><b><img src="{a("assets/brand/waterdrop-filter-logo.png")}" alt="Waterdrop Filter" width="140" height="27"></b><span>Distribuidor oficial en Colombia</span></p>
      {kick("Nasfeco Colombia · Medellín", True)}
      <h1 class="h1">Chao botellón.<br><em>Hola agua pura.</em></h1>
      <p class="lead lt">Purificadores Waterdrop Filter instalados en tu casa en Medellín. Tú eliges el equipo; nosotros revisamos tu cocina, lo instalamos, te damos tu kit de bienvenida y seguimos pendientes.</p>
      {checker("hero-zone")}
      <div class="row hero-btns">{btn("Agenda tu valoración", "data-book", "b-gold")}{btn("Ver los equipos", "", "b-ghost", "#equipos", I_RIGHT)}</div>
    </div>
    <div class="duo rv">
      <article class="duo-a"><p class="duo-k">Lo que compras</p><div class="duo-m"><img class="p1" src="{a(MODELS["x12"]["photo"])}" alt="Waterdrop X12" width="560" height="560"><img class="p2" src="{a(MODELS["uf"]["photo"])}" alt="Waterdrop Ultrafiltración UF" loading="lazy"></div>
        <h3>Waterdrop X12 <small>o</small> UF</h3><ul><li>Equipo original Waterdrop Filter</li><li>Con su llave dedicada</li><li>Certificado NSF/ANSI</li></ul></article>
      <span class="duo-plus" aria-hidden="true">+</span>
      <article class="duo-b"><p class="duo-k">Lo que te damos</p><div class="duo-m"><img src="{a("assets/img/kit-bienvenida.webp")}" alt="Kit de bienvenida Nasfeco" loading="lazy"></div>
        <h3>Servicio Nasfeco</h3><ul><li>Valoración de tu cocina</li><li>Instalación en Medellín</li><li>Kit de bienvenida y seguimiento</li></ul></article>
      <p class="duo-eq"><b>Equipo + servicio Nasfeco</b> = un solo precio en pesos, IVA incluido</p>
      {seal()}
    </div>
  </div>
  {mountains("m-hero")}
</section>''' + ribbon(RIBBON)

def card(k):
    m = MODELS[k]
    return f'''
    <article class="sy rv">
      <a class="sy-m" href="{m["file"]}" aria-label="Ver {full(k)}"><img src="{a(m["photo"])}" alt="{full(k)}" loading="lazy"><span class="sy-tag">{m["tag"]}</span><span class="sy-save" data-promo-on>Ahorras <b data-save="{k}"></b></span></a>
      <div class="sy-b"><p class="brand">Waterdrop Filter · instalado por Nasfeco</p>
        <h3>{m["name"]} <small>{m["gpd"]}</small></h3><p class="sy-d">{m["card"]}</p>
        <ul class="sy-l">{"".join(f"<li>{ico(I_CHECK, 15, 2.4)}{b}</li>" for b in m["bullets"])}</ul>
        <div class="price"><b data-price="{k}"></b><s data-was="{k}"></s><small>IVA incluido · valoración, instalación en Medellín y kit de bienvenida</small></div>
        <span class="code" data-promo-on>Código <b data-code="{k}"></b></span>
        <div class="row">{btn("Agendar valoración", f'data-book="{k}"', "b-gold")}<a class="ul" href="{m["file"]}">Ver detalles {ico(I_ARR, 14, 1.9)}</a></div></div>
    </article>'''

def systems():
    return f'''
<section class="sec" id="equipos">
  <div class="wrap">
    <div class="sec-split"><div class="sec-h rv">{kick("01 · Elige tu equipo")}<h2 class="h2">{em("Dos equipos.<br>[La misma atención Nasfeco.]")}</h2>
      <p class="lead">Waterdrop Filter hace el equipo; Nasfeco se encarga de todo lo demás. Precios finales en pesos colombianos, con IVA y la instalación en Medellín.</p></div>
      <div class="row"><button type="button" class="btn b-line" data-compare><span>Comparar lado a lado</span><i>{ico("M7 16l-4-4 4-4M17 8l4 4-4 4M3 12h18", 15, 1.8)}</i></button><button type="button" class="btn b-line" data-quiz><span>¿Cuál es para mí?</span><i>{ico(I_ARR, 15, 1.8)}</i></button></div></div>
    <div class="sys-g">{card("x12")}{card("uf")}</div>
  </div>
</section>'''

ICONS = {
  "tinto": '<path d="M10 24h30v10a13 13 0 01-13 13h-4A13 13 0 0110 34z"/><path d="M40 27h4a6 6 0 010 12h-5"/><path d="M8 52h36"/><path d="M19 8c-3 4 3 6 0 10M27 6c-3 4 3 6 0 10M35 8c-3 4 3 6 0 10"/>',
  "jugo": '<path d="M14 16h28l-4 34H18z"/><path d="M15 26h26"/><path d="M30 16l6-10h6"/><circle cx="44" cy="20" r="6"/>',
  "panela": '<path d="M12 22h30v8a15 15 0 01-15 15A15 15 0 0112 30z"/><path d="M42 25h3a5 5 0 010 10h-4"/><rect x="19" y="8" width="10" height="9" rx="1.5"/><path d="M33 12l4-4"/>',
  "sancocho": '<path d="M6 24h44"/><path d="M10 24v12a12 12 0 0012 12h12a12 12 0 0012-12V24"/><path d="M4 30h6M46 30h6"/><path d="M20 16c-2 3 2 4 0 7M28 13c-2 3 2 4 0 7M36 16c-2 3 2 4 0 7"/>'}
def nuestro():
    items = [("tinto", "El tinto de la mañana", "El café colombiano es de los mejores del mundo. No lo dañes con agua que sabe a cloro."),
             ("jugo", "Jugos naturales", "Lulo, maracuyá, mora, guanábana: el jugo de la casa queda más rico con agua pura."),
             ("panela", "Aguapanela y chocolate", "Para la aguapanela con limón, el chocolate con queso y la arepa de las onces."),
             ("sancocho", "El sancocho del domingo", "La olla grande de la familia también merece agua sin sedimentos ni cloro.")]
    c = "".join(f'<article class="nu rv"><svg viewBox="0 0 56 56" width="56" height="56" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[i]}</svg><h3>{t}</h3><p>{d}</p></article>' for i, t, d in items)
    return f'''
<section class="sec nuestro" id="lo-nuestro">
  {wayuu("w-top")}
  <div class="wrap">
    <div class="sec-h c rv">{kick("02 · Hecho para nuestra cocina", c=True)}<h2 class="h2">{em("Lo nuestro sabe mejor<br>[con agua pura.]")}</h2>
      <p class="lead">En la casa paisa el agua está en todo: el tinto, los jugos, la aguapanela, la arepa. Con un purificador todo eso sabe a lo que tiene que saber.</p></div>
    <div class="nu-g">{c}</div>
  </div>
</section>'''

VS_ALONE = ["Te llega una caja a la puerta", "Lo instalas tú o buscas un plomero", "Tú revisas mueble, desagüe y tomacorriente", "Soporte por los canales del fabricante", "Sin kit de bienvenida"]
VS_NF = ["Primero valoramos tu cocina", "Instalado y probado por Nasfeco", "Alcance por escrito, sin sorpresas", "Una persona de Medellín que te responde", "Tu kit de bienvenida Nasfeco"]
def porque():
    you = ["Escribirnos o agendar tu valoración", "Elegir tu equipo", "Disfrutar tu agua"]
    us = ["Te escuchamos y te ayudamos a elegir", "Revisamos espacio, agua, desagüe y tomacorriente", "Te damos el alcance por escrito antes de instalar", "Cuadramos la visita a tu horario",
          "Lo instalamos y comprobamos que funcione", "Te enseñamos a usar el equipo", "Te entregamos tu kit de bienvenida", "Te hacemos seguimiento y te recordamos el mantenimiento"]
    return f'''
<section class="sec" id="por-que">
  <div class="wrap">
    <div class="sec-h rv">{kick("03 · Por qué Nasfeco")}<h2 class="h2">{em("El mismo equipo.<br>[Otra experiencia.]")}</h2></div>
    <div class="vs2 rv"><div class="vs2-a"><p class="ez-t">Comprarlo por tu cuenta</p><ul>{"".join(f"<li>{ico(I_X, 15, 2)}{t}</li>" for t in VS_ALONE)}</ul></div>
      <div class="vs2-b"><p class="ez-t">{mark(22)}Con Nasfeco</p><ul>{"".join(f"<li>{ico(I_CHECK, 16, 2.4)}{t}</li>" for t in VS_NF)}</ul></div></div>
    <h3 class="h3 ez-h rv">{em("Tú eliges. [Del resto nos encargamos nosotros.]")}</h3>
    <div class="ez-g">
      <article class="ez-c ez-you rv"><p class="ez-t">Lo único que haces tú</p><ol>{"".join(f"<li><span>0{i+1}</span>{t}</li>" for i, t in enumerate(you))}</ol></article>
      <article class="ez-c ez-us rv"><p class="ez-t">{mark(22)}Todo lo que hace Nasfeco</p><ul>{"".join(f"<li>{ico(I_CHECK, 16, 2.2)}<span>{t}</span></li>" for t in us)}</ul>{btn("Empieza con tu valoración", "data-book", "b-gold")}</article>
    </div>
  </div>
</section>'''

def kit_sec(num="04 · Tu bienvenida"):
    items = [("Bolso Nasfeco", "De lona, con asas verdes y el bordado Nasfeco Colombia. Pa' la finca, el mercado o el día a día."),
             ("Tu botella Owala personalizada", "Térmica, con la personalización Nasfeco, para llevar tu agua pura al gimnasio, a la U o a la oficina."),
             ("Toalla bordada", "Verde esmeralda, con textura y el logo Nasfeco bordado en dorado.")]
    li = "".join(f"<li><span>0{i+1}</span><div><b>{t}</b><p>{d}</p></div></li>" for i, (t, d) in enumerate(items))
    return f'''
<section class="sec dark" id="bienvenida">
  {wayuu("w-dark")}
  <div class="wrap kit-g">
    <figure class="kit-img rv"><img src="{a("assets/img/kit-bienvenida.webp")}" alt="Kit de bienvenida Nasfeco Colombia: bolso de lona, botella Owala personalizada y toalla verde bordada" loading="lazy" width="1536" height="1024"><small>Imagen ilustrativa · acabados por confirmar</small></figure>
    <div class="rv">{kick(num, True)}<h2 class="h2 lt">{em("Más que una instalación.<br>[Un detallazo.]")}</h2>
      <p class="lead lt">Cada instalación Nasfeco termina con este kit, sin costo adicional. Porque el agua pura también se lleva pa' la calle.</p>
      <ul class="kit-l">{li}</ul>
      <p class="fine lt">Incluido con la X12 y con la Ultrafiltración UF. Owala es una marca de su fabricante; Nasfeco aparece como personalización.</p></div>
  </div>
</section>'''

def techs():
    pts = [("ID", "Uniforme y credencial", "Llega con la camiseta Nasfeco Colombia y una credencial con su nombre, pa' que sepas quién está en tu puerta."),
           ("RO · UF", "Especialista en tu equipo", "Conoce la X12 y la UF: espacio, conexiones, llave y la primera prueba."),
           ("MDE", "De aquí, de Medellín", "Conoce la ciudad, el agua de EPM y cómo son las cocinas de los edificios y casas paisas."),
           ("1:1", "De principio a fin", "El mismo equipo valora tu cocina, instala, te enseña a usar el equipo y te hace seguimiento.")]
    return f'''
<section class="sec" id="tecnico">
  <div class="wrap tec-g">
    <figure class="tec-img rv"><img src="{a("assets/img/tecnico.webp")}" alt="Técnico de Nasfeco Colombia con camiseta bordada con el logo" loading="lazy" width="480" height="834"><figcaption>Así llega: uniforme Nasfeco Colombia · imagen ilustrativa</figcaption></figure>
    <div class="rv">{kick("05 · Quién llega a tu casa")}<h2 class="h2">{em("Tu técnico [Nasfeco.]")}</h2>
      <p class="lead">Nada de desconocidos con una caja de herramientas. Llega alguien de Nasfeco que conoce tu equipo y responde por su trabajo.</p>
      <ul class="tec-l">{"".join(f"<li><i>{i}</i><b>{t}</b><p>{d}</p></li>" for i, t, d in pts)}</ul>
      {btn("Agenda tu valoración", "data-book", "b-green")}</div>
  </div>
</section>'''

def j_media(kind, k="x12"):
    if kind == "chat":
        return '<div class="j-chat"><p class="me">¡Hola! ¿El purificador cabe bajo mi lavaplatos? Te mando foto pues. 📷</p><p class="them">¡Hola! Te escribe Nasfeco. Con mucho gusto revisamos tu espacio y lo cuadramos contigo.</p></div>'
    if kind == "check":
        items = ["Espacio del mueble", "Toma de agua y desagüe", "Tomacorriente" if MODELS[k]["power"] else "Presión del agua", "Lugar de la llave", "Alcance por escrito"]
        return '<ul class="j-check">' + "".join(f"<li>{ico(I_CHECK, 15, 2.4)}{t}</li>" for t in items) + "</ul>"
    return media(kind)

def install_sec(k="x12", num="06 · Así instalamos"):
    m = MODELS[k]
    mm = ["assets/clips/x12-cabinet.mp4", "assets/clips/x12-tds.mp4", "assets/clips/x12-pour.mp4"] if k == "x12" else [m["feats"][2][0], m["feats"][3][0], m["gallery"][1]]
    steps = [("chat", "Te escuchamos", "Nos cuentas de tu casa, tu rutina y tus dudas. Te responde una persona de Nasfeco, aquí en Medellín."),
             ("check", "Revisamos tu cocina", "Antes de instalar confirmamos la compatibilidad y te dejamos por escrito el alcance y cualquier adaptación."),
             (mm[0], "Instalamos", "Sin obras ni perforar paredes. El equipo queda ordenado bajo tu lavaplatos."),
             (mm[1], "Probamos y te enseñamos", "Servimos juntos el primer vaso y te mostramos cómo funciona el equipo."),
             ("assets/img/kit-bienvenida.webp", "Tu bienvenida", "Te entregamos tu kit Nasfeco: bolso, botella Owala personalizada y toalla bordada."),
             (mm[2], "Seguimos pendientes", "Seguimiento, orientación y recordatorios de mantenimiento. Siempre sabes a quién llamar.")]
    c = "".join(f'<article class="st rv"><div class="st-m">{j_media(md, k)}</div><div class="st-t"><span>Paso 0{i+1}</span><h3>{t}</h3><p>{d}</p></div></article>' for i, (md, t, d) in enumerate(steps))
    return f'''
<section class="sec stone" id="instalacion">
  <div class="wrap">
    <div class="sec-split"><div class="sec-h rv">{kick(num)}<h2 class="h2">{em("Tu cocina, [lista en una visita.]")}</h2></div>{btn("Agenda tu valoración", f'data-book="{k}"', "b-green")}</div>
    <div class="steps">{c}</div>
    <p class="fine">{"Videos oficiales de Waterdrop Filter (X12). " if k == "x12" else ""}El alcance y cualquier adaptación se confirman en tu valoración.</p>
  </div>
</section>'''

def includes(k=None):
    serv = [(I_HOME, "Valoración de tu cocina"), (I_TOOL, "Instalación profesional estándar"), (I_SPARK, "Prueba de funcionamiento y enseñanza"),
            (I_GIFT, "Kit de bienvenida Nasfeco"), (I_CHAT, "Seguimiento y recordatorios"), (I_SHIELD, "Garantía gestionada en Colombia")]
    rows = [k] if k else ORDER
    dl = "".join(f'<div><dt>{full(x)}</dt><dd><span data-price="{x}"></span></dd></div>' for x in rows)
    return f'''
<section class="sec" id="incluye">
  <div class="wrap">
    <div class="sec-h rv">{kick("Qué incluye")}<h2 class="h2">{em("Un solo precio.<br>[Todo resuelto.]")}</h2></div>
    <div class="inc-g">
      <ul class="inc-l rv">{"".join(f"<li><i>{ico(i, 22, 1.6)}</i>{t}</li>" for i, t in serv)}</ul>
      <div class="inc-p rv">{wayuu("w-card")}<div><p class="ez-t" style="color:var(--oro)">Tu equipo + todo esto</p><dl>{dl}</dl></div>
        <p class="fine lt">Pesos colombianos, IVA del 19 % incluido. Instalación estándar en Medellín. Cualquier trabajo adicional se acuerda contigo antes, por escrito.</p>
        {btn("Agenda tu valoración", f'data-book="{k}"' if k else "data-book", "b-gold")}</div>
    </div>
  </div>
</section>'''

def calc_sec(jug=12000, default="x12"):
    seg = "".join(f'<button type="button" class="{"on" if x == default else ""}" data-cp="{x}" aria-pressed="{"true" if x == default else "false"}">{MODELS[x]["name"].replace("Ultrafiltración ", "")}</button>' for x in ORDER)
    return f'''
<section class="sec stone" id="ahorro">
  <div class="wrap">
    <div class="sec-h c rv">{kick("Calcula tu ahorro", c=True)}<h2 class="h2">{em("¿Cuánta plata se te va [en botellones?]")}</h2><p class="lead">Haz la cuenta en 10 segundos y compárala con tener agua pura en tu propia cocina.</p></div>
    <div class="calc rv" data-calc data-default="{default}">
      <div class="calc-in"><h3>Tu consumo actual</h3><p class="fine" style="margin-top:2px">Ajusta los valores a lo que compras normalmente.</p>
        <div class="cf"><label for="c-ppl">Personas en casa <output data-o="ppl"></output></label><input type="range" id="c-ppl" name="ppl" min="1" max="10" value="4"></div>
        <div class="cf"><label for="c-bot">Botellones de 20 L por semana</label><input type="number" id="c-bot" name="bot" min="0" max="30" step="1" value="3" inputmode="numeric"></div>
        <div class="cf"><label for="c-jug">Precio por botellón (COP)</label><input type="number" id="c-jug" name="jug" min="0" max="60000" step="500" value="{jug}" inputmode="numeric"></div>
        <div class="cf"><label>Compararlo con</label><div class="seg2">{seg}</div></div></div>
      <div class="calc-out">{wayuu("w-card")}<div><small>Se te van en botellones al año</small><b class="big" data-o="year">$0</b></div>
        <div class="two"><div><small>Al mes</small><b data-o="month">$0</b></div><div><small>Botellones de plástico al año</small><b data-o="jugs">0</b></div></div>
        <p data-o="msg"></p>{btn("Agendar mi valoración", 'data-o="book" data-book="' + default + '"', "b-gold")}</div>
    </div>
    <p class="fine" style="text-align:center">Cálculo referencial en pesos. El botellón viene en {C.cop(jug)} como referencia ⟦confirmar precio en Medellín⟧: cámbialo por el que pagas. No incluye el mantenimiento de los filtros.</p>
  </div>
</section>'''

def videos_sec():
    c = "".join(f'<article class="short rv">{yt_box(MODELS[k]["yt"], "Video de " + full(k))}<h3>{full(k)}</h3><a href="{MODELS[k]["file"]}">Ver equipo →</a></article>' for k in ORDER)
    return f'''
<section class="sec dark" id="videos">
  {wayuu("w-dark")}
  <div class="wrap psh-g">
    <div class="rv">{kick("Míralos en acción", True)}<h2 class="h2 lt">{em("La tecnología, [en casas reales.]")}</h2>
      <p class="lead lt">Shorts de Waterdrop Filter y de usuarios. Si aceptas las cookies, se reproducen solos y sin sonido; toca uno para escucharlo.</p>
      <ul class="psh-l lt"><li>Casa real, cocina real</li><li>Así se usan en el día a día</li><li>Agua pura al instante</li></ul></div>
    <div class="sh2">{c}</div>
  </div>
</section>'''

def medellin():
    chips = "".join(f"<span>{z}</span>" for z in C.COMUNAS)
    return f'''
<section class="sec mde" id="medellin">
  <div class="wrap mde-g">
    <div class="rv">{kick("07 · Somos de aquí")}<h2 class="h2">{em("De Medellín,<br>[pa' Medellín.]")}</h2>
      <p class="lead">En la ciudad de la eterna primavera el agua de la red, que distribuye EPM, es potable y de buena calidad. Aun así, el cloro que la mantiene segura se nota en el sabor, y en muchos edificios pasa por tanques donde se pueden acumular sedimentos. Un purificador lo resuelve justo antes de tu vaso.</p>
      <div class="mde-n"><div><b>16</b><span>comunas donde instalamos</span></div><div><b>1</b><span>visita y queda listo</span></div><div><b>$0</b><span>de costo extra por el kit</span></div></div></div>
    <div class="mde-c rv">{checker("mde-zone", lt=False)}<p class="mde-k">Instalamos en todas las comunas</p><div class="chips">{chips}</div>
      <p class="fine">En los corregimientos (Santa Elena, San Antonio de Prado, San Cristóbal, Altavista y Palmitas) lo coordinamos contigo. Por ahora no instalamos fuera de Medellín.</p></div>
  </div>
  {mountains("m-mde")}
</section>'''

FAQ_HOME = [
    ("¿Nasfeco es distribuidor oficial de Waterdrop Filter?", "Sí. Nasfeco es distribuidor oficial de Waterdrop Filter en Colombia. Los equipos que instalamos son originales, con garantía y soporte local."),
    ("¿En qué zonas instalan?", "Hoy instalamos en las 16 comunas de Medellín, y en los corregimientos lo coordinamos contigo. Por ahora no instalamos en otros municipios del valle de Aburrá; si vives en Envigado, Sabaneta, Itagüí o Bello, escríbenos y te avisamos cuando lleguemos."),
    ("¿X12 o Ultrafiltración UF?", "Si quieres la máxima pureza (quitar sarro, metales y sales disueltas), la X12; necesita tomacorriente bajo el lavaplatos. Si el agua te llega bien y lo que buscas es mejor sabor sin gastar luz ni desperdiciar agua, la UF."),
    ("¿Qué incluye el precio?", "El precio es final, en pesos y con IVA del 19 %: el equipo con su llave original, la valoración de tu cocina, la instalación estándar en Medellín, el kit de bienvenida y el seguimiento."),
    ("¿Por qué un purificador si el agua de Medellín es potable?", "El agua de EPM llega potable, pero el cloro se nota en el sabor y en las tuberías y tanques de los edificios se pueden acumular sedimentos. Un purificador quita todo eso justo antes de tu vaso."),
    ("¿Qué revisan antes de instalar?", "El espacio bajo el lavaplatos, la toma de agua, el desagüe, dónde va la llave y, para la X12, el tomacorriente. También si la administración del edificio pide alguna autorización. Cualquier adaptación se acuerda antes."),
    ("¿Cada cuánto se cambian los filtros?", "En la X12, entre 6 y 24 meses según el filtro; en la UF, hasta 12 meses. El equipo te avisa y nosotros te recordamos cuándo toca."),
    ("¿Cómo uso el código de descuento?", "No tienes que hacer nada: el código de la oferta va escrito en tu solicitud de WhatsApp. Vale hasta que termine la cuenta regresiva."),
    ("¿Cuándo y cómo pago?", "Envías tu solicitud por WhatsApp y un asesor te confirma la fecha y las formas de pago ⟦confirmar: Nequi, Daviplata, PSE, transferencia o tarjeta⟧. En esta web no se cobra nada."),
    ("¿Quién responde por la garantía?", f"{C.COMPANY}. La gestionamos aquí en Colombia, conforme al Estatuto del Consumidor (Ley 1480 de 2011): si algo falla, nos escribes y lo resolvemos sin que tengas que tratar con el exterior.")]

def faq_sec(items, title="Preguntas que<br>[nos hacen siempre.]", num="08 · Preguntas"):
    q = "".join(f'<details class="rv"><summary>{x}<i>{ico(I_PLUS, 16, 1.8)}</i></summary><p>{y}</p></details>' for x, y in items)
    return f'''
<section class="sec faq" id="faq">
  <div class="wrap faq-g">
    <div class="faq-l rv">{kick(num)}<h2 class="h2">{em(title)}</h2><p class="lead">¿Te quedó alguna duda? Escríbenos con toda la confianza.</p>{wa_btn("Pregúntanos por WhatsApp", "¡Hola Nasfeco! Tengo una pregunta sobre los purificadores.", "b-green")}</div>
    <div>{q}</div>
  </div>
</section>'''

def faq_ld(items): return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", C.finish(x))}} for q, x in items]}

def closing(k=None):
    return f'''
<section class="close">
  {wayuu("w-dark")}
  <div class="wrap close-c rv">{kick("Tu casa. Tu ritmo.", True, True)}<h2 class="h2 lt">{em("¿Qué más pues?<br>[Chao botellón.]")}</h2>
    <p class="lead lt">Agenda tu valoración y cuadramos contigo tu experiencia Nasfeco, paso a paso.</p>
    <div class="row">{btn("Agenda tu valoración", f'data-book="{k}"' if k else "data-book", "b-gold")}{wa_btn("WhatsApp", "¡Hola Nasfeco! Quiero saber más de la experiencia.", "b-ghost")}</div></div>
  {mountains("m-close")}
</section>'''

def org_ld():
    return {"@type": "LocalBusiness", "@id": SITE + "#negocio", "name": "Nasfeco Colombia", "legalName": C.COMPANY, "url": SITE, "logo": SITE + "assets/brand/nasfeco-colombia.png",
            "image": SITE + "assets/img/kit-bienvenida.webp", "telephone": "§TEL§", "email": "§MAIL§", "priceRange": "$$",
            "description": "Distribuidor oficial de Waterdrop Filter en Colombia. Purificadores de agua X12 y Ultrafiltración UF con valoración, instalación en Medellín, kit de bienvenida y seguimiento.",
            "address": {"@type": "PostalAddress", "addressLocality": "Medellín", "addressRegion": "Antioquia", "addressCountry": "CO"},
            "areaServed": {"@type": "City", "name": "Medellín"}, "sameAs": ["https://nasfecousa.com/"]}

def product_ld(k):
    m = MODELS[k]
    return {"@type": "Product", "name": full(k), "brand": {"@type": "Brand", "name": "Waterdrop"}, "sku": m["specs"][0][1], "description": m["desc"], "image": [SITE + g for g in m["gallery"][:4]],
            "offers": {"@type": "Offer", "url": SITE + m["file"].replace(".html", ""), "priceCurrency": "COP", "price": f"{C.price(k):.0f}", "priceValidUntil": C.PROMO_END,
                       "availability": "https://schema.org/InStock", "areaServed": "Medellín", "seller": {"@id": SITE + "#negocio"}}}

def end(req=None): return footer() + dialogs(req) + "\n</body>\n</html>\n"

# ------------------------------------------------------------------ páginas
def page_home():
    t = "Purificadores de Agua en Medellín | Waterdrop X12 y UF con Instalación · Nasfeco Colombia"
    d = "Chao botellón: purificadores Waterdrop Filter X12 y Ultrafiltración UF instalados en tu casa en Medellín. Valoración, instalación, kit de bienvenida y seguimiento, con IVA incluido."
    ld = {"@context": "https://schema.org", "@graph": [org_ld(), {"@type": "WebSite", "url": SITE, "name": "Nasfeco Colombia", "inLanguage": "es-CO"}, product_ld("x12"), product_ld("uf"), faq_ld(FAQ_HOME)]}
    return (head(t, d, "", ld) + header() + '<main id="main">' + hero_home() + systems() + nuestro() + porque() + kit_sec() + techs() + install_sec() + includes()
            + calc_sec() + videos_sec() + medellin() + faq_sec(FAQ_HOME) + closing() + "</main>" + end())

def pdh(k):
    m = MODELS[k]
    return f'''
<section class="pdh" id="top" data-pdp="{k}">
  {wayuu("w-hero")}
  <div class="pdh-big" aria-hidden="true">{m["name"].split()[-1]}</div>
  <div class="wrap pdh-g">
    <div><p class="crumb"><a href="index.html">Inicio</a> / <a href="index.html#equipos">Equipos</a> / {m["name"]}</p>
      {kick(m["kick"], True)}<h1 class="h1">{em(m["h1"])}</h1>
      <div class="chips lt">{"".join(f"<span>{c}</span>" for c in m["chips"])}</div>
      <div class="row">{btn("Agenda tu valoración", f'data-book="{k}"', "b-gold")}{wa_btn("WhatsApp", f"¡Hola Nasfeco! Me interesa el {full(k)}.", "b-ghost")}</div>
      <p class="from">Desde <b data-price="{k}"></b> · IVA, instalación en Medellín y kit de bienvenida incluidos</p></div>
    <div class="pdh-img"><img src="{a(m["photo"])}" alt="{full(k)}" fetchpriority="high" width="640" height="640">{seal()}</div>
  </div>
  {mountains("m-hero")}
</section>''' + ribbon(RIBBON)

def pdp(k):
    m = MODELS[k]
    th = "".join(f'<button type="button" class="{"on" if i == 0 else ""}" data-photo="{a(g)}" aria-label="Foto {i+1}"><img src="{g}" alt="" loading="lazy"></button>' for i, g in enumerate(m["gallery"]))
    inc = [(I_HOME, "Valoración de tu cocina"), (I_TOOL, "Instalación en Medellín"), (I_GIFT, "Kit de bienvenida Nasfeco"), (I_CHAT, "Seguimiento y garantía local")]
    req = f'<button type="button" class="req-btn" data-req-open>{ico("M10.3 3.9L1.8 18.2A2 2 0 003.5 21h17a2 2 0 001.7-2.8L13.7 3.9a2 2 0 00-3.4 0zM12 9v4M12 17h.01", 20, 2)}<span>Revisar antes de comprar</span><em>Importante</em></button>'
    sub = [("#fotos", "Fotos"), ("#video", "Video"), ("#resumen", "Lo que hace"), ("#instalacion", "Instalación"), ("#ficha", "Ficha técnica"), ("#faq", "Preguntas")]
    return f'''
<nav class="sub" aria-label="{m["name"]}"><div class="wrap sub-in"><b>{full(k)}</b>{"".join(f'<a href="{h}">{t}</a>' for h, t in sub)}<button type="button" class="hd-cta" data-book="{k}">Agendar <i>{ico(I_ARR, 14, 1.9)}</i></button></div></nav>
<section class="sec" id="fotos">
  <div class="wrap pdp-g">
    <div><div class="pdp-photo"><img id="pdp-photo" src="{m["gallery"][0]}" alt="{full(k)}"></div><div class="pdp-ths">{th}</div></div>
    <div class="pdp-i">{kick("Fotos y precio")}<h2>{em(m["h1"])}</h2><p class="pdp-d">{m["desc"]}</p>
      <div class="pz">
        <div data-promo-on><p class="pz-tag"><span data-promo-name></span> · código <code data-code="{k}"></code></p><div class="pz-row"><b data-price="{k}"></b><s data-was="{k}"></s><span class="pz-save">Ahorras <span data-save="{k}"></span></span></div>
          <p class="pz-cd">La oferta termina en <i data-cd>…</i></p></div>
        <div data-promo-off hidden><div class="pz-row"><b data-price="{k}"></b></div></div>
        <p class="pz-inc">Pesos colombianos · IVA incluido · equipo + valoración + instalación en Medellín + kit de bienvenida + seguimiento</p>
      </div>
      <div class="row">{btn("Agenda tu valoración", f'data-book="{k}"', "b-gold")}{wa_btn("WhatsApp", f"¡Hola Nasfeco! Me interesa el {full(k)}.", "b-line")}</div>
      {req}
      <ul class="pdp-inc">{"".join(f"<li><i>{ico(i, 18, 1.6)}</i>{t}</li>" for i, t in inc)}</ul>
    </div>
  </div>
</section>'''

def pshort(k):
    m = MODELS[k]
    return f'''
<section class="sec dark" id="video">
  {wayuu("w-dark")}
  <div class="wrap psh-g">
    <div class="rv">{kick("Míralo", True)}<h2 class="h2 lt">{em(f"{m['art'].capitalize()} {m['name']}, [en segundos.]")}</h2>
      <p class="lead lt">Un short de una casa real, para que veas el equipo funcionando antes de tu valoración. En Medellín lo instalan los técnicos de Nasfeco.</p>
      <ul class="psh-l lt"><li>Casa real, cocina real</li><li>Así se usa en el día a día</li><li>Agua pura al instante</li></ul>{btn("Agenda tu valoración", f'data-book="{k}"', "b-gold")}</div>
    <div class="sh2 one"><article class="short rv">{yt_box(m["yt"], "Video de " + full(k))}</article></div>
  </div>
</section>'''

def features(k):
    m = MODELS[k]
    c = "".join(f'<article class="fc rv"><div class="fc-m">{media(s, t)}</div><div class="fc-t"><h3>{t}</h3><p>{d}</p></div></article>' for s, t, d in m["feats"])
    return f'''
<section class="sec" id="resumen"><div class="wrap">
  <div class="sec-h rv">{kick("Lo que hace")}<h2 class="h2">{em(f"Todo lo que hace {m['art']} {m['name']}, [sin pedirte nada.]")}</h2></div>
  <div class="feat-g">{c}</div>
  <p class="fine">Imágenes y videos oficiales de Waterdrop Filter.</p></div></section>'''

def specs(k):
    m = MODELS[k]
    return f'''
<section class="sec stone" id="ficha"><div class="wrap spx-g">
  <div class="rv">{kick("Ficha técnica")}<h2 class="h2">{em("Los detalles, [claros.]")}</h2><div class="spx-img"><img src="{a(m["spec_img"])}" alt="Medidas del {full(k)}" loading="lazy"></div></div>
  <dl class="spx-l rv">{"".join(f"<div><dt>{x}</dt><dd>{y}</dd></div>" for x, y in m["specs"])}</dl>
</div></section>'''

def other(k):
    o = "uf" if k == "x12" else "x12"; m = MODELS[o]
    return f'''
<section class="sec"><div class="wrap">
  <a class="oth1 rv" href="{m["file"]}"><img src="{a(m["photo"])}" alt="" loading="lazy"><div>{kick("Conoce también")}<h3>{full(o)}</h3><p>{m["card"]}</p><p class="price"><b data-price="{o}"></b><s data-was="{o}"></s></p></div><span class="go">{ico(I_ARR, 20, 1.9)}</span></a>
  <div class="row" style="justify-content:center;margin-top:20px"><button type="button" class="btn b-line" data-compare><span>Comparar los dos</span></button><button type="button" class="btn b-line" data-quiz><span>¿Cuál es para mí?</span></button></div>
</div></section>'''

def page_product(k):
    m = MODELS[k]
    t = f"{full(k)} en Medellín | Purificador con Instalación · Nasfeco Colombia"
    d = f"{full(k)} en Medellín: {m['card']} Precio en pesos con IVA, instalación, kit de bienvenida y seguimiento de Nasfeco."
    items = m["faq"] + [("¿El precio incluye la instalación?", "Sí. Es el precio final en pesos: incluye IVA, la valoración, la instalación estándar en Medellín, el kit de bienvenida y el seguimiento."),
                        ("¿Quién responde por la garantía?", f"{C.COMPANY}, distribuidor oficial de Waterdrop Filter en Colombia, conforme al Estatuto del Consumidor (Ley 1480 de 2011).")]
    ld = {"@context": "https://schema.org", "@graph": [org_ld(), product_ld(k), {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE},
          {"@type": "ListItem", "position": 2, "name": full(k), "item": SITE + m["file"].replace(".html", "")}]}, faq_ld(items)]}
    body = pdh(k) + pdp(k) + pshort(k) + features(k) + kit_sec("Tu bienvenida") + install_sec(k, "Así instalamos") + includes(k) + specs(k) + other(k) + faq_sec(items, num="Preguntas") + closing(k)
    return head(t, d, m["file"].replace(".html", ""), ld, m["photo"]) + header() + '<main id="main">' + body + "</main>" + end((m["req"], full(k)))

def page_legal():
    ck = [("Almacenamiento imprescindible", "<p>Guardamos tu elección sobre cookies en tu navegador (localStorage, clave <code>nf-consent</code>) para no volver a preguntarte. Es necesaria para respetar tu decisión y no se comparte con nadie.</p>"),
          ("Cookies de terceros: YouTube y Google Ads", "<p><b>YouTube.</b> Los videos son Shorts de YouTube insertados en modo de privacidad mejorada (youtube-nocookie.com). Aun así, YouTube (Google LLC) puede colocar cookies cuando un video se reproduce. Por eso solo se cargan si aceptas; hasta entonces ves una imagen fija guardada en nuestra web.</p><p><b>Google Ads.</b> Si activamos la medición de anuncios y aceptas, cargamos la etiqueta de Google Ads (Google LLC), que coloca cookies para saber si nuestros anuncios funcionan. Si rechazas, no se carga.</p>"),
          ("Sin analítica ni otros rastreadores", "<p>No usamos herramientas de analítica, píxeles de redes sociales ni otras cookies de publicidad. Las tipografías se sirven desde nuestra propia web.</p>"),
          ("Cómo cambiar tu elección", '<p>Puedes aceptar o rechazar cuando quieras: <button type="button" class="ul" data-cookie-settings>abrir la configuración de cookies</button>. También puedes borrar los datos guardados desde la configuración de tu navegador.</p>')]
    dp = [("Responsable del tratamiento", f"<p><b>{C.COMPANY}</b>, NIT {C.NIT}, con domicilio en {C.ADDRESS}, Medellín, Colombia. Correo: §MAIL§ · WhatsApp: §TEL§.</p>"),
          ("Marco legal", "<p>Esta política cumple la Ley Estatutaria 1581 de 2012 de protección de datos personales y el Decreto 1377 de 2013 (compilado en el Decreto 1074 de 2015). La autoridad de control en Colombia es la Superintendencia de Industria y Comercio (SIC).</p>"),
          ("Qué datos tratamos", "<p>Los que tú nos das al armar tu solicitud de valoración o al escribirnos por WhatsApp: nombre, celular, correo, comuna y barrio, tipo de vivienda y la información que quieras contarnos. Si compras, también los necesarios para la instalación, la factura y la garantía. No pedimos datos sensibles ni datos de niñas, niños o adolescentes.</p>"),
          ("Para qué los usamos", "<ul><li>Responder tus solicitudes de valoración o asesoría.</li><li>Gestionar tu compra: disponibilidad, pago, instalación, factura electrónica y garantía.</li><li>Darte soporte técnico y recordarte el mantenimiento de tu equipo.</li><li>Cumplir obligaciones legales, contables y tributarias.</li><li>Enviarte información sobre productos y promociones de Nasfeco, solo si nos autorizas y hasta que nos pidas parar.</li></ul>"),
          ("Con quién los compartimos", "<p>No vendemos tus datos. Los compartimos solo con proveedores que nos ayudan a prestar el servicio y actúan por nuestra cuenta (encargados): la herramienta que recibe las solicitudes de la web (n8n), WhatsApp (Meta Platforms) para la conversación con nuestros asesores y, si aceptaste las cookies de publicidad, Google. Algunos guardan la información en servidores fuera de Colombia; les exigimos niveles adecuados de protección.</p>"),
          ("Tus derechos como titular", "<p>Según el artículo 8 de la Ley 1581 de 2012 tienes derecho a <b>conocer, actualizar y rectificar</b> tus datos; pedir prueba de la autorización; saber qué uso les hemos dado; <b>revocar la autorización y/o pedir que los suprimamos</b> cuando no haya un deber legal o contractual de conservarlos; acceder a ellos gratis; y presentar quejas ante la Superintendencia de Industria y Comercio.</p>"),
          ("Cómo hacer consultas y reclamos", "<p>Escríbenos a §MAIL§ o por WhatsApp al §TEL§ con tu nombre, tu documento de identidad, lo que pides y un dato de contacto. Las <b>consultas</b> se responden en máximo diez (10) días hábiles, prorrogables cinco (5) más si te avisamos el motivo. Los <b>reclamos</b> (corrección, actualización, supresión o revocatoria) se resuelven en máximo quince (15) días hábiles, prorrogables ocho (8) más. Antes de acudir a la SIC debes haber presentado tu consulta o reclamo ante nosotros.</p>"),
          ("Autorización y vigencia", "<p>Al marcar la casilla de autorización en la solicitud de valoración o al escribirnos por WhatsApp, nos autorizas a tratar tus datos para las finalidades anteriores. Los conservamos mientras sean necesarios para esas finalidades y para cumplir la ley. Esta política rige desde el 18 de octubre de 2026; si la cambiamos de forma importante, lo publicaremos aquí.</p>")]
    sec = lambda xs: "".join(f'<h2><i>0{n+1}</i>{h}</h2>{t_}' for n, (h, t_) in enumerate(xs))
    t = "Política de Cookies y Tratamiento de Datos Personales | Nasfeco Colombia"
    d = f"Política de cookies y de tratamiento de datos personales de {C.COMPANY} (Ley 1581 de 2012): qué guardamos, para qué usamos tus datos y cómo ejercer tus derechos."
    body = f'''<main id="main" class="lg"><div class="wrap lg-g">
  <aside class="lg-a"><p class="crumb"><a href="index.html">Inicio</a> / Legal</p><h1 class="h2">{em("Cookies y [datos personales]")}</h1><p class="fine">Última actualización: 18 de octubre de 2026</p>
    <p class="fine"><a class="ul" href="#datos-personales">Ir a tratamiento de datos personales</a></p></aside>
  <div class="lg-b">{sec(ck)}
    <h3 id="datos-personales">Política de tratamiento de datos personales</h3><p class="fine">Cómo {C.COMPANY} recolecta, usa y protege tus datos, y cómo puedes ejercer tus derechos. <span class="todo">⟦revisar con un abogado antes de publicar⟧</span></p>
    {sec(dp)}</div>
</div></main>'''
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": "Política de cookies y tratamiento de datos personales", "url": SITE + "politica-cookies"}
    return head(t, d, "politica-cookies", ld) + header(solid=True) + body + end()

# ------------------------------------------------------------------ escribir
if __name__ == "__main__":
    C.write("index.html", page_home())
    for k in ORDER: C.write(MODELS[k]["file"], page_product(k))
    C.write("politica-cookies.html", page_legal())
    # páginas que ya no existen en esta versión (solo X12 y UF, solo Medellín, sin Empresas)
    for old in ["product-g5p700a.html", "product-g2p600.html", "product-smart.html", "nasfeco.html"] + [f"purificadores-agua-{c}.html" for c in ("bogota", "medellin", "cali", "barranquilla")]:
        p = os.path.join(ROOT, old)
        if os.path.exists(p): os.remove(p); print("borrada", old)
