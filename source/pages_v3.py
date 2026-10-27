exec(open(os.path.join(B, 'iso.py')).read())
# Pages et sections ajoutées en v3 (exécuté dans build.py, après les définitions de base)

COMPANIES = [
    dict(id='numa', name='Nüma', sector='Sécurité', year='2025', mode='BUILD', img='numa.jpg', g='g-peche', il='strates', ilc='p',
         tagline='L’alarme professionnelle que l’on configure soi-même.',
         desc='La nouvelle façon de sécuriser son logement. Une alarme professionnelle configurée en ligne en quelques minutes, au prix affiché, avec un matériel qui vous appartient et une télésurveillance sans engagement.',
         points=['Configurateur en ligne, prix affiché en temps réel', 'Matériel Ajax qui appartient au client', 'Pose par soi-même ou par un technicien certifié', 'Télésurveillance à 19,99 € par mois, résiliable'],
         role='Co-fondation, structuration de la croissance, acquisition digitale.'),
    dict(id='aurus', name='Aurus System', sector='Sécurité', year='2025', mode='BUILD', img='aurus.jpg', g='g-orange', il='trame', ilc='o7',
         tagline='La sécurité des chantiers, de l’audit à la maintenance.',
         desc='Sécurise les chantiers et les bâtiments professionnels, en installation temporaire ou permanente, avec télésurveillance 24/7. Un seul interlocuteur de l’audit à la maintenance.',
         points=['Installation temporaire ou permanente', 'Télésurveillance 24/7', 'Un seul interlocuteur, de l’audit à la maintenance', 'Île-de-France et Orléans'],
         role='Co-fondation, structuration de la croissance.'),
    dict(id='capfield', name='CapField', sector='Services techniques', year='2026', mode='BUILD', img='capfield.jpg', g='g-peche', il='trame', ilc='p',
         tagline='Le réseau d’intervenants de proximité.',
         desc='Réseau d’intervenants de proximité qui réalise les poses, contrôles et remises en service pour les entreprises qui déploient des équipements sur le terrain.',
         points=['Poses, contrôles et remises en service', 'Un prix à l’acte', 'Une preuve d’intervention systématique', 'Pour les entreprises du groupe et pour des tiers'],
         role='Co-fondation avec un opérateur issu de l’industrie, structuration du modèle et de l’outil de pilotage.'),
    dict(id='taskia', name='Taskia', sector='Services aux indépendants', year=None, mode=None, img=None, g='g-lilas', il='arcs', ilc='l7',
         tagline='L’assistant administratif des artisans, dans WhatsApp.',
         desc='Un assistant opérationnel dans WhatsApp pour les indépendants, les artisans et les petites entreprises. Devis, factures, rendez-vous et relances se gèrent par simple message écrit ou vocal.',
         points=['Devis, factures, rendez-vous et relances', 'Par message écrit ou vocal, dans WhatsApp', 'Un relais humain pour les missions complexes', 'Aucun nouvel outil à apprendre'],
         role='[À préciser]'),
]

METIERS = [
    dict(id='securite', name='Sécurité électronique', icon='shield-check', g='g-orange', il='trame', ilc='o7',
         text='Protéger les sites, les chantiers et les personnes, de l’installation à la télésurveillance.',
         items=['Alarme intrusion', 'Vidéosurveillance', 'Contrôle d’accès', 'Télésurveillance', 'Sécurité incendie', 'Interphonie']),
    dict(id='batiment', name='Bâtiment second œuvre', icon='paint-roller', g='g-peche', il='strates', ilc='p',
         text='Les corps de métier qui font vivre un bâtiment, du chantier neuf à la rénovation.',
         items=['Électricité', 'Plomberie et chauffage', 'CVC', 'Menuiserie', 'Peinture et finitions', 'Rénovation énergétique']),
    dict(id='techniques', name='Services techniques', icon='wrench', g='g-lilas', il='arcs', ilc='l7',
         text='Les équipes qui installent, entretiennent et dépannent, chaque jour sur le terrain.',
         items=['Installation', 'Maintenance', 'Dépannage', 'Déploiement terrain', 'Contrôle et mise en service']),
    dict(id='entreprises', name='Services aux entreprises', icon='buildings', g='g-soleil', il='rosace', ilc='o7',
         text='Les services qui font tourner les sites et les bureaux de nos clients.',
         items=['Nettoyage', 'Gardiennage', 'Facility management', 'Multiservice']),
]

POSTS = [
    dict(slug='article.html', cat='Guides', title='Reprendre une entreprise du bâtiment, étape par étape', excerpt='Du premier contact avec le cédant aux cent premiers jours, ce qu’il faut préparer pour réussir une reprise.', img='grue.jpg', read='8 min'),
    dict(slug='article.html', cat='Actualités', title='Capstone lance CapField, son réseau d’intervenants de proximité', excerpt='Poses, contrôles et remises en service. Une nouvelle entreprise rejoint le groupe.', img='capfield.jpg', read='3 min'),
    dict(slug='article.html', cat='Guides', title='Par où commencer pour digitaliser l’acquisition d’une PME de services', excerpt='Site, référencement, avis clients. Les premiers chantiers qui changent vraiment le carnet de commandes.', img='chantier.jpg', read='6 min'),
    dict(slug='article.html', cat='Guides', title='Structurer sa croissance quand tout passe par le dirigeant', excerpt='Les signes qui montrent qu’une entreprise a atteint un palier, et comment le dépasser.', img=None, g='g-lilas', il='rosace', ilc='l7', read='7 min'),
    dict(slug='article.html', cat='Actualités', title='Nüma et Aurus System, deux entreprises co-fondées en 2025', excerpt='Retour sur la première année du groupe dans la sécurité électronique.', img='aurus.jpg', read='4 min'),
    dict(slug='article.html', cat='Guides', title='Ce qu’il faut regarder avant de signer un contrat de télésurveillance', excerpt='Engagement, propriété du matériel, temps d’intervention. Les questions à poser.', img='numa.jpg', read='5 min'),
]

def post_card(p, big=False):
    media = f'<img src="img/{p["img"]}" alt="" loading="lazy">' if p.get('img') else f'<div class="pc-ill grain {p["g"]}">{illu(p["il"], p["ilc"])}</div>'
    cls = 'post big' if big else 'post'
    return f'''<a class="{cls}" href="{p["slug"]}" data-cat="{p["cat"]}">
  <div class="pc-media">{media}<span class="pc-tag">{p["cat"]}</span></div>
  <div class="pc-body"><span class="pc-meta">Exemple · {p["read"]} de lecture</span><h3>{p["title"]}</h3><p>{p["excerpt"]}</p><span class="arrow-link"><span class="c">{ARROW}</span>Lire l’article</span></div>
</a>'''

def blog_teaser():
    return f'''<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Blog</span><h2 class="d2">Actualités et guides.</h2></div>
      <div style="justify-self:end;display:grid;gap:24px"><p class="lead">Les nouvelles du groupe et des guides pratiques pour les dirigeants des métiers concrets.</p><a class="arrow-link" href="blog.html"><span class="c">{ARROW}</span>Tous les articles</a></div>
    </div>
    <div class="posts">{''.join(post_card(p) for p in POSTS[:3])}</div>
  </div>
</section>'''

def metiers_tabs():
    tabs = ''.join(f'<button class="mt-tab" role="tab" id="tab-{m["id"]}" aria-controls="pan-{m["id"]}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{ico(m["icon"])}<span>{m["name"]}</span><small>{len(m["items"])}</small></button>' for i, m in enumerate(METIERS))
    pans = ''.join(f'''<div class="mt-pan grain {m["g"]}" role="tabpanel" id="pan-{m["id"]}" aria-labelledby="tab-{m["id"]}"{"" if i == 0 else " hidden"}>
      <div class="mt-top"><h3>{m["name"]}</h3>{illu(m["il"], m["ilc"])}</div>
      <p>{m["text"]}</p>
      <ul class="mt-list">{"".join(f"<li>{x}</li>" for x in m["items"])}</ul>
    </div>''' for i, m in enumerate(METIERS))
    return f'''<section class="sec" id="metiers">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Les métiers</span><h2 class="d2">Des métiers concrets, <span class="grey">ancrés dans le réel.</span></h2></div>
      <p class="lead">Nous co-fondons et accompagnons des entreprises dans quatre familles de métiers, où l’équipement, la structuration et le digital changent la donne.</p>
    </div>
    <div class="mt">
      <div class="mt-tabs" role="tablist" aria-label="Familles de métiers">{tabs}</div>
      <div class="mt-pans">{pans}</div>
    </div>
  </div>
</section>'''

def faq_block(items, title='Questions fréquentes', sub='Les réponses aux questions que l’on nous pose le plus souvent.', bg='bg-paper', labelcls=''):
    qs = ''.join(f'<details><summary>{q}<span class="pm">{PLUS}</span></summary><p>{a}</p></details>' for q, a in items)
    return f'''<section class="sec {bg}" id="faq">
  <div class="wrap faq2">
    <div class="faq2-side">
      <span class="label {labelcls}">FAQ</span>
      <h2 class="d2" style="margin-top:24px">{title}</h2>
      <p class="lead" style="margin-top:20px">{sub}</p>
      <div class="faq2-more">{ico('chat-circle-text')}<div><b>Une autre question ?</b><a class="arrow-link" href="contact.html"><span class="c">{ARROW}</span>Écrivez-nous</a></div></div>
    </div>
    <div class="faq" style="margin-top:0">{qs}</div>
  </div>
</section>'''

FAQ_HOME = [
    ('Qu’est-ce qu’un venture studio ?', 'Un venture studio co-fonde des entreprises. Il prend des responsabilités et une participation au capital, apporte l’équipe et les outils, et s’associe à un expert du métier. Ce n’est pas un fonds d’investissement. Capstone le fait dans les secteurs traditionnels, avec une forte composante digitale.'),
    ('Quelle différence entre BUILD et ADVISE ?', 'Avec BUILD, nous co-fondons pour créer ou reprendre une entreprise. Avec ADVISE, nous aidons une entreprise existante à passer un palier, et nous intervenons en task force ou en advisory board.'),
    ('Dans quels métiers intervenez-vous ?', 'Sécurité électronique, bâtiment second œuvre, services techniques et services aux entreprises.'),
    ('Quelle taille d’entreprise accompagnez-vous ?', 'De la création jusqu’à des entreprises de plus de 20 M€ de chiffre d’affaires. Ce qui compte, c’est un métier solide et l’envie de structurer la croissance.'),
    ('Où intervenez-vous ?', 'En France et en Belgique.'),
    ('Comment se passe le premier échange ?', 'Vous nous présentez votre projet ou votre entreprise en quelques lignes. Nous revenons vers vous sous 5 jours ouvrés pour un premier rendez-vous, sans engagement.'),
]

def co_card(c):
    media = f'<img src="img/{c["img"]}" alt="" loading="lazy">' if c['img'] else ''
    tint = '' if c['img'] else f' tint grain {c["g"]}'
    ill = '' if c['img'] else illu(c['il'], c['ilc'])
    meta = ''.join(f'<span class="pill">{x}</span>' for x in [c['sector'], c['year']] if x)
    return f'<a class="co{tint}" href="portfolio.html#{c["id"]}" data-open="{c["id"]}">{media}{ill}<div class="meta">{meta}</div><h3>{c["name"]}</h3><p>{c["tagline"]}</p></a>'

def co_dialogs():
    out = ''
    for c in COMPANIES:
        media = f'<img src="img/{c["img"]}" alt="{c["name"]}">' if c['img'] else f'<div class="cm-ill grain {c["g"]}">{illu(c["il"], c["ilc"])}<span class="cap">Photo à fournir</span></div>'
        pills = ''.join(f'<span>{x}</span>' for x in [c['sector'], c['year'], c['mode']] if x)
        pts = ''.join(f'<li>{ico("check-circle")}{p}</li>' for p in c['points'])
        out += f'''<dialog class="cm" id="cm-{c["id"]}" aria-labelledby="cm-{c["id"]}-t">
  <div class="cm-in">
    <div class="cm-media">{media}</div>
    <div class="cm-body">
      <div class="cm-bar"><div class="cm-pills">{pills}</div><button class="cm-x" type="button" aria-label="Fermer">{ico('x')}</button></div>
      <h2 id="cm-{c["id"]}-t">{c["name"]}</h2>
      <p class="cm-lead">{c["desc"]}</p>
      <ul class="cm-pts">{pts}</ul>
      <div class="cm-role"><small>Rôle de Capstone</small>{c["role"]}</div>
      <div class="cm-nav"><button type="button" class="cm-prev">{ico('arrow-left')}Précédente</button><button type="button" class="cm-next">Suivante{ico('arrow-right')}</button></div>
    </div>
  </div>
</dialog>'''
    return out

def cta_multi():
    return f'''<section class="wrap" style="margin-top:var(--sec)">
  <div class="cta-band grain g-soleil cta-multi">
    <div><span class="label k">Travailler avec nous</span><h2>Prêt à bâtir ?</h2><p class="lead">Dites-nous d’où vous partez, nous vous orientons vers le bon format.</p></div>
    <div class="cta-doors">
      <a href="contact.html#build">{ico('rocket-launch')}<span><b>Je porte un projet</b><small>Créer ou reprendre</small></span>{ARROW}</a>
      <a href="contact.html#advise">{ico('buildings')}<span><b>Je dirige une entreprise</b><small>Passer un palier</small></span>{ARROW}</a>
      <a href="contact.html#partenaire">{ico('handshake')}<span><b>Je suis partenaire</b><small>Déployer ensemble</small></span>{ARROW}</a>
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------- Accueil v3
def home():
    return page_head('Capstone', 'Capstone co-fonde et développe des entreprises dans la sécurité, le bâtiment et les services.') + header('./') + f'''
<main>
<section class="ph">
  <div class="mesh grain" aria-hidden="true"></div>
  <div class="wrap ph-in">
    <span class="label">Venture studio et operating partner</span>
    <h1 class="d1" style="max-width:9.6em">Bâtir des entreprises <span class="grey">qui durent.</span></h1>
    <div class="ph-foot">
      <p class="lead">Nous co-fondons et développons des entreprises dans <span class="rot" id="rot" data-words="la sécurité|le bâtiment|les services">la sécurité</span>. Associés, sur le terrain, et dans la durée.</p>
      <div class="ctas"><a class="btn" href="contact.html">Présenter un projet {ARROW}</a><a class="btn ghost" href="portfolio.html">Nos entreprises</a></div>
    </div>
  </div>
  <div class="wrap">
    <p class="intro-big">Capstone est le venture studio des secteurs traditionnels. <span>Nous co-fondons et développons, main dans la main avec celles et ceux qui font ces métiers, des entreprises qui durent, à chaque étape de leur parcours.</span></p>
    <div class="stages">
      <a class="stage" href="build.html">
        <span class="st-range">De 0 à 1</span>
        <h2 class="st-title">Build</h2>
        <span class="st-sub">Venture studio</span>
        {plan_svg('build', 'o')}
        <p>Créer ou reprendre une entreprise. Nous co-fondons avec vous.</p>
        <span class="arrow-link"><span class="c">{ARROW}</span>Découvrir Build</span>
      </a>
      <a class="stage" href="advise.html">
        <span class="st-range">De 10 à 100</span>
        <h2 class="st-title">Advise</h2>
        <span class="st-sub">Operating partner</span>
        {plan_svg('advise', 'l')}
        <p>Faire passer un palier à une entreprise établie.</p>
        <span class="arrow-link"><span class="c">{ARROW}</span>Découvrir Advise</span>
      </a>
    </div>
  </div>
  <div style="height:clamp(48px,6vw,88px)"></div>
</section>

<div class="ticker" aria-hidden="true"><div class="track">{''.join(''.join(f'<span>{x}</span>' for x in ['Sécurité électronique', 'Bâtiment', 'Services techniques', 'Services aux entreprises']) for _ in range(3))}</div></div>

<section class="dark-photo">
  <img src="img/chantier.jpg" alt="" loading="lazy">
  <div class="wrap">
    <div>
      <span class="label w">Notre approche</span>
      <h2>Pas des conseillers.<br>Des associés.</h2>
      <p class="lead">Nous prenons des responsabilités et une participation au capital, nous menons les sujets clés, et nous restons. Nous travaillons avec les équipes pour faire avancer l’entreprise, pas pour rendre un rapport.</p>
    </div>
    <div>
      <p class="chips-title">Ce que nous apportons</p>
      <div class="chips">
        <span class="chip">{ico('coins')}Responsabilité et participation au capital</span>
        <span class="chip">{ico('strategy')}Structuration de la croissance</span>
        <span class="chip">{ico('megaphone')}Acquisition digitale</span>
        <span class="chip">{ico('gear-six')}Outils et automatisation</span>
        <span class="chip">{ico('chart-line-up')}Pilotage et reporting</span>
        <span class="chip">{ico('user-circle-plus')}Recrutement</span>
        <span class="chip">{ico('handshake')}Réseau et accès marché</span>
      </div>
    </div>
  </div>
</section>

{metiers_tabs()}

<section class="sec bg-orange">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Pourquoi ces métiers</span><h2 class="d2">Des entreprises solides, <span style="color:var(--orange-700)">qui ont tout pour aller plus loin.</span></h2></div>
      <p class="lead" style="color:var(--ink-2)">La sécurité, le bâtiment et les services font tourner le quotidien. Ces entreprises ont des clients fidèles et un vrai savoir-faire. Elles partagent souvent les mêmes freins, avec une acquisition au bouche-à-oreille, peu d’outils et un dirigeant qui porte tout. C’est là que nous intervenons.</p>
    </div>
    <div class="cards">
      <div class="card">{ico('hard-hat')}<h3>Un savoir-faire réel</h3><p>Des équipes qui maîtrisent leur métier et des clients qui leur font confiance depuis des années.</p></div>
      <div class="card">{ico('lightning')}<h3>Des leviers encore inexploités</h3><p>Le digital, les outils et la structuration de la croissance changent la donne, et restent rares dans ces secteurs.</p></div>
      <div class="card">{ico('key')}<h3>Une relève à construire</h3><p>De nombreuses entreprises vont changer de mains dans les prochaines années. Nous aidons à les reprendre et à les moderniser.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Portfolio</span><h2 class="d2">Ce que nous avons construit.</h2></div>
      <div style="justify-self:end;display:grid;gap:24px"><p class="lead">Un écosystème, pas un portefeuille. Nos entreprises servent les mêmes mondes et se renforcent entre elles.</p><a class="arrow-link" href="portfolio.html"><span class="c">{ARROW}</span>Voir le portfolio</a></div>
    </div>
    <div class="cos">{''.join(co_card(c) for c in COMPANIES)}</div>
  </div>
</section>

<section class="quote-sec grain g-lilas">
  <div class="wrap">
    {ico('quotes', 'ico q-ico')}
    <blockquote>La valeur se crée en exécutant, <span>pas en recommandant.</span></blockquote>
    <div class="q-by">
      <div class="q-faces"><img src="img/charles.jpg" alt=""></div>
      <div><b>Charles Vosters</b><span>Associé, Capstone</span></div>
      <a class="arrow-link" href="about.html" style="margin-left:auto"><span class="c">{ARROW}</span>Qui sommes-nous</a>
    </div>
  </div>
</section>

{faq_block(FAQ_HOME, bg='')}

{blog_teaser() if SHOW_BLOG else ''}
''' + cta_multi() + '\n</main>\n' + co_dialogs() + FOOTER

# ---------------------------------------------------------------- Portfolio v3
def portfolio():
    cards = ''
    for c in COMPANIES:
        media = f'<img src="img/{c["img"]}" alt="" loading="lazy">' if c['img'] else f'<div class="pf-ill grain {c["g"]}">{illu(c["il"], c["ilc"])}</div>'
        pills = ''.join(f'<span>{x}</span>' for x in [c['sector'], c['year'], c['mode']] if x)
        cards += f'''<a class="pf" href="#{c["id"]}" data-open="{c["id"]}">
  <div class="pf-media">{media}</div>
  <div class="pf-body"><div class="pf-pills">{pills}</div><h3>{c["name"]}</h3><p>{c["tagline"]}</p><span class="arrow-link"><span class="c">{PLUS}</span>Découvrir l’activité</span></div>
</a>'''
    return page_head('Capstone Portfolio', 'Les entreprises du groupe Capstone : Nüma, Aurus System, CapField et Taskia.') + header('portfolio.html') + '\n<main>\n' + ph(
        'Portfolio', 'Portfolio', 'Un écosystème, pas un portefeuille.',
        'Nos entreprises servent les mêmes mondes et se renforcent entre elles. Cliquez sur une entreprise pour découvrir son activité.',
        f'<a class="btn ghost" href="#entreprises">Voir les entreprises</a>') + f'''
<section class="bg-paper" id="entreprises" style="padding-bottom:var(--sec)">
  <div class="wrap">
    <div class="pfs">{cards}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Comment elles se renforcent</span><h2 class="d2">Chaque nouvelle entreprise profite <span class="grey">de celles qui existent déjà.</span></h2></div>
      <p class="lead">Aurus System et Nüma équipent les chantiers et les sites. CapField exécute sur le terrain pour elles et pour des tiers. Taskia outille les artisans qui composent ce réseau.</p>
    </div>
    <div class="eco">
      <div class="g-orange grain"><span class="v">Équipe les chantiers</span><b>Aurus System</b><span>Sécurité des chantiers et bâtiments professionnels.</span></div>
      <div class="g-peche grain"><span class="v">Équipe les sites</span><b>Nüma</b><span>Alarme professionnelle pour particuliers et petits pros.</span></div>
      <div style="background:var(--paper)"><span class="v">Exécute sur le terrain</span><b>CapField</b><span>Pour les entreprises du groupe et pour des tiers.</span></div>
      <div class="g-lilas grain"><span class="v">Outille les artisans</span><b>Taskia</b><span>Les indépendants qui composent le réseau.</span></div>
    </div>
  </div>
</section>

<section class="dark-photo">
  <img src="img/grue.jpg" alt="" loading="lazy">
  <div class="wrap">
    <div>
      <span class="label w">Et la suite</span>
      <h2>La prochaine, c’est peut-être la vôtre.</h2>
      <p class="lead">Nous co-fondons avec des experts de leur métier, dans la sécurité, le bâtiment et les services.</p>
    </div>
    <div><a class="btn white" href="build.html">Découvrir Capstone BUILD {ARROW}</a></div>
  </div>
</section>
''' + '\n</main>\n' + co_dialogs() + FOOTER

# ---------------------------------------------------------------- À propos
def about():
    return page_head('Capstone À propos', 'Capstone, venture studio franco-belge fondé en 2025, co-fonde et développe des entreprises dans les secteurs traditionnels.') + header('about.html') + '\n<main>\n' + ph(
        'À propos', 'À propos', 'Au service des métiers concrets.',
        'Capstone co-fonde et développe des entreprises dans la sécurité, le bâtiment et les services. Nous les bâtissons avec celles et ceux qui font ces métiers, pour qu’elles durent.',
        f'<a class="btn" href="contact.html">Nous rencontrer {ARROW}</a>') + f'''
<div class="ph-media">
  <div class="wrap"><div class="frame"><img src="img/chantier.jpg" alt="Chantier de nuit" style="object-position:50% 60%"></div></div>
</div>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Notre parcours</span><h2 class="d2">Un groupe qui grandit, <span class="grey">entreprise après entreprise.</span></h2></div>
      
    </div>
    <ol class="timeline">
      <li><span class="y num">2025</span><h3>Capstone</h3><p>Création du venture studio, en France et en Belgique.</p></li>
      <li><span class="y num">2025</span><h3>Nüma</h3><p>L’alarme professionnelle que l’on configure soi-même.</p></li>
      <li><span class="y num">2025</span><h3>Aurus System</h3><p>La sécurité des chantiers et des bâtiments professionnels.</p></li>
      <li class="now"><span class="y num">2026</span><h3>CapField</h3><p>Le groupe s’étend aux services techniques sur le terrain.</p></li>
    </ol>
  </div>
</section>

<section class="sec bg-orange">
  <div class="wrap">
    <span class="label">Notre mission</span>
    <p class="mission">Apporter aux entreprises des secteurs traditionnels l’excellence digitale, opérationnelle et commerciale qui leur manque, <span>et bâtir avec elles des entreprises qui durent.</span></p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Nos principes</span><h2 class="d2">Trois principes, <span class="grey">parce que nous sommes associés.</span></h2></div>
    </div>
    <div class="cards">
      <div class="card big paper">{illu('strates','')}<span class="n">01 · ASSOCIÉS</span><h3>Alignés</h3><p>Nous partageons les responsabilités et le capital, et nous gagnons quand l’entreprise gagne.</p></div>
      <div class="card big paper">{illu('trame','p')}<span class="n">02 · SUR LE TERRAIN</span><h3>Opérationnels</h3><p>Nous exécutons avec les équipes, de la structuration de la croissance aux outils.</p></div>
      <div class="card big paper">{illu('rosace','l')}<span class="n">03 · DANS LE TEMPS</span><h3>Durables</h3><p>Nous ne cherchons pas la sortie rapide. Nous restons au capital et au conseil.</p></div>
    </div>
  </div>
</section>

''' + cta() + '\n</main>\n' + FOOTER

# ---------------------------------------------------------------- Blog
def blog(preview):
    pv = ' data-preview' if preview else ''
    return page_head('Capstone Blog', 'Actualités du groupe Capstone et guides pratiques pour les dirigeants des secteurs traditionnels.') + header('blog.html') + '\n<main>\n' + ph(
        'Blog', 'Blog', 'Actualités et guides pour les métiers concrets.',
        'Les nouvelles du groupe et des guides pratiques pour créer, reprendre et développer une entreprise dans la sécurité, le bâtiment et les services.',
        '') + f'''
<section class="sec" style="padding-top:clamp(40px,5vw,64px)">
  <div class="wrap">
    <p class="note">{ico('info')}Articles d’exemple pour montrer la mise en page, à remplacer par vos contenus.</p>
    <div class="filters" role="group" aria-label="Filtrer les articles">
      <button type="button" class="flt" aria-pressed="true" data-f="all">Tous</button>
      <button type="button" class="flt" aria-pressed="false" data-f="Actualités">Actualités</button>
      <button type="button" class="flt" aria-pressed="false" data-f="Guides">Guides</button>
    </div>
    <div class="feat">{post_card(POSTS[0], big=True)}</div>
    <div class="posts" id="posts">{''.join(post_card(p) for p in POSTS[1:])}</div>
  </div>
</section>

<section class="wrap">
  <div class="news grain g-lilas">
    <div><span class="label l">Newsletter</span><h2>Un article par mois, rien de plus.</h2><p class="lead">Les nouvelles du groupe et nos guides, directement dans votre boîte mail.</p></div>
    <form class="news-form" name="newsletter" method="POST" data-netlify="true" id="nform"{pv}>
      <input type="hidden" name="form-name" value="newsletter">
      <label class="sr" for="n-mail">E-mail</label>
      <input id="n-mail" name="email" type="email" placeholder="votre@email.com" required autocomplete="email">
      <button class="btn" type="submit">S’inscrire {ARROW}</button>
      <span class="status" id="nstatus" role="status"></span>
    </form>
  </div>
</section>
''' + '\n</main>\n' + FOOTER

# ---------------------------------------------------------------- Article (modèle)
def article():
    toc = [('clarifier', 'Clarifier son projet'), ('cible', 'Trouver la bonne entreprise'), ('evaluer', 'Évaluer avant de s’engager'), ('financer', 'Financer la reprise'), ('cent-jours', 'Préparer les cent premiers jours')]
    return page_head('Reprendre une entreprise du bâtiment', 'Guide Capstone sur les étapes clés pour reprendre une entreprise du bâtiment.') + header('blog.html') + f'''
<main>
<section class="ph art-hero">
  <div class="mesh grain" aria-hidden="true"></div>
  <div class="wrap ph-in" style="padding-bottom:clamp(40px,5vw,64px)">
    <a class="back" href="blog.html">{ico('arrow-left')}Tous les articles</a>
    <div class="art-meta"><span class="pc-tag static">Guides</span><span>Exemple · 8 min de lecture</span></div>
    <h1 class="d2" style="max-width:14em;margin-top:20px">Reprendre une entreprise du bâtiment, étape par étape</h1>
    <p class="lead" style="margin-top:24px">Du premier contact avec le cédant aux cent premiers jours, ce qu’il faut préparer pour réussir une reprise.</p>
  </div>
</section>
<div class="ph-media"><div class="wrap"><div class="frame"><img src="img/grue.jpg" alt="Grue de chantier" style="object-position:50% 100%"></div></div></div>

<section class="sec">
  <div class="wrap art">
    <aside class="toc"><span class="label">Sommaire</span><ol>{''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)}</ol>
      <div class="share"><span>Partager</span><a href="https://www.linkedin.com/" rel="noopener" aria-label="Partager sur LinkedIn">{ico('linkedin-logo')}</a></div></aside>
    <article class="prose">
      <p class="note">{ico('info')}Article d’exemple pour montrer la mise en page.</p>
      <p class="intro">D’ici 2030, 370 000 TPE, PME et ETI françaises pourraient être à céder. Dans le bâtiment, beaucoup sont des entreprises saines, avec une clientèle fidèle et un savoir-faire réel. Les reprendre est une formidable opportunité, à condition de s’y préparer.</p>
      <h2 id="clarifier">1. Clarifier son projet</h2>
      <p>Avant de chercher une cible, il faut savoir ce que l’on cherche : quel métier, quelle taille, quelle zone géographique, quel rôle on veut tenir. Un expert technique et un profil commercial ne reprendront pas la même entreprise.</p>
      <h2 id="cible">2. Trouver la bonne entreprise</h2>
      <p>Les meilleures opportunités circulent rarement sur les plateformes. Le réseau, les fournisseurs, les experts-comptables et les chambres de métiers sont souvent les premières sources.</p>
      <blockquote>Une bonne reprise commence par une bonne relation avec le cédant.</blockquote>
      <h2 id="evaluer">3. Évaluer avant de s’engager</h2>
      <p>Au-delà des comptes, regardez la dépendance au dirigeant, la qualité des équipes, le carnet de commandes et l’état des outils. C’est souvent là que se cachent les vrais leviers de croissance.</p>
      <ul><li>Quelle part du chiffre d’affaires dépend du dirigeant ?</li><li>Les process sont-ils écrits ou dans les têtes ?</li><li>Comment arrivent les nouveaux clients ?</li></ul>
      <h2 id="financer">4. Financer la reprise</h2>
      <p>Apport personnel, dette bancaire, crédit vendeur ou investisseurs, la structure du financement conditionne la marge de manœuvre des premières années.</p>
      <h2 id="cent-jours">5. Préparer les cent premiers jours</h2>
      <p>Rencontrer chaque collaborateur, rassurer les clients clés, sécuriser la trésorerie, puis lancer les premiers chantiers de structuration, des outils à l’acquisition et au pilotage.</p>
      <div class="art-cta grain g-orange"><div><b>Vous préparez une reprise ?</b><span>Capstone BUILD peut co-reprendre avec vous.</span></div><a class="btn" href="build.html">Découvrir BUILD {ARROW}</a></div>
    </article>
  </div>
</section>

<section class="sec bg-paper">
  <div class="wrap">
    <div class="sec-head"><div><span class="label">À lire aussi</span><h2 class="d2">Dans la même veine.</h2></div><a class="arrow-link" href="blog.html" style="justify-self:end"><span class="c">{ARROW}</span>Tous les articles</a></div>
    <div class="posts">{''.join(post_card(p) for p in POSTS[2:5])}</div>
  </div>
</section>
</main>
''' + FOOTER


# ---------------------------------------------------------------- Mentions légales et confidentialité
def mentions():
    return page_head('Capstone Mentions légales', 'Mentions légales et politique de confidentialité du site Capstone.', 'mentions.html') + header('') + f'''
<main>
<section class="ph" style="padding-bottom:0">
  <div class="mesh grain" aria-hidden="true"></div>
  <div class="wrap ph-in" style="padding-bottom:clamp(32px,4vw,48px)"><span class="label">Informations légales</span><h1 class="d2" style="margin-top:20px">Mentions légales et confidentialité</h1></div>
</section>
<section class="sec" style="padding-top:clamp(40px,5vw,64px);padding-bottom:0">
  <div class="wrap"><article class="prose">
    <h2>Éditeur du site</h2>
    <p>[RAISON SOCIALE], [FORME JURIDIQUE] au capital de [MONTANT] €<br>Siège social [ADRESSE]<br>[RCS / SIREN ou numéro BCE] · TVA [NUMÉRO]<br>Contact {SITE["email"]}</p>
    <p>Directeur de la publication [NOM].</p>
    <h2>Hébergement</h2>
    <p>Netlify, Inc., 512 2nd Street, Suite 200, San Francisco, CA 94107, États-Unis. netlify.com</p>
    <h2>Propriété intellectuelle</h2>
    <p>Les textes, visuels, logos et illustrations de ce site appartiennent à Capstone ou à ses entreprises. Toute reproduction sans autorisation écrite est interdite.</p>
    <h2>Données personnelles</h2>
    <p>Les informations envoyées par le formulaire de contact (nom, e-mail, entreprise, téléphone, message) servent uniquement à répondre à votre demande. Elles sont conservées au plus trois ans après le dernier échange et ne sont jamais cédées.</p>
    <p>Vous pouvez demander l’accès, la rectification ou la suppression de vos données en écrivant à {SITE["email"]}. Vous pouvez aussi saisir la CNIL (France) ou l’Autorité de protection des données (Belgique).</p>
    <h2>Cookies</h2>
    <p>Ce site n’utilise ni cookie publicitaire ni outil de mesure d’audience. Aucun bandeau de consentement n’est donc nécessaire.</p>
  </article></div>
</section>
</main>
''' + FOOTER

def notfound():
    return page_head('Page introuvable · Capstone', 'Cette page n’existe pas ou a été déplacée.', '404.html') + header('') + f'''
<main>
<section class="ph" style="min-height:70vh">
  <div class="mesh grain" aria-hidden="true"></div>
  <div class="wrap ph-in"><span class="label">Erreur 404</span><h1 class="d1">Page introuvable.</h1><span class="ph-sub">Cette page n’existe pas ou a été déplacée.</span>
  <div class="ph-foot"><p class="lead"></p><div class="ctas"><a class="btn" href="./">Retour à l’accueil {ARROW}</a></div></div></div>
</section>
</main>
''' + FOOTER
