import json, re, os, sys, shutil
B = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(B)
V = os.path.join(B, 'vendor')
ILL = json.load(open(os.path.join(V, 'illus.json')))
PH = os.path.join(V, 'icons')
PROD = '--prod' in sys.argv

def ico(name, cls='ico'):
    s = open(f'{PH}/{name}.svg').read()
    s = re.sub(r'<svg[^>]*>', f'<svg class="{cls}" viewBox="0 0 256 256" fill="currentColor" aria-hidden="true">', s, count=1)
    return s

def illu(name, cls=''):
    inner = re.sub(r'<(path|circle)', r'<\1 pathLength="1"', ILL[name])
    kind = {'rosace': 'spin', 'strates': 'stack'}.get(name, 'bob')
    return f'<svg class="illu {cls} {kind}" viewBox="0 0 240 240" aria-hidden="true">{inner}</svg>'

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 12L12 4M5.5 4H12V10.5"/></svg>'
PLUS = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M8 2V14M2 8H14"/></svg>'

SITE = dict(
    domain='https://capstone.ac',
    email='[E-MAIL]',
    phone='[TÉLÉPHONE]',
    linkedin='https://www.linkedin.com/',  # URL de la page LinkedIn Capstone
)
SHOW_BLOG = False   # le blog reste préparé mais n'est ni lié ni publié

NAV = [('build.html', 'Build'), ('advise.html', 'Advise'), ('portfolio.html', 'Portfolio'), ('about.html', 'À propos')] + ([('blog.html', 'Blog')] if SHOW_BLOG else []) + [('contact.html', 'Contact')]

def header(cur):
    AC = ' aria-current="page"'
    links = ''.join(f'<a href="{h}"{AC if h == cur else ""}>{t}</a>' for h, t in NAV)
    mlinks = ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in [('./', 'Accueil')] + NAV)
    return f'''<header class="top">
  <div class="wrap">
    <a class="wordmark" href="./" aria-label="Capstone, accueil">Capstone.</a>
    <nav class="nav" aria-label="Navigation principale">{links}</nav>
    <a class="btn s" href="contact.html">Présenter un projet {ARROW}</a>
    <button class="menu-btn" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mnav">{ico('list')}</button>
  </div>
</header>
<div class="mobile-nav" id="mnav" hidden>
  <div class="row"><span class="wordmark">Capstone.</span><button type="button" aria-label="Fermer le menu">{ico('x')}</button></div>
  <ul>{mlinks}</ul>
  <a class="btn white" href="contact.html">Présenter un projet {ARROW}</a>
</div>'''

BLOGLI = '<li><a href="blog.html">Blog</a></li>' if SHOW_BLOG else ''
EMAIL, LINKEDIN = SITE['email'], SITE['linkedin']

FOOTER = f'''<footer>
  <div class="wrap foot-in">
    <div class="foot-cols">
      <div><p class="big">Nous co-fondons et développons des entreprises dans les secteurs traditionnels.</p></div>
      <div><h4>Capstone</h4><ul><li><a href="build.html">Build · Venture studio</a></li><li><a href="advise.html">Advise · Operating partner</a></li><li><a href="portfolio.html">Portfolio</a></li><li><a href="about.html">À propos</a></li>{BLOGLI}<li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Entreprises</h4><ul><li><a href="portfolio.html#numa">Nüma</a></li><li><a href="portfolio.html#aurus">Aurus System</a></li><li><a href="portfolio.html#capfield">CapField</a></li><li><a href="portfolio.html#taskia">Taskia</a></li></ul></div>
      <div><h4>Nous écrire</h4><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{LINKEDIN}" rel="noopener">LinkedIn</a></li><li>Rue Emile Francqui 6<br>1435 Mont-Saint-Guibert, Belgique</li><li>Orléans, France</li></ul></div>
    </div>
    <div class="foot-legal"><span>© 2026 Capstone. Tous droits réservés. <a href="mentions.html" style="text-decoration:underline;text-underline-offset:3px">Mentions légales et confidentialité</a></span><span>Sécurité · Bâtiment · Services</span></div>
    <p class="giant" aria-hidden="true"><span style="--i:0">C</span><span style="--i:1">a</span><span style="--i:2">p</span><span style="--i:3">s</span><span style="--i:4">t</span><span style="--i:5">o</span><span style="--i:6">n</span><span style="--i:7">e</span><i style="--i:8">.</i></p>
  </div>
</footer>'''

def cta(title='Bâtissons ensemble des entreprises qui durent.', lead='Porteur de projet, dirigeant ou partenaire, présentez-nous votre projet en quelques lignes. Nous revenons vers vous sous 5 jours ouvrés.', href='contact.html', g='g-soleil'):
    return f'''<section class="wrap" style="margin-top:var(--sec)">
  <div class="cta-band grain {g}">
    <div><span class="label k">Travailler avec nous</span><h2>{title}</h2><p class="lead">{lead}</p></div>
    <a class="btn" href="{href}">Présenter un projet {ARROW}</a>
  </div>
</section>'''

def page_head(title, desc, path=''):
    url = SITE['domain'].rstrip('/') + '/' + path
    return (f'<title>{title}</title>\n<meta name="description" content="{desc}">\n'
            f'<link rel="canonical" href="{url}">\n<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">\n'
            f'<meta name="theme-color" content="#F4F4F6">\n<meta property="og:type" content="website">\n<meta property="og:site_name" content="Capstone">\n'
            f'<meta property="og:title" content="{title}">\n<meta property="og:description" content="{desc}">\n<meta property="og:url" content="{url}">\n'
            f'<meta property="og:image" content="{SITE["domain"].rstrip("/")}/assets/og.png">\n<meta name="twitter:card" content="summary_large_image">\n'
            f'<link rel="stylesheet" href="assets/style.css">\n')

def ph(label, title, sub, lead, ctas, mesh='', labelcls=''):
    return f'''<section class="ph">
  <div class="mesh grain {mesh}" aria-hidden="true"></div>
  <div class="wrap ph-in">
    <span class="label {labelcls} rise">{label}</span>
    <h1 class="d1 rise d1x">{title}</h1>
    <span class="ph-sub rise d2x">{sub}</span>
    <div class="ph-foot rise d3x"><p class="lead">{lead}</p><div class="ctas">{ctas}</div></div>
  </div>
</section>'''

# ---------------------------------------------------------------- Accueil
def home():
    return page_head('Capstone', 'Capstone co-fonde et développe des entreprises dans la sécurité, le bâtiment et les services.') + header('./') + f'''
<main>
<section class="ph">
  <div class="mesh grain" aria-hidden="true"></div>
  <div class="wrap ph-in">
    <span class="label rise">Venture studio et operating partner</span>
    <h1 class="d1 rise d1x" style="max-width:9.6em">Bâtir des entreprises <span class="grey">qui durent.</span></h1>
    <div class="ph-foot rise d2x">
      <p class="lead">Nous co-fondons et développons des entreprises dans <span class="rot" id="rot" data-words="la sécurité|le bâtiment|les services">la sécurité</span>. Au capital, sur le terrain, et dans la durée.</p>
      <div class="ctas"><a class="btn" href="contact.html">Présenter un projet {ARROW}</a><a class="btn ghost" href="portfolio.html">Nos entreprises</a></div>
    </div>
  </div>
  <div class="wrap" style="padding-bottom:0">
    <div class="mosaic rise d3x">
      <a href="portfolio.html#aurus" aria-label="Aurus System"><img src="img/aurus.jpg" alt="Aurus System, sécurité de chantier" style="object-position:50% 40%"></a>
      <div class="tile grain g-orange">{illu('strates','o7')}<div><b class="num">04</b><span>entreprises co-fondées depuis 2025</span></div></div>
      <a href="portfolio.html#numa" aria-label="Nüma"><img src="img/numa.jpg" alt="Nüma, alarme pour particuliers"></a>
    </div>
  </div>
  <div style="height:clamp(48px,6vw,88px)"></div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Deux façons d’entrer</span><h2 class="d2">Créer une entreprise ou faire passer un palier à la vôtre.</h2></div>
      <p class="lead">Dans les deux cas, nous entrons au capital et nous exécutons avec les équipes. Ce qui change, c’est le point de départ.</p>
    </div>
    <div class="duo">
      <a class="mode grain g-orange" href="build.html">
        <div class="top-row"><div><div class="kicker">Build · Venture studio</div><div class="range">De 0 à 1</div></div><span class="arrow-link"><span class="c">{ARROW}</span></span></div>
        {illu('strates','o7')}
        <h3>De l’idée à l’entreprise.</h3>
        <div class="foot"><p>Vous apportez l’expertise métier. Nous injectons le capital et l’infrastructure entrepreneuriale, et nous co-fondons.</p></div>
      </a>
      <a class="mode grain g-lilas" href="advise.html">
        <div class="top-row"><div><div class="kicker">Advise · Operating partner</div><div class="range">De 10 à 100</div></div><span class="arrow-link"><span class="c">{ARROW}</span></span></div>
        {illu('rosace','l7')}
        <h3>Du palier à la croissance.</h3>
        <div class="foot"><p>Votre entreprise est rentable mais plafonne. Nous intervenons en task force ou en advisory board.</p></div>
      </a>
    </div>
  </div>
</section>

<section class="dark-photo">
  <img src="img/equipe.jpg" alt="" loading="lazy" style="object-position:50% 45%">
  <div class="wrap">
    <div>
      <span class="label w">Notre approche</span>
      <h2>Des opérateurs,<br>pas des conseillers.</h2>
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

<section class="sec bg-orange">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">La conviction</span><h2 class="d2">Ce ne sont pas des entreprises à disrupter. <span style="color:var(--orange-700)">Ce sont des entreprises à équiper.</span></h2></div>
      <p class="lead" style="color:var(--ink-2)">Pendant que le capital se concentre sur la tech, des milliers d’entreprises solides et rentables sont pilotées comme il y a vingt ans. C’est là qu’est la valeur.</p>
    </div>
    <div class="figs">
      <div class="fig">{ico('buildings')}<b>193 Md€</b><p>de chiffre d’affaires dans le bâtiment en France, porté à 95 % par des entreprises artisanales.</p><small>FFB, 2025</small></div>
      <div class="fig">{ico('handshake')}<b>370 000</b><p>TPE, PME et ETI françaises potentiellement à céder d’ici 2030.</p><small>CCI Lyon Métropole, 2025</small></div>
      <div class="fig">{ico('lightning')}<b>26 %</b><p>des TPE et PME seulement utilisent l’intelligence artificielle, alors que 78 % en voient les bénéfices.</p><small>France Num, 2025</small></div>
    </div>
  </div>
</section>

<div class="ticker" aria-hidden="true"><div class="track">{''.join('<span>Sécurité</span><span>Bâtiment</span><span>Services</span>' for _ in range(4))}</div></div>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Portfolio</span><h2 class="d2">Ce que nous avons construit.</h2></div>
      <div style="justify-self:end;display:grid;gap:24px"><p class="lead">Un écosystème, pas un portefeuille. Nos entreprises servent les mêmes mondes et se renforcent entre elles.</p><a class="arrow-link" href="portfolio.html"><span class="c">{ARROW}</span>Voir toutes nos entreprises</a></div>
    </div>
    <div class="cos">
      <a class="co" href="portfolio.html#numa"><img src="img/numa.jpg" alt="" loading="lazy"><div class="meta"><span class="pill">Sécurité</span><span class="pill">2025</span></div><h3>Nüma</h3><p>L’alarme professionnelle que l’on configure soi-même.</p></a>
      <a class="co" href="portfolio.html#aurus"><img src="img/aurus.jpg" alt="" loading="lazy"><div class="meta"><span class="pill">Sécurité</span><span class="pill">2025</span></div><h3>Aurus System</h3><p>La sécurité des chantiers, de l’audit à la maintenance.</p></a>
      <a class="co tint grain g-peche" href="portfolio.html#capfield">{illu('trame','p')}<div class="meta"><span class="pill">Services</span><span class="pill">2026</span></div><h3>CapField</h3><p>Le réseau d’intervenants de proximité.</p></a>
      <a class="co tint grain g-lilas" href="portfolio.html#taskia">{illu('arcs','l7')}<div class="meta"><span class="pill">Services</span></div><h3>Taskia</h3><p>L’assistant des artisans, dans WhatsApp.</p></a>
    </div>
  </div>
</section>

<section class="sec bg-paper">
  <div class="wrap split">
    <div class="duo-img">
      <img src="img/charles.jpg" alt="Portrait de Charles Vosters" loading="lazy">
      <img src="img/mathieu.jpg" alt="Portrait de Mathieu Proux" loading="lazy">
    </div>
    <div>
      <span class="label">L’équipe</span>
      <h2 class="d2">On ne construit jamais seul.</h2>
      <p class="lead">La valeur se crée en exécutant, pas en recommandant.</p>
      <div class="people">
        <div><b>Charles Vosters</b><span>Associé · Stratégie et marketing</span></div>
        <div><b>Mathieu Proux</b><span>Associé · Stratégie et opérations</span></div>
      </div>
    </div>
  </div>
</section>
''' + cta() + '\n</main>\n' + FOOTER

# ---------------------------------------------------------------- Build
def build():
    return page_head('Capstone Build', 'Capstone BUILD : un venture studio pour passer de 0 à 1 dans les secteurs traditionnels.') + header('build.html') + '\n<main>\n' + ph(
        'Venture studio', 'BUILD', 'Un venture studio pour passer de 0 à 1.',
        'Lancer une idée, entreprendre ou reprendre une entreprise exige de changer de casquette en permanence. Il est rare de réunir seul toutes les expertises pour franchir chaque étape. Capstone BUILD a été pensé pour vous. Vous apportez l’expertise métier, nous apportons l’infrastructure entrepreneuriale et prenons notre part de responsabilités et de capital.',
        f'<a class="btn" href="contact.html#build">Porteur de projet · Présentez-vous {ARROW}</a>') + f'''
<div class="ph-media">
  <div class="wrap"><div class="frame"><img src="img/grue.jpg" alt="Grue de chantier au coucher du soleil" style="object-position:50% 100%"></div></div>
</div>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Pour qui</span><h2 class="d2">Vous maîtrisez un métier. <span class="grey">Il vous manque une équipe pour en faire une entreprise.</span></h2></div>
      <p class="lead">Nous co-fondons avec des personnes qui connaissent leur terrain mieux que quiconque, dans la sécurité, le bâtiment et les services.</p>
    </div>
    <div class="cards four">
      <div class="card paper"><span class="ico-wrap">{ico('hard-hat')}</span><h3>Expert métier salarié</h3><p>Vous connaissez votre métier par cœur et voulez créer votre propre entreprise.</p></div>
      <div class="card paper"><span class="ico-wrap">{ico('rocket-launch')}</span><h3>Fondateur en démarrage</h3><p>Votre activité est lancée depuis peu et vous voulez la structurer pour passer à l’échelle.</p></div>
      <div class="card paper"><span class="ico-wrap">{ico('key')}</span><h3>Repreneur</h3><p>Vous voulez reprendre une entreprise saine et la moderniser.</p></div>
      <div class="card paper"><span class="ico-wrap">{ico('hand-heart')}</span><h3>Cédant sans successeur</h3><p>Vous dirigez une entreprise et cherchez la relève pour qu’elle continue après vous.</p></div>
    </div>
    <div class="metier-row"><span class="mono-s">Dans quatre familles de métiers</span>{''.join(f'<a class="chip-l" href="./#metiers">{ico(m["icon"])}{m["name"]}</a>' for m in METIERS)}</div>
  </div>
</section>

<section class="sec bg-orange">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Ce que nous apportons</span><h2 class="d2">Des associés, <span class="grey">pas un fonds.</span></h2></div>
      <p class="lead" style="color:var(--ink-2)">Nous prenons des responsabilités, une participation au capital et le lead sur les sujets clés. Toujours avec l’entrepreneur, sauf quand nous créons nous-mêmes la société.</p>
    </div>
    <div class="gives">
      <div class="give">{ico('coins')}<div><h3>Responsabilité et capital</h3><p>Nous participons au capital et prenons le lead sur les sujets clés. Nous ne sommes pas un fonds d’investissement.</p></div></div>
      <div class="give">{ico('strategy')}<div><h3>Structuration de la croissance</h3><p>Marketing, commerce et opérations reliés, pour l’excellence commerciale comme pour celle du delivery.</p></div></div>
      <div class="give">{ico('megaphone')}<div><h3>Acquisition digitale</h3><p>Site, référencement, campagnes et génération de demandes, construits en interne.</p></div></div>
      <div class="give">{ico('gear-six')}<div><h3>Outils et automatisation</h3><p>Les bons outils dès le premier jour, pour éviter que tout repose sur le dirigeant.</p></div></div>
      <div class="give">{ico('chart-line-up')}<div><h3>Pilotage et reporting</h3><p>Des indicateurs simples pour piloter par la donnée plutôt que par l’intuition.</p></div></div>
      <div class="give">{ico('user-circle-plus')}<div><h3>Recrutement</h3><p>Nous vous aidons à recruter les premiers postes clés.</p></div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Méthode</span><h2 class="d2">Quatre marches, <span class="grey">un engagement qui monte.</span></h2></div>
      <p class="lead">Chaque étape engage un peu plus Capstone. La dernière ne s’arrête pas.</p>
    </div>
    <ol class="stairs">
      <li class="stair"><span class="n num">01</span><h3>Rencontre</h3><p>Nous challengeons le projet et la personne.</p></li>
      <li class="stair"><span class="n num">02</span><h3>Cadrage</h3><p>Nous définissons ensemble la thèse, les rôles et la structure.</p></li>
      <li class="stair grain g-peche"><span class="n num">03</span><h3>Construction</h3><p>Nous participons au capital et exécutons côte à côte.</p></li>
      <li class="stair grain g-orange"><span class="n num">04</span><h3>Durée</h3><p>Nous restons au capital et au conseil.</p></li>
    </ol>
  </div>
</section>

<section class="wrap">
  <span class="label">Un cas BUILD</span>
  <div class="case grain g-orange" style="margin-top:28px">
    <div class="txt">
      <div class="pills"><span>Sécurité</span><span>2025</span><span>BUILD</span></div>
      <h3>Nüma</h3>
      <p>La nouvelle façon de sécuriser son logement. Une alarme professionnelle configurée en ligne en quelques minutes, au prix affiché, avec un matériel qui vous appartient et une télésurveillance sans engagement.</p>
      <div class="role"><small>Rôle de Capstone</small>Co-fondation, structuration de la croissance, acquisition digitale.</div>
      <a class="arrow-link" href="portfolio.html#numa"><span class="c">{ARROW}</span>Voir le portfolio</a>
    </div>
    <div class="img"><img src="img/construire.jpg" alt="Enfants jouant dans un salon protégé par Nüma" loading="lazy"></div>
  </div>
</section>

<section class="sec" style="padding-bottom:0">
  <div class="wrap">
    <span class="label">Questions fréquentes</span>
    <h2 class="d2" style="margin-top:24px">Avant de vous lancer.</h2>
    <div class="faq">
      <details><summary>Faut-il déjà avoir créé une entreprise ?<span class="pm">{PLUS}</span></summary><p>Non. Nous cherchons d’abord une expertise métier et une personne prête à s’engager. L’entreprise, nous la construisons ensemble.</p></details>
      <details><summary>Dans quels secteurs intervenez-vous ?<span class="pm">{PLUS}</span></summary><p>La sécurité, le bâtiment et les services, des métiers concrets et ancrés dans le réel, où l’équipement et la structuration changent la donne.</p></details>
      <details><summary>Que demande Capstone en échange ?<span class="pm">{PLUS}</span></summary><p>Nous prenons des responsabilités et une participation au capital, sans être un fonds d’investissement. La répartition, les rôles et la gouvernance sont définis ensemble pendant le cadrage.</p></details>
      <details><summary>Combien de temps restez-vous ?<span class="pm">{PLUS}</span></summary><p>Nous ne cherchons pas la sortie rapide. Nous restons au capital et au conseil dans la durée.</p></details>
    </div>
  </div>
</section>
''' + cta(title='Votre métier, notre infrastructure.', href='contact.html#build', g='g-orange') + '\n</main>\n' + FOOTER

# ---------------------------------------------------------------- Advise
def advise():
    return page_head('Capstone Advise', 'Capstone ADVISE : un operating partner pour les entreprises établies qui plafonnent sur un palier de croissance.') + header('advise.html') + '\n<main>\n' + ph(
        'Operating partner', 'ADVISE', 'Un operating partner pour franchir le palier.',
        'Votre entreprise est rentable, votre métier est solide, mais la croissance plafonne. Capstone ADVISE intervient en task force ou en advisory board pour lever ce qui bloque, qu’il s’agisse de l’organisation commerciale, des outils ou du pilotage.',
        f'<a class="btn" href="contact.html#advise">Dirigeant · Parlons de votre entreprise {ARROW}</a>', mesh='lilas', labelcls='l') + f'''
<div class="ph-media">
  <div class="wrap"><div class="frame"><img src="img/bureau.jpg" alt="Salle de réunion d’une entreprise" style="object-position:50% 55%"></div></div>
</div>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label l">Pour qui</span><h2 class="d2">Une entreprise établie, <span class="grey">bloquée sur un palier de croissance.</span></h2></div>
      <p class="lead">Les signes reviennent souvent. Tout passe par le dirigeant, l’acquisition reste artisanale, les outils manquent et les chiffres arrivent trop tard.</p>
    </div>
    <div class="cards">
      <div class="card paper"><span class="ico-wrap l">{ico('user-focus')}</span><h3>Tout repose sur vous</h3><p>Les process sont dans la tête du dirigeant. L’entreprise ne peut pas grandir plus vite que lui.</p></div>
      <div class="card paper"><span class="ico-wrap l">{ico('megaphone')}</span><h3>L’acquisition plafonne</h3><p>Le bouche-à-oreille a fait ses preuves, mais il ne suffit plus pour aller chercher la suite.</p></div>
      <div class="card paper"><span class="ico-wrap l">{ico('chart-bar')}</span><h3>Vous pilotez à vue</h3><p>Les chiffres existent quelque part, mais pas sous une forme qui aide à décider.</p></div>
    </div>
    <div class="sizes">
      <div class="sizes-t"><span class="mono-s">Chiffre d’affaires</span><b>De la TPE à l’ETI</b></div>
      <div class="sizes-bar"><span>Moins de 1 M€</span><span>1 à 5 M€</span><span>5 à 20 M€</span><span>Plus de 20 M€</span></div>
    </div>
    <div class="metier-row"><span class="mono-s">Dans quatre familles de métiers</span>{''.join(f'<a class="chip-l" href="./#metiers">{ico(m["icon"])}{m["name"]}</a>' for m in METIERS)}</div>
  </div>
</section>

<section class="sec bg-lilas">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label l">Deux formats</span><h2 class="d2">Au cœur de l’exécution, ou à vos côtés.</h2></div>
      <p class="lead" style="color:var(--ink-2)">Nous choisissons ensemble le format selon l’urgence et la nature du blocage.</p>
    </div>
    <div class="cards two">
      <div class="card big">{illu('trame','l')}<span class="n">FORMAT 01</span><h3>Task force</h3><p>Une équipe Capstone intervient directement dans l’entreprise sur un chantier précis, comme la structuration de la croissance, l’acquisition digitale, les outils ou le pilotage.</p></div>
      <div class="card big">{illu('arcs','l')}<span class="n">FORMAT 02</span><h3>Advisory board</h3><p>Nous rejoignons votre gouvernance pour challenger la stratégie, prioriser les chantiers et suivre l’exécution dans la durée.</p></div>
    </div>
  </div>
</section>

<section class="dark-photo">
  <img src="img/atelier.jpg" alt="" loading="lazy" style="object-position:50% 40%">
  <div class="wrap">
    <div>
      <span class="label w">Les leviers</span>
      <h2>Ce qui fait passer le palier.</h2>
      <p class="lead">Nous n’apportons pas un rapport. Nous apportons les compétences qui manquent, et nous les mettons en œuvre avec vos équipes.</p>
    </div>
    <div>
      <p class="chips-title">Nos leviers</p>
      <div class="chips">
        <span class="chip">{ico('strategy')}Structuration de la croissance</span>
        <span class="chip">{ico('megaphone')}Acquisition digitale</span>
        <span class="chip">{ico('gear-six')}Outils et automatisation</span>
        <span class="chip">{ico('chart-line-up')}Pilotage et reporting</span>
        <span class="chip">{ico('users-three')}Organisation</span>
        <span class="chip">{ico('user-circle-plus')}Recrutement</span>
        <span class="chip">{ico('handshake')}Réseau et accès marché</span>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label l">Méthode</span><h2 class="d2">Du diagnostic <span class="grey">à la durée.</span></h2></div>
      <p class="lead">Un déroulé court au départ, un engagement qui s’installe si la collaboration fonctionne.</p>
    </div>
    <ol class="stairs l">
      <li class="stair"><span class="n num">01</span><h3>Rencontre</h3><p>Nous comprenons l’entreprise, son marché et ce qui bloque.</p></li>
      <li class="stair"><span class="n num">02</span><h3>Cadrage</h3><p>Nous fixons les priorités, le format et les indicateurs de réussite.</p></li>
      <li class="stair grain g-lilas"><span class="n num">03</span><h3>Exécution</h3><p>Nous intervenons avec vos équipes, chantier par chantier.</p></li>
      <li class="stair grain" style="background:linear-gradient(160deg,var(--lilas-400),#E9A9C4 70%,var(--peche-400))"><span class="n num">04</span><h3>Durée</h3><p>Nous restons à vos côtés au conseil, et parfois au capital.</p></li>
    </ol>
  </div>
</section>

<section class="sec" style="padding-top:0;padding-bottom:0">
  <div class="wrap">
    <span class="label l">Questions fréquentes</span>
    <h2 class="d2" style="margin-top:24px">Avant de nous appeler.</h2>
    <div class="faq">
      <details><summary>Quelle taille d’entreprise accompagnez-vous ?<span class="pm">{PLUS}</span></summary><p>Des entreprises établies et rentables, dans la sécurité, le bâtiment ou les services, qui plafonnent sur un palier de croissance.</p></details>
      <details><summary>Êtes-vous un cabinet de conseil ?<span class="pm">{PLUS}</span></summary><p>Non. Nous exécutons avec vos équipes et nous pouvons prendre une participation au capital. Notre intérêt est aligné sur la croissance de l’entreprise, pas sur le nombre de jours facturés.</p></details>
      <details><summary>Quelle différence entre task force et advisory board ?<span class="pm">{PLUS}</span></summary><p>La task force intervient dans l’opérationnel sur un chantier précis. L’advisory board accompagne la direction dans la durée, au niveau de la gouvernance.</p></details>
    </div>
  </div>
</section>
''' + cta(title='Votre croissance mérite mieux qu’un palier.', href='contact.html#advise', g='g-lilas') + '\n</main>\n' + FOOTER

# ---------------------------------------------------------------- Portfolio
def portfolio():
    return page_head('Capstone Portfolio', 'Les entreprises du groupe Capstone : Nüma, Aurus System, CapField et Taskia.') + header('portfolio.html') + '\n<main>\n' + ph(
        'Portfolio', 'Portfolio', 'Un écosystème, pas un portefeuille.',
        'Nos entreprises servent les mêmes mondes et se renforcent entre elles. Chaque nouvelle entreprise profite de celles qui existent déjà.',
        f'<a class="btn ghost" href="#numa">Découvrir les entreprises</a>') + f'''
<section class="bg-paper" style="padding-bottom:clamp(64px,8vw,120px)">
  <div class="wrap">
    <div class="eco">
      <div class="g-orange grain"><span class="v">Équipe les chantiers</span><b>Aurus System</b><span>Sécurité des chantiers et bâtiments professionnels.</span></div>
      <div class="g-peche grain"><span class="v">Équipe les sites</span><b>Nüma</b><span>Alarme professionnelle pour particuliers et petits pros.</span></div>
      <div style="background:var(--white)"><span class="v">Exécute sur le terrain</span><b>CapField</b><span>Pour les entreprises du groupe et pour des tiers.</span></div>
      <div class="g-lilas grain"><span class="v">Outille les artisans</span><b>Taskia</b><span>Les indépendants qui composent le réseau.</span></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <article class="case grain g-peche" id="numa">
      <div class="txt">
        <div class="pills"><span>Sécurité</span><span>2025</span><span>BUILD</span></div>
        <h3>Nüma</h3>
        <p>La nouvelle façon de sécuriser son logement. Une alarme professionnelle configurée en ligne en quelques minutes, au prix affiché, avec un matériel qui vous appartient et une télésurveillance sans engagement.</p>
        <div class="role"><small>Rôle de Capstone</small>Co-fondation, structuration de la croissance, acquisition digitale.</div>
      </div>
      <div class="img"><img src="img/numa.jpg" alt="Nüma" loading="lazy"></div>
    </article>
    <article class="case rev grain g-orange" id="aurus">
      <div class="txt">
        <div class="pills"><span>Sécurité</span><span>2025</span><span>BUILD</span></div>
        <h3>Aurus System</h3>
        <p>Sécurise les chantiers et les bâtiments professionnels, en installation temporaire ou permanente, avec télésurveillance 24/7. Un seul interlocuteur de l’audit à la maintenance, en Île-de-France et à Orléans.</p>
        <div class="role"><small>Rôle de Capstone</small>Co-fondation, structuration de la croissance.</div>
      </div>
      <div class="img"><img src="img/aurus.jpg" alt="Aurus System" loading="lazy" style="object-position:50% 45%"></div>
    </article>
    <article class="case" id="capfield" style="background:var(--paper)">
      <div class="txt">
        <div class="pills"><span style="background:var(--white)">Services et déploiement</span><span style="background:var(--white)">2026</span><span style="background:var(--white)">BUILD</span></div>
        <h3>CapField</h3>
        <p>Réseau d’intervenants de proximité qui réalise les poses, contrôles et remises en service pour les entreprises qui déploient des équipements sur le terrain. Un prix à l’acte, une preuve d’intervention systématique.</p>
        <div class="role"><small>Rôle de Capstone</small>Co-fondation avec un opérateur issu de l’industrie, structuration du modèle et de l’outil de pilotage.</div>
      </div>
      <div class="img placeholder grain g-peche">{illu('trame','p')}<span class="cap">Photo à fournir</span></div>
    </article>
    <article class="case rev grain g-lilas" id="taskia">
      <div class="txt">
        <div class="pills"><span>Services aux indépendants</span></div>
        <h3>Taskia</h3>
        <p>Un assistant opérationnel dans WhatsApp pour les indépendants, les artisans et les petites entreprises. Devis, factures, rendez-vous et relances se gèrent par simple message écrit ou vocal, avec un relais humain pour les missions complexes.</p>
        <div class="role"><small>La promesse</small>Moins d’administratif, plus de métier, sans apprendre un nouvel outil.</div>
      </div>
      <div class="img placeholder" style="background:var(--lilas-100)">{illu('arcs','l7')}<span class="cap">Photo à fournir</span></div>
    </article>
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
''' + '\n</main>\n' + FOOTER

# ---------------------------------------------------------------- Contact
def contact(preview):
    pv = ' data-preview' if preview else ''
    return page_head('Capstone Contact', 'Présentez votre projet à Capstone : porteurs de projet, dirigeants et partenaires.') + header('contact.html') + f'''
<main>
<section class="ph" style="padding-bottom:clamp(64px,8vw,120px)">
  <div class="mesh grain" aria-hidden="true"></div>
  <div class="wrap ph-in" style="padding-bottom:clamp(40px,5vw,64px)">
    <span class="label rise">Contact</span>
    <h1 class="d1 rise d1x" style="max-width:8em">Parlons de votre projet.</h1>
  </div>
  <div class="wrap contact-grid">
    <form class="cform rise d2x" name="contact" method="POST" data-netlify="true" netlify-honeypot="adresse" id="form"{pv}>
      <input type="hidden" name="form-name" value="contact">
      <p class="hp"><label>Ne pas remplir <input name="adresse" id="f-hp"></label></p>
      <fieldset>
        <legend>Vous êtes</legend>
        <div class="profiles">
          <input type="radio" name="profil" id="p-build" value="Porteur de projet (BUILD)" checked><label for="p-build">{ico('rocket-launch')}Porteur de projet<small>Créer ou reprendre</small></label>
          <input type="radio" name="profil" id="p-advise" value="Dirigeant (ADVISE)"><label for="p-advise">{ico('buildings')}Dirigeant<small>Passer un palier</small></label>
          <input type="radio" name="profil" id="p-part" value="Partenaire"><label for="p-part">{ico('handshake')}Partenaire<small>Déployer ensemble</small></label>
        </div>
      </fieldset>
      <div class="row2">
        <label class="f" for="f-nom">Nom et prénom<input id="f-nom" name="nom" autocomplete="name" required></label>
        <label class="f" for="f-mail">E-mail<input id="f-mail" name="email" type="email" autocomplete="email" required></label>
      </div>
      <div class="row2">
        <label class="f" for="f-ent">Entreprise ou projet<input id="f-ent" name="entreprise" autocomplete="organization"></label>
        <label class="f" for="f-tel">Téléphone<input id="f-tel" name="telephone" type="tel" autocomplete="tel"></label>
      </div>
      <label class="f" for="f-msg">Votre projet en quelques lignes<textarea id="f-msg" name="message" required></textarea></label>
      <div class="form-foot"><span class="status" id="status" role="status">Réponse sous 5 jours ouvrés.</span><button class="btn" type="submit">Envoyer {ARROW}</button></div>
    </form>
    <aside class="side grain g-soleil rise d3x">
      <span class="label k">Nous joindre</span>
      <div class="info">
        <div>{ico('envelope-simple')}<div><small>E-mail</small><span>{SITE["email"]}</span></div></div>
        <div>{ico('phone')}<div><small>Téléphone</small><span>{SITE["phone"]}</span></div></div>
        <div>{ico('map-pin')}<div><small>Belgique</small><span>Rue Emile Francqui 6<br>1435 Mont-Saint-Guibert</span></div></div>
        <div>{ico('map-pin')}<div><small>France</small><span>Orléans</span></div></div>
        <div>{ico('linkedin-logo')}<div><small>LinkedIn</small><span><a href="{SITE["linkedin"]}" rel="noopener">Capstone</a></span></div></div>
      </div>
      {illu('strates','o7')}
    </aside>
  </div>
</section>

<section class="sec" style="padding-bottom:0">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="label">Avec qui nous travaillons</span><h2 class="d2">Trois portes d’entrée.</h2></div>
      <p class="lead">Quel que soit votre point de départ, le premier échange sert à comprendre votre projet et votre métier.</p>
    </div>
    <div class="cards">
      <a class="card paper" href="build.html"><span class="ico-wrap">{ico('rocket-launch')}</span><h3>Porteurs de projet</h3><p>Vous maîtrisez un métier et voulez créer ou reprendre une entreprise.</p><span class="arrow-link"><span class="c">{ARROW}</span>Capstone BUILD</span></a>
      <a class="card paper" href="advise.html"><span class="ico-wrap l">{ico('buildings')}</span><h3>Dirigeants</h3><p>Votre entreprise est rentable mais plafonne sur un palier de croissance.</p><span class="arrow-link"><span class="c">{ARROW}</span>Capstone ADVISE</span></a>
      <div class="card paper"><span class="ico-wrap" style="background:var(--peche-100);color:var(--peche-600)">{ico('handshake')}</span><h3>Partenaires industriels</h3><p>Vous équipez ou servez les mêmes marchés et cherchez à déployer plus vite sur le terrain.</p></div>
    </div>
  </div>
</section>
</main>
''' + FOOTER

exec(open(os.path.join(B, 'pages_v3.py')).read())

# ---------------------------------------------------------------- Sortie
def full(body, preview):
    head, rest = body.split('<header', 1)
    return ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + head + '</head>\n<body>\n<header' + rest + '\n<script src="assets/main.js"></script>\n</body>\n</html>\n')

def write(outdir, preview):
    os.makedirs(f'{outdir}/assets', exist_ok=True)
    css = open(f'{B}/src/style.css').read()
    import base64
    for k, f in [('{{MANROPE}}', 'Manrope-Variable-latin'), ('{{PLEXM}}', 'IBMPlexMono-Medium-latin')]:
        css = css.replace(k, base64.b64encode(open(f'{V}/fonts/{f}.woff2', 'rb').read()).decode())
    open(f'{outdir}/assets/style.css', 'w').write(css)
    shutil.copy(f'{B}/src/main.js', f'{outdir}/assets/main.js')
    if os.path.abspath(f'{outdir}/img') != os.path.abspath(f'{B}/img'):
        shutil.copytree(f'{B}/img', f'{outdir}/img', dirs_exist_ok=True)
    pages = {'index.html': home(), 'build.html': build(), 'advise.html': advise(), 'portfolio.html': portfolio(), 'about.html': about(), 'contact.html': contact(preview), 'mentions.html': mentions(), '404.html': notfound()}
    if SHOW_BLOG: pages.update({'blog.html': blog(preview), 'article.html': article()})
    for old_f in ['blog.html', 'article.html']:
        if not SHOW_BLOG and os.path.exists(f'{outdir}/{old_f}'): os.remove(f'{outdir}/{old_f}')
    dom = SITE['domain'].rstrip('/')
    for name in list(pages):
        if name not in ('index.html',):
            pages[name] = pages[name].replace(f'href="{dom}/"', f'href="{dom}/{name}"').replace(f'og:url" content="{dom}/"', f'og:url" content="{dom}/{name}"')
    if name == '404.html': pass
    for f in ['favicon.svg', 'apple-touch-icon.png', 'og.png']:
        if os.path.exists(f'{B}/src/{f}'): shutil.copy(f'{B}/src/{f}', f'{outdir}/assets/{f}')
    if not preview:
        open(f'{outdir}/robots.txt', 'w').write(f'User-agent: *\nAllow: /\nSitemap: {dom}/sitemap.xml\n')
        urls = ''.join(f'<url><loc>{dom}/{"" if n == "index.html" else n}</loc></url>' for n in pages if n not in ('404.html',))
        open(f'{outdir}/sitemap.xml', 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
        shutil.copy(f'{B}/src/netlify.toml', f'{outdir}/netlify.toml')
    for name, body in pages.items():
        body = re.sub(r'<div class="mesh grain ?([a-z]*)" aria-hidden="true"></div>', lambda m: f'<div class="mesh {m.group(1)}" aria-hidden="true"><i class="b b1"></i><i class="b b2"></i><i class="b b3"></i><i class="mg"></i></div><div class="glow" aria-hidden="true"></div>', body)
        body = re.sub(r' rise(?: d[123]x)?', '', body)
        if preview and name == 'index.html':
            out = body + '\n<script src="assets/main.js"></script>\n'   # la page principale de l'artefact reçoit son squelette à la publication
        else:
            out = full(body, preview)
        open(f'{outdir}/{name}', 'w').write(out)

# ---------------------------------------------------------------- Contrôle avant mise en ligne
def placeholders(outdir):
    found = []
    for f in sorted(os.listdir(outdir)):
        if f.endswith('.html'):
            t = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', open(f'{outdir}/{f}').read(), flags=re.S)
            for m in sorted(set(re.findall(r'\[[A-ZÀ-Ý][^\]<]{1,40}\]', t))): found.append(f'{f} : {m}')
            if 'href="https://www.linkedin.com/"' in t: found.append(f'{f} : lien LinkedIn générique')
    return found

out = os.path.join(ROOT, 'site')
write(out, False)
todo = placeholders(out)
if PROD and todo:
    print('Mise en ligne refusée, il reste à compléter :'); [print('  -', x) for x in todo]; sys.exit(1)
dom = SITE['domain'].rstrip('/')
headers = '''/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()
  Strict-Transport-Security: max-age=31536000
  Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self'; font-src 'self' data:; connect-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'self'
''' + ('' if PROD else '  X-Robots-Tag: noindex, nofollow\n') + '''
/assets/*
  Cache-Control: public, max-age=604800

/img/*
  Cache-Control: public, max-age=604800
'''
open(f'{out}/_headers', 'w').write(headers)
if os.path.isdir(f'{B}/signature'): shutil.copytree(f'{B}/signature', f'{out}/signature', dirs_exist_ok=True)
if not PROD:
    open(f'{out}/robots.txt', 'w').write('User-agent: *\nDisallow: /\n')
    for f in os.listdir(out):
        if f.endswith('.html'):
            p = f'{out}/{f}'; t = open(p).read()
            open(p, 'w').write(t.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex, nofollow">', 1))
if os.path.exists(f'{out}/netlify.toml'): os.remove(f'{out}/netlify.toml')
print('Version', 'publique' if PROD else 'de préproduction (non indexable)', 'générée dans site/.')
if todo: print('À compléter avant la version publique :'); [print('  -', x) for x in todo]
print('ok')
