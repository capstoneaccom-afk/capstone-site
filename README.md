# Site Capstone

Site statique (HTML, CSS, un peu de JavaScript), publié sur Netlify. Pas de base de données, pas de serveur.

## Organisation

| Dossier | Rôle |
|---|---|
| `site/` | **Le site publié.** Netlify ne publie que ce dossier. Ne pas le modifier à la main : il est régénéré. |
| `source/` | Le générateur : `build.py` (en-tête, pied de page, pages Build, Advise, Contact, réglages `SITE`), `pages_v3.py` (accueil, portfolio, à propos, blog, mentions légales), `iso.py` (illustrations « du plan au volume »), `src/` (styles, script, icônes du site), `img/` (photos), `vendor/` (polices, icônes, illustrations du design system). |

## Modifier le site

1. Modifier les textes dans `source/build.py` ou `source/pages_v3.py`. Les coordonnées et le domaine sont dans le bloc `SITE` en haut de `source/build.py`.
2. `python3 source/build.py`.
3. Envoyer les changements sur GitHub : Netlify republie automatiquement.

Le blog est prêt mais masqué (`SHOW_BLOG = False` dans `source/build.py`).

## Préproduction et version publique

`python3 source/build.py` produit une version de **préproduction non indexable** (`noindex`, `robots.txt` fermé) et liste tout ce qui reste à compléter.

`python3 source/build.py --prod` **refuse de générer le site** tant qu'il reste un texte provisoire entre crochets (`[E-MAIL]`, `[DOMAINE]`…) ou le lien LinkedIn générique.

## Mise en ligne sur Netlify

1. Créer un site Netlify relié au dépôt GitHub (dossier à publier : `site`, aucune commande de construction).
2. Ajouter le domaine dans *Domain management* et suivre les consignes DNS chez OVH. Choisir la version principale (avec ou sans `www`), la même que `SITE['domain']`.
3. Vérifier dans *Forms* que le formulaire « contact » est détecté, puis régler les notifications vers l'adresse de contact.
4. Générer la version publique (`python3 source/build.py --prod`), envoyer sur GitHub, puis déclarer `sitemap.xml` dans Google Search Console.
