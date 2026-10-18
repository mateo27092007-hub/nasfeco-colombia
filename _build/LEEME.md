# Generador del sitio · Nasfeco Colombia (Medellín)

Como las webs de Miami y España: **dos equipos** (Waterdrop X12 y Ultrafiltración UF), **solo Medellín** y todo el servicio Nasfeco
(valoración, instalación, kit de bienvenida y seguimiento). Sin carrito, sin repuestos y sin Nasfeco Empresas (pedido de Nasfeco, 18/10/2026).

## Identidad de Colombia (distinta de Miami, España y Ecuador)
- **Esmeralda y oro**: las esmeraldas colombianas y El Dorado, a partir del logo NASFECO COLOMBIA. Arena cálida de fondo.
- **Acentos**: franja tricolor arriba y bandas de **tejido wayúu** (rombos amarillo, rojo, azul, esmeralda y coral).
- **Medellín**: las montañas del valle de Aburrá con el **Metrocable** (portada, Medellín, cierre), "la ciudad de la eterna primavera", comprobador por **comuna**.
- **Voz paisa** sin perder lo profesional: "Chao botellón. Hola agua pura.", "¿Cuánta plata se te va en botellones?", "Un detallazo", "¿Qué más pues?".
- **Lo nuestro**: el tinto, los jugos, la aguapanela y el sancocho.
- Titulares en **Bricolage Grotesque**, texto en Montserrat (las dos en `assets/fonts/`).
- De la esencia Nasfeco: sello giratorio de distribuidor oficial, "Lo que compras + Lo que te damos", valoración en 3 pasos, concierge, barra de oferta.

```
python _build/build_co.py    # index, product-x12, product-uf, politica-cookies
python _build/build_seo.py   # sitemap.xml y robots.txt
```

## Dónde se cambia cada cosa
| Qué | Dónde |
|---|---|
| WhatsApp, precios, precio normal, códigos, nombre y fecha de la oferta, webhook, Google Ads | Objeto `WD` al inicio de `js/co.js` |
| Dominio, razón social, NIT, correo, dirección, teléfono, comunas y municipios, `PREVIEW`, versión `VER` | `_build/co.py` |
| Textos, fotos, ficha técnica y preguntas de cada equipo | `MODELS` en `_build/build_co.py` |
| Diseño · comportamiento | `css/co.css` · `js/co.js` |

- `PREVIEW = True` pone `noindex` (vista previa en GitHub Pages). Cámbialo a `False` el día del lanzamiento.
- Sube `VER` en `co.py` cada vez que cambies `css/co.css` o `js/co.js`.
- Marcadores: `§WA§` WhatsApp · `§TEL§` teléfono · `§MAIL§` correo · `⟦texto⟧` sale como `{{texto}}` (pendiente). Antes de publicar, busca `{{`.

## Vista previa
https://mateo27092007-hub.github.io/nasfeco-colombia/ · para actualizarla: `git add -A`, `git commit -m "..."`, `git push` (o `deploy.bat`).

`_build/` y `_archivo/` no se publican. Versiones anteriores y fotos que ya no se usan: `_archivo/`.
