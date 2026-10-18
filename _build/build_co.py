# -*- coding: utf-8 -*-
"""NASFECO COLOMBIA · genera toda la web (estructura inspirada en nasfecousa.com, con colores del logo NASFECO COLOMBIA).

Uso:  python _build/build_co.py   (y después  python _build/build_seo.py)
Escribe: index.html (Waterdrop Hogar), product-x12/g5p700a/g2p600/uf/smart.html, nasfeco.html (Empresas),
purificadores-agua-bogota/medellin/cali/barranquilla.html y politica-cookies.html.

Datos de la empresa: _build/co.py · WhatsApp, precios, códigos y oferta: js/co.js (objeto WD).
Marcadores: §WA§ §TEL§ §MAIL§ y ⟦pendiente⟧ (ver co.py → finish)."""
import os, re, json, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import co as C
from nf_wow import DAY as NF_DAY, JS as NF_JS

ROOT, SITE, V = C.ROOT, C.SITE, C.VER
WA_PATH = re.sub(r'^<path d="|"$', "", open(os.path.join(HERE, "wa_path.txt"), encoding="utf-8").read().strip())

def a(path):
    """Ruta a un recurso; falla si no existe (así no se publica una imagen rota)."""
    if not os.path.exists(os.path.join(ROOT, path)): raise FileNotFoundError(path)
    return path

def ico(d, w=20, sw=1.6):
    return f'<svg viewBox="0 0 24 24" width="{w}" height="{w}" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{d}"/></svg>'
I_ARR = "M7 17L17 7M9 7h8v8"; I_RIGHT = "M5 12h14M13 6l6 6-6 6"; I_X = "M6 6l12 12M18 6L6 18"; I_MENU = "M4 8h16M4 16h16"; I_PLUS = "M12 5v14M5 12h14"
I_UP = "M12 19V5M6 11l6-6 6 6"; I_CHAT = "M4 5h16v11H9l-5 4z"; I_HOME = "M3 11l9-7 9 7v9H3zM9 20v-6h6v6"
I_TOOL = "M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.8-3.8a6 6 0 01-7.9 7.9l-6.9 6.9a2.1 2.1 0 01-3-3l6.9-6.9a6 6 0 017.9-7.9z"
I_SHIELD = "M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6zM8.5 12l2.5 2.5 4.5-5"
I_GIFT = "M4 11h16v10H4zM2 7h20v4H2zM12 7v14M12 7c-1.5-3-5-3.5-5-1s3 1 5 1zm0 0c1.5-3 5-3.5 5-1s-3 1-5 1z"
I_SPARK = "M12 3l1.8 5.4L19 10l-5.2 1.6L12 17l-1.8-5.4L5 10l5.2-1.6z"; I_CHECK = "M5 12l5 5 9-10"; I_TAG = "M3 12V4h8l10 10-8 8zM7.5 7.5h.01"
I_PIN = "M12 22s7-6.2 7-12a7 7 0 10-14 0c0 5.8 7 12 7 12zM12 12.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"; I_MAIL = "M4 5h16v14H4zM4 6l8 7 8-7"
I_SUN = "M12 17a5 5 0 100-10 5 5 0 000 10zM12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"
I_DROP = "M12 3s7 7.5 7 12a7 7 0 01-14 0c0-4.5 7-12 7-12z"; I_DOC = "M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8zM14 2v6h6"
WA = f'<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="{WA_PATH}"/></svg>'

def em(t): return t.replace("[", "<em>").replace("]", "</em>")
def kick(text, lt=False, c=False): return f'<p class="kick{" lt" if lt else ""}{" c" if c else ""}">{text}</p>'
def btn(text, attrs="", cls="b-gold", href=None, icon=I_ARR):
    inner = f'<span>{text}</span><i>{ico(icon, 15, 1.9)}</i>'
    return f'<a class="btn {cls}" href="{href}" {attrs}>{inner}</a>' if href else f'<button type="button" class="btn {cls}" {attrs}>{inner}</button>'
def wa_btn(text, msg, cls="b-wa"): return f'<a class="btn {cls}" href="{C.wa(msg)}" target="_blank" rel="noopener"><span>{text}</span><i>{WA}</i></a>'

# ------------------------------------------------------------------ logo NASFECO COLOMBIA (SVG, a partir del logo de la marca)
MARK = '<path d="M6 4H27L95 50H73L27 19V73L6 87Z" fill="{g}"/><path d="M6 96C42 92 72 76 95 50H73C58 64 36 76 6 80Z" fill="{o}"/>'
def logo(kind="c", h=40, cls=""):
    g, o, t = ("#0B4F3E", "#A07A33", "#0B4F3E") if kind == "c" else ("#FFFFFF", "#C9A04E", "#FFFFFF")
    return (f'<svg class="logo {cls}" viewBox="0 0 400 100" width="{h * 4}" height="{h}" role="img" aria-label="NASFECO Colombia">{MARK.format(g=g, o=o)}'
            f'<text x="114" y="66" font-family="Montserrat,Arial,sans-serif" font-weight="700" font-size="60" fill="{t}" textLength="280" lengthAdjust="spacingAndGlyphs">NASFECO</text>'
            f'<text x="118" y="94" font-family="Montserrat,Arial,sans-serif" font-weight="600" font-size="19" fill="{o}" textLength="272" lengthAdjust="spacing">COLOMBIA</text></svg>')
def mark(w=34, kind="w"):
    g, o = ("#FFFFFF", "#C9A04E") if kind == "w" else ("#0B4F3E", "#A07A33")
    return f'<svg viewBox="0 0 100 100" width="{w}" height="{w}" aria-hidden="true">{MARK.format(g=g, o=o)}</svg>'

# ------------------------------------------------------------------ los 5 equipos
X, G5, G2, UF, ED = "assets/x12/", "assets/g5/", "assets/g2/", "assets/uf/", "assets/ed01/"
def vid(path, cls=""):
    return f'<video class="{cls}" muted playsinline loop preload="none" data-auto poster="{a(path + "-poster.jpg")}"><source src="{a(path + ".mp4")}" type="video/mp4"></video>'
def media(src, alt=""):
    return vid(src[:-4]) if src.endswith(".mp4") else f'<img src="{a(src)}" alt="{alt}" loading="lazy">'

MODELS = {
  "x12": dict(name="X12", gpd="1200 GPD", tag="El más completo", file="product-x12.html", install=True, power=True, art="la",
    photo=X + "ui-wd-x12-new-vis-pr-logo.webp", yt="26BQXx1PgIE", req="assets/req/requisitos-instalacion.jpg",
    card="11 etapas, minerales alcalinos y llave inteligente. Máxima pureza y caudal para familias de 3 a 6 personas.",
    kick="Serie X · Ósmosis inversa sin tanque", h1="Waterdrop [X12]",
    desc="El equilibrio perfecto para la mayoría de familias: agua pura al instante, minerales alcalinos y una llave inteligente que te muestra cómo está tu agua. Valorada, instalada y acompañada por Nasfeco.",
    chips=["1200 GPD", "11 etapas", "3:1", "pH 7.5", "NSF/ANSI 42 · 58 · 372"],
    gallery=[X + f for f in ["ui-wd-x12-main-sello.webp", "ui-wd-x12-b-new-vis-main.webp", "ui-wd-x12-new-vis-pr-logo-white.jpg", "WD_X12_new.webp", "1226-WD-_1016-1200g__2.jpg", "1226-WD-_1016-1200g__3.jpg", "X12_3.jpg", "X12_4.jpg", "1226-WD-_1016-1200g__7.jpg", "X12_8.jpg", "X12-NSF_ANTI-4258372.jpg"]],
    feats=[("assets/clips/x12-tds.mp4", "Una llave que te informa", "Muestra el TDS de tu agua en tiempo real y te avisa cuándo toca cambiar cada filtro."),
           ("assets/clips/x12-pour.mp4", "Una taza en unos 3 segundos", "Sin tanque que llenar: el agua pasa por los filtros directo a tu vaso, con 1200 galones por día."),
           (X + "7f24c79c8deb40ad8173c66aa62464a8.mp4", "Con minerales alcalinos", "Después de purificar, le devuelve calcio y magnesio al agua y la deja con un pH cercano a 7.5."),
           ("assets/x16/38fc560a5a7b46c2b2d5d6b2549e4ceb.mp4", "11 etapas de filtración", "Membrana de ósmosis inversa de 0.0001 μm y protección LED: reduce TDS, cloro, flúor, plomo, PFOA, PFOS y más."),
           ("assets/clips/x12-cabinet.mp4", "Tu mueble, de vuelta", "Delgado y de pie, sin tanque: libera hasta un 70 % del espacio bajo el lavaplatos."),
           ("assets/clips/x12-inside.mp4", "Filtros en segundos", "Tres filtros que se giran y se cambian sin herramientas ni goteos.")],
    specs=[("Modelo", "WD-X12"), ("Capacidad nominal", "1200 GPD"), ("Agua pura / desagüe", "3:1"), ("Filtración", "11 etapas · membrana de 0.0001 μm"), ("Remineralización", "Minerales alcalinos · pH 7.5±"),
           ("Llave", "Inteligente: TDS, volumen programable y aviso de filtros"), ("Certificación", "NSF/ANSI 42, 58 y 372"), ("Medidas", "46 × 16 × 42 cm"), ("Peso", "17.7 kg"),
           ("Electricidad", "Tomacorriente bajo el lavaplatos"), ("Vida de los filtros", "F1A 12 meses · F2 6 meses · X12-F3 24 meses, según el uso")],
    spec_img=X + "X12-Spec.jpg",
    cmp=["Ósmosis inversa + remineralización", "1200 GPD", "11 etapas · 0.0001 μm", "Sí, tomacorriente", "Bajo el lavaplatos, sin tanque", "Familias de 3 a 6 personas"],
    faq=[("¿Por qué la X12 es la más recomendada?", "Tiene caudal suficiente para una familia de 3 a 6 personas, 11 etapas de filtración, minerales alcalinos y una llave con volumen programable."),
         ("¿Necesita electricidad?", "Sí: un tomacorriente bajo el lavaplatos para la bomba sin tanque, la llave inteligente y la protección LED. Si no lo tienes, lo revisamos en la valoración."),
         ("¿Quita los minerales del agua?", "La ósmosis inversa retiene casi todo, pero la X12 tiene una etapa que le devuelve calcio y magnesio y deja el pH alrededor de 7.5."),
         ("¿Cada cuánto se cambian los filtros?", "F2 cada 6 meses, F1A cada 12 meses y X12-F3 cada 24 meses, según el uso. La llave te avisa y nosotros te recordamos cuándo toca."),
         ("¿Puedo usar mi propia llave?", "No. La llave de la X12 es parte del sistema: tiene el monitor de calidad, la protección LED y el aviso de cambio de filtros.")]),
  "g5": dict(name="G5P700A", gpd="700 GPD", tag="Alcalino", file="product-g5p700a.html", install=True, power=True, art="el",
    photo=G5 + "ui-wd-g5p700a-product.webp", yt="TrO42mLP9z0", req="assets/req/requisitos-instalacion.jpg",
    card="Ósmosis inversa con minerales alcalinos en un equipo compacto. Agua pura y equilibrada para toda la familia.",
    kick="Serie G5 · Ósmosis inversa alcalina", h1="Waterdrop [G5P700A]",
    desc="700 galones por día, 8 etapas y minerales alcalinos en un equipo compacto y sin tanque. Agua pura y con mejor sabor, con la valoración, la instalación y el seguimiento de Nasfeco.",
    chips=["700 GPD", "8 etapas", "2:1", "Alcalina", "NSF/ANSI 58 · 372"],
    gallery=[G5 + "ui-wd-g5p700a-product.webp"] + [G5 + f"wd-g5p700a-product_{n}.jpg" for n in (2, 3, 1, 4, 5, 6, 7, 9)] + [G5 + "ui-wd-g5p700a-nsf-vis.jpg", G5 + "ui-wd-g5p700a-w.jpg"],
    feats=[(G5 + "wd-g5p700a-product_3.jpg", "Agua con minerales alcalinos", "Después de purificar, le devuelve minerales al agua para un sabor suave y un pH equilibrado."),
           (G5 + "wd-g5p700a-product_2.jpg", "8 etapas de filtración", "Membrana de 0.0001 μm que reduce PFOA, PFOS, cloro, plomo, flúor, metales pesados y sales disueltas."),
           (G5 + "wd-g5p700a-product_4.jpg", "Llave con pantalla", "Muestra el TDS en tiempo real y te avisa cuándo cambiar los filtros."),
           (G5 + "wd-g5p700a-product_6.jpg", "Compacto y sin tanque", "Ocupa hasta un 70 % menos espacio bajo el lavaplatos y evita el agua estancada."),
           (G5 + "wd-product-g5p700a-img10.jpg", "Menos conexiones", "Solo 3 puntos de conexión frente a los 26 de un purificador tradicional: menos riesgo de fugas."),
           (G5 + "wd-product-g5p700a-img11.jpg", "Protección contra fugas", "Aviso de fugas, alerta de fallas y cierre automático del agua.")],
    specs=[("Modelo", "G5P700A"), ("Capacidad nominal", "700 GPD"), ("Agua pura / desagüe", "2:1"), ("Filtración", "8 etapas · membrana de 0.0001 μm"), ("Remineralización", "Minerales alcalinos"),
           ("Llave", "Con pantalla TDS"), ("Certificación", "NSF/ANSI 58 y 372 (IAPMO)"), ("Medidas", "42 × 14 × 35 cm"), ("Peso", "11.8 kg"),
           ("Electricidad", "Tomacorriente bajo el lavaplatos"), ("Vida de los filtros", "G5P700A-CF 6 meses · G5P700-RO 24 meses, según el uso")],
    spec_img=G5 + "ui-wd-g5p700a-spec.jpg",
    cmp=["Ósmosis inversa + minerales alcalinos", "700 GPD", "8 etapas · 0.0001 μm", "Sí, tomacorriente", "Bajo el lavaplatos, sin tanque", "Agua alcalina a mejor precio"],
    faq=[("¿Qué diferencia hay con la X12?", "La X12 tiene más caudal (1200 GPD), 11 etapas y llave con volumen programable. El G5P700A ofrece ósmosis inversa con minerales alcalinos en un equipo más compacto y a mejor precio."),
         ("¿Reduce PFOA y PFOS?", "Sí. Sus 8 etapas con membrana de ósmosis inversa reducen PFOA, PFOS, cloro, plomo, flúor y metales pesados."),
         ("¿Necesita electricidad?", "Sí, un tomacorriente bajo el lavaplatos. Si no lo tienes, lo revisamos en la valoración."),
         ("¿Cada cuánto se cambian los filtros?", "El filtro CF cada 6 meses y el RO cada 24 meses, según el uso. El equipo te avisa y nosotros te recordamos cuándo toca.")]),
  "g2": dict(name="G2P600", gpd="600 GPD", tag="Mejor precio", file="product-g2p600.html", install=True, power=True, art="el",
    photo=G2 + "WD-G2P600-W-NSF.webp", yt="8OztpiA46eg", req="assets/req/requisitos-instalacion.jpg",
    card="La forma más accesible de tener ósmosis inversa sin tanque en casa: 7 etapas y relación 2:1.",
    kick="Serie G · Ósmosis inversa al mejor precio", h1="Waterdrop [G2P600]",
    desc="600 galones por día, 7 etapas de filtración y relación 2:1 en un equipo compacto y sin tanque. La ósmosis inversa más accesible, con todo el servicio Nasfeco.",
    chips=["600 GPD", "7 etapas", "2:1", "Sin tanque", "NSF/ANSI 372"],
    gallery=[G2 + "WD-G2P600-W-NSF.webp"] + [G2 + f"ui-wd-g2p600-product-new-vis_{n}.jpg" for n in (5, 6, 1, 4, 7, 2, 3)] + [G2 + "ui-wd-g2p600-w-cz-no.png"],
    feats=[(G2 + "g2-video.mp4", "Así funciona el G2P600", "Un vaso de agua pura en unos 8 segundos, filtros que se cambian girando y un diseño sin tanque."),
           (G2 + "wd-product-g2p600-vis-img1.jpg", "7 etapas de filtración", "Algodón PP, carbón activado, microfiltración y membrana de ósmosis inversa de 0.0001 μm."),
           (G2 + "ui-wd-g2p600-product-new-vis_5.jpg", "Flujo rápido", "Llena un vaso más rápido que un purificador tradicional de 400 GPD."),
           (G2 + "ui-wd-g2p600-product-new-vis_7.jpg", "Instalación en una visita", "Sin obras: los técnicos de Nasfeco lo dejan funcionando y te enseñan a usarlo."),
           (G2 + "wd-product-g2p600-vis-img16.jpg", "Desperdicia mucho menos agua", "Relación 2:1: por cada litro que va al desagüe, entrega 2 litros de agua pura."),
           (G2 + "wd-product-g2p600-vis-img18.jpg", "Probado por SGS y CSA", "Según las normas NSF/ANSI 42, 53, 58 y 401. Materiales certificados NSF/ANSI 372.")],
    specs=[("Modelo", "WD-G2P600-W"), ("Capacidad nominal", "600 GPD"), ("Agua pura / desagüe", "2:1"), ("Filtración", "7 etapas · membrana de 0.0001 μm"),
           ("Certificación", "NSF/ANSI 372"), ("Pruebas", "SGS y CSA según NSF/ANSI 42, 53, 58 y 401"), ("Instalación", "Bajo el lavaplatos, sin tanque"),
           ("Electricidad", "Tomacorriente bajo el lavaplatos"), ("Vida de los filtros", "G2CF 12 meses · G2P6MRO 24 meses, según el uso")],
    spec_img=G2 + "ui-wd-g2p600-w-cz-no.png",
    cmp=["Ósmosis inversa", "600 GPD", "7 etapas · 0.0001 μm", "Sí, tomacorriente", "Bajo el lavaplatos, sin tanque", "Hogares de 1 a 3 personas"],
    faq=[("¿Qué diferencia hay con el G5P700A?", "El G5P700A tiene más caudal (700 GPD), 8 etapas y minerales alcalinos. El G2P600 es la ósmosis inversa sin tanque más accesible: 600 GPD y 7 etapas."),
         ("¿Qué contaminantes reduce?", "Su membrana de 0.0001 μm reduce TDS, PFOA, PFOS, plomo, cloro, flúor, arsénico, cromo VI, nitratos y sedimentos, entre otros."),
         ("¿Necesita electricidad?", "Sí, un tomacorriente bajo el lavaplatos."),
         ("¿Cada cuánto se cambian los filtros?", "El filtro CF hasta 12 meses y el MRO hasta 24 meses, según el uso. Te recordamos cuándo toca.")]),
  "uf": dict(name="Ultrafiltración UF", gpd="0.01 μm", tag="Sin electricidad", file="product-uf.html", install=True, power=False, art="la",
    photo=UF + "10UB-UF-NSF.png", yt="tL_2gSpSn20", req="assets/req/requisitos-instalacion-uf.jpg",
    card="Agua limpia que conserva sus minerales, sin gastar luz y sin desperdiciar agua. Llave de acero inoxidable incluida.",
    kick="Bajo el lavaplatos · Sin electricidad", h1="Waterdrop [Ultrafiltración UF]",
    desc="Agua limpia que conserva sus minerales naturales. Sin electricidad, sin desperdicio de agua y con llave de acero inoxidable incluida. Ideal si el agua de tu ciudad llega en buen estado.",
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
    cmp=["Membrana de ultrafiltración", "2.8 L/min", "0.01 μm · conserva minerales", "No", "Bajo el lavaplatos", "Agua de red en buen estado"],
    faq=[("¿La UF necesita electricidad?", "No. Funciona con la presión de agua de tu casa, así que no gasta luz y sigue funcionando aunque se vaya la energía."),
         ("¿Cuál es la diferencia con la ósmosis inversa?", "La UF retiene bacterias, óxido y sedimentos y conserva los minerales, pero no reduce las sales disueltas (TDS). Si tu agua tiene mucho sarro, te recomendamos la X12 o el G5P700A."),
         ("¿Cada cuánto se cambia el filtro?", "Hasta 12 meses u 8000 galones, según tu consumo. El indicador te avisa con luz.")]),
  "smart": dict(name="Dispensador ED01", gpd="Agua en 1 s", tag="Sin instalación", file="product-smart.html", install=False, power=False, art="el",
    photo=ED + "1_33c5e044-eb97-4485-ae99-684bc658886e.webp", yt="Nm090TXf6oM", req=None,
    card="Sobre la mesa, sin técnicos ni obras: lo llenas, lo cargas y tienes agua filtrada en 1 segundo. Ideal para arriendo.",
    kick="Sobre la mesa · Sin instalación", h1="Waterdrop [Dispensador ED01]",
    desc="Agua filtrada en 1 segundo, donde la necesites. Sin tuberías ni técnicos: lo llenas con agua de la llave, tocas el botón y sirves. Perfecto para apartamentos, oficinas y arriendos.",
    chips=["Agua en 1 s", "5 μm", "30+ contaminantes", "Portátil", "NSF/ANSI 42 · 372"],
    gallery=[ED + f for f in ["1_33c5e044-eb97-4485-ae99-684bc658886e.webp", "319IZ2UmO8L.jpg", "41Au5hMvngL.jpg", "51ii-WXfo8L.jpg", "White-AlkalineAlkaline-02.jpg", "White-AlkalineAlkaline-08.jpg", "White-AlkalineAlkaline-09.jpg"]],
    feats=None, detail=[ED + f"wd-product-countertop-electric-water-pitcher-ed01a-pc-img{n}.jpg" for n in (3, 10, 11, 6, 7, 8, 9)],
    specs=[("Modelo", "WD-ED01A"), ("Caudal", "Hasta 0.8 L/min"), ("Capacidad", "15 tazas"), ("Filtración", "5 μm · más de 30 contaminantes"), ("Certificación", "NSF/ANSI 42 y 372"),
           ("Vida del filtro", "WD-EDF 3 meses o 200 galones"), ("Medidas", "18 × 25 × 26 cm"), ("Instalación", "No necesita"), ("Alimentación", "Batería recargable")],
    spec_img=None,
    cmp=["Filtración eléctrica de alta densidad", "Hasta 0.8 L/min", "5 μm · 30+ contaminantes", "Batería recargable", "Ninguna: sobre la mesa", "Apartamentos, oficinas y arriendos"],
    faq=[("¿Necesita instalación?", "No. Solo llénalo con agua de la llave, cárgalo y úsalo. Es ideal si vives en arriendo o no quieres modificar tu cocina."),
         ("¿Reduce el TDS (sales disueltas)?", "No. El ED01 reduce cloro, plomo, PFAS, microplásticos y más de 30 contaminantes, pero no reduce el TDS. Para eso te recomendamos la ósmosis inversa."),
         ("¿Lo envían a toda Colombia?", "Sí. Como no necesita técnico, lo enviamos a cualquier ciudad. El costo del envío se confirma por WhatsApp con tu pedido."),
         ("¿Cada cuánto se cambia el filtro?", "Cada filtro WD-EDF dura hasta 3 meses o 200 galones. El indicador te avisa cuándo cambiarlo.")]),
}
ORDER = ["x12", "g5", "g2", "uf", "smart"]
INSTALLED = [k for k in ORDER if MODELS[k]["install"]]
def full(k): return C.WD["products"][k]["name"]

# ------------------------------------------------------------------ cabecera, pie y piezas comunes
def head(title, desc, path, ld, img="assets/home/escena-cocina.jpg", robots="index, follow", extra=""):
    url = SITE + path
    return f'''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{"noindex, nofollow" if C.PREVIEW else robots}">
<link rel="canonical" href="{url}">{C.hreflang(path)}
<meta name="theme-color" content="#052A21">
<meta property="og:type" content="website"><meta property="og:site_name" content="Nasfeco Colombia"><meta property="og:locale" content="es_CO"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{SITE}{a(img)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="preload" href="assets/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/co.css?v={V}">{extra}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Ir al contenido</a>'''

def promo_bar():
    return f'''
<div class="pbar" data-promo role="region" aria-label="Oferta"><div class="pbar-in"><b data-promo-name></b><span>Hasta <strong data-maxoff></strong> de descuento con tu código</span><a href="index.html#equipos">Ver equipos</a><span class="pbar-t">Termina en <i data-cd>…</i></span></div></div>'''

NAV_HOGAR = [("index.html#equipos", "Equipos"), ("index.html#experiencia", "La experiencia"), ("index.html#bienvenida", "Tu bienvenida"), ("index.html#ciudades", "Ciudades"), ("index.html#faq", "Preguntas"), ("nasfeco.html", "Empresas")]
NAV_NF = [("#soluciones", "Soluciones"), ("#dia-solar", "Un día solar"), ("#calculadora", "Calculadora"), ("#proceso", "Cómo trabajamos"), ("#contacto", "Contacto"), ("index.html", "Hogar")]

def header(nav=NAV_HOGAR, solid=False, cta=True, home_href="index.html"):
    links = "".join(f'<a href="{h}">{t}</a>' for h, t in nav)
    c = (f'<button type="button" class="hd-cta dk" data-book>Agenda tu valoración <i>{ico(I_ARR, 14, 1.9)}</i></button>' if cta
         else f'<a class="hd-cta dk" href="#contacto">Cotizar proyecto <i>{ico(I_ARR, 14, 1.9)}</i></a>')
    mc = btn("Agenda tu valoración", "data-book", "b-gold") if cta else btn("Cotizar proyecto", "", "b-gold", "#contacto")
    return promo_bar() * cta + f'''
<header class="hd{" solid" if solid else ""}" id="hd">
  <a class="hd-logo" href="{home_href}" aria-label="NASFECO Colombia, inicio">{logo("w", 38, "lg-w")}{logo("c", 38, "lg-c")}</a>
  <nav class="hd-nav" aria-label="Principal">{links}</nav>
  <div class="hd-r">{c}<button type="button" class="hd-menu" data-menu aria-expanded="false" aria-controls="mnav" aria-label="Abrir menú">{ico(I_MENU, 22, 1.6)}</button></div>
</header>
<div class="mnav" id="mnav" hidden><nav aria-label="Menú móvil">{links}</nav>{mc}<small>WhatsApp §TEL§</small></div>'''

def footer():
    eq = "".join(f'<a href="{MODELS[k]["file"]}">{full(k)}</a>' for k in ORDER)
    ct = "".join(f'<a href="purificadores-agua-{s}">Purificadores en {n}</a>' for s, n, _ in C.CITIES)
    return f'''
<footer class="ft">
  <div class="wrap ft-g">
    <div class="ft-brand">{logo("w", 40)}<p>Agua y energía para hogares y empresas en Colombia. {C.COMPANY}, distribuidor oficial de Waterdrop Filter en Colombia.</p>
      <a class="ft-us" href="https://nasfecousa.com/"><img src="{a("assets/brand/nasfeco-us-white.png")}" alt="NASFECO US International" width="70" height="24">Miami, FL ↗</a></div>
    <div><h3 class="ft-h">Purificadores</h3>{eq}<button type="button" class="ft-l" data-compare>Comparar equipos</button></div>
    <div><h3 class="ft-h">Nasfeco</h3>{ct}<a href="nasfeco.html">Nasfeco Empresas</a><a href="politica-cookies">Política de cookies</a><a href="{C.PRIVACY_URL}">Tratamiento de datos personales</a><button type="button" class="ft-l" data-cookie-settings>Configurar cookies</button></div>
    <div><h3 class="ft-h">Contacto</h3><a href="{C.wa("¡Hola Nasfeco! Quiero información sobre los purificadores.")}" target="_blank" rel="noopener">WhatsApp §TEL§</a><a href="mailto:§MAIL§">§MAIL§</a><p>Instalación en {C.CITY_LIST}</p><p>Envíos a toda Colombia</p></div>
  </div>
  <div class="ft-b"><span>© 2026 Nasfeco · Colombia. {C.COMPANY} · NIT {C.NIT}. Distribuidor oficial de Waterdrop Filter. Waterdrop Filter es una marca registrada de su fabricante.</span><span>Creado por <strong>Mateo Perez</strong></span></div>
</footer>'''

def yt_box(i, label):
    return (f'<div class="yt-s" data-ytauto="{i}" aria-label="{label}"><img src="{a(f"assets/img/yt/{i}.webp")}" alt="" loading="lazy">'
            f'<div class="yt-gate"><p>Este video está en YouTube, que usa cookies.</p><button type="button" class="btn b-gold" data-consent="yes"><span>Aceptar y ver</span></button></div></div>')

def cmp_table():
    rows = ["Tecnología", "Capacidad", "Filtración", "Electricidad", "Instalación", "Ideal para"]
    th = "".join(f'<th><img src="{a(MODELS[k]["photo"])}" alt=""><br>{full(k).replace("Waterdrop ", "")}</th>' for k in ORDER)
    tb = "".join(f'<tr><th>{r}</th>{"".join(f"<td>{MODELS[k]["cmp"][i]}</td>" for k in ORDER)}</tr>' for i, r in enumerate(rows))
    tb += '<tr><th>Precio final</th>' + "".join(f'<td><b data-price="{k}"></b></td>' for k in ORDER) + "</tr>"
    tb += '<tr><th>Servicio Nasfeco</th>' + "".join(f'<td>{"Valoración, instalación, kit y seguimiento" if MODELS[k]["install"] else "Asesoría y envío"}</td>' for k in ORDER) + "</tr>"
    tb += '<tr><th></th>' + "".join(f'<td><button type="button" class="ul" data-book="{k}">{"Agendar" if MODELS[k]["install"] else "Pedir"}</button></td>' for k in ORDER) + "</tr>"
    return f'<div class="cmp"><table><thead><tr><th>Compara</th>{th}</tr></thead><tbody>{tb}</tbody></table></div>'

def dialogs(req=None):
    x = f'<button type="button" class="dx" data-close aria-label="Cerrar">{ico(I_X, 20, 1.6)}</button>'
    cfg = {"models": {k: {"img": MODELS[k]["photo"], "gpd": MODELS[k]["gpd"], "install": MODELS[k]["install"], "url": MODELS[k]["file"]} for k in ORDER},
           "cities": C.CITY_NAMES, "company": C.COMPANY, "privacy": C.PRIVACY_URL}
    reqd = (f'<dialog class="dlg dlg-wide" id="d-req" aria-labelledby="rq-t">{x}{kick("Revisar antes de comprar")}<h2 class="h3" id="rq-t">{em("Requisitos de [instalación.]")}</h2>'
            f'<div class="req-img"><a href="{a(req[0])}" target="_blank" rel="noopener"><img src="{req[0]}" alt="Requisitos para instalar el {req[1]}: tomas de agua visibles debajo del lavaplatos" loading="lazy"></a></div><p class="fine">Toca la imagen para verla en grande. Si tienes dudas, lo revisamos en la valoración.</p></dialog>') if req else ""
    return f'''
<dialog class="dlg dlg-wide" id="d-compare" aria-labelledby="cmp-t">{x}{kick("Elige lo que va contigo")}<h2 class="h3" id="cmp-t">{em("Cinco equipos, [lado a lado.]")}</h2>{cmp_table()}
  <p class="fine">Precios finales en pesos colombianos, con IVA. GPD: capacidad nominal en galones por día en condiciones de ensayo; el caudal real depende de la presión de tu casa.</p></dialog>
<dialog class="dlg" id="d-quiz" aria-labelledby="qz-t">{x}{kick("Un minuto para conocerte")}<h2 class="h3" id="qz-t">{em("¿Qué equipo va [contigo?]")}</h2><div id="qz-body"></div></dialog>
<dialog class="dlg dlg-book" id="d-book" aria-labelledby="bk-title">
  <aside class="bk-side">{mark(44)}<h3>{em("Tu casa.<br>Tu agua.<br>[Tu experiencia.]")}</h3>
    <div class="bk-sum"><img id="bk-img" src="{a(MODELS["x12"]["photo"])}" alt=""><div><b id="bk-model"></b><span id="bk-price"></span><small id="bk-inc"></small></div></div></aside>
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
<button type="button" class="cc-btn" data-cc aria-expanded="false" aria-controls="cc">{ico(I_SPARK, 18, 1.6)}<span>Tu asesor Nasfeco</span></button>
<div class="cc" id="cc" hidden role="dialog" aria-label="Tu asesor Nasfeco">
  <div class="cc-h">{mark(34, "c")}<div><small>Tu asesor · Nasfeco</small><b>Estamos para ti.</b></div><button type="button" class="dx" data-cc-close aria-label="Cerrar">{ico(I_X, 18, 1.6)}</button></div>
  <p class="cc-q">¿Qué te gustaría saber?</p>
  <div class="cc-t">{"".join(f'<button type="button" data-cc-topic="{k}">{t}</button>' for k, t in [("which", "¿Cuál equipo me conviene?"), ("inc", "Todo lo que incluye"), ("kitchen", "¿Funciona en mi cocina?"), ("care", "Después de instalar"), ("pay", "Precios y pago")])}</div>
  <p class="cc-a" id="cc-a" aria-live="polite"></p>
  <div class="cc-f">{wa_btn("Hablar con una persona por WhatsApp", "¡Hola Nasfeco! Tengo una pregunta sobre los purificadores.")}{btn("Agendar mi valoración", "data-book", "b-line")}<button type="button" class="btn b-line" data-quiz><span>Encontrar mi equipo</span><i>{ico(I_ARR, 15, 1.9)}</i></button></div>
  <small>Respuestas preparadas. Para todo lo demás, te responde una persona por WhatsApp.</small>
</div>
<script>window.NF_CFG = {json.dumps(cfg, ensure_ascii=False)};</script>
<script src="js/co.js?v={V}"></script>'''

# ------------------------------------------------------------------ secciones del inicio
VS_ALONE = ["Te llega una caja a la puerta", "Lo instalas tú o buscas un plomero", "Tú revisas mueble, desagüe y tomacorriente", "Soporte por los canales del fabricante", "Sin kit de bienvenida"]
VS_NF = ["Primero valoramos tu cocina", "Instalado y probado por Nasfeco", "Alcance por escrito, sin sorpresas", "Una persona real que te responde después", "Tu kit de bienvenida Nasfeco"]

def hero_fig():
    return (f'<figure class="hero-fig rv"><img src="{a("assets/home/escena-cocina.jpg")}" alt="Cocina con purificadores Waterdrop: el Dispensador ED01 sobre el mesón y la Ultrafiltración, la X12 y el G5P700A bajo el lavaplatos" fetchpriority="high" width="1600" height="1058">'
            '<span class="hero-tag t1"><i></i>ED01 · sobre el mesón</span><span class="hero-tag t2"><i></i>UF · X12 · G5P700A · bajo el lavaplatos</span><figcaption>Ambientación ilustrativa</figcaption></figure>')

def hero_home():
    return f'''
<section class="hero" id="top">
  <div class="wrap hero-g">
    <div>
      <p class="auth"><b><img src="{a("assets/brand/waterdrop-filter-logo.png")}" alt="Waterdrop Filter" width="140" height="27"></b><span>Distribuidor oficial en Colombia</span></p>
      {kick("Purificadores Waterdrop Filter · Instalados en Colombia", True)}
      <h1 class="h1">{em("Agua pura en casa.<br>[Nosotros nos encargamos.]")}</h1>
      <p class="lead lt">Elige tu purificador Waterdrop Filter. Nasfeco revisa tu cocina, lo instala, te entrega tu kit de bienvenida y sigue contigo después. Tú solo disfrutas tu agua.</p>
      <div class="row" style="margin-top:32px">{btn("Agenda tu valoración", "data-book", "b-gold")}{btn("Ver los equipos", "", "b-ghost", "#equipos", I_RIGHT)}</div>
      <p class="from">Con instalación desde <b data-price="uf"></b> · sin instalación desde <b data-price="smart"></b> · IVA incluido</p>
    </div>
    {hero_fig()}
  </div>
</section>''' + trust()

def trust():
    it = [(I_SHIELD, "Distribuidor oficial", "Waterdrop Filter en Colombia"), (I_HOME, "Valoración de tu cocina", "Antes de decidir"),
          (I_TOOL, "Instalación profesional", C.CITY_LIST), (I_GIFT, "Kit de bienvenida", "Bolso, botella Owala y toalla")]
    return '<section class="trust" aria-label="Lo que tienes seguro"><ul class="wrap">' + "".join(f"<li><i>{ico(i, 20, 1.6)}</i><div><b>{t}</b><span>{d}</span></div></li>" for i, t, d in it) + "</ul></section>"

def card(k, big=False):
    m = MODELS[k]; act = "Agendar valoración" if m["install"] else "Pedir el mío"
    return f'''
    <article class="sy{" big" if big else ""} rv">
      <a class="sy-m" href="{m["file"]}" aria-label="Ver {full(k)}"><img src="{a(m["photo"])}" alt="{full(k)}" loading="lazy"><span class="sy-tag">{m["tag"]}</span><span class="sy-save" data-promo-on>Ahorras <b data-save="{k}"></b></span></a>
      <div class="sy-b"><p class="brand">Waterdrop Filter · {"Instalado por Nasfeco" if m["install"] else "Sin instalación"}</p>
        <h3>{m["name"]} <small>{m["gpd"]}</small></h3><p class="sy-d">{m["card"]}</p>
        <div class="price"><b data-price="{k}"></b><s data-was="{k}"></s><small>IVA incluido{" · valoración, instalación y kit de bienvenida" if m["install"] else " · envío por confirmar"}</small></div>
        <span class="code" data-promo-on>Código <b data-code="{k}"></b></span>
        <div class="row">{btn("Ver detalles", "", "b-green", m["file"])}<button type="button" class="ul" data-book="{k}">{act} {ico(I_ARR, 14, 1.9)}</button></div></div>
    </article>'''

def systems(title="Cinco equipos.<br>[La misma atención Nasfeco.]", lead=None, kicker="01 · Elige tu equipo"):
    lead = lead or f"Waterdrop Filter hace el equipo; Nasfeco se encarga de todo lo demás. Precios finales en pesos colombianos, con IVA. Instalamos en {C.CITY_LIST} y enviamos a toda Colombia."
    return f'''
<section class="sec" id="equipos">
  <div class="wrap">
    <div class="sec-h rv">{kick(kicker)}<h2 class="h2">{em(title)}</h2><p class="lead">{lead}</p></div>
    <div class="sys-g">{card("x12", True)}{card("g5", True)}{card("g2")}{card("uf")}{card("smart")}</div>
    <div class="sys-a rv"><button type="button" class="btn b-line" data-compare><span>Comparar lado a lado</span><i>{ico("M7 16l-4-4 4-4M17 8l4 4-4 4M3 12h18", 15, 1.8)}</i></button><button type="button" class="btn b-line" data-quiz><span>Encuentra el tuyo en 3 preguntas</span><i>{ico(I_ARR, 15, 1.8)}</i></button></div>
  </div>
</section>'''

def kit_sec():
    items = [("Bolso Nasfeco", "De lona, con asas verdes y el bordado Nasfeco Colombia. Para la playa, el mercado o el día a día."),
             ("Tu botella Owala personalizada", "Térmica, con la personalización Nasfeco, para llevar tu agua pura a todas partes."),
             ("Toalla bordada", "Verde bosque, con textura y el logo Nasfeco bordado en dorado.")]
    li = "".join(f"<li><span>0{i+1}</span><div><b>{t}</b><p>{d}</p></div></li>" for i, (t, d) in enumerate(items))
    return f'''
<section class="sec dark" id="bienvenida">
  <div class="wrap kit-g">
    <figure class="kit-img rv"><img src="{a("assets/img/kit-bienvenida.webp")}" alt="Kit de bienvenida Nasfeco Colombia: bolso de lona, botella Owala personalizada y toalla verde bordada" loading="lazy" width="1536" height="1024"><small>Imagen ilustrativa · acabados por confirmar</small></figure>
    <div class="rv">{kick("02 · Tu bienvenida", True)}<h2 class="h2 lt">{em("Más que una instalación.<br>[Una bienvenida.]")}</h2>
      <p class="lead lt">Cada instalación Nasfeco termina con este kit, sin costo adicional. Un detalle para que la experiencia siga más allá de tu cocina.</p>
      <ul class="kit-l">{li}</ul>
      <p class="fine lt">Incluido con la X12, el G5P700A, el G2P600 y la Ultrafiltración UF ⟦confirmar⟧. Owala es una marca de su fabricante; Nasfeco aparece como personalización.</p></div>
  </div>
</section>'''

def experience():
    you = ["Escribirnos o agendar tu valoración", "Elegir tu equipo", "Disfrutar tu agua"]
    us = ["Te escuchamos y te ayudamos a elegir", "Revisamos espacio, agua, desagüe y tomacorriente", "Te damos el alcance por escrito antes de instalar", "Coordinamos la visita a tu horario",
          "Lo instalamos y comprobamos que funcione", "Te enseñamos a usar el equipo", "Te entregamos tu kit de bienvenida", "Hacemos seguimiento y te recordamos el mantenimiento"]
    return f'''
<section class="sec" id="experiencia">
  <div class="wrap">
    <div class="sec-h rv">{kick("03 · La experiencia Nasfeco")}<h2 class="h2">{em("El mismo equipo.<br>[Otra experiencia.]")}</h2></div>
    <div class="vs2 rv"><div class="vs2-a"><p class="ez-t">Comprarlo por tu cuenta</p><ul>{"".join(f"<li>{ico(I_X, 15, 2)}{t}</li>" for t in VS_ALONE)}</ul></div>
      <div class="vs2-b"><p class="ez-t">{mark(22)}Con Nasfeco</p><ul>{"".join(f"<li>{ico(I_CHECK, 16, 2.4)}{t}</li>" for t in VS_NF)}</ul></div></div>
    <h3 class="h3 ez-h rv">{em("Tú eliges. [Nosotros nos encargamos de todo lo demás.]")}</h3>
    <div class="ez-g">
      <article class="ez-c ez-you rv"><p class="ez-t">Lo único que haces tú</p><ol>{"".join(f"<li><span>0{i+1}</span>{t}</li>" for i, t in enumerate(you))}</ol></article>
      <article class="ez-c ez-us rv"><p class="ez-t">{mark(22)}Todo lo que hace Nasfeco</p><ul>{"".join(f"<li>{ico(I_CHECK, 16, 2.2)}<span>{t}</span></li>" for t in us)}</ul>{btn("Empieza con tu valoración", "data-book", "b-gold")}</article>
    </div>
  </div>
</section>'''

def techs():
    pts = [("ID", "Uniforme y credencial", "Llegan con el uniforme Nasfeco Colombia y una credencial con su nombre, para que sepas quién está en tu puerta."),
           ("RO · UF", "Especialistas en purificación", "Conocen los equipos Waterdrop Filter: espacio, conexiones, llave y la primera prueba."),
           ("4", "En tu ciudad", f"Técnicos en {C.CITY_LIST}. En otras ciudades te acompañamos por videollamada."),
           ("1:1", "De principio a fin", "El mismo equipo valora tu cocina, instala, te enseña a usar el equipo y hace el seguimiento.")]
    return f'''
<section class="sec dark" id="tecnico">
  <div class="wrap tec-g">
    <figure class="tec-img rv"><img src="{a("assets/img/tecnico-polo.webp")}" alt="Técnica de Nasfeco Colombia con polo verde bordado con el logo" loading="lazy" width="559" height="788"><figcaption>Así llegan: uniforme Nasfeco Colombia · imagen ilustrativa</figcaption></figure>
    <div class="rv">{kick("04 · Quién llega a tu casa", True)}<h2 class="h2 lt">{em("Tu técnico [Nasfeco.]")}</h2>
      <p class="lead lt">No es un desconocido con una caja de herramientas. Es un especialista que conoce tu equipo y responde por su trabajo.</p>
      <ul class="tec-l">{"".join(f"<li><i>{i}</i><b>{t}</b><p>{d}</p></li>" for i, t, d in pts)}</ul>
      {btn("Agenda tu valoración", "data-book", "b-gold")}</div>
  </div>
</section>'''

def j_media(kind, k="x12"):
    if kind == "chat":
        return '<div class="j-chat"><p class="me">¡Hola! ¿El purificador cabe bajo mi lavaplatos? Te mando foto. 📷</p><p class="them">Hola, te escribe Nasfeco. ¡Gracias! Revisamos tu espacio y lo planeamos contigo.</p></div>'
    if kind == "check":
        items = ["Espacio del mueble", "Toma de agua y desagüe", "Tomacorriente" if MODELS[k]["power"] else "Presión del agua", "Lugar de la llave", "Alcance por escrito"]
        return '<ul class="j-check">' + "".join(f"<li>{ico(I_CHECK, 15, 2.4)}{t}</li>" for t in items) + "</ul>"
    return media(kind)

def install_sec(k="x12", num="05 · Así instalamos"):
    m = MODELS[k]
    if k == "x12": mm = ["assets/clips/x12-cabinet.mp4", "assets/clips/x12-tds.mp4", "assets/clips/x12-pour.mp4"]
    else: mm = [m["feats"][3][0], m["feats"][2][0], m["gallery"][1]]
    steps = [("chat", "Te escuchamos", "Nos cuentas de tu casa, tu rutina y tus dudas. Te responde una persona de Nasfeco."),
             ("check", "Revisamos tu cocina", "Antes de instalar confirmamos la compatibilidad y te dejamos por escrito el alcance y cualquier adaptación."),
             (mm[0], "Instalamos", "Sin obras ni perforar paredes. El equipo queda ordenado bajo tu lavaplatos."),
             (mm[1], "Probamos y te enseñamos", "Servimos juntos el primer vaso y te mostramos cómo funciona el equipo."),
             ("assets/img/kit-bienvenida.webp", "Tu bienvenida", "Te entregamos tu kit Nasfeco: bolso, botella Owala personalizada y toalla bordada."),
             (mm[2], "Seguimos cerca", "Seguimiento, orientación y recordatorios de mantenimiento. Siempre sabes a quién llamar.")]
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
    rows = [k] if k else INSTALLED
    dl = "".join(f'<div><dt>{full(x)}</dt><dd><span data-price="{x}"></span></dd></div>' for x in rows)
    return f'''
<section class="sec" id="incluye">
  <div class="wrap">
    <div class="sec-h rv">{kick("Qué incluye")}<h2 class="h2">{em("Un solo precio.<br>[Todo resuelto.]")}</h2></div>
    <div class="inc-g">
      <ul class="inc-l rv">{"".join(f"<li><i>{ico(i, 22, 1.6)}</i>{t}</li>" for i, t in serv)}</ul>
      <div class="inc-p rv"><div><p class="ez-t" style="color:var(--gold)">Tu equipo + todo esto</p><dl>{dl}</dl></div>
        <p class="fine lt">Pesos colombianos, IVA del 19 % incluido. Instalación estándar en {C.CITY_LIST}. Cualquier trabajo adicional se acuerda contigo antes, por escrito.</p>
        {btn("Agenda tu valoración", f'data-book="{k}"' if k else "data-book", "b-gold")}</div>
    </div>
  </div>
</section>'''

def calc_sec(jug=12000, default="g5"):
    seg = "".join(f'<button type="button" class="{"on" if x == default else ""}" data-cp="{x}" aria-pressed="{"true" if x == default else "false"}">{MODELS[x]["name"].replace("Ultrafiltración ", "")}</button>' for x in ["g2", "g5", "x12", "uf"])
    return f'''
<section class="sec stone" id="ahorro">
  <div class="wrap">
    <div class="sec-h c rv">{kick("Calcula tu ahorro", c=True)}<h2 class="h2">{em("¿Cuánto gastas hoy [en botellones?]")}</h2><p class="lead">Haz la cuenta en 10 segundos y compárala con tener agua pura en tu propia cocina.</p></div>
    <div class="calc rv" data-calc data-default="{default}">
      <div class="calc-in"><h3>Tu consumo actual</h3><p class="fine" style="margin-top:2px">Ajusta los valores a lo que compras normalmente.</p>
        <div class="cf"><label for="c-ppl">Personas en casa <output data-o="ppl"></output></label><input type="range" id="c-ppl" name="ppl" min="1" max="10" value="4"></div>
        <div class="cf"><label for="c-bot">Botellones de 20 L por semana</label><input type="number" id="c-bot" name="bot" min="0" max="30" step="1" value="3" inputmode="numeric"></div>
        <div class="cf"><label for="c-jug">Precio por botellón (COP)</label><input type="number" id="c-jug" name="jug" min="0" max="60000" step="500" value="{jug}" inputmode="numeric"></div>
        <div class="cf"><label>Compararlo con</label><div class="seg2">{seg}</div></div></div>
      <div class="calc-out"><div><small>Gastas en botellones al año</small><b class="big" data-o="year">$0</b></div>
        <div class="two"><div><small>Al mes</small><b data-o="month">$0</b></div><div><small>Botellones de plástico al año</small><b data-o="jugs">0</b></div></div>
        <p data-o="msg"></p>{btn("Agendar mi valoración", 'data-o="book" data-book="' + default + '"', "b-gold")}</div>
    </div>
    <p class="fine" style="text-align:center">Cálculo referencial en pesos. El botellón viene en {C.cop(jug)} como referencia ⟦confirmar precio local⟧: cámbialo por el que pagas. No incluye el mantenimiento de los filtros.</p>
  </div>
</section>'''

def shorts_sec():
    c = "".join(f'<article class="short rv">{yt_box(MODELS[k]["yt"], "Video de " + full(k))}<h3>{full(k)}</h3><a href="{MODELS[k]["file"]}">Ver equipo →</a></article>' for k in ORDER)
    return f'''
<section class="sec" id="videos">
  <div class="wrap">
    <div class="sec-h rv">{kick("Míralos en acción")}<h2 class="h2">{em("La tecnología, [en casas reales.]")}</h2><p class="lead">Shorts de Waterdrop Filter y de usuarios. Si aceptas las cookies, se reproducen solos y sin sonido; toca uno para escucharlo.</p></div>
    <div class="sh-g">{c}</div>
  </div>
</section>'''

def cities_sec():
    c = "".join(f'<a class="cty rv" href="purificadores-agua-{s}"><small>Instalación en</small><b>{n}</b><span>Valoración, instalación y seguimiento →</span></a>' for s, n, _ in C.CITIES)
    return f'''
<section class="sec stone" id="ciudades">
  <div class="wrap">
    <div class="sec-split"><div class="sec-h rv">{kick("06 · Dónde estamos")}<h2 class="h2">{em("Instalamos en [cuatro ciudades.]")}</h2><p class="lead">Y enviamos a toda Colombia. En otras ciudades te acompañamos por videollamada durante la instalación, que trae guía paso a paso.</p></div></div>
    <div class="cty-g">{c}</div>
  </div>
</section>'''

FAQ_HOME = [
    ("¿Nasfeco es distribuidor oficial de Waterdrop Filter?", "Sí. Nasfeco es distribuidor oficial de Waterdrop Filter en Colombia. Los equipos que instalamos son originales, con garantía y soporte local."),
    ("¿Qué incluye el precio?", f"El precio es final, en pesos y con IVA del 19 %. En la X12, el G5P700A, el G2P600 y la Ultrafiltración UF incluye el equipo con su llave original, la valoración de tu cocina, la instalación estándar en {C.CITY_LIST}, el kit de bienvenida y el seguimiento. El Dispensador ED01 no necesita instalación; el envío se confirma aparte."),
    ("¿Por qué un purificador si el agua de mi ciudad es potable?", "En las grandes ciudades de Colombia el agua de la red llega potabilizada, pero en el camino puede recoger sedimentos de tuberías antiguas y de los tanques de los edificios, y lleva cloro, que se nota en el sabor. Un purificador quita todo eso justo antes de tu vaso."),
    ("¿Qué revisan antes de instalar?", "El espacio bajo el lavaplatos, la toma de agua, el desagüe, el tomacorriente (en los equipos de ósmosis inversa) y dónde va la llave. También si el conjunto o el edificio necesita alguna autorización. Cualquier adaptación se acuerda antes."),
    ("¿Instalan fuera de esas cuatro ciudades?", "Enviamos a toda Colombia. Fuera de Bogotá, Medellín, Cali y Barranquilla te acompañamos por videollamada durante la instalación, que es sencilla y trae guía paso a paso."),
    ("¿Cada cuánto se cambian los filtros?", "Depende del equipo y de tu consumo: entre 6 y 24 meses en los equipos bajo el lavaplatos y unos 3 meses en el ED01. El equipo te avisa y nosotros te recordamos cuándo toca."),
    ("¿Cómo uso el código de descuento?", "No tienes que hacer nada: el código de la oferta va escrito en tu solicitud de WhatsApp. Vale hasta que termine la cuenta regresiva."),
    ("¿Cuándo y cómo pago?", "Envías tu solicitud por WhatsApp y un asesor confirma disponibilidad, fecha y formas de pago. En esta web no se cobra nada."),
    ("¿Quién responde por la garantía?", f"{C.COMPANY}. La gestionamos aquí en Colombia, conforme al Estatuto del Consumidor (Ley 1480 de 2011): si algo falla, nos escribes y lo resolvemos sin que tengas que tratar con el exterior."),
    ("¿El purificador trata toda el agua de la casa?", "No. Los equipos bajo el lavaplatos están pensados para el agua de tomar y cocinar, mediante su llave dedicada. No son un sistema para todas las llaves de la vivienda.")]

def faq_sec(items, title="La confianza<br>empieza con<br>[claridad.]", num="07 · Preguntas"):
    q = "".join(f'<details class="rv"><summary>{x}<i>{ico(I_PLUS, 16, 1.8)}</i></summary><p>{y}</p></details>' for x, y in items)
    return f'''
<section class="sec faq" id="faq">
  <div class="wrap faq-g">
    <div class="faq-l rv">{kick(num)}<h2 class="h2">{em(title)}</h2>{wa_btn("Pregúntanos por WhatsApp", "¡Hola Nasfeco! Tengo una pregunta sobre los purificadores.", "b-green")}</div>
    <div>{q}</div>
  </div>
</section>'''

def faq_ld(items): return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", x)}} for q, x in items]}

def b2b_sec():
    return f'''
<section class="sec">
  <div class="wrap"><div class="b2b rv">
    <div class="b2b-c">{kick("Nasfeco Empresas", True)}<h2 class="h2 lt">{em("¿Oficina, consultorio<br>o [restaurante?]")}</h2>
      <p class="lead lt">Nasfeco también diseña soluciones de agua y energía solar para negocios e industrias: varios puntos de agua purificada, mantenimiento programado y factura para tu empresa.</p>
      <ul><li>Oficinas y coworking</li><li>Consultorios y clínicas</li><li>Restaurantes y cafeterías</li><li>Conjuntos residenciales</li><li>Colegios</li><li>Industria y minería</li></ul>
      <div class="row">{btn("Conocer Nasfeco Empresas", "", "b-gold", "nasfeco.html")}{wa_btn("Cotizar por WhatsApp", "¡Hola Nasfeco! Quiero una cotización de purificadores para mi empresa.", "b-ghost")}</div></div>
    <div class="b2b-i"><img src="{a("assets/nf/oficinas.jpg")}" alt="Oficina con soluciones de agua y energía de Nasfeco" loading="lazy"></div>
  </div></div>
</section>'''

def closing(img="assets/home/escena-cocina.jpg", k=None):
    return f'''
<section class="close">
  <img src="{a(img)}" alt="" loading="lazy">
  <div class="wrap close-c rv">{kick("Tu casa. Tu ritmo.", True)}<h2 class="h2 lt">{em("Déjanos el resto<br>[a nosotros.]")}</h2>
    <p class="lead lt">Agenda tu valoración y planeamos contigo tu experiencia Nasfeco, paso a paso.</p>
    <div class="row">{btn("Agenda tu valoración", f'data-book="{k}"' if k else "data-book", "b-gold")}{wa_btn("WhatsApp", "¡Hola Nasfeco! Quiero saber más de la experiencia.", "b-ghost")}</div></div>
</section>'''

def org_ld():
    return {"@type": "LocalBusiness", "@id": SITE + "#negocio", "name": "Nasfeco Colombia", "legalName": C.COMPANY, "url": SITE, "logo": SITE + "favicon.svg",
            "image": SITE + "assets/home/escena-cocina.jpg", "telephone": "§TEL§", "email": "§MAIL§", "priceRange": "$$",
            "description": "Distribuidor oficial de Waterdrop Filter en Colombia. Purificadores de agua con valoración, instalación, kit de bienvenida y seguimiento.",
            "address": {"@type": "PostalAddress", "addressLocality": C.HQ_CITY, "addressRegion": C.HQ_REGION, "addressCountry": "CO"},
            "areaServed": [{"@type": "City", "name": n} for n in C.CITY_NAMES], "sameAs": ["https://nasfecousa.com/"]}

def product_ld(k):
    m = MODELS[k]
    return {"@type": "Product", "name": full(k), "brand": {"@type": "Brand", "name": "Waterdrop"}, "sku": m["specs"][0][1], "description": re.sub("<[^>]+>", "", m["desc"]),
            "image": [SITE + g for g in m["gallery"][:4]],
            "offers": {"@type": "Offer", "url": SITE + m["file"].replace(".html", ""), "priceCurrency": "COP", "price": f"{C.price(k):.0f}", "priceValidUntil": C.PROMO_END,
                       "availability": "https://schema.org/InStock", "seller": {"@id": SITE + "#negocio"}}}

# ------------------------------------------------------------------ páginas
def page_home():
    t = "Purificadores de Agua Waterdrop en Colombia | Instalación y Kit de Bienvenida · Nasfeco"
    d = f"Purificadores Waterdrop Filter en Colombia: X12, G5P700A, G2P600, ultrafiltración y dispensador ED01. Nasfeco valora tu cocina, instala en {C.CITY_LIST} y te da tu kit de bienvenida."
    ld = {"@context": "https://schema.org", "@graph": [org_ld(), {"@type": "WebSite", "url": SITE, "name": "Nasfeco Colombia", "inLanguage": "es-CO"},
          {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE + MODELS[k]["file"].replace(".html", ""), "name": full(k)} for i, k in enumerate(ORDER)]}, faq_ld(FAQ_HOME)]}
    return (head(t, d, "", ld) + header() + '<main id="main">' + hero_home() + systems() + kit_sec() + experience() + techs() + install_sec() + includes()
            + calc_sec() + shorts_sec() + cities_sec() + faq_sec(FAQ_HOME) + b2b_sec() + closing() + "</main>" + footer() + dialogs() + "\n</body>\n</html>\n")

def pdh(k):
    m = MODELS[k]
    return f'''
<section class="pdh" id="top" data-pdp="{k}">
  <div class="pdh-big" aria-hidden="true">{m["name"].split()[-1]}</div>
  <div class="wrap pdh-g">
    <div><p class="crumb"><a href="index.html">Inicio</a> / <a href="index.html#equipos">Equipos</a> / {m["name"]}</p>
      {kick(m["kick"], True)}<h1 class="h1">{em(m["h1"])}</h1>
      <div class="chips lt">{"".join(f"<span>{c}</span>" for c in m["chips"])}</div>
      <div class="row">{btn("Agenda tu valoración" if m["install"] else "Pedir el mío", f'data-book="{k}"', "b-gold")}{wa_btn("WhatsApp", f"¡Hola Nasfeco! Me interesa el {full(k)}.", "b-ghost")}</div>
      <p class="from">Desde <b data-price="{k}"></b> · IVA incluido{" · instalación y kit de bienvenida" if m["install"] else ""}</p></div>
    <div class="pdh-img"><img src="{a(m["photo"])}" alt="{full(k)}" fetchpriority="high" width="640" height="640"></div>
  </div>
</section>'''

def pdp(k):
    m = MODELS[k]
    th = "".join(f'<button type="button" class="{"on" if i == 0 else ""}" data-photo="{a(g)}" aria-label="Foto {i+1}"><img src="{g}" alt="" loading="lazy"></button>' for i, g in enumerate(m["gallery"]))
    inc = ([(I_HOME, "Valoración de tu cocina"), (I_TOOL, "Instalación profesional"), (I_GIFT, "Kit de bienvenida Nasfeco"), (I_CHAT, "Seguimiento y garantía local")] if m["install"]
           else [(I_DROP, "Sin instalación ni técnicos"), (I_CHAT, "Asesoría por WhatsApp"), (I_SHIELD, "Garantía gestionada en Colombia"), (I_TAG, "Envío a toda Colombia")])
    req = f'<button type="button" class="req-btn" data-req-open>{ico("M10.3 3.9L1.8 18.2A2 2 0 003.5 21h17a2 2 0 001.7-2.8L13.7 3.9a2 2 0 00-3.4 0zM12 9v4M12 17h.01", 20, 2)}<span>Revisar antes de comprar</span><em>Importante</em></button>' if m["req"] else ""
    sub = [("#fotos", "Fotos"), ("#video", "Video"), ("#resumen", "Lo que hace")] + ([("#instalacion", "Instalación")] if m["install"] else []) + [("#ficha", "Ficha técnica"), ("#faq", "Preguntas")]
    return f'''
<nav class="sub" aria-label="{m["name"]}"><div class="wrap sub-in"><b>{full(k)}</b>{"".join(f'<a href="{h}">{t}</a>' for h, t in sub)}<button type="button" class="hd-cta" data-book="{k}">{"Agendar" if m["install"] else "Pedir"} <i>{ico(I_ARR, 14, 1.9)}</i></button></div></nav>
<section class="sec" id="fotos">
  <div class="wrap pdp-g">
    <div><div class="pdp-photo"><img id="pdp-photo" src="{m["gallery"][0]}" alt="{full(k)}"></div><div class="pdp-ths">{th}</div></div>
    <div class="pdp-i">{kick("Fotos y precio")}<h2>{em(m["h1"])}</h2><p class="pdp-d">{m["desc"]}</p>
      <div class="pz">
        <div data-promo-on><p class="pz-tag"><span data-promo-name></span> · código <code data-code="{k}"></code></p><div class="pz-row"><b data-price="{k}"></b><s data-was="{k}"></s><span class="pz-save">Ahorras <span data-save="{k}"></span></span></div>
          <p class="pz-cd">La oferta termina en <i data-cd>…</i></p></div>
        <div data-promo-off hidden><div class="pz-row"><b data-price="{k}"></b></div></div>
        <p class="pz-inc">Pesos colombianos · IVA incluido · {"equipo + valoración + instalación + kit de bienvenida + seguimiento" if m["install"] else "envío por confirmar"}</p>
      </div>
      <div class="row">{btn("Agenda tu valoración" if m["install"] else "Pedir el mío", f'data-book="{k}"', "b-gold")}{wa_btn("WhatsApp", f"¡Hola Nasfeco! Me interesa el {full(k)}.", "b-line")}</div>
      {req}
      <ul class="pdp-inc">{"".join(f"<li><i>{ico(i, 18, 1.6)}</i>{t}</li>" for i, t in inc)}</ul>
    </div>
  </div>
</section>'''

def pshort(k):
    m = MODELS[k]
    pts = ["Casa real, cocina real", "Así se usa en el día a día", "Agua pura al instante"]
    return f'''
<section class="sec stone" id="video">
  <div class="wrap psh-g">
    <div class="rv">{kick("Míralo")}<h2 class="h2">{em(f"{m['art'].capitalize()} {m['name']}, [en segundos.]")}</h2>
      <p class="lead">Un short de una casa real, para que veas el equipo funcionando antes de tu {"valoración" if m["install"] else "pedido"}.{" En " + C.CITY_LIST + " lo instalan los técnicos de Nasfeco." if m["install"] else ""}</p>
      <ul class="psh-l">{"".join(f"<li>{x}</li>" for x in pts)}</ul>{btn("Agenda tu valoración" if m["install"] else "Pedir el mío", f'data-book="{k}"', "b-green")}</div>
    <article class="short rv">{yt_box(m["yt"], "Video de " + full(k))}</article>
  </div>
</section>'''

def features(k):
    m = MODELS[k]
    if m["feats"]:
        c = "".join(f'<article class="fc rv"><div class="fc-m">{media(s, t)}</div><div class="fc-t"><h3>{t}</h3><p>{d}</p></div></article>' for s, t, d in m["feats"])
    else:
        c = "".join(f'<article class="fc rv"><div class="fc-m"><img src="{a(s)}" alt="Detalle del Dispensador ED01" loading="lazy"></div></article>' for s in m["detail"][:6])
    return f'''
<section class="sec" id="resumen"><div class="wrap">
  <div class="sec-h rv">{kick("Lo que hace")}<h2 class="h2">{em(f"Todo lo que hace {m['art']} {m['name']}, [sin pedirte nada.]")}</h2></div>
  <div class="feat-g">{c}</div>
  <p class="fine">Imágenes y videos oficiales de Waterdrop Filter.</p></div></section>'''

def specs(k):
    m = MODELS[k]
    img = f'<div class="spx-img"><img src="{a(m["spec_img"])}" alt="Medidas del {full(k)}" loading="lazy"></div>' if m["spec_img"] else ""
    return f'''
<section class="sec stone" id="ficha"><div class="wrap spx-g">
  <div class="rv">{kick("Ficha técnica")}<h2 class="h2">{em("Los detalles, [claros.]")}</h2>{img}</div>
  <dl class="spx-l rv">{"".join(f"<div><dt>{x}</dt><dd>{y}</dd></div>" for x, y in m["specs"])}</dl>
</div></section>'''

def others(k):
    c = "".join(f'<a href="{MODELS[x]["file"]}"><img src="{a(MODELS[x]["photo"])}" alt="" loading="lazy"><b>{full(x).replace("Waterdrop ", "")}</b><span data-price="{x}"></span></a>' for x in ORDER if x != k)
    return f'''
<section class="sec"><div class="wrap">
  <div class="sec-split"><div class="sec-h rv">{kick("Conoce también")}<h2 class="h2">{em("Otro equipo para [tu casa.]")}</h2></div><div class="row"><button type="button" class="btn b-line" data-compare><span>Comparar los cinco</span></button><button type="button" class="btn b-line" data-quiz><span>Encuentra el tuyo</span></button></div></div>
  <div class="oth rv">{c}</div></div></section>'''

def page_product(k):
    m = MODELS[k]
    t = f"{full(k)} en Colombia | {'Purificador con Instalación' if m['install'] else 'Agua Purificada sin Instalación'} · Nasfeco"
    d = f"{full(k)} en Colombia: {re.sub('<[^>]+>', '', m['card'])} Precio en pesos con IVA{', instalación en ' + C.CITY_LIST + ' y kit de bienvenida' if m['install'] else ' y envío a toda Colombia'}."
    gen = [("¿Quién responde por la garantía?", f"{C.COMPANY}, distribuidor oficial de Waterdrop Filter en Colombia, conforme al Estatuto del Consumidor (Ley 1480 de 2011).")]
    if m["install"]:
        gen.insert(0, ("¿El precio incluye la instalación?", f"Sí. Es el precio final en pesos: incluye IVA, la valoración, la instalación estándar en {C.CITY_LIST}, el kit de bienvenida y el seguimiento."))
    items = m["faq"] + gen
    ld = {"@context": "https://schema.org", "@graph": [org_ld(), product_ld(k), {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE},
          {"@type": "ListItem", "position": 2, "name": full(k), "item": SITE + m["file"].replace(".html", "")}]}, faq_ld(items)]}
    body = pdh(k) + pdp(k) + pshort(k) + features(k)
    if m["install"]: body += kit_sec().replace("02 · Tu bienvenida", "Tu bienvenida") + install_sec(k, "Así instalamos") + includes(k)
    body += specs(k) + others(k) + faq_sec(items, num="Preguntas") + closing(m["gallery"][1] if not m["install"] else "assets/home/escena-cocina.jpg", k)
    return head(t, d, m["file"].replace(".html", ""), ld, m["photo"]) + header() + '<main id="main">' + body + "</main>" + footer() + dialogs((m["req"], full(k)) if m["req"] else None) + "\n</body>\n</html>\n"

# ------------------------------------------------------------------ páginas por ciudad
# ⟦verificar⟧ Los textos sobre el agua de cada ciudad son generales y prudentes: revísalos con la empresa de acueducto local antes de publicar.
CITY_TXT = {
    "bogota": ("En Bogotá el agua de la red, que potabiliza la Empresa de Acueducto, es de buena calidad. Aun así llega con cloro, que se nota en el sabor del café y la comida, y en casas y edificios con tuberías antiguas o tanques de reserva puede recoger sedimentos antes de llegar a tu vaso.",
               "El agua de la red es potable, pero conserva el cloro y en el recorrido por tuberías antiguas y tanques de edificios puede recoger sedimentos. Un purificador quita todo eso justo antes de tu vaso y mejora el sabor.",
               ["Chapinero", "Usaquén", "Suba", "Teusaquillo", "Kennedy", "Fontibón", "Chía", "Cajicá"], 12000),
    "medellin": ("En Medellín y el Valle de Aburrá el agua que distribuye EPM es potable y de buena calidad. El cloro que la mantiene segura se nota en el sabor, y en muchos edificios el agua pasa por tanques de almacenamiento donde se pueden acumular sedimentos si no se lavan con frecuencia.",
                 "El agua de EPM es potable, pero el cloro se nota en el sabor y los tanques de los edificios pueden acumular sedimentos. Un purificador te da agua pura y con mejor sabor directo de la llave.",
                 ["El Poblado", "Laureles", "Belén", "Envigado", "Sabaneta", "Itagüí", "Bello", "Rionegro"], 12000),
    "cali": ("En Cali, en temporada de lluvias el río Cauca llega muy turbio y eso puede obligar a reducir la producción de agua potable. El agua de la red sale tratada, pero muchas familias prefieren tener en casa una barrera extra contra sedimentos, cloro y mal sabor, y dejar de depender de botellones.",
             "El agua de la red sale potabilizada, pero en temporada de lluvias el río Cauca llega muy turbio y en las tuberías se pueden acumular sedimentos. Un purificador agrega una barrera más en tu casa y quita el cloro y el mal sabor.",
             ["Ciudad Jardín", "Granada", "San Fernando", "Pance", "Jamundí", "Yumbo"], 12000),
    "barranquilla": ("En Barranquilla el agua se capta del río Magdalena y llega potabilizada, pero con el calor se toma mucha más agua y el sabor a cloro se nota. Muchas familias terminan comprando botellones cada semana: con un purificador en casa tienes agua pura ilimitada directo de la llave.",
                     "El agua de la red llega potabilizada, pero el cloro se nota en el sabor y con el calor se consume mucha agua. Un purificador mejora el sabor y te ahorra los botellones de cada semana.",
                     ["Alto Prado", "Riomar", "El Prado", "Villa Country", "Puerto Colombia", "Soledad"], 12000)}

def page_city(slug, city, region):
    intro, need, zones, jug = CITY_TXT[slug]
    items = [(f"¿Instalan purificadores de agua en {city}?", f"Sí. Los técnicos de Nasfeco valoran tu cocina e instalan en {city} y alrededores. El precio de la X12, el G5P700A, el G2P600 y la Ultrafiltración UF incluye IVA, instalación y kit de bienvenida."),
             (f"¿Cuánto cuesta un purificador de agua en {city}?", f"{C.price_list()}. Precios finales en pesos colombianos con IVA; el Dispensador ED01 no incluye envío."),
             ("¿Son equipos originales?", "Sí. Nasfeco es distribuidor oficial de Waterdrop Filter en Colombia: equipos originales con garantía y soporte local."),
             (f"¿El agua de {city} necesita purificador?", need),
             ("¿Cómo pago?", "Envías tu solicitud por WhatsApp y un asesor confirma disponibilidad, fecha de instalación y formas de pago.")]
    t = f"Purificadores de Agua en {city} con Instalación | Waterdrop · Nasfeco Colombia"
    d = f"Purificadores de agua Waterdrop en {city}: valoración, instalación y kit de bienvenida incluidos. X12, G5P700A, G2P600, ultrafiltración y ED01. Precios en pesos con IVA."
    ld = {"@context": "https://schema.org", "@graph": [{**org_ld(), "@id": SITE + f"purificadores-agua-{slug}#negocio", "name": f"Nasfeco · Purificadores Waterdrop {city}", "url": SITE + f"purificadores-agua-{slug}",
          "areaServed": {"@type": "City", "name": city}, "address": {"@type": "PostalAddress", "addressLocality": city, "addressRegion": region, "addressCountry": "CO"}}, faq_ld(items)]}
    hero = f'''
<section class="hero" id="top">
  <div class="wrap hero-g">
    <div>{kick(f"Nasfeco · {city}", True)}<h1 class="h1">{em(f"Purificadores de agua<br>[en {city}.]")}</h1>
      <p class="lead lt">{intro}</p>
      <div class="row" style="margin-top:32px">{btn(f"Agendar valoración en {city}", "data-book", "b-gold")}{wa_btn("Cotizar por WhatsApp", f"¡Hola Nasfeco! Estoy en {city} y quiero información sobre los purificadores.", "b-ghost")}</div>
      <p class="from">Cobertura en {city} y alrededores:</p><div class="chips lt" style="margin-top:10px">{"".join(f"<span>{z}</span>" for z in zones)}</div></div>
    {hero_fig()}
  </div>
</section>''' + trust()
    steps = f'''
<section class="sec stone"><div class="wrap">
  <div class="sec-h rv">{kick("Cómo comprar")}<h2 class="h2">{em(f"En {city}, [en 3 pasos.]")}</h2></div>
  <div class="steps">{"".join(f'<article class="st rv"><div class="st-t"><span>Paso 0{i+1}</span><h3>{x}</h3><p>{y}</p></div></article>' for i, (x, y) in enumerate([("Elige tu equipo", "O pide asesoría gratis por WhatsApp y te recomendamos uno."), (f"Valoramos e instalamos en {city}", "Coordinamos la visita a tu horario, revisamos tu cocina e instalamos."), ("Disfrutas tu agua", "Con tu kit de bienvenida, garantía y el seguimiento de Nasfeco.")]))}</div>
</div></section>'''
    body = hero + systems(f"Purificadores con instalación<br>[en {city}.]", f"Precios finales en pesos colombianos, con IVA, instalación en {city} y kit de bienvenida. El Dispensador ED01 no necesita instalación.", "Equipos") + steps + calc_sec(jug) + experience() + faq_sec(items, f"Preguntas<br>[en {city}.]", "Preguntas") + closing()
    return head(t, d, f"purificadores-agua-{slug}", ld) + header() + '<main id="main">' + body + "</main>" + footer() + dialogs() + "\n</body>\n</html>\n"

# ------------------------------------------------------------------ Nasfeco Empresas
SOL = [("nf/solar.jpg", "01", "Energía solar", "Sistemas fotovoltaicos para empresas: diseño, instalación y monitoreo para bajar tu factura de energía.", ["Estudio de consumo", "Paneles y estructura", "Instalación", "Monitoreo"]),
       ("nf/agua.jpg", "02", "Purificación de agua", "Ósmosis inversa, ultrafiltración y puntos de agua para oficinas, plantas y comercios.", ["Ósmosis inversa", "Ultrafiltración", "Puntos de agua", "Mantenimiento"]),
       ("nf/quimico.jpg", "03", "Tratamiento químico", "Tratamiento de agua para procesos industriales y mineros, con dosificación según el análisis de cada planta.", ["Análisis de agua", "Dosificación", "Industria", "Minería"]),
       ("nf/consultoria.jpg", "04", "Consultoría técnica", "Del diagnóstico a la puesta en marcha: la solución que tiene sentido para tu operación y tu presupuesto.", ["Diagnóstico", "Diseño", "Implementación", "Postventa"])]
STEPS_NF = [("01", "Diagnóstico", "Visitamos tu operación y revisamos consumo de energía, calidad de agua y necesidades."), ("02", "Propuesta a medida", "Diseñamos la solución con tiempos, costos y retorno esperado."),
            ("03", "Implementación", "Instalamos, probamos y dejamos todo funcionando sin frenar tu operación."), ("04", "Acompañamiento", "Mantenimiento, monitoreo y soporte local durante años.")]
IND = [("nf/manufactura.jpg", "Manufactura", "Energía y agua para procesos productivos"), ("nf/mineria.jpg", "Minería", "Tratamiento químico y agua para la operación"),
       ("nf/agro.jpg", "Agroindustria", "Bombeo solar y agua para riego y procesos"), ("nf/agua.jpg", "Alimentos y bebidas", "Agua purificada para producción"),
       ("nf/oficinas.jpg", "Oficinas y comercio", "Paneles solares y puntos de agua"), ("nf/tecnico.jpg", "Construcción e inmobiliario", "Soluciones para proyectos nuevos")]
FAQ_NF = [("¿En qué ciudades trabajan?", f"Tenemos presencia en {C.CITY_LIST} y llevamos proyectos a todo el país. Coordinamos la visita técnica según la ubicación de tu operación."),
          ("¿Cómo empieza un proyecto?", "Con una conversación y una visita técnica para entender tu consumo y tus necesidades. Con eso preparamos una propuesta a medida."),
          ("¿Ofrecen mantenimiento?", "Sí. Acompañamos cada proyecto con mantenimiento, monitoreo y soporte técnico local."),
          ("¿Hay beneficios tributarios por instalar energía solar?", "Pueden aplicar. La Ley 1715 de 2014 (modificada por la Ley 2099 de 2021) contempla incentivos para proyectos de energías renovables, como la deducción en el impuesto de renta de parte de la inversión, la exclusión del IVA y la exención de aranceles para los equipos, además de depreciación acelerada. Que apliquen a tu empresa depende de cumplir los requisitos y trámites ante la UPME y la DIAN: lo revisamos según la evaluación de tu caso, de la mano de tu contador."),
          ("¿También atienden hogares?", "Sí. Nasfeco es distribuidor oficial de Waterdrop Filter en Colombia: purificadores para el hogar con valoración, instalación y kit de bienvenida.")]

def day_sec():
    s = NF_DAY
    for x, y in (('class="nf-day"', 'class="day"'), ("nf-day-stage", "day-stage"), ("nf-day-hud", "day-hud"), ("nf-day-cap", "day-cap"), ("nf-day-stats", "day-st"), ("nf-day-note", "day-n"),
                 ('<p class="x-eyebrow">', '<p class="kick lt">'), ("<h2>Un día con <b>energía solar</b> en Colombia</h2>", '<h2 class="h2 lt">Un día con <em>energía solar</em> en Colombia</h2>')):
        assert x in s, x; s = s.replace(x, y)
    return s

def scalc_sec():
    return f'''
<section class="sec" id="calculadora">
  <div class="wrap">
    <div class="sec-h c rv">{kick("Calculadora solar", c=True)}<h2 class="h2">{em("¿Cuánto ahorraría tu empresa [con energía solar?]")}</h2><p class="lead">Mueve los valores y mira el resultado al instante.</p></div>
    <div class="scalc rv" data-scalc>
      <div class="scalc-in"><h3 style="font-size:20px;font-weight:600">Tu consumo eléctrico</h3><p class="fine" style="margin-top:2px">Usa el valor aproximado de tu factura de energía, en pesos.</p>
        <div class="cf"><label for="sc-bill">Factura mensual de energía <output id="o-bill">$6.000.000</output></label><input type="range" id="sc-bill" min="500000" max="100000000" step="100000" value="6000000"><p class="fine" style="display:flex;justify-content:space-between;margin-top:4px"><span>$500.000</span><span>$100.000.000</span></p></div>
        <div class="cf"><label>Tarifa aproximada por kWh</label><div class="seg2" id="sc-tar"><button type="button" data-t="700">$700 · Industrial</button><button type="button" data-t="850" class="on">$850 · Comercial</button><button type="button" data-t="950">$950 · Residencial</button></div></div>
        <div class="cf"><label for="sc-cov">Consumo que quieres cubrir con sol <output id="o-cov">80%</output></label><input type="range" id="sc-cov" min="30" max="100" step="5" value="80"></div></div>
      <div class="scalc-out"><div><small style="color:#AFC3B9">Ahorro estimado al año</small><b class="big" id="r-year" style="display:block;font-size:clamp(38px,4vw,56px);font-weight:700;color:var(--gold);letter-spacing:-.03em">$0</b></div>
        <div class="kpis"><div><small>Ahorro al mes</small><b id="r-month">$0</b></div><div><small>Recuperas la inversión en</small><b id="r-pay">–</b></div><div><small>Tamaño de la planta</small><b id="r-kwp">0 kWp</b></div>
          <div><small>Área de techo aprox.</small><b id="r-area">0 m²</b></div><div><small>CO₂ evitado al año</small><b id="r-co2">0 t</b></div><div><small>Paneles de 550 W</small><b id="r-pan">0</b></div></div>
        <div class="pan" id="r-viz" aria-hidden="true"></div>
        <div class="row"><a href="#" class="btn b-gold" id="r-wa" target="_blank" rel="noopener"><span>Quiero mi estudio solar</span><i>{WA}</i></a><a href="#contacto" class="btn b-ghost" id="r-form"><span>Llenar formulario</span></a></div></div>
    </div>
    <p class="fine" style="text-align:center">Estimación referencial en pesos colombianos: tarifas por kWh de referencia, rendimiento de 120 kWh por kWp al mes (entre 110 y 130 según la ciudad), inversión de $3.500.000 a $4.500.000 por kWp instalado y factor de emisión de la red colombiana de 0,13 kg de CO₂ por kWh ⟦confirmar tarifas, inversión y factor de emisión⟧. El valor real depende del estudio técnico de tu sitio.</p>
  </div>
</section>'''

def page_nf():
    t = "Nasfeco Empresas | Energía Solar y Soluciones de Agua para Empresas en Colombia"
    d = f"Nasfeco diseña e instala energía solar, purificación y tratamiento de agua para empresas, industrias y minería en Colombia. Presencia en {C.CITY_LIST}."
    ld = {"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": SITE + "#empresa", "name": "Nasfeco Colombia", "legalName": C.COMPANY, "url": SITE + "nasfeco", "email": "§MAIL§", "telephone": "§TEL§",
          "areaServed": {"@type": "Country", "name": "Colombia"}, "address": {"@type": "PostalAddress", "addressLocality": C.HQ_CITY, "addressRegion": C.HQ_REGION, "addressCountry": "CO"},
          "description": "Energía solar, purificación y tratamiento de agua para empresas e industrias en Colombia. Distribuidor oficial de Waterdrop Filter."}, faq_ld(FAQ_NF)]}
    tick = "".join(f"<span>{x}</span>" for x in ["Energía solar", "Purificación de agua", "Tratamiento químico", "Consultoría técnica", "Minería", "Industria", "Agroindustria", "Comercio"] * 2)
    sol = "".join(f'<article class="sol rv"><img src="{a("assets/" + i)}" alt="{t_}" loading="lazy"><div><small>{n}</small><h3>{t_}</h3><p>{d_}</p><ul>{"".join(f"<li>{x}</li>" for x in tags)}</ul><a class="ul" href="#contacto">Cotizar {t_.lower()} {ico(I_ARR, 14, 1.9)}</a></div></article>' for i, n, t_, d_, tags in SOL)
    nums = '<div class="nums"><div><b>+3</b><span>Años de experiencia</span></div><div><b>500+</b><span>Proyectos ejecutados</span></div><div><b>99 %</b><span>Satisfacción operativa</span></div></div><p class="fine lt">⟦confirmar cifras para Colombia⟧</p>'
    body = f'''
<section class="nfh" id="top"><img src="{a("assets/nf/hero.jpg")}" alt="Planta solar al atardecer" fetchpriority="high">
  <div class="wrap">{kick("Nasfeco Empresas · Colombia y Miami, Florida", True)}<h1 class="h1">{em("Energía y agua para la industria<br>[que mueve a Colombia.]")}</h1>
    <p class="lead lt">Diseñamos, instalamos y mantenemos soluciones de energía solar, purificación y tratamiento de agua para empresas, plantas y operaciones mineras.</p>
    <div class="row" style="margin-top:32px">{btn("Calcula tu ahorro solar", "", "b-gold", "#calculadora")}{btn("Cotizar proyecto", "", "b-ghost", "#contacto", I_RIGHT)}</div>{nums}</div></section>
<div class="tick" aria-hidden="true"><div>{tick}</div></div>
<section class="sec" id="soluciones"><div class="wrap"><div class="sec-h rv">{kick("Soluciones")}<h2 class="h2">{em("Un solo aliado para [tu energía y tu agua.]")}</h2></div><div class="sol-g">{sol}</div></div></section>
{day_sec()}
{scalc_sec()}
<section class="sec dark" id="proceso"><div class="wrap"><div class="sec-h rv">{kick("Cómo trabajamos", True)}<h2 class="h2 lt">{em("Del diagnóstico a la operación, [sin sorpresas.]")}</h2><p class="lead lt">Un mismo equipo te acompaña en cada etapa, con respaldo técnico aquí en Colombia.</p></div>
  <ol class="proc">{"".join(f'<li class="rv"><b>{n}</b><h3>{t_}</h3><p>{d_}</p></li>' for n, t_, d_ in STEPS_NF)}</ol></div></section>
<section class="sec" id="industrias"><div class="wrap"><div class="sec-h rv">{kick("Industrias")}<h2 class="h2">{em("Soluciones para [cada sector.]")}</h2></div>
  <div class="ind-g">{"".join(f'<a class="ind rv" href="#contacto"><img src="{a("assets/" + i)}" alt="{t_}" loading="lazy"><div><h3>{t_}</h3><p>{d_}</p></div></a>' for i, t_, d_ in IND)}</div></div></section>
<section class="sec stone"><div class="wrap"><div class="b2b rv"><div class="b2b-c">{kick("Distribuidor oficial", True)}<h2 class="h2 lt">{em("Somos distribuidores oficiales de [Waterdrop Filter en Colombia.]")}</h2>
  <p class="lead lt">Purificadores originales para casas, apartamentos y oficinas, con valoración, instalación, kit de bienvenida y seguimiento de Nasfeco.</p>
  <div class="row" style="margin-top:24px">{btn("Ver purificadores", "", "b-gold", "index.html#equipos")}</div></div><div class="b2b-i"><img src="{a("assets/home/escena-cocina.jpg")}" alt="" loading="lazy"></div></div></div></section>
{faq_sec(FAQ_NF, "Lo que nos preguntan<br>[las empresas.]", "Preguntas")}
<section class="sec stone" id="contacto"><div class="wrap ct-g">
  <div class="rv">{kick("Contacto")}<h2 class="h2">{em("Potenciemos juntos [tu proyecto.]")}</h2><p class="lead">Cuéntanos qué necesitas y un especialista de Nasfeco te contactará para agendar el diagnóstico.</p>
    <ul class="ct-l"><li><i>{WA}</i>§TEL§</li><li><i>{ico(I_MAIL, 18)}</i>§MAIL§</li><li><i>{ico(I_PIN, 18)}</i>{C.CITY_LIST} · proyectos en todo el país</li><li><i>{ico(I_PIN, 18)}</i>También en Miami, Florida (EE. UU.)</li></ul>
    {wa_btn("Escribir por WhatsApp", "¡Hola Nasfeco! Quiero cotizar un proyecto para mi empresa.")}</div>
  <form class="form rv" data-lead="Nasfeco CO B2B">
    <div class="f2"><div class="fld"><label for="n_name">Nombre</label><input id="n_name" name="name" required autocomplete="name" placeholder="Ej. Juan Pérez"></div><div class="fld"><label for="n_company">Empresa</label><input id="n_company" name="company" required placeholder="Empresa S.A.S."></div></div>
    <div class="f2"><div class="fld"><label for="n_email">Correo</label><input id="n_email" name="email" type="email" required autocomplete="email" placeholder="contacto@empresa.com"></div><div class="fld"><label for="n_phone">Celular / WhatsApp</label><input id="n_phone" name="phone" type="tel" required autocomplete="tel" placeholder="300 123 4567"></div></div>
    <div class="fld"><label for="n_service">Solución</label><select id="n_service" name="service"><option>Energía solar</option><option>Purificación de agua</option><option>Tratamiento químico</option><option>Consultoría técnica</option><option>Otro</option></select></div>
    <div class="fld"><label for="n_details">Cuéntanos del proyecto</label><textarea id="n_details" name="details" required placeholder="Ciudad, tipo de operación, valor aproximado de la factura de energía..."></textarea></div>
    <div class="fld"><label class="chk"><input type="checkbox" name="ok" required><span>Autorizo a {C.COMPANY} a tratar mis datos para responder esta solicitud, según la <a href="{C.PRIVACY_URL}" target="_blank" rel="noopener">política de tratamiento de datos</a> (Ley 1581 de 2012).</span></label></div>
    <button type="submit" class="btn b-green">Solicitar contacto</button>
  </form></div></section>'''
    extra = f'\n<script src="js/vendor/gsap.min.js"></script>\n<script src="js/vendor/ScrollTrigger.min.js"></script>\n{NF_JS.replace(".nf-day-stage", ".day-stage")}'
    return (head(t, d, "nasfeco", ld, "assets/nf/hero.jpg") + header(NAV_NF, cta=False, home_href="nasfeco.html") + '<main id="main">' + body + "</main>" + footer() + dialogs() + extra + "\n</body>\n</html>\n")

# ------------------------------------------------------------------ política de cookies y de datos personales
def page_legal():
    ck = [("Almacenamiento imprescindible", "<p>Guardamos tu elección sobre cookies en tu navegador (localStorage, clave <code>nf-consent</code>) para no volver a preguntarte. Es necesaria para respetar tu decisión y no se comparte con nadie.</p>"),
          ("Cookies de terceros: YouTube y Google Ads", "<p><b>YouTube.</b> Los videos son Shorts de YouTube insertados en modo de privacidad mejorada (youtube-nocookie.com). Aun así, YouTube (Google LLC) puede colocar cookies cuando un video se reproduce. Por eso solo se cargan si aceptas; hasta entonces ves una imagen fija guardada en nuestra web.</p><p><b>Google Ads.</b> Si activamos la medición de anuncios y aceptas, cargamos la etiqueta de Google Ads (Google LLC), que coloca cookies para saber si nuestros anuncios funcionan. Si rechazas, no se carga.</p>"),
          ("Sin analítica ni otros rastreadores", "<p>No usamos herramientas de analítica, píxeles de redes sociales ni otras cookies de publicidad. La tipografía se sirve desde nuestra propia web.</p>"),
          ("Cómo cambiar tu elección", '<p>Puedes aceptar o rechazar cuando quieras: <button type="button" class="ul" data-cookie-settings>abrir la configuración de cookies</button>. También puedes borrar los datos guardados desde la configuración de tu navegador.</p>')]
    dp = [("Responsable del tratamiento", f"<p><b>{C.COMPANY}</b>, NIT {C.NIT}, con domicilio en {C.ADDRESS}, {C.HQ_CITY}, Colombia. Correo: §MAIL§ · WhatsApp: §TEL§.</p>"),
          ("Marco legal", "<p>Esta política cumple la Ley Estatutaria 1581 de 2012 de protección de datos personales y el Decreto 1377 de 2013 (compilado en el Decreto 1074 de 2015). La autoridad de control en Colombia es la Superintendencia de Industria y Comercio (SIC).</p>"),
          ("Qué datos tratamos", "<p>Los que tú nos das al llenar un formulario, al armar tu solicitud de valoración o al escribirnos por WhatsApp: nombre, celular, correo, ciudad y barrio, tipo de vivienda, empresa y la información que quieras contarnos. Si compras, también los necesarios para la entrega, la instalación, la factura y la garantía. No pedimos datos sensibles ni datos de niñas, niños o adolescentes.</p>"),
          ("Para qué los usamos", "<ul><li>Responder tus solicitudes de valoración, asesoría o cotización.</li><li>Gestionar tus pedidos: disponibilidad, pago, envío, instalación, factura electrónica y garantía.</li><li>Darte soporte técnico y recordarte el mantenimiento de tu equipo.</li><li>Cumplir obligaciones legales, contables y tributarias.</li><li>Enviarte información sobre productos y promociones de Nasfeco, solo si nos autorizas y hasta que nos pidas parar.</li></ul>"),
          ("Con quién los compartimos", "<p>No vendemos tus datos. Los compartimos solo con proveedores que nos ayudan a prestar el servicio y actúan por nuestra cuenta (encargados): la herramienta que recibe los formularios de la web (n8n), WhatsApp (Meta Platforms) para la conversación con nuestros asesores y, si aceptaste las cookies de publicidad, Google. Algunos guardan la información en servidores fuera de Colombia; les exigimos niveles adecuados de protección.</p>"),
          ("Tus derechos como titular", "<p>Según el artículo 8 de la Ley 1581 de 2012 tienes derecho a <b>conocer, actualizar y rectificar</b> tus datos; pedir prueba de la autorización; saber qué uso les hemos dado; <b>revocar la autorización y/o pedir que los suprimamos</b> cuando no haya un deber legal o contractual de conservarlos; acceder a ellos gratis; y presentar quejas ante la Superintendencia de Industria y Comercio.</p>"),
          ("Cómo hacer consultas y reclamos", "<p>Escríbenos a §MAIL§ o por WhatsApp al §TEL§ con tu nombre, tu documento de identidad, lo que pides y un dato de contacto. Las <b>consultas</b> se responden en máximo diez (10) días hábiles, prorrogables cinco (5) más si te avisamos el motivo. Los <b>reclamos</b> (corrección, actualización, supresión o revocatoria) se resuelven en máximo quince (15) días hábiles, prorrogables ocho (8) más. Antes de acudir a la SIC debes haber presentado tu consulta o reclamo ante nosotros.</p>"),
          ("Autorización y vigencia", "<p>Al marcar la casilla de autorización en nuestros formularios o al escribirnos por WhatsApp, nos autorizas a tratar tus datos para las finalidades anteriores. Los conservamos mientras sean necesarios para esas finalidades y para cumplir la ley. Esta política rige desde el 17 de octubre de 2026; si la cambiamos de forma importante, lo publicaremos aquí.</p>")]
    sec = lambda xs: "".join(f'<h2><i>0{n+1}</i>{h}</h2>{t_}' for n, (h, t_) in enumerate(xs))
    t = "Política de Cookies y Tratamiento de Datos Personales | Nasfeco Colombia"
    d = f"Política de cookies y de tratamiento de datos personales de {C.COMPANY} (Ley 1581 de 2012): qué guardamos, para qué usamos tus datos y cómo ejercer tus derechos."
    body = f'''<main id="main" class="lg"><div class="wrap lg-g">
  <aside class="lg-a"><p class="crumb"><a href="index.html">Inicio</a> / Legal</p><h1 class="h2">{em("Cookies y [datos personales]")}</h1><p class="fine">Última actualización: 17 de octubre de 2026</p>
    <p class="fine"><a class="ul" href="#datos-personales">Ir a tratamiento de datos personales</a></p></aside>
  <div class="lg-b">{sec(ck)}
    <h3 id="datos-personales">Política de tratamiento de datos personales</h3><p class="fine">Cómo {C.COMPANY} recolecta, usa y protege tus datos, y cómo puedes ejercer tus derechos. <span class="todo">⟦revisar con un abogado antes de publicar⟧</span></p>
    {sec(dp)}</div>
</div></main>'''
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": "Política de cookies y tratamiento de datos personales", "url": SITE + "politica-cookies"}
    return head(t, d, "politica-cookies", ld) + header(solid=True) + body + footer() + dialogs() + "\n</body>\n</html>\n"

# ------------------------------------------------------------------ escribir
if __name__ == "__main__":
    C.write("index.html", page_home())
    for k in ORDER: C.write(MODELS[k]["file"], page_product(k))
    for slug, city, region in C.CITIES: C.write(f"purificadores-agua-{slug}.html", page_city(slug, city, region))
    C.write("nasfeco.html", page_nf())
    C.write("politica-cookies.html", page_legal())
