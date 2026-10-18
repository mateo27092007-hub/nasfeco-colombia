# Generador del sitio · Nasfeco Colombia (v2)

Estructura inspirada en nasfecousa.com (valoración, kit de bienvenida, técnico, "tú eliges / nosotros nos encargamos"),
con los colores del logo NASFECO COLOMBIA: verde bosque, dorado y crema.

```
python _build/build_co.py    # todas las páginas
python _build/build_seo.py   # sitemap.xml y robots.txt (lastmod = hoy)
```

## Páginas
| Archivo | Qué es |
|---|---|
| `index.html` | Inicio · Waterdrop Hogar: equipos, kit de bienvenida, experiencia, técnico, instalación, calculadora de botellones, videos, ciudades, preguntas |
| `product-x12/g5p700a/g2p600/uf/smart.html` | Fichas de producto |
| `nasfeco.html` | Nasfeco Empresas: soluciones, "Un día con energía solar", calculadora solar, proceso, industrias, contacto |
| `purificadores-agua-bogota/medellin/cali/barranquilla.html` | Páginas por ciudad (SEO) |
| `politica-cookies.html` | Cookies + tratamiento de datos personales (Ley 1581 de 2012) |

No hay carrito ni página de repuestos: cada compra empieza con "Agenda tu valoración" (3 pasos) y termina en WhatsApp,
con copia al webhook de n8n cuando la persona autoriza el tratamiento de datos.

## Dónde se cambia cada cosa
| Qué | Dónde |
|---|---|
| WhatsApp, precios, precio normal, códigos, nombre y fecha de la oferta, webhook, Google Ads | Objeto `WD` al inicio de `js/co.js` (los generadores también lo leen: vuelve a ejecutarlos) |
| Dominio, razón social, NIT, correo, dirección, teléfono visible, ciudades, "oficial" o "exclusivo", versión de caché `VER` | `_build/co.py` |
| Textos, fotos, ficha técnica y preguntas de cada equipo | `MODELS` en `_build/build_co.py` |
| Texto del agua, barrios y precio del botellón de cada ciudad | `CITY_TXT` en `_build/build_co.py` |
| Tarifa, inversión por kWp y factor de emisión | `_build/nf_wow.py` (simulación) y `scalc_sec()` en `build_co.py` (nota visible) |
| Diseño | `css/co.css` · comportamiento: `js/co.js` |

Sube `VER` en `co.py` cada vez que cambies `css/co.css` o `js/co.js`.

## Marcadores
`§WA§` → WhatsApp · `§TEL§` → teléfono visible · `§MAIL§` → correo · `⟦texto⟧` → sale como `{{texto}}` (pendiente).
Antes de publicar, busca `{{` en todo el proyecto: no debería quedar ninguno.

`_build/` y `_archivo/` no se publican (`.assetsignore`). La versión anterior (tienda con carrito) está en `_archivo/v1`.
