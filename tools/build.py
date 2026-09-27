# -*- coding: utf-8 -*-
"""
Génère les pages secondaires du site : guides, page des filtres, calculateur,
page d'accueil anglaise, index des guides, et le sitemap.

    python3 tools/build.py        (depuis la racine du dépôt)

Pourquoi un générateur plutôt que des pages écrites à la main : l'en-tête, le
pied, les balises `hreflang` et les données structurées doivent être RIGOUREUSEMENT
identiques d'une page à l'autre. Écrites à la main, elles divergent en trois
versions — et une balise `hreflang` qui ne se répond pas est pire que pas de
balise du tout.

La page des filtres est construite depuis `rules.json`, le fichier réellement
servi aux appareils. Elle ne peut donc pas mentir : si une règle disparaît du
jeu, elle disparaît de la page à la génération suivante.
"""

import json
import os
import subprocess
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contenu import ARTICLES  # noqa: E402

SITE = 'https://slowcial-app.com'
APP = 'https://apps.apple.com/fr/app/id6802452087'
AUJ = date.today().isoformat()
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def date_des_regles() -> str:
    """Date du dernier changement de `rules.json`, lue dans l'historique git.

    La page des filtres affichait la date de GÉNÉRATION, qui change à chaque
    passage du script même quand rien n'a bougé — une fraîcheur de façade, que
    les moteurs finissent par ignorer. Celle-ci dit quelque chose de vrai : le
    jour où les règles servies aux appareils ont réellement changé.
    """
    try:
        out = subprocess.run(
            ['git', 'log', '-1', '--format=%ad', '--date=short', '--', 'rules.json'],
            cwd=RACINE, capture_output=True, text=True, timeout=10, check=True)
        return out.stdout.strip() or AUJ
    except Exception:
        # Dépôt absent, git indisponible : la date du jour reste correcte, elle
        # est simplement moins précise. Une page qui ne se génère pas serait pire.
        return AUJ

# Réseaux annoncés mais pas encore ouvrables dans l'application (v1.0.4).
# Le site ne doit jamais promettre ce que l'application ne laisse pas faire.
SOON = {'tiktok', 'snapchat'}

NETS = {
    'instagram': 'Instagram', 'youtube': 'YouTube', 'facebook': 'Facebook',
    'reddit': 'Reddit', 'x': 'X', 'tiktok': 'TikTok', 'snapchat': 'Snapchat',
}

LABELS = {
    'fr': {
        'reels': ("Masquer les reels", "Vidéos courtes et shorts"),
        'shorts': ("Masquer les Shorts", "Les vidéos verticales courtes"),
        'sugg': ("Masquer les suggestions", "Fil recommandé « pour toi »"),
        'explore': ("Masquer l'explore", "Page de découverte"),
        'ads': ("Masquer les pubs", "Publicités et contenus sponsorisés"),
    },
    'en': {
        'reels': ("Hide reels", "Short videos and shorts"),
        'shorts': ("Hide Shorts", "Short vertical videos"),
        'sugg': ("Hide suggestions", "The “for you” recommendation feed"),
        'explore': ("Hide explore", "Discovery page"),
        'ads': ("Hide ads", "Adverts and sponsored content"),
    },
}

T = {
    'fr': {
        'lang': 'fr', 'locale': 'fr_FR',
        'nav_guides': 'Guides', 'nav_filters': 'Les filtres', 'nav_calc': 'Calculateur',
        'nav_home': 'Accueil',
        'cta_h': "Reprends ton temps.",
        'cta_p': "Un réseau filtré, gratuitement. Pas de compte à créer, pas de publicité, et rien qui quitte ton téléphone.",
        'cta_btn': "Télécharger sur l'App Store",
        'cta_ghost': "Voir ce que Slowcial retire",
        'cta_fine': "iPhone · huit langues · sans compte",
        'related': "À lire ensuite",
        'faq_h': "Questions fréquentes",
        'updated': "Mis à jour le",
        'read': "min de lecture",
        'foot_a': 'Guides', 'foot_b': 'Slowcial', 'foot_c': 'Légal',
        'privacy': 'Confidentialité', 'terms': 'Conditions',
        'fine': "Slowcial n'est affilié à aucun des services qu'il ouvre. Les noms cités le sont à titre descriptif.",
        'back': "Tous les guides",
    },
    'en': {
        'lang': 'en', 'locale': 'en_GB',
        'nav_guides': 'Guides', 'nav_filters': 'Filters', 'nav_calc': 'Calculator',
        'nav_home': 'Home',
        'cta_h': "Take your time back.",
        'cta_p': "One filtered network, free. No account to create, no ads, and nothing that leaves your phone.",
        'cta_btn': "Download on the App Store",
        'cta_ghost': "See what Slowcial removes",
        'cta_fine': "iPhone · eight languages · no account",
        'related': "Read next",
        'faq_h': "Frequently asked questions",
        'updated': "Updated",
        'read': "min read",
        'foot_a': 'Guides', 'foot_b': 'Slowcial', 'foot_c': 'Legal',
        'privacy': 'Privacy', 'terms': 'Terms',
        'fine': "Slowcial is not affiliated with any of the services it opens. Names are used descriptively.",
        'back': "All guides",
    },
}

# Chemins des pages fixes, par langue.
PATHS = {
    'fr': {'home': '/', 'guides': '/guides/', 'filters': '/filtres/', 'calc': '/calculateur/',
           'privacy': '/confidentialite/', 'terms': '/conditions/'},
    'en': {'home': '/en/', 'guides': '/en/guides/', 'filters': '/en/filters/', 'calc': '/en/calculator/',
           'privacy': '/privacy/', 'terms': '/conditions/'},
}


# —————————————————————————————————————————————— gabarit

def head(lang, path, alt, title, desc, img, extra_ld=None, img_alt=None):
    """En-tête complet : métadonnées, hreflang réciproque, données structurées."""
    o = T[lang]
    url = SITE + path
    alt_url = SITE + alt
    fr_url = url if lang == 'fr' else alt_url
    en_url = alt_url if lang == 'fr' else url
    ld = [{
        "@context": "https://schema.org", "@type": "WebPage",
        "@id": url + "#page", "url": url, "name": title, "description": desc,
        "inLanguage": o['locale'].replace('_', '-'),
        "isPartOf": {"@type": "WebSite", "@id": SITE + "/#site"},
    }]
    if extra_ld:
        ld += extra_ld
    return f"""<!doctype html>
<html lang="{o['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#F4EDDE">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="fr" href="{fr_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Slowcial">
<meta property="og:locale" content="{o['locale']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/media/articles/{img}.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/media/articles/{img}.jpg">
<link rel="icon" type="image/png" sizes="32x32" href="/media/icon-32.png">
<link rel="icon" type="image/png" sizes="512x512" href="/media/icon-512.png">
<link rel="apple-touch-icon" href="/media/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,800&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/sl.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(',', ':'))}</script>
</head>
<body>
<div class="progress" id="prog"></div>
{topbar(lang, path, alt)}
"""


def topbar(lang, path, alt):
    o, p = T[lang], PATHS[lang]
    other = 'EN' if lang == 'fr' else 'FR'
    def cur(href):
        return ' aria-current="page"' if href == path else ''
    return f"""<header class="top"><div class="wrap">
  <a class="brand" href="{p['home']}"><i>slowcial</i><i>.</i></a>
  <nav>
    <a class="hide-s" href="{p['guides']}"{cur(p['guides'])}>{o['nav_guides']}</a>
    <a class="hide-s" href="{p['filters']}"{cur(p['filters'])}>{o['nav_filters']}</a>
    <a class="hide-s" href="{p['calc']}"{cur(p['calc'])}>{o['nav_calc']}</a>
    <a class="lang" href="{alt}" hreflang="{'en' if lang == 'fr' else 'fr'}">{other}</a>
  </nav>
</div></header>"""


def cta(lang):
    o, p = T[lang], PATHS[lang]
    return f"""<section class="wrap"><div class="cta rev">
  <h2>{o['cta_h']}</h2>
  <p>{o['cta_p']}</p>
  <div class="btns">
    <a class="btn" href="{APP}" rel="nofollow">{o['cta_btn']}</a>
    <a class="btn ghost" href="{p['filters']}">{o['cta_ghost']}</a>
  </div>
  <small>{o['cta_fine']}</small>
</div></section>"""


def foot(lang, guides):
    o, p = T[lang], PATHS[lang]
    liens = ''.join(f'<a href="{p["guides"]}{g["slug"]}/">{g["short"]}</a>' for g in guides[:5])
    return f"""<footer><div class="wrap">
  <div class="cols">
    <div><h4>{o['foot_a']}</h4>{liens}</div>
    <div><h4>{o['foot_b']}</h4>
      <a href="{p['home']}">{o['nav_home']}</a>
      <a href="{p['filters']}">{o['nav_filters']}</a>
      <a href="{p['calc']}">{o['nav_calc']}</a>
      <a href="{APP}" rel="nofollow">App Store</a></div>
    <div><h4>{o['foot_c']}</h4>
      <a href="{p['privacy']}">{o['privacy']}</a>
      <a href="{p['terms']}">{o['terms']}</a>
      <a href="mailto:contact@slowcial-app.com">contact@slowcial-app.com</a></div>
  </div>
  <p class="fine">{o['fine']}</p>
</div></footer>
<script>
(function(){{
  var calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var io = new IntersectionObserver(function(es){{
    es.forEach(function(e){{ if(e.isIntersecting){{ e.target.classList.add('in'); io.unobserve(e.target); }} }});
  }}, {{threshold:.12}});
  document.querySelectorAll('.rev').forEach(function(el){{ calm ? el.classList.add('in') : io.observe(el); }});
  var pr = document.getElementById('prog');
  if(pr && !calm) addEventListener('scroll', function(){{
    var h = document.documentElement;
    pr.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight) * 100) + '%';
  }}, {{passive:true}});
}})();
</script>
</body>
</html>
"""


def ecrire(path, html):
    dossier = os.path.join(RACINE, path.strip('/'))
    os.makedirs(dossier, exist_ok=True)
    with open(os.path.join(dossier, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)


def banniere(img, eyebrow, h1, lede, meta):
    return f"""<section class="ahero">
  <picture>
    <source type="image/webp" media="(max-width:700px)" srcset="/media/articles/{img}-800.webp">
    <source type="image/webp" srcset="/media/articles/{img}.webp">
    <img src="/media/articles/{img}.jpg" alt="" width="1600" height="686" fetchpriority="high">
  </picture>
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <p class="meta">{meta}</p>
  </div>
</section>"""


# —————————————————————————————————————————————— rendu des blocs

def bloc(b):
    k, v = b
    if k == 'p':
        return f'<p>{v}</p>'
    if k == 'big':
        return f'<p class="big">{v}</p>'
    if k == 'h2':
        return f'<h2 class="rev">{v}</h2>'
    if k == 'pull':
        return f'<p class="pull rev">{v}</p>'
    if k == 'ul':
        return '<ul>' + ''.join(f'<li>{i}</li>' for i in v) + '</ul>'
    if k == 'note':
        t, txt = v
        return f'<aside class="note rev"><span class="k">{t}</span><p>{txt}</p></aside>'
    if k == 'steps':
        c = ''.join(
            f'<div class="stepc rev"><div class="n">{i+1}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
            for i, (t, d) in enumerate(v))
        return f'<div class="steps">{c}</div>'
    if k == 'compare':
        ta, la, tb, lb = v
        a = ''.join(f'<li>{i}</li>' for i in la)
        b2 = ''.join(f'<li>{i}</li>' for i in lb)
        return (f'<div class="compare rev"><div class="col bad"><h3>{ta}</h3><ul>{a}</ul></div>'
                f'<div class="col good"><h3>{tb}</h3><ul>{b2}</ul></div></div>')
    raise ValueError('bloc inconnu : ' + k)


def mots(a):
    n = 0
    for k, v in a['body']:
        if k in ('p', 'big', 'h2', 'pull'):
            n += len(v.split())
        elif k == 'ul':
            n += sum(len(i.split()) for i in v)
        elif k == 'steps':
            n += sum(len(t.split()) + len(d.split()) for t, d in v)
        elif k == 'note':
            n += len(v[1].split())
        elif k == 'compare':
            n += sum(len(i.split()) for i in v[1]) + sum(len(i.split()) for i in v[3])
    n += sum(len(q.split()) + len(r.split()) for q, r in a['faq'])
    return n


# —————————————————————————————————————————————— pages

def liste_guides(lang):
    """Les guides d'une langue, sous une forme courte réutilisable."""
    out = []
    for a in ARTICLES:
        d = a[lang]
        out.append({'slug': d['slug'], 'title': d['title'], 'h1': d['h1'],
                    'short': d['h1'].replace('<em>', '').replace('</em>', ''),
                    'desc': d['desc'], 'img': a['img'], 'eyebrow': d['eyebrow']})
    return out


def page_article(a, lang):
    d, o, p = a[lang], T[lang], PATHS[lang]
    autre = 'en' if lang == 'fr' else 'fr'
    path = f"{p['guides']}{d['slug']}/"
    alt = f"{PATHS[autre]['guides']}{a[autre]['slug']}/"
    url = SITE + path
    lecture = max(2, round(mots(d) / 200))

    ld = [{
        "@context": "https://schema.org", "@type": "Article",
        "headline": d['title'], "description": d['desc'],
        "image": f"{SITE}/media/articles/{a['img']}.jpg",
        "datePublished": AUJ, "dateModified": AUJ, "inLanguage": o['locale'].replace('_', '-'),
        "author": {"@type": "Organization", "name": "Slowcial", "url": SITE + '/'},
        "publisher": {"@type": "Organization", "name": "Slowcial",
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/media/icon-512.png"}},
        "mainEntityOfPage": {"@id": url + "#page"},
    }, {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in d['faq']],
    }, {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Slowcial", "item": SITE + p['home']},
            {"@type": "ListItem", "position": 2, "name": o['nav_guides'], "item": SITE + p['guides']},
            {"@type": "ListItem", "position": 3, "name": d['h1'].replace('<em>', '').replace('</em>', '')},
        ],
    }]
    # Un HowTo n'a de sens que si la page décrit vraiment des étapes.
    etapes = next((v for k, v in d['body'] if k == 'steps'), None)
    if etapes:
        ld.append({
            "@context": "https://schema.org", "@type": "HowTo", "name": d['title'],
            "description": d['desc'], "inLanguage": o['locale'].replace('_', '-'),
            "step": [{"@type": "HowToStep", "position": i + 1, "name": t, "text": txt}
                     for i, (t, txt) in enumerate(etapes)],
        })

    corps = ''.join(bloc(b) for b in d['body'])
    faq = ''.join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="a"><p>{r}</p></div></details>'
        for i, (q, r) in enumerate(d['faq']))

    autres = [g for g in liste_guides(lang) if g['slug'] != d['slug']][:3]
    cartes = ''.join(f"""<a class="rcard rev" href="{p['guides']}{g['slug']}/">
      <img src="/media/articles/{g['img']}-800.webp" alt="" width="800" height="343" loading="lazy">
      <div class="b"><h3>{g['short']}</h3><p>{g['desc'][:105]}…</p></div></a>""" for g in autres)

    html = head(lang, path, alt, d['title'], d['desc'], a['img'], ld)
    html += banniere(a['img'], d['eyebrow'], d['h1'], d['lede'],
                     f"<span>{o['updated']} {AUJ}</span><span>{lecture} {o['read']}</span>")
    html += f"""<article class="wrap prose">{corps}
  <h2 class="rev">{o['faq_h']}</h2>
  <div class="faq rev">{faq}</div>
</article>
{cta(lang)}
<section class="wrap related"><h2 class="rev">{o['related']}</h2><div class="rgrid">{cartes}</div></section>
"""
    html += foot(lang, liste_guides(lang))
    ecrire(path, html)
    return path


def page_guides(lang):
    o, p = T[lang], PATHS[lang]
    autre = 'en' if lang == 'fr' else 'fr'
    path, alt = p['guides'], PATHS[autre]['guides']
    titre = ("Guides — retirer ce qui te retient sur les réseaux" if lang == 'fr'
             else "Guides — removing what keeps you scrolling")
    desc = ("Des guides concrets pour retirer les reels, les shorts, les suggestions et les pages "
            "de découverte des réseaux sociaux. Ce que les réglages permettent vraiment, et ce qu'ils ne permettent pas."
            if lang == 'fr' else
            "Practical guides to removing reels, shorts, suggestions and discovery pages from social "
            "networks. What the settings genuinely allow, and what they don't.")
    intro = ("Chaque guide répond d'abord avec les réglages du réseau concerné — y compris quand la "
             "réponse est « il n'y en a pas ». Ensuite seulement, ce que Slowcial fait à la place."
             if lang == 'fr' else
             "Every guide answers first with the network's own settings — including when the answer is "
             "“there aren't any”. Only then, what Slowcial does instead.")
    gs = liste_guides(lang)
    cartes = ''.join(f"""<a class="rcard rev" href="{p['guides']}{g['slug']}/">
      <img src="/media/articles/{g['img']}-800.webp" alt="" width="800" height="343" loading="lazy">
      <div class="b"><p class="eyebrow">{g['eyebrow']}</p><h3 style="margin-top:8px">{g['short']}</h3>
      <p>{g['desc'][:120]}…</p></div></a>""" for g in gs)
    ld = [{"@context": "https://schema.org", "@type": "ItemList",
           "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                "url": f"{SITE}{p['guides']}{g['slug']}/", "name": g['short']}
                               for i, g in enumerate(gs)]}]
    html = head(lang, path, alt, titre, desc, 'p3', ld)
    html += banniere('p3', o['nav_guides'],
                     "Retirer ce qui te retient" if lang == 'fr' else "Remove what keeps you scrolling",
                     intro, f"<span>{len(gs)} {'guides' if lang == 'fr' else 'guides'}</span>")
    html += f"""<section class="wrap" style="padding:64px 0 20px">
  <div class="rgrid">{cartes}</div></section>
{cta(lang)}"""
    html += foot(lang, gs)
    ecrire(path, html)
    return path


def page_filters(lang):
    o, p = T[lang], PATHS[lang]
    autre = 'en' if lang == 'fr' else 'fr'
    path, alt = p['filters'], PATHS[autre]['filters']
    with open(os.path.join(RACINE, 'rules.json'), encoding='utf-8') as f:
        jeu = json.load(f)

    titre = (f"Ce que Slowcial retire, réseau par réseau (règles v{jeu['version']})" if lang == 'fr'
             else f"What Slowcial removes, network by network (rules v{jeu['version']})")
    desc = ("La liste exacte des filtres appliqués par Slowcial sur chaque réseau, générée depuis le "
            "jeu de règles réellement servi aux appareils." if lang == 'fr' else
            "The exact list of filters Slowcial applies to each network, generated from the rule set "
            "actually served to devices.")
    intro = ("Cette page est produite à partir de rules.json, le fichier que les appareils téléchargent. "
             "Elle ne peut donc pas promettre un filtre qui n'existe plus." if lang == 'fr' else
             "This page is generated from rules.json, the file devices download. It therefore cannot "
             "promise a filter that no longer exists.")

    lignes = ''
    for net, fl in jeu['filters'].items():
        nom = NETS.get(net, net)
        bientot = (' <span style="color:var(--ink2);font-size:14px">— '
                   + ('arrive prochainement' if lang == 'fr' else 'coming soon')
                   + '</span>') if net in SOON else ''
        for i, flt in enumerate(fl):
            lab, sub = LABELS[lang].get(flt['key'], (flt['key'], ''))
            gratuit = ('Gratuit' if lang == 'fr' else 'Free') if flt.get('free') else '—'
            defaut = ('Oui' if lang == 'fr' else 'Yes') if flt['defaultOn'] else ('Non' if lang == 'fr' else 'No')
            r = flt['rule']
            quoi = []
            def pl(n, sing, plur):
                return f"{n} {sing if n == 1 else plur}"
            if r.get('css'):
                quoi.append(pl(len(r['css']), *(('sélecteur', 'sélecteurs') if lang == 'fr'
                                                else ('selector', 'selectors'))))
            if r.get('text'):
                quoi.append(pl(len(r['text']), *(('libellé', 'libellés') if lang == 'fr'
                                                 else ('label', 'labels'))))
            if r.get('switch') or r.get('switchUrl'):
                quoi.append('bascule de fil' if lang == 'fr' else 'feed switch')
            if r.get('pruneKeys'):
                quoi.append('élagage du lecteur' if lang == 'fr' else 'player pruning')
            prem = f'<td rowspan="{len(fl)}"><strong>{nom}</strong>{bientot}</td>' if i == 0 else ''
            lignes += (f'<tr>{prem}<td><strong>{lab}</strong><br><span style="color:var(--ink2);'
                       f'font-size:14.5px">{sub}</span></td><td>{gratuit}</td><td>{defaut}</td>'
                       f'<td><code>{", ".join(quoi)}</code></td></tr>')

    th = (['Réseau', 'Filtre', 'Sans abonnement', 'Actif par défaut', 'Mécanique']
          if lang == 'fr' else ['Network', 'Filter', 'Without subscription', 'On by default', 'Mechanism'])
    html = head(lang, path, alt, titre, desc, 'p5')
    maj = date_des_regles()
    html += banniere('p5', o['nav_filters'],
                     "Ce que Slowcial <em>retire</em>" if lang == 'fr' else "What Slowcial <em>removes</em>",
                     intro, f"<span>{'Règles' if lang == 'fr' else 'Rules'} v{jeu['version']}</span>"
                            f"<span>{'Règles mises à jour le' if lang == 'fr' else 'Rules updated'} {maj}</span>")
    html += f"""<section class="wrap prose">
  <div class="tablewrap rev" style="max-width:100%"><table>
    <thead><tr>{''.join(f'<th>{h}</th>' for h in th)}</tr></thead>
    <tbody>{lignes}</tbody></table></div>
  <aside class="note rev"><span class="k">{'Comment ça marche' if lang == 'fr' else 'How it works'}</span>
  <p>{"Les règles décrivent le HTML de sites que nous ne contrôlons pas. Quand un réseau refait son interface, un filtre cesse de mordre — nous corrigeons alors le jeu de règles et le republions ici. Les appareils le prennent au lancement suivant, sans mise à jour de l'application." if lang == 'fr' else "The rules describe the HTML of sites we don't control. When a network redesigns, a filter stops biting — we then fix the rule set and republish it here. Devices pick it up on their next launch, with no app update."}</p></aside>
</section>
{cta(lang)}"""
    html += foot(lang, liste_guides(lang))
    ecrire(path, html)
    return path


def page_calc(lang):
    o, p = T[lang], PATHS[lang]
    autre = 'en' if lang == 'fr' else 'fr'
    path, alt = p['calc'], PATHS[autre]['calc']
    fr = lang == 'fr'
    titre = ("Combien de temps te prennent les réseaux ? Le calcul" if fr
             else "How much time do social networks take? The maths")
    desc = ("Deux heures par jour font trente jours pleins par an. Fais le calcul avec ton propre "
            "chiffre : par semaine, par an, et sur dix ans." if fr else
            "Two hours a day is thirty full days a year. Run the numbers with your own figure: "
            "per week, per year, and over ten years.")
    intro = ("Pas de statistique inventée : ta durée quotidienne, multipliée. C'est de l'arithmétique, "
             "et c'est bien pour ça que le résultat pique." if fr else
             "No invented statistics: your daily figure, multiplied. It's arithmetic, which is exactly "
             "why the answer stings.")

    js_labels = json.dumps({
        'day': 'par jour' if fr else 'a day',
        'week': 'par semaine' if fr else 'a week',
        'year': 'par an' if fr else 'a year',
        'ten': 'sur dix ans' if fr else 'over ten years',
        'h': 'h', 'min': 'min', 'd': 'jours' if fr else 'days',
        'months': 'mois' if fr else 'months',
        'ctx': ("soit %s pleins, sommeil compris — des journées entières, pas des heures perdues ici et là" if fr
                else "that's %s, around the clock — whole days, not hours here and there"),
    }, ensure_ascii=False)

    html = head(lang, path, alt, titre, desc, 'p8')
    html += banniere('p8', o['nav_calc'],
                     "Le calcul que <em>personne</em> ne fait" if fr else "The maths <em>nobody</em> does",
                     intro, f"<span>{'Arithmétique, pas sondage' if fr else 'Arithmetic, not a survey'}</span>")
    html += f"""
<style>
.calc{{background:var(--card);border:1px solid var(--line);border-radius:26px;
  padding:clamp(26px,4vw,44px);margin:56px 0;max-width:100%}}
.calc .lab{{font-family:var(--body);font-weight:600;font-size:12.5px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink2)}}
.calc .val{{font-family:var(--display);font-weight:800;font-size:clamp(40px,8vw,74px);
  letter-spacing:-.045em;line-height:1;color:var(--ink);margin:10px 0 4px}}
input[type=range]{{-webkit-appearance:none;appearance:none;width:100%;height:5px;border-radius:99px;
  background:linear-gradient(90deg,var(--terra) var(--pct,25%),var(--line) var(--pct,25%));
  margin:26px 0 6px;cursor:pointer}}
input[type=range]::-webkit-slider-thumb{{-webkit-appearance:none;width:30px;height:30px;border-radius:50%;
  background:var(--terra);border:4px solid var(--card);box-shadow:0 3px 12px -2px rgba(59,42,30,.5)}}
input[type=range]::-moz-range-thumb{{width:30px;height:30px;border:4px solid var(--card);border-radius:50%;
  background:var(--terra);box-shadow:0 3px 12px -2px rgba(59,42,30,.5)}}
.scale{{display:flex;justify-content:space-between;font-size:13.5px;color:var(--ink2)}}
.out{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));margin-top:38px}}
.out div{{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:20px 22px}}
.out .n{{font-family:var(--display);font-weight:700;font-size:clamp(25px,4vw,34px);
  letter-spacing:-.035em;color:var(--terra);line-height:1.05}}
.out .k{{font-size:13.5px;color:var(--ink2);margin-top:7px}}
.verdict{{margin-top:30px;font-family:var(--display);font-weight:500;font-size:clamp(19px,2.6vw,25px);
  line-height:1.3;letter-spacing:-.025em;color:var(--ink)}}
</style>
<section class="wrap prose">
  <div class="calc rev">
    <p class="lab">{'Ton temps sur les réseaux' if fr else 'Your time on social networks'}</p>
    <p class="val" id="v">1 h 45</p>
    <input type="range" id="r" min="10" max="360" step="5" value="105"
      aria-label="{'Minutes par jour' if fr else 'Minutes per day'}">
    <div class="scale"><span>10 min</span><span>3 h</span><span>6 h</span></div>
    <div class="out">
      <div><p class="n" id="o1">—</p><p class="k">{'par semaine' if fr else 'a week'}</p></div>
      <div><p class="n" id="o2">—</p><p class="k">{'par an' if fr else 'a year'}</p></div>
      <div><p class="n" id="o3">—</p><p class="k">{'sur dix ans' if fr else 'over ten years'}</p></div>
    </div>
    <p class="verdict" id="vd"></p>
  </div>

  <h2 class="rev">{'Ce que le chiffre ne dit pas' if fr else "What the number doesn't say"}</h2>
  <p>{"Le total est déjà brutal, mais il sous-estime le coût réel. Une session de scroll ne prend pas que sa durée : elle prend aussi le temps qu'il faut pour revenir à ce qu'on faisait. Les études sur l'interruption de tâche parlent de plusieurs minutes de reprise — donc chaque incursion coûte plus que ce que mesure l'horloge." if fr else "The total is already blunt, but it underestimates the real cost. A scrolling session doesn't only take its own duration: it also takes the time needed to get back to what you were doing. Research on task interruption puts recovery at several minutes — so each visit costs more than the clock measures."}</p>
  <p class="pull rev">{"Le temps n'est pas perdu au moment où tu scrolles. Il est perdu après." if fr else "The time isn't lost while you scroll. It's lost afterwards."}</p>
  <p>{"L'autre chose que le chiffre ne dit pas : tout ce temps n'est pas à jeter. Répondre à un message, regarder les photos d'un ami, poster quelque chose — ça, c'est ce pour quoi tu as installé l'application. Ce qui coûte, c'est le reste : les vidéos courtes qui s'enchaînent, les suggestions, la page de découverte." if fr else "The other thing the number doesn't say: not all of that time is waste. Replying to a message, looking at a friend's photos, posting something — that's what you installed the app for. What costs you is the rest: the short videos that autoplay, the suggestions, the discovery page."}</p>
  <p>{"C'est exactement la ligne que trace Slowcial : il retire la seconde catégorie et laisse la première intacte." if fr else "That's exactly the line Slowcial draws: it removes the second category and leaves the first intact."}</p>
</section>
{cta(lang)}
<script>
(function(){{
  var L = {js_labels};
  var r = document.getElementById('r'), v = document.getElementById('v');
  var o1 = document.getElementById('o1'), o2 = document.getElementById('o2'),
      o3 = document.getElementById('o3'), vd = document.getElementById('vd');
  function hm(m){{ var h = Math.floor(m/60), x = Math.round(m%60);
    return (h ? h + ' ' + L.h + (x ? ' ' + String(x).padStart(2,'0') : '') : x + ' ' + L.min); }}
  function jours(m){{ return Math.round(m/1440); }}
  function maj(){{
    var m = +r.value;
    r.style.setProperty('--pct', ((m - 10) / 350 * 100) + '%');
    v.textContent = hm(m);
    o1.textContent = hm(m*7);
    var an = m*365, dj = jours(an);
    o2.textContent = dj + ' ' + L.d;
    o3.textContent = Math.round(jours(an*10)/30.4) + ' ' + L.months;
    vd.textContent = L.ctx.replace('%s', dj + ' ' + L.d);
  }}
  r.addEventListener('input', maj); maj();
}})();
</script>
"""
    html += foot(lang, liste_guides(lang))
    ecrire(path, html)
    return path


def page_home_en():
    lang, autre = 'en', 'fr'
    p = PATHS[lang]
    path, alt = p['home'], PATHS[autre]['home']
    titre = "Slowcial — Social networks, minus what keeps you scrolling"
    desc = ("Slowcial removes reels, shorts, recommendation feeds and discovery pages from Instagram, "
            "YouTube, Facebook, Reddit and X — and keeps your messages and the people you follow. "
            "Nothing leaves your phone.")
    gs = liste_guides(lang)
    cartes = ''.join(f"""<a class="rcard rev" href="{p['guides']}{g['slug']}/">
      <img src="/media/articles/{g['img']}-800.webp" alt="" width="800" height="343" loading="lazy">
      <div class="b"><h3>{g['short']}</h3><p>{g['desc'][:100]}…</p></div></a>""" for g in gs[:3])

    shots = [('accueil', 'Your networks, and the time they take'),
             ('reseaux', 'Filters you set one by one'),
             ('nuit', 'Night mode closes Slowcial, not your phone'),
             ('stats', 'What you actually spend, measured on the device'),
             ('endormir', 'A sound to fall asleep to, with a timer')]
    rail = ''.join(f"""<figure class="rcard rev" style="border-radius:22px">
      <img src="/media/screens-en/{f}.jpg" alt="{c}" loading="lazy" style="height:auto">
      <figcaption class="b" style="font-size:15px;color:var(--ink2)">{c}</figcaption></figure>"""
                   for f, c in shots)

    ld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Slowcial",
           "applicationCategory": "HealthApplication", "operatingSystem": "iOS",
           "inLanguage": ["fr", "en", "de", "es", "it", "pl", "pt", "nl"],
           "description": desc, "url": SITE + '/en/',
           "offers": [{"@type": "Offer", "price": "0", "priceCurrency": "EUR",
                       "description": "One filtered network, free"},
                      {"@type": "Offer", "price": "34.99", "priceCurrency": "EUR",
                       "description": "Premium yearly — unlimited filtering"},
                      {"@type": "Offer", "price": "4.99", "priceCurrency": "EUR",
                       "description": "Premium monthly — unlimited filtering"}]}]

    html = head(lang, path, alt, titre, desc, 'p3', ld)
    html += banniere('p3', 'Digital wellbeing',
                     "Social networks, <em>minus</em> what keeps you scrolling",
                     "Slowcial opens the networks you already use and strips the mechanics built to hold "
                     "you: short-video feeds, recommendation tabs, discovery pages, sponsored posts. Your "
                     "messages and the people you follow don't move.",
                     "<span>iPhone</span><span>One network free</span><span>No account</span>")
    html += f"""
<section class="wrap prose">
  <p class="big">It doesn't block anything. Blocking isn't realistic — you'd lose your messages along
  with the reels, and you'd reinstall within three days. Slowcial removes, surgically, and leaves the
  rest of the network intact.</p>

  <div class="compare rev">
    <div class="col bad"><h3>What it removes</h3><ul>
      <li>Short-video feeds that autoplay endlessly</li>
      <li>Algorithmic recommendations and “for you” tabs</li>
      <li>Explore and discovery pages</li>
      <li>Sponsored posts in the feed</li></ul></div>
    <div class="col good"><h3>What you keep</h3><ul>
      <li>Your messages and conversations</li>
      <li>The accounts you chose to follow</li>
      <li>Profiles you decide to visit</li>
      <li>Posting, replying, searching</li></ul></div>
  </div>

  <h2 class="rev">Three steps, one minute</h2>
  <div class="steps">
    <div class="stepc rev"><div class="n">1</div><div><h3>Pick a network</h3>
      <p>Instagram, YouTube, Facebook, Reddit or X. One is free, for as long as you like.</p></div></div>
    <div class="stepc rev"><div class="n">2</div><div><h3>Sign in as usual</h3>
      <p>Directly on the network, in a web view. Slowcial never sees your credentials — it has no
      server to send them to.</p></div></div>
    <div class="stepc rev"><div class="n">3</div><div><h3>Scroll what's left</h3>
      <p>Which is the part you came for. Set each filter on or off, network by network.</p></div></div>
  </div>

  <h2 class="rev">What it looks like</h2>
</section>
<section class="wrap" style="padding-bottom:10px"><div class="rgrid">{rail}</div></section>

<section class="wrap prose">
  <h2 class="rev">Privacy, plainly</h2>
  <p>There is no account and no backend. Your settings, your screen time and the pages you open stay
  on the device. What does leave: an anonymous crash report you can switch off, subscription validation,
  and advertising attribution — none of which contains what you browse.</p>

  <h2 class="rev">Price</h2>
  <p>One filtered network is <strong>free</strong>, with night mode and statistics included. Premium
  unlocks every network and every filter at <strong>€34.99 a year</strong> (€2.92 a month) or
  <strong>€4.99 a month</strong>. No ads, ever — the app is funded by the people who use it.</p>

  <h2 class="rev">Guides</h2>
</section>
<section class="wrap" style="padding-bottom:20px"><div class="rgrid">{cartes}</div>
  <p style="margin-top:22px"><a href="{p['guides']}" style="color:var(--terra);text-decoration:none;
  border-bottom:1px solid currentColor">All guides →</a></p></section>
{cta(lang)}"""
    html += foot(lang, gs)
    ecrire(path, html)
    return path


def sitemap(chemins):
    lignes = ''
    for c, prio, freq in chemins:
        lignes += (f'  <url><loc>{SITE}{c}</loc><lastmod>{AUJ}</lastmod>'
                   f'<changefreq>{freq}</changefreq><priority>{prio}</priority></url>\n')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + lignes + '</urlset>\n')
    with open(os.path.join(RACINE, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(xml)


def main():
    chemins = [('/', '1.0', 'weekly')]
    for lang in ('fr', 'en'):
        for a in ARTICLES:
            chemins.append((page_article(a, lang), '0.8', 'monthly'))
        chemins.append((page_guides(lang), '0.9', 'weekly'))
        chemins.append((page_filters(lang), '0.8', 'weekly'))
        chemins.append((page_calc(lang), '0.7', 'monthly'))
    chemins.append((page_home_en(), '1.0', 'weekly'))
    for c in ('/confidentialite/', '/conditions/', '/privacy/'):
        chemins.append((c, '0.4', 'yearly'))
    sitemap(sorted(set(chemins)))
    print(f'{len(chemins)} URL dans le sitemap')
    for c, _, _ in sorted(set(chemins)):
        print('  ', c)


if __name__ == '__main__':
    main()
