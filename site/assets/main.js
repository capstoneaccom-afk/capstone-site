/* Navigation entre pages : chaque nouvelle page commence en haut, sauf lien vers une ancre précise */
(function () {
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  function land() {
    var h = (location.hash || '').slice(1);
    var t = h && !document.getElementById('cm-' + h) ? document.getElementById(h) : null;
    if (t) { var y = t.getBoundingClientRect().top + window.pageYOffset - 88; window.scrollTo({ top: Math.max(0, y), left: 0, behavior: 'instant' }); }
    else window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
  }
  land();
  window.addEventListener('pageshow', land);
  window.addEventListener('load', function () { setTimeout(land, 0); });
})();

(function () {
  var top = document.querySelector('.top');
  function onScroll() { if (top) top.classList.toggle('solid', window.scrollY > 24); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  var openBtn = document.querySelector('.menu-btn'), panel = document.getElementById('mnav');
  if (openBtn && panel) {
    var closeBtn = panel.querySelector('button');
    openBtn.addEventListener('click', function () { panel.hidden = false; openBtn.setAttribute('aria-expanded', 'true'); closeBtn.focus(); document.body.style.overflow = 'hidden'; });
    function close() { panel.hidden = true; openBtn.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; }
    closeBtn.addEventListener('click', close);
    panel.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', close); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) close(); });
  }

  var rot = document.getElementById('rot');
  var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (rot && !still) {
    var words = rot.dataset.words.split('|'), i = 0;
    setInterval(function () {
      rot.classList.add('out');
      setTimeout(function () { i = (i + 1) % words.length; rot.textContent = words[i]; rot.classList.remove('out'); }, 300);
    }, 2600);
  }

  // Pré-sélection du profil depuis l'URL (contact.html#build, #advise, #partenaire)
  var h = (location.hash || '').replace('#', '');
  var pre = { build: 'p-build', advise: 'p-advise', partenaire: 'p-part' }[h];
  if (pre && document.getElementById(pre)) document.getElementById(pre).checked = true;

  var form = document.getElementById('form'), status = document.getElementById('status');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (form.hasAttribute('data-preview')) { status.textContent = 'Aperçu : l’envoi sera actif une fois le site en ligne sur Netlify.'; return; }
    status.className = 'status'; status.textContent = 'Envoi…';
    fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(new FormData(form)).toString() })
      .then(function (r) { if (!r.ok) throw new Error(); form.reset(); status.className = 'status ok'; status.textContent = 'Merci, votre message est bien parti. Nous revenons vers vous sous 5 jours ouvrés.'; })
      .catch(function () { status.textContent = 'L’envoi a échoué. Réessayez dans un instant.'; });
  });
})();

/* ---------- Vie et mouvement ---------- */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (reduce || !('IntersectionObserver' in window)) return;
  var root = document.documentElement;

  // 1. Titres découpés en mots (en conservant les <span> internes)
  function splitWords(el) {
    var wi = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var parts = n.textContent.split(/(\s+)/), frag = document.createDocumentFragment();
          parts.forEach(function (p) {
            if (!p) return;
            if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(p)); return; }
            var w = document.createElement('span'); w.className = 'w';
            var i = document.createElement('span'); i.textContent = p; i.style.setProperty('--wi', wi++);
            w.appendChild(i); frag.appendChild(w);
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'BR' && !n.classList.contains('rot')) { walk(n); }
        else if (n.nodeType === 1 && n.classList.contains('rot')) {
          var w = document.createElement('span'); w.className = 'w'; n.parentNode.insertBefore(w, n);
          var i = document.createElement('span'); i.style.setProperty('--wi', wi++); w.appendChild(i); i.appendChild(n);
        }
      });
    })(el);
    el.classList.add('splitw', 'split-in');
  }
  document.querySelectorAll('.d1, .d2, .dark-photo h2, .cta-band h2, .case h3, .ph-sub, .mission, .quote-sec blockquote, .news h2').forEach(splitWords);

  // 2. Éléments qui apparaissent, décalés entre frères
  var sel = '.label, .lead, .ph-foot .ctas, .card, .fig, .co, .mode, .stair, .give, .chip, .faq details, .eco > div, .people > div, .duo-img img, .split .media, .ph-media .frame, .mosaic > *, form.cform, aside.side, .case .txt > *, .case .img, .apports, .chips-title, .foot-cols > div, .sec-head .arrow-link, .post, .pf, .mt-tab, .mt-pans, .timeline li, .member, .q-by, .faq2-more, .cta-doors a, .sizes, .metier-row, .filters, .note, .news-form, .intro-big, .stage';
  document.querySelectorAll(sel).forEach(function (el) {
    if (el.closest('.split-in')) return;
    el.classList.add('reveal');
    var sibs = Array.prototype.filter.call(el.parentNode.children, function (c) { return c.matches(sel); });
    var k = sibs.indexOf(el);
    if (k > 0) el.style.setProperty('--delay', Math.min(k * 0.08, 0.56) + 's');
  });
  document.querySelectorAll('.illu').forEach(function (s) { s.classList.add('draw'); });
  var giant = document.querySelector('.giant');
  root.classList.add('anim');

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var t = e.target; t.classList.add('in');
      if (t.dataset.count) countUp(t);
      if (t.classList.contains('reveal')) {
        // une fois entré, l'élément retrouve ses styles normaux (survol, inclinaison, lumière)
        var d = parseFloat(getComputedStyle(t).getPropertyValue('--delay')) || 0;
        setTimeout(function () { t.classList.remove('reveal', 'in'); t.style.removeProperty('--delay'); }, 1100 + d * 1000);
      }
      io.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
  document.querySelectorAll('.reveal, .split-in, .illu.draw, .iso').forEach(function (el) { io.observe(el); });
  if (giant) io.observe(giant);

  // 3. Chiffres qui défilent
  function countUp(el) {
    var target = parseFloat(el.dataset.count), pad = el.dataset.pad | 0, pre = el.dataset.pre, suf = el.dataset.suf, t0 = null, dur = 1600;
    function fmt(v) { var s = Math.round(v).toLocaleString('fr-FR').replace(/ | /g, ' '); while (s.length < pad) s = '0' + s; return pre + s + suf; }
    function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / dur); el.textContent = fmt(target * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  document.querySelectorAll('.fig b, .mosaic .tile b, .stair .n').forEach(function (el) {
    var m = el.textContent.match(/^(\D*)([\d\s  ]+)(.*)$/);
    if (!m) return;
    var digits = m[2].replace(/\D/g, '');
    el.dataset.count = digits; el.dataset.pad = /^0/.test(digits) ? digits.length : 0;
    el.dataset.pre = m[1]; el.dataset.suf = m[3];
    el.textContent = m[1] + (el.dataset.pad > 0 ? '0'.repeat(digits.length) : '0') + m[3];
    if (!el.classList.contains('reveal')) io.observe(el);
    else { var o = new MutationObserver(function () { if (el.classList.contains('in')) { countUp(el); o.disconnect(); } }); o.observe(el, { attributes: true, attributeFilter: ['class'] }); }
  });

  // 4. Photos sombres : parallaxe au défilement
  var darks = document.querySelectorAll('.dark-photo');
  function onScroll() {
    darks.forEach(function (d) {
      var r = d.getBoundingClientRect(), vh = window.innerHeight;
      if (r.bottom < 0 || r.top > vh) return;
      var p = (r.top + r.height / 2 - vh / 2) / vh;
      d.querySelector('img').style.setProperty('--py', (p * -60).toFixed(1) + 'px');
    });
  }
  window.addEventListener('scroll', function () { requestAnimationFrame(onScroll); }, { passive: true }); onScroll();

  if (!fine) return;

  // 5. Bandeau d'ouverture : les taches suivent la souris, halo lumineux sous le curseur
  document.querySelectorAll('.ph').forEach(function (ph) {
    var mx = 0, my = 0, tx = 0, ty = 0, gx = 0, gy = 0, gtx = 0, gty = 0, raf = null;
    function loop() {
      mx += (tx - mx) * 0.06; my += (ty - my) * 0.06; gx += (gtx - gx) * 0.12; gy += (gty - gy) * 0.12;
      ph.style.setProperty('--mx', mx.toFixed(3)); ph.style.setProperty('--my', my.toFixed(3));
      ph.style.setProperty('--gx', gx.toFixed(1) + 'px'); ph.style.setProperty('--gy', gy.toFixed(1) + 'px');
      if (Math.abs(tx - mx) + Math.abs(ty - my) + Math.abs(gtx - gx) + Math.abs(gty - gy) > 0.01) raf = requestAnimationFrame(loop); else raf = null;
    }
    ph.addEventListener('pointermove', function (e) {
      var r = ph.getBoundingClientRect();
      tx = (e.clientX - r.left) / r.width * 2 - 1; ty = (e.clientY - r.top) / r.height * 2 - 1;
      gtx = e.clientX - r.left; gty = e.clientY - r.top;
      if (!ph.classList.contains('hot')) { gx = gtx; gy = gty; ph.classList.add('hot'); }
      if (!raf) raf = requestAnimationFrame(loop);
    });
    ph.addEventListener('pointerleave', function () { tx = 0; ty = 0; ph.classList.remove('hot'); if (!raf) raf = requestAnimationFrame(loop); });
  });

  // 6. Lumière sur les objets en dégradé + inclinaison des grandes cartes
  document.querySelectorAll('.mode, .cta-band, .mosaic .tile, .case, .card, .fig, .side').forEach(function (el) {
    el.classList.add('lit');
    el.addEventListener('pointermove', function (e) {
      var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
      el.style.setProperty('--lx', (x * 100).toFixed(1) + '%'); el.style.setProperty('--ly', (y * 100).toFixed(1) + '%');
      if (el.classList.contains('mode')) { el.classList.add('tilting'); el.style.setProperty('--ry', ((x - .5) * 6).toFixed(2) + 'deg'); el.style.setProperty('--rx', ((.5 - y) * 6).toFixed(2) + 'deg'); }
    });
    el.addEventListener('pointerleave', function () { el.classList.remove('tilting'); el.style.setProperty('--rx', '0deg'); el.style.setProperty('--ry', '0deg'); });
  });

  // 7. Boutons aimantés
  document.querySelectorAll('.btn, .arrow-link').forEach(function (b) {
    var t = b.classList.contains('arrow-link') ? b.querySelector('.c') : b;
    if (!t) return;
    b.addEventListener('pointermove', function (e) {
      var r = t.getBoundingClientRect();
      t.style.setProperty('--bx', ((e.clientX - r.left - r.width / 2) * 0.18).toFixed(1) + 'px');
      t.style.setProperty('--by', ((e.clientY - r.top - r.height / 2) * 0.28).toFixed(1) + 'px');
    });
    b.addEventListener('pointerleave', function () { t.style.setProperty('--bx', '0px'); t.style.setProperty('--by', '0px'); });
  });
})();

/* ---------- v3 : onglets métiers, fenêtres entreprises, filtres blog, newsletter, sommaire ---------- */
(function () {
  // Onglets
  document.querySelectorAll('.mt').forEach(function (mt) {
    var tabs = Array.prototype.slice.call(mt.querySelectorAll('.mt-tab'));
    function select(t, focus) {
      tabs.forEach(function (x) {
        var on = x === t, pan = document.getElementById(x.getAttribute('aria-controls'));
        x.setAttribute('aria-selected', on ? 'true' : 'false'); x.tabIndex = on ? 0 : -1;
        pan.hidden = !on; pan.classList.toggle('show', on);
      });
      if (focus) t.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t); });
      t.addEventListener('mouseenter', function () { if (window.matchMedia('(hover: hover)').matches) select(t); });
      t.addEventListener('keydown', function (e) {
        var k = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
        if (k) { e.preventDefault(); select(tabs[(i + k + tabs.length) % tabs.length], true); }
      });
    });
  });

  // Fenêtres entreprises
  var order = Array.prototype.map.call(document.querySelectorAll('dialog.cm'), function (d) { return d.id.replace('cm-', ''); });
  function open(id) {
    var d = document.getElementById('cm-' + id); if (!d) return false;
    document.querySelectorAll('dialog.cm[open]').forEach(function (o) { o.close(); });
    if (d.showModal) d.showModal(); else d.setAttribute('open', '');
    document.body.style.overflow = 'hidden';
    return true;
  }
  document.querySelectorAll('[data-open]').forEach(function (a) {
    a.addEventListener('click', function (e) { if (open(a.dataset.open)) e.preventDefault(); });
  });
  document.querySelectorAll('dialog.cm').forEach(function (d) {
    var id = d.id.replace('cm-', ''), i = order.indexOf(id);
    d.querySelector('.cm-x').addEventListener('click', function () { d.close(); });
    d.querySelector('.cm-prev').addEventListener('click', function () { open(order[(i - 1 + order.length) % order.length]); });
    d.querySelector('.cm-next').addEventListener('click', function () { open(order[(i + 1) % order.length]); });
    d.addEventListener('click', function (e) { if (e.target === d) d.close(); });
    d.addEventListener('close', function () { if (!document.querySelector('dialog.cm[open]')) document.body.style.overflow = ''; });
  });
  var h = (location.hash || '').replace('#', '');
  if (h && order.indexOf(h) > -1) setTimeout(function () { open(h); }, 350);

  // Filtres du blog
  var flts = document.querySelectorAll('.flt');
  flts.forEach(function (b) {
    b.addEventListener('click', function () {
      flts.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var f = b.dataset.f;
      document.querySelectorAll('.feat .post, #posts .post').forEach(function (p) { p.classList.toggle('hide', f !== 'all' && p.dataset.cat !== f); });
    });
  });

  // Newsletter
  var nf = document.getElementById('nform'), ns = document.getElementById('nstatus');
  if (nf) nf.addEventListener('submit', function (e) {
    e.preventDefault();
    if (nf.hasAttribute('data-preview')) { ns.textContent = 'Aperçu : l’inscription sera active une fois le site en ligne.'; return; }
    fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(new FormData(nf)).toString() })
      .then(function (r) { if (!r.ok) throw new Error(); nf.reset(); ns.textContent = 'Merci, vous êtes inscrit.'; })
      .catch(function () { ns.textContent = 'L’inscription a échoué. Réessayez dans un instant.'; });
  });

  // Sommaire de l'article : section en cours
  var links = document.querySelectorAll('.toc a');
  if (links.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) links.forEach(function (l) { l.classList.toggle('on', l.getAttribute('href') === '#' + e.target.id); }); });
    }, { rootMargin: '-20% 0px -70% 0px' });
    document.querySelectorAll('.prose h2[id]').forEach(function (h2) { io.observe(h2); });
  }
})();
