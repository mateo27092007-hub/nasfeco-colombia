/* =========================================================
   NASFECO COLOMBIA · comportamiento de la web
   ---------------------------------------------------------
   >>> WHATSAPP, PRECIOS, CÓDIGOS Y OFERTA: EDITA SOLO AQUÍ <<<
   Precios en pesos colombianos (COP), enteros, precio final con IVA del 19 % incluido.
   price = precio con la oferta · was = precio normal (se usa solo cuando termina la oferta).
   Los generadores de _build/ también leen este objeto (JSON-LD y páginas por ciudad):
   después de cambiarlo, ejecuta los scripts de _build/ y sube VER en _build/co.py.
   {{PENDIENTE}}: número de WhatsApp, precios, códigos y promo son provisionales hasta que se confirmen.
   ========================================================= */
const WD = {
  whatsapp: '57XXXXXXXXXX',                  // {{WhatsApp sin + ni espacios}}
  promo: {
    name: '{{nombre de la promo}}',
    end: '2026-11-30T23:59:59-05:00'         // {{fecha de fin}} · hora de Colombia (UTC-5)
  },
  // Formularios y solicitudes de valoración (n8n): cada envío lleva source y country: 'CO'.
  webhook: 'https://guachotw1.app.n8n.cloud/webhook/727f04bc-196b-4e54-947b-70ed61e854dd',
  // Google Ads: vacío = no se envía nada. El ID (AW-...) va en ADS, más abajo.
  ads: { id: '', wa: '', lead: '' },         // {{ID 'AW-...' y etiquetas de conversión 'AW-XXXX/YYYY'}}
  products: {
    x12:   { name: 'Waterdrop X12', price: 7990000, was: 8790000, code: 'COX12' },
    g5:    { name: 'Waterdrop G5P700A', price: 5590000, was: 6790000, code: 'COG5' },
    g2:    { name: 'Waterdrop G2P600', price: 3590000, was: 4790000, code: 'COG2' },
    uf:    { name: 'Waterdrop Ultrafiltración UF', price: 1190000, was: 1520000, code: 'COUF' },
    smart: { name: 'Waterdrop Dispensador ED01', price: 399000, was: 519000, code: 'COED01' }
  }
};

(function () {
  'use strict';
  document.documentElement.classList.add('js');
  const CFG = window.NF_CFG || { models: {} }, M = CFG.models, P = WD.products;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const esc = v => String(v == null ? '' : v).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const money = n => '$' + Math.round(n).toLocaleString('es-CO');
  const wa = t => `https://wa.me/${WD.whatsapp}?text=${encodeURIComponent(t)}`;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const store = { get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }, set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} } };

  /* ---------- oferta: precios, código y cuenta regresiva; al terminar todo pasa solo a precio normal ---------- */
  const END = new Date(WD.promo.end).getTime();
  let promoOn = Date.now() < END;
  const now = k => promoOn ? P[k].price : P[k].was;
  function paint() {
    document.documentElement.classList.toggle('no-promo', !promoOn);
    $$('[data-price]').forEach(e => { if (P[e.dataset.price]) e.textContent = money(now(e.dataset.price)); });
    $$('[data-was]').forEach(e => { const p = P[e.dataset.was]; if (p) e.textContent = promoOn && p.was > p.price ? money(p.was) : ''; });
    $$('[data-save]').forEach(e => { const p = P[e.dataset.save]; if (p) e.textContent = money(p.was - p.price); });
    $$('[data-code]').forEach(e => { const p = P[e.dataset.code]; if (p) e.textContent = p.code; });
    $$('[data-promo-name]').forEach(e => e.textContent = WD.promo.name);
    $$('[data-maxoff]').forEach(e => e.textContent = money(Math.max(...Object.values(P).map(p => p.was - p.price))));
    $$('[data-promo-on]').forEach(e => e.hidden = !promoOn);
    $$('[data-promo-off]').forEach(e => e.hidden = promoOn);
  }
  function tick() {
    const left = Math.max(0, END - Date.now());
    if (!left && promoOn) { promoOn = false; paint(); }
    if (!promoOn) { $$('[data-promo]').forEach(b => b.remove()); return false; }
    const d = Math.floor(left / 864e5), h = Math.floor(left / 36e5) % 24, mi = Math.floor(left / 6e4) % 60, se = Math.floor(left / 1e3) % 60;
    $$('[data-cd]').forEach(e => e.textContent = d > 0 ? `${d}d ${h}h ${mi}m` : `${h}h ${mi}m ${String(se).padStart(2, '0')}s`);
    return true;
  }
  paint();
  if (tick()) { const iv = setInterval(() => { if (!tick()) clearInterval(iv); }, 1000); }

  /* ---------- Google Ads (solo con ID configurado y cookies aceptadas) ---------- */
  let adsLoaded = false;
  function adsOn() {
    if (!WD.ads.id || adsLoaded) return; adsLoaded = true;
    window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date()); gtag('config', WD.ads.id);
    const s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + WD.ads.id; document.head.appendChild(s);
  }
  const conv = label => { if (label && typeof window.gtag === 'function') gtag('event', 'conversion', { send_to: label, transport_type: 'beacon' }); };
  document.addEventListener('click', e => { if (e.target.closest('a[href*="wa.me/"]')) conv(WD.ads.wa); }, true);

  /* ---------- encabezado y menú móvil ---------- */
  const hd = $('#hd'), mnav = $('#mnav'), menuBtn = $('[data-menu]');
  const onScroll = () => hd && hd.classList.toggle('scr', scrollY > 40 || (mnav && !mnav.hidden));
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  const setMenu = open => {
    if (!mnav) return; mnav.hidden = !open; menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú'); document.body.style.overflow = open ? 'hidden' : ''; onScroll();
  };
  menuBtn && menuBtn.addEventListener('click', () => setMenu(mnav.hidden));
  mnav && $$('a, button', mnav).forEach(el => el.addEventListener('click', () => setMenu(false)));

  /* ---------- ventanas (dialog) ---------- */
  let opener = null;
  const openDlg = id => {
    const d = $('#' + id); if (!d) return;
    $$('dialog[open]').forEach(x => { if (x !== d) x.close(); });
    setMenu(false); setCC(false);
    opener = document.activeElement; if (!d.open) d.showModal(); document.body.style.overflow = 'hidden';
  };
  $$('dialog').forEach(d => {
    d.addEventListener('close', () => { if (!$('dialog[open]')) { document.body.style.overflow = ''; opener && opener.focus && opener.focus({ preventScroll: true }); } });
    d.addEventListener('click', e => { if (e.target === d) d.close(); });
    $$('[data-close]', d).forEach(b => b.addEventListener('click', () => d.close()));
  });
  $$('[data-compare]').forEach(b => b.addEventListener('click', () => openDlg('d-compare')));
  $$('[data-req-open]').forEach(b => b.addEventListener('click', () => openDlg('d-req')));

  /* ---------- galería de la ficha ---------- */
  $$('[data-photo]').forEach(b => b.addEventListener('click', () => {
    const img = $('#pdp-photo'); if (!img) return;
    $$('[data-photo]').forEach(x => x.classList.toggle('on', x === b));
    img.style.opacity = 0; setTimeout(() => { img.src = b.dataset.photo; img.style.opacity = 1; }, 140);
  }));

  /* ---------- buscador: 3 preguntas → un equipo (orientación, no diagnóstico) ---------- */
  const QZ = [
    ['¿Dónde vives?', [['casa', 'Casa o apartamento propio', 'Puedo instalar algo bajo el lavaplatos'], ['arriendo', 'Arriendo o no quiero instalar nada', 'Prefiero algo sobre la mesa']]],
    ['¿Qué te preocupa más del agua?', [['sabor', 'El sabor y el olor a cloro', 'Quiero agua más rica para tomar y cocinar'], ['todo', 'Sarro, metales y lo que no se ve', 'Quiero la máxima pureza']]],
    ['¿Cuántos son en casa?', [['1', '1 o 2 personas', ''], ['3', '3 a 5 personas', ''], ['6', '6 o más personas', '']]]
  ];
  const WHY = {
    smart: 'Sin obras ni técnicos: lo llenas, lo cargas y tienes agua filtrada en 1 segundo. Ideal si vives en arriendo.',
    uf: 'Quita el cloro y el mal sabor y conserva los minerales, sin electricidad ni desperdicio de agua.',
    g2: 'Ósmosis inversa sin tanque al mejor precio: 7 etapas y 600 GPD, perfecta para hogares pequeños.',
    g5: 'Ósmosis inversa con minerales alcalinos y 700 GPD en un equipo compacto, para toda la familia.',
    x12: 'El más completo: 11 etapas, minerales, 1200 GPD y llave inteligente para familias grandes.'
  };
  function quiz() {
    let step = 0; const ans = {};
    const body = $('#qz-body');
    const pick = () => ans[0] === 'arriendo' ? 'smart' : ans[1] === 'sabor' ? 'uf' : ans[2] === '1' ? 'g2' : ans[2] === '3' ? 'g5' : 'x12';
    const render = () => {
      if (step < QZ.length) {
        const [q, o] = QZ[step];
        body.innerHTML = `<div class="qz-bar"><i style="width:${step / QZ.length * 100}%"></i></div><p class="qz-n">Pregunta ${step + 1} de ${QZ.length}</p><h3 class="qz-q">${q}</h3>
          <div class="qz-o">${o.map(([v, t, s]) => `<button type="button" data-qa="${v}"><b>${t}</b>${s ? `<span>${s}</span>` : ''}</button>`).join('')}</div>`;
        $$('[data-qa]', body).forEach(b => b.addEventListener('click', () => { ans[step] = b.dataset.qa; step++; render(); }));
      } else {
        const k = pick(), m = M[k];
        body.innerHTML = `<div class="qz-bar"><i style="width:100%"></i></div><p class="qz-n">Te recomendamos</p>
          <div class="qz-r"><img src="${m.img}" alt=""><div><h3>${P[k].name}</h3><p>${WHY[k]}</p>
          <p class="qz-p"><b>${money(now(k))}</b>${promoOn ? `<s>${money(P[k].was)}</s>` : ''}</p>
          <div class="row"><button type="button" class="btn b-gold" data-book="${k}"><span>${m.install ? 'Agendar valoración' : 'Pedir el mío'}</span><i>↗</i></button><a class="ul" href="${m.url}">Ver detalles</a></div></div></div>
          <p class="fine">Es un punto de partida según tus respuestas. La compatibilidad de tu cocina se confirma en la valoración. <button type="button" class="ul" id="qz-again">Volver a empezar</button></p>`;
        $('#qz-again').addEventListener('click', () => { step = 0; render(); });
      }
    };
    render();
  }
  $$('[data-quiz]').forEach(b => b.addEventListener('click', () => { quiz(); openDlg('d-quiz'); }));

  /* ---------- valoración / pedido en 3 pasos → WhatsApp (y copia al webhook con autorización de datos) ---------- */
  const CITIES = CFG.cities || ['Bogotá', 'Medellín', 'Cali', 'Barranquilla'];
  const B = { model: null }; let stepB = 0;
  const val = k => esc(B[k] || '');
  const opt = (name, v, label) => `<label><input type="radio" name="${name}" value="${v}"${(B[name] || '') === v ? ' checked' : ''}><span>${label}</span></label>`;
  const needsPower = k => ['x12', 'g5', 'g2'].includes(k);
  const today = () => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };
  const LAB = { apto: 'Apartamento', casa: 'Casa', oficina: 'Oficina o negocio', yes: 'Sí', no: 'No', unsure: 'No lo sé', morning: 'Mañana', afternoon: 'Tarde', any: 'Cualquiera' };
  function side() {
    const k = B.model, m = M[k]; if (!m) return;
    $('#bk-img').src = m.img; $('#bk-model').textContent = P[k].name;
    $('#bk-price').textContent = money(now(k)) + (promoOn ? ` · código ${P[k].code}` : '');
    $('#bk-inc').textContent = m.install ? 'IVA, valoración, instalación y kit de bienvenida incluidos.' : 'IVA incluido · sin instalación · envío por confirmar.';
  }
  function renderBook() {
    const s = stepB, k = B.model, inst = M[k] && M[k].install;
    $('#bk-err').textContent = '';
    $('#bk-step').textContent = `0${Math.min(s + 1, 3)} / 03`;
    $$('.bk-prog span').forEach((el, i) => el.classList.toggle('on', i <= s));
    $('#bk-back').hidden = s === 0 || s === 3; $('.bk-btns').hidden = s === 3;
    $('#bk-next span').textContent = s === 2 ? 'Ver mi solicitud' : 'Continuar';
    const T = [['Empecemos por tu equipo.', 'Todos incluyen IVA. Los equipos bajo el lavaplatos incluyen valoración, instalación y kit de bienvenida.'],
      [inst ? 'Cuéntanos de tu casa.' : '¿A dónde lo enviamos?', inst ? 'Así preparamos tu valoración. La compatibilidad se confirma después.' : 'El ED01 no necesita instalación: te lo enviamos a cualquier ciudad.'],
      ['¿Cómo te contactamos?', 'Te responde una persona de Nasfeco por WhatsApp.'],
      ['Tu solicitud está lista.', 'Revísala y envíala por WhatsApp. La cita o el pedido se confirman cuando Nasfeco te responda.']][s];
    $('#bk-title').textContent = T[0]; $('#bk-sub').textContent = T[1];
    let h = '';
    if (s === 0) {
      h = Object.keys(M).map(x => `<label class="choice"><input type="radio" name="model" value="${x}"${k === x ? ' checked' : ''}><img src="${M[x].img}" alt=""><span><b>${P[x].name}</b><small>${M[x].gpd} · ${M[x].install ? 'con instalación' : 'sin instalación'}</small></span><strong>${money(now(x))}</strong></label>`).join('');
    } else if (s === 1) {
      h = `<div class="f2"><div class="fld" data-f="city"><label for="f-city">Ciudad</label><select id="f-city" name="city"><option value="">Elige tu ciudad</option>${CITIES.map(c => `<option${B.city === c ? ' selected' : ''}>${c}</option>`).join('')}<option${B.city === 'Otra ciudad' ? ' selected' : ''}>Otra ciudad</option></select><span class="msg"></span></div>
        <div class="fld"><label for="f-zone">Barrio o municipio <small>(opcional)</small></label><input id="f-zone" name="zone" value="${val('zone')}" placeholder="Ej. Chapinero"></div></div>
        <div class="fld"><label>Tipo de vivienda</label><div class="seg">${opt('home', 'apto', 'Apartamento')}${opt('home', 'casa', 'Casa')}${opt('home', 'oficina', 'Oficina o negocio')}</div></div>
        ${needsPower(k) ? `<div class="fld" data-f="outlet"><label>¿Hay tomacorriente bajo el lavaplatos?</label><div class="seg">${opt('outlet', 'yes', 'Sí')}${opt('outlet', 'no', 'No')}${opt('outlet', 'unsure', 'No lo sé')}</div><span class="msg"></span></div>` : ''}
        <p class="fine">${inst ? `Instalamos en ${CITIES.join(', ').replace(/, ([^,]*)$/, ' y $1')}. En otra ciudad te acompañamos por videollamada.` : 'El costo del envío se confirma por WhatsApp.'}</p>`;
    } else if (s === 2) {
      h = `<div class="f2"><div class="fld" data-f="name"><label for="f-name">Nombre</label><input id="f-name" name="name" autocomplete="name" value="${val('name')}"><span class="msg"></span></div>
        <div class="fld" data-f="phone"><label for="f-phone">Celular / WhatsApp</label><input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" value="${val('phone')}" placeholder="300 123 4567"><span class="msg"></span></div></div>
        <div class="f2"><div class="fld" data-f="email"><label for="f-email">Correo <small>(opcional)</small></label><input id="f-email" name="email" type="email" autocomplete="email" value="${val('email')}"><span class="msg"></span></div>
        ${inst ? `<div class="fld" data-f="date"><label for="f-date">Fecha preferida <small>(opcional)</small></label><input id="f-date" name="date" type="date" min="${today()}" value="${val('date')}"><span class="msg"></span></div>` : '<div></div>'}</div>
        ${inst ? `<div class="fld"><label>Franja horaria</label><div class="seg">${opt('slot', 'morning', 'Mañana')}${opt('slot', 'afternoon', 'Tarde')}${opt('slot', 'any', 'Cualquiera')}</div></div>` : ''}
        <div class="fld" data-f="ok"><label class="chk"><input type="checkbox" name="ok" value="1"${B.ok ? ' checked' : ''}><span>Autorizo a ${esc(CFG.company || 'Nasfeco')} a tratar mis datos para responder esta solicitud, según la <a href="${CFG.privacy || 'politica-cookies#datos-personales'}" target="_blank" rel="noopener">política de tratamiento de datos</a> (Ley 1581 de 2012).</span></label><span class="msg"></span></div>`;
    } else {
      h = `<div class="bk-done"><dl>${summary().map(([a, b]) => `<dt>${esc(a)}</dt><dd>${esc(b)}</dd>`).join('')}</dl>
        <div class="row"><a class="btn b-wa" id="bk-send" href="${wa(summaryText())}" target="_blank" rel="noopener"><span>Enviar por WhatsApp</span><i>↗</i></a><button type="button" class="ul" id="bk-edit">Editar</button></div>
        <p class="fine">Se abre WhatsApp con tu solicitud escrita; nada se envía hasta que presiones enviar. En esta web no se cobra nada.</p></div>`;
    }
    $('#bk-fields').innerHTML = h; side();
    $$('#bk-fields input, #bk-fields select').forEach(i => i.addEventListener('change', () => { capture(); side(); }));
    if (s === 3) {
      $('#bk-edit').addEventListener('click', () => { stepB = 0; renderBook(); });
      $('#bk-send').addEventListener('click', () => { lead({ source: 'Waterdrop CO valoracion', ...flat() }); conv(WD.ads.lead); });
    }
  }
  function capture() {
    const f = $('#bk-form'); B.ok = false;
    new FormData(f).forEach((v, k) => { B[k] = k === 'ok' ? true : String(v).trim(); });
  }
  const phoneOK = v => /^(\+?57)?3\d{9}$/.test((v || '').replace(/[\s().-]/g, ''));
  function summary() {
    const k = B.model, m = M[k], r = [['Equipo', `${P[k].name} · ${money(now(k))}${promoOn ? ` con el código ${P[k].code} (${WD.promo.name})` : ''}`],
      ['Ciudad', [B.city, B.zone].filter(Boolean).join(' · ')], ['Vivienda', LAB[B.home] || '—']];
    if (needsPower(k)) r.push(['Tomacorriente bajo el lavaplatos', LAB[B.outlet] || '—']);
    r.push(['Nombre', B.name], ['Celular', B.phone], ['Correo', B.email || '—']);
    if (m.install) r.push(['Fecha preferida', B.date || '—'], ['Franja', LAB[B.slot] || '—']);
    return r;
  }
  const flat = () => ({ country: 'CO', model: P[B.model].name, price: now(B.model), code: promoOn ? P[B.model].code : '', city: B.city || '', zone: B.zone || '', home: LAB[B.home] || '', outlet: LAB[B.outlet] || '', name: B.name || '', phone: B.phone || '', email: B.email || '', date: B.date || '', slot: LAB[B.slot] || '' });
  const summaryText = () => (M[B.model].install ? '¡Hola Nasfeco! Quiero agendar mi valoración.' : '¡Hola Nasfeco! Quiero hacer un pedido.') + '\n\n' + summary().map(([a, b]) => `${a}: ${b}`).join('\n');
  function validate() {
    const s = stepB, er = {};
    $$('.fld.bad').forEach(f => { f.classList.remove('bad'); const m = $('.msg', f); if (m) m.textContent = ''; });
    if (s === 0 && !B.model) er._ = 'Elige un equipo.';
    if (s === 1) { if (!B.city) er.city = 'Elige tu ciudad.'; if (needsPower(B.model) && !B.outlet) er.outlet = 'Elige una opción.'; }
    if (s === 2) {
      if ((B.name || '').length < 2) er.name = 'Escribe tu nombre.';
      if (!phoneOK(B.phone)) er.phone = 'Escribe un celular colombiano de 10 dígitos (empieza por 3).';
      if (B.email && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(B.email)) er.email = 'Revisa el formato del correo.';
      if (B.date && B.date < today()) er.date = 'Elige una fecha de hoy en adelante.';
      if (!B.ok) er.ok = 'Necesitamos tu autorización para responderte.';
    }
    Object.entries(er).forEach(([k, msg]) => { const f = $(`.fld[data-f="${k}"]`); if (f) { f.classList.add('bad'); $('.msg', f).textContent = msg; } });
    if (Object.keys(er).length) { $('#bk-err').textContent = er._ || 'Revisa los campos marcados.'; const first = $('.fld.bad input, .fld.bad select'); first && first.focus(); return false; }
    return true;
  }
  if ($('#bk-form')) {
    $('#bk-form').addEventListener('submit', e => { e.preventDefault(); capture(); if (!validate()) return; stepB++; renderBook(); $('#bk-title').setAttribute('tabindex', '-1'); $('#bk-title').focus(); });
    $('#bk-back').addEventListener('click', () => { capture(); stepB = Math.max(0, stepB - 1); renderBook(); });
    document.addEventListener('click', e => {
      const b = e.target.closest('[data-book]'); if (!b) return;
      const k = b.dataset.book;
      B.model = M[k] ? k : (B.model || ($('[data-pdp]') && $('[data-pdp]').dataset.pdp) || 'x12');
      stepB = M[k] ? 1 : 0; renderBook(); openDlg('d-book');
    });
  }

  /* ---------- envío a n8n (formularios con autorización de datos) ---------- */
  function lead(data) {
    try { return fetch(WD.webhook, { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(data), keepalive: true }); }
    catch (e) { return Promise.reject(e); }
  }
  $$('form[data-lead]').forEach(f => f.addEventListener('submit', async e => {
    e.preventDefault();
    const b = $('button[type=submit]', f), txt = b.textContent, d = { source: f.dataset.lead, country: 'CO' };
    new FormData(f).forEach((v, k) => { if (k !== 'ok') d[k] = v; });
    b.textContent = 'Enviando...'; b.disabled = true;
    try {
      const r = await lead(d);
      if (r.ok || r.type === 'opaque') { b.textContent = '¡Solicitud enviada! Te contactaremos pronto'; f.reset(); conv(WD.ads.lead); return; }
      throw new Error();
    } catch (err) { b.textContent = 'Error al enviar. Intenta de nuevo.'; setTimeout(() => { b.textContent = txt; b.disabled = false; }, 3000); }
  }));

  /* ---------- concierge: respuestas preparadas + una persona por WhatsApp ---------- */
  const cc = $('#cc'), ccBtn = $('[data-cc]');
  function setCC(open) { if (!cc) return; cc.hidden = !open; ccBtn.setAttribute('aria-expanded', String(open)); if (open) $('[data-cc-close]').focus(); }
  if (cc) {
    ccBtn.addEventListener('click', () => setCC(cc.hidden));
    $('[data-cc-close]').addEventListener('click', () => { setCC(false); ccBtn.focus(); });
    const CC = {
      which: `Para máxima pureza y familias grandes, la X12 (${money(now('x12'))}). Con minerales alcalinos, el G5P700A (${money(now('g5'))}). Ósmosis inversa al mejor precio, el G2P600 (${money(now('g2'))}). Sin electricidad, la UF (${money(now('uf'))}). Si vives en arriendo, el Dispensador ED01 (${money(now('smart'))}). El buscador de 3 preguntas te orienta en un minuto.`,
      inc: 'En la X12, el G5P700A, el G2P600 y la UF: el equipo original, la valoración de tu cocina, la instalación estándar, el kit de bienvenida (bolso, botella Owala personalizada y toalla bordada) y el seguimiento. Todo con IVA incluido. El ED01 no necesita instalación.',
      kitchen: 'Revisamos el espacio bajo el lavaplatos, la toma de agua, el desagüe, el tomacorriente (en los equipos de ósmosis) y dónde va la llave. Si hace falta alguna adaptación, te la decimos por escrito antes de instalar.',
      care: 'Te enseñamos a usar el equipo, hacemos seguimiento y te recordamos cuándo toca el mantenimiento. La garantía la gestiona Nasfeco en Colombia, conforme al Estatuto del Consumidor (Ley 1480 de 2011).',
      pay: 'Arma tu solicitud y envíala por WhatsApp: un asesor confirma disponibilidad, fecha y las formas de pago. En esta web no se cobra nada.'
    };
    $$('[data-cc-topic]').forEach(b => b.addEventListener('click', () => { $('#cc-a').textContent = CC[b.dataset.ccTopic]; $$('[data-cc-topic]').forEach(x => x.classList.toggle('on', x === b)); }));
  }
  document.addEventListener('keydown', e => { if (e.key === 'Escape') { if (cc && !cc.hidden) { setCC(false); ccBtn.focus(); } if (mnav && !mnav.hidden) setMenu(false); } });

  /* ---------- FAQ: una abierta a la vez ---------- */
  $$('.faq details').forEach(d => d.addEventListener('toggle', () => { if (d.open) $$('.faq details').forEach(o => { if (o !== d) o.open = false; }); }));

  /* ---------- calculadora de botellones ---------- */
  $$('[data-calc]').forEach(c => {
    const ppl = $('[name=ppl]', c), bot = $('[name=bot]', c), pr = $('[name=jug]', c); let k = c.dataset.default || 'g5', touched = false;
    const out = n => $(`[data-o="${n}"]`, c);
    const run = () => {
      const p = +ppl.value; if (!touched) bot.value = Math.max(1, Math.round(p * .75));
      const b = Math.max(0, +bot.value || 0), price = Math.max(0, +pr.value || 0), month = b * price * 52 / 12, year = b * price * 52, months = month > 0 ? now(k) / month : 0;
      out('ppl').textContent = p + (p === 1 ? ' persona' : ' personas');
      out('year').textContent = money(year); out('month').textContent = money(month); out('jugs').textContent = Math.round(b * 52);
      out('msg').textContent = month > 0 ? `Con lo que hoy gastas en botellones, el ${P[k].name.replace('Waterdrop ', '')} se paga solo en unos ${months < 1 ? 'menos de 1' : Math.ceil(months)} ${months < 1 || Math.ceil(months) === 1 ? 'mes' : 'meses'}.` : 'Escribe cuántos botellones compran a la semana.';
      const bk = out('book'); if (bk) bk.dataset.book = k;
    };
    $$('[data-cp]', c).forEach(b => b.addEventListener('click', () => { k = b.dataset.cp; $$('[data-cp]', c).forEach(x => { x.classList.toggle('on', x === b); x.setAttribute('aria-pressed', String(x === b)); }); run(); }));
    ppl.addEventListener('input', run); bot.addEventListener('input', () => { touched = true; run(); }); pr.addEventListener('input', run); run();
  });

  /* ---------- cookies: solo lo imprescindible; YouTube y Google Ads esperan a que aceptes ---------- */
  let consent = store.get('nf-consent');            // 'yes' | 'no' | null
  const ck = $('#ck');
  const showBar = on => { if (ck) { ck.hidden = !on; document.documentElement.classList.toggle('ck-on', on); } };
  function setConsent(v) {
    consent = v; store.set('nf-consent', v); showBar(false);
    document.documentElement.classList.toggle('yt-ok', v === 'yes');
    if (v === 'yes') { adsOn(); $$('[data-ytauto]').forEach(b => { yio.unobserve(b); yio.observe(b); }); }
    else { $$('[data-ytauto] iframe').forEach(f => f.remove()); $$('[data-ytauto]').forEach(b => b.classList.remove('on')); if (typeof window.gtag === 'function') { gtag('consent', 'update', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' }); window.gtag = undefined; } }
  }
  document.addEventListener('click', e => {
    const c = e.target.closest('[data-consent]'); if (c) { setConsent(c.dataset.consent); return; }
    if (e.target.closest('[data-cookie-settings]')) { e.preventDefault(); showBar(true); ck && $('button', ck).focus({ preventScroll: true }); }
  });

  /* ---------- Shorts de YouTube (youtube-nocookie, solo con consentimiento): suenan en silencio mientras se ven ---------- */
  const ytCmd = (f, func) => f.contentWindow && f.contentWindow.postMessage(JSON.stringify({ event: 'command', func, args: [] }), '*');
  const yio = new IntersectionObserver(es => es.forEach(en => {
    const box = en.target, id = box.dataset.ytauto; let f = $('iframe', box);
    if (consent !== 'yes') return;
    if (en.isIntersecting) {
      if (!f) {
        f = document.createElement('iframe');
        f.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&mute=1&loop=1&playlist=${id}&controls=1&playsinline=1&rel=0&modestbranding=1&enablejsapi=1`;
        f.title = box.getAttribute('aria-label') || 'Video'; f.allow = 'autoplay; encrypted-media; picture-in-picture'; f.allowFullscreen = true;
        f.addEventListener('load', () => box.classList.add('on')); box.appendChild(f);
      } else { ytCmd(f, 'playVideo'); }
    } else if (f) ytCmd(f, 'pauseVideo');
  }), { threshold: .5 });
  $$('[data-ytauto]').forEach(b => yio.observe(b));
  if (consent === 'yes') { document.documentElement.classList.add('yt-ok'); adsOn(); } else if (consent !== 'no') showBar(true);

  /* ---------- videos oficiales: solo se reproducen en pantalla ---------- */
  const vio = new IntersectionObserver(es => es.forEach(en => { const v = en.target; if (en.isIntersecting && !reduce) { v.preload = 'auto'; const pr = v.play(); pr && pr.catch(() => {}); } else v.pause(); }), { threshold: .35 });
  $$('video[data-auto]').forEach(v => vio.observe(v));

  /* ---------- aparición suave ---------- */
  const rio = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); rio.unobserve(en.target); } }), { threshold: .08, rootMargin: '0px 0px -6% 0px' });
  $$('.rv').forEach(el => rio.observe(el));
})();
