# -*- coding: utf-8 -*-
"""
Le contenu des guides, en français et en anglais.
Rendu par tools/build.py. Aucun HTML ici : uniquement des blocs typés.

Blocs disponibles :
  ('h2', texte) ('p', texte) ('big', texte) ('ul', [..]) ('pull', texte)
  ('note', (titre, texte)) ('steps', [(titre, texte), ..])
  ('compare', (titre_a, [..], titre_b, [..]))

Le HTML inline toléré dans les textes : <strong>, <em>, <a href>.

RÈGLE DE FOND — chaque guide répond VRAIMENT avant de parler de Slowcial.
Une page qui ne fait que vendre ne se positionne pas, et se fait démolir en
commentaires. Quand un réglage natif existe, on le donne. Quand il n'existe
pas, on le dit. C'est aussi ce qui rend la page utile à quelqu'un qui
n'installera jamais l'application — et c'est ce que les moteurs mesurent.
"""

ARTICLES = [
    # ————————————————————————————————————————————————— 1. Reels Instagram
    {
        'id': 'ig-reels', 'img': 'p1', 'net': 'Instagram',
        'fr': {
            'slug': 'enlever-les-reels-instagram',
            'title': "Comment enlever les Reels d'Instagram (2026)",
            'h1': "Enlever les Reels d'<em>Instagram</em>",
            'eyebrow': 'Guide · Instagram',
            'lede': "Il n'existe pas de bouton pour les supprimer. Voici ce que les réglages d'Instagram permettent vraiment, et ce qu'il faut faire pour ne plus les voir du tout.",
            'desc': "Instagram ne propose aucun réglage pour retirer les Reels. Voici les options natives qui existent vraiment, leurs limites, et la méthode qui les fait disparaître pour de bon.",
            'body': [
                ('big', "Cherchons tout de suite à être honnête : <strong>Instagram ne propose pas de réglage pour retirer les Reels</strong>. Ni dans les paramètres, ni dans un menu caché. Si tu es arrivé ici en espérant un interrupteur, il n'y en a pas."),
                ('p', "Ce qui existe en revanche, ce sont trois contournements partiels et une solution qui tient. Prenons-les dans l'ordre."),

                ('h2', "Pourquoi il n'y a pas de bouton"),
                ('p', "Les Reels ne sont pas une fonctionnalité parmi d'autres : c'est la réponse d'Instagram à TikTok, et la partie de l'application où les gens passent le plus de temps. Un réglage qui les retirerait ferait chuter la seule métrique qui compte pour un réseau financé par la publicité — le temps passé."),
                ('p', "Ce n'est pas un oubli, donc, et il ne faut pas l'attendre. Ce qui explique aussi pourquoi les contournements listés plus bas sont toujours <em>temporaires</em> : quand un réglage de ce genre existe, il s'éteint tout seul au bout de quelques semaines."),
                ('pull', "Un réglage qui s'expire au bout de 30 jours n'est pas un réglage. C'est un sursis."),

                ('h2', "Ce que tu peux faire dans Instagram, aujourd'hui"),
                ('steps', [
                    ("Passer le fil en « Abonnements »",
                     "Touche « Instagram » en haut à gauche du fil : un menu propose <strong>Abonnements</strong> et <strong>Favoris</strong>. Le fil devient alors chronologique, limité aux comptes que tu suis. C'est le réglage le plus efficace du lot. Sa limite : Instagram ne le garde pas — à la prochaine ouverture, tu es revenu sur le fil algorithmique."),
                    ("Mettre les contenus suggérés en pause",
                     "Dans Paramètres → Préférences de contenu, un réglage permet de suspendre les publications suggérées pendant trente jours. Il ne touche pas à l'onglet Reels, et il expire — mais il calme le fil principal."),
                    ("Répondre « Pas intéressé »",
                     "Sur chaque Reel suggéré, le menu « … » propose <em>Pas intéressé</em>. Tu apprends à l'algorithme ce que tu ne veux pas, un élément à la fois. Concrètement, ça déplace le problème plutôt que de le résoudre : il te proposera autre chose."),
                ]),
                ('note', ("À savoir", "Les interfaces changent sans prévenir, et ces chemins peuvent différer selon ta version de l'application ou ton pays. Le principe, lui, ne bouge pas : rien de ce que propose Instagram ne retire l'onglet Reels.")),

                ('h2', "Ce qui ne marche pas, et qu'on te conseillera quand même"),
                ('ul', [
                    "<strong>Supprimer l'application.</strong> Tu perds tes messages et tes groupes en même temps que les Reels. C'est pour ça que ça tient trois jours : la détox demande de choisir entre son temps et ses gens.",
                    "<strong>Les bloqueurs d'applications.</strong> Ils coupent l'accès entier à heure fixe. Le problème n'a jamais été d'ouvrir Instagram ; c'est ce qui se passe une fois dedans.",
                    "<strong>Le mode restreint.</strong> Il filtre du contenu sensible, pas les mécaniques d'engagement. Aucun effet sur les Reels.",
                    "<strong>Se désabonner de tout.</strong> Le fil suggéré ne dépend pas de tes abonnements — c'est exactement son principe.",
                ]),

                ('h2', "La méthode qui tient : retirer, pas bloquer"),
                ('p', "Slowcial ouvre Instagram dans une vue web et retire les éléments avant qu'ils ne s'affichent : l'accès aux Reels, la page Explorer, les publications suggérées, les posts sponsorisés. Ton compte, tes messages, tes abonnements et tes publications ne bougent pas — c'est le même Instagram, avec la partie conçue pour te retenir en moins."),
                ('compare', ("Supprimer l'application", [
                    "Tu perds tes messages",
                    "Tu perds tes groupes et tes contacts",
                    "Tu réinstalles au bout de trois jours",
                    "Tout ou rien",
                ], "Retirer les mécaniques", [
                    "Tes messages restent",
                    "Tes abonnements restent",
                    "Le réglage ne s'expire pas",
                    "Tu choisis quoi enlever, filtre par filtre",
                ])),
                ('p', "La bascule vers le fil « Abonnements » est rejouée à chaque ouverture, donc elle ne se perd plus entre deux sessions. Et le filtrage se règle élément par élément : si tu veux garder Explorer mais enlever les Reels, c'est un interrupteur."),
            ],
            'faq': [
                ("Peut-on désactiver les Reels dans les paramètres d'Instagram ?",
                 "Non. Aucun réglage d'Instagram ne retire les Reels ni l'onglet qui y mène. Les options existantes — fil « Abonnements », pause des contenus suggérés, « Pas intéressé » — réduisent les suggestions dans le fil principal, mais l'onglet Reels reste."),
                ("Le fil « Abonnements » reste-t-il sélectionné ?",
                 "Non, et c'est sa principale limite : Instagram revient au fil algorithmique à l'ouverture suivante. Il faut le resélectionner à chaque fois — sauf à passer par un outil qui rejoue la bascule pour toi."),
                ("Est-ce que ça marche sans donner ses identifiants à une application tierce ?",
                 "Oui. Avec Slowcial, tu te connectes directement à Instagram dans une vue web, comme dans un navigateur. L'application ne lit pas, ne copie pas et ne transmet pas tes identifiants, et n'a aucun serveur pour les recevoir."),
            ],
        },
        'en': {
            'slug': 'remove-instagram-reels',
            'title': "How to Remove Reels from Instagram (2026)",
            'h1': "Remove Reels from <em>Instagram</em>",
            'eyebrow': 'Guide · Instagram',
            'lede': "There is no button for it. Here is what Instagram's settings actually allow, and what it takes to stop seeing Reels for good.",
            'desc': "Instagram has no setting to remove Reels. Here are the native options that do exist, what they can't do, and the method that makes Reels disappear for good.",
            'body': [
                ('big', "Let's be straight from the start: <strong>Instagram has no setting that removes Reels</strong>. Not in preferences, not in a hidden menu. If you came here hoping for a switch, there isn't one."),
                ('p', "What does exist is three partial workarounds and one thing that actually holds. In order."),

                ('h2', "Why there is no switch"),
                ('p', "Reels aren't just another feature — they're Instagram's answer to TikTok, and the part of the app where people spend the most time. A setting that removed them would sink the one metric that matters to an ad-funded network: time spent."),
                ('p', "So it isn't an oversight, and it isn't coming. That also explains why every workaround below is <em>temporary</em>: when a setting like this exists at all, it expires on its own after a few weeks."),
                ('pull', "A setting that expires after 30 days isn't a setting. It's a reprieve."),

                ('h2', "What you can do inside Instagram today"),
                ('steps', [
                    ("Switch the feed to Following",
                     "Tap “Instagram” at the top left of your feed: a menu offers <strong>Following</strong> and <strong>Favourites</strong>. The feed becomes chronological, limited to accounts you follow. It's the most effective option here. The catch: Instagram doesn't keep it — next launch, you're back on the algorithmic feed."),
                    ("Pause suggested content",
                     "Under Settings → Content preferences, you can pause suggested posts for thirty days. It doesn't touch the Reels tab, and it expires — but it quiets the main feed."),
                    ("Tap “Not interested”",
                     "On any suggested Reel, the “…” menu offers <em>Not interested</em>. You're teaching the algorithm what you don't want, one item at a time. In practice it moves the problem rather than solving it: it will suggest something else."),
                ]),
                ('note', ("Worth knowing", "Interfaces change without notice, and these paths may differ by app version or country. The principle doesn't change: nothing Instagram offers removes the Reels tab.")),

                ('h2', "What doesn't work — and gets recommended anyway"),
                ('ul', [
                    "<strong>Deleting the app.</strong> You lose your messages and your groups along with the Reels. That's why it lasts three days: a detox asks you to choose between your time and your people.",
                    "<strong>App blockers.</strong> They cut off access at a set hour. Opening Instagram was never the problem; what happens once you're inside is.",
                    "<strong>Restricted mode.</strong> It filters sensitive content, not engagement mechanics. No effect on Reels.",
                    "<strong>Unfollowing everyone.</strong> The suggested feed doesn't depend on who you follow — that's precisely the point of it.",
                ]),

                ('h2', "The method that holds: remove, don't block"),
                ('p', "Slowcial opens Instagram in a web view and strips the elements before they render: access to Reels, the Explore page, suggested posts, sponsored posts. Your account, your messages, the people you follow and your own posts don't move — it's the same Instagram, minus the part built to keep you there."),
                ('compare', ("Deleting the app", [
                    "You lose your messages",
                    "You lose your groups and contacts",
                    "You reinstall within three days",
                    "All or nothing",
                ], "Removing the mechanics", [
                    "Your messages stay",
                    "The people you follow stay",
                    "The setting never expires",
                    "You choose what goes, filter by filter",
                ])),
                ('p', "The switch to the Following feed is replayed every time you open the app, so it no longer gets lost between sessions. And filtering is per element: keep Explore but drop Reels, and that's one toggle."),
            ],
            'faq': [
                ("Can you disable Reels in Instagram's settings?",
                 "No. No Instagram setting removes Reels or the tab that leads to them. The options that exist — the Following feed, pausing suggested content, “Not interested” — reduce suggestions in the main feed, but the Reels tab stays."),
                ("Does the Following feed stay selected?",
                 "No, and that's its main limitation: Instagram reverts to the algorithmic feed next time you open it. You have to reselect it every session — unless something replays the switch for you."),
                ("Does this work without giving a third-party app my login?",
                 "Yes. With Slowcial you sign in to Instagram directly in a web view, exactly as you would in a browser. The app doesn't read, copy or transmit your credentials, and has no server to receive them."),
            ],
        },
    },

    # ————————————————————————————————————————————————— 2. Shorts YouTube
    {
        'id': 'yt-shorts', 'img': 'p4', 'net': 'YouTube',
        'fr': {
            'slug': 'desactiver-les-shorts-youtube',
            'title': "Désactiver les Shorts YouTube sur mobile (2026)",
            'h1': "Désactiver les <em>Shorts</em> YouTube",
            'eyebrow': 'Guide · YouTube',
            'lede': "YouTube laisse masquer l'étagère Shorts — pendant trente jours. Voici les réglages réels, et comment obtenir un YouTube sans Shorts qui ne se réactive pas.",
            'desc': "YouTube ne propose que de masquer les Shorts pendant 30 jours. Voici tous les réglages disponibles, l'historique de visionnage, et la méthode pour un YouTube sans Shorts durable.",
            'body': [
                ('big', "YouTube est un peu plus généreux qu'Instagram : il existe bien un réglage pour masquer les Shorts. Il dure <strong>trente jours</strong>, puis tout revient."),
                ('p', "C'est déjà ça, et ça vaut la peine de l'activer. Mais si tu es ici pour la troisième fois en six mois, tu sais déjà que ce n'est pas une solution."),

                ('h2', "Les deux réglages qui existent vraiment"),
                ('steps', [
                    ("Masquer l'étagère Shorts",
                     "Sur la page d'accueil, à côté du bandeau « Shorts », le menu « … » propose de <strong>masquer</strong> l'étagère. YouTube indique alors qu'elle ne reviendra pas avant trente jours. À refaire chaque mois, donc, et ça ne retire pas l'onglet Shorts de la barre du bas."),
                    ("Couper l'historique de visionnage",
                     "Dans les paramètres de ton compte Google, suspendre l'historique des vidéos regardées vide la page d'accueil de ses recommandations. C'est radical et ça marche — au prix de perdre aussi les suggestions que tu trouvais utiles, et la reprise de lecture."),
                ]),
                ('note', ("La version web", "Sur ordinateur, un bloqueur de contenu avec la bonne règle CSS retire les Shorts définitivement. Sur mobile, l'application native n'accepte aucune extension — d'où toute la difficulté.")),

                ('h2', "Pourquoi les Shorts reviennent toujours"),
                ('p', "Le format court est ce que YouTube oppose à TikTok, et l'étagère de la page d'accueil est son meilleur point d'entrée. Un masquage permanent enlèverait à YouTube son principal levier de rétention sur mobile ; les trente jours sont le compromis entre te laisser souffler et ne pas te laisser partir."),
                ('pull', "Trente jours, c'est assez long pour que tu oublies, et assez court pour que ça revienne."),

                ('h2', "Un YouTube sans Shorts, durablement"),
                ('p', "Slowcial ouvre YouTube dans une vue web et retire les Shorts à chaque chargement : les vignettes dans le fil, les étagères de la page d'accueil, et l'onglet dans la barre de navigation. Les abonnements, l'historique, les playlists et les commentaires restent intacts."),
                ('p', "Contrairement au réglage natif, il n'y a rien à refaire tous les mois : la règle s'applique à chaque ouverture, et elle est vérifiée avant chaque publication. L'audit le plus récent relevait huit vignettes, deux étagères et l'onglet de la barre, tous retirés."),
                ('ul', [
                    "Les vidéos de tes abonnements s'ouvrent normalement",
                    "La recherche fonctionne comme d'habitude",
                    "Un Short qu'on t'envoie en lien reste regardable — tu ne peux simplement pas enchaîner",
                ]),
            ],
            'faq': [
                ("Peut-on désactiver les Shorts définitivement sur YouTube ?",
                 "Pas depuis l'application elle-même. Le masquage de l'étagère Shorts dure trente jours, puis elle réapparaît, et l'onglet Shorts de la barre du bas n'est jamais concerné. Seul un outil qui retire les éléments à chaque chargement donne un résultat durable."),
                ("Couper l'historique de visionnage suffit-il ?",
                 "Ça vide la page d'accueil de ses recommandations, donc des Shorts qu'elle contenait — mais tu perds aussi les suggestions utiles, la reprise de lecture et l'onglet Shorts reste en place."),
                ("Est-ce que ça marche avec YouTube Premium ?",
                 "Oui. Le filtrage porte sur l'affichage des pages, pas sur ton compte : un abonnement Premium continue de fonctionner normalement."),
            ],
        },
        'en': {
            'slug': 'turn-off-youtube-shorts',
            'title': "How to Turn Off YouTube Shorts on Mobile (2026)",
            'h1': "Turn off YouTube <em>Shorts</em>",
            'eyebrow': 'Guide · YouTube',
            'lede': "YouTube lets you hide the Shorts shelf — for thirty days. Here are the real settings, and how to get a YouTube without Shorts that doesn't switch itself back on.",
            'desc': "YouTube only lets you hide Shorts for 30 days. Here are every available setting, the watch-history trick, and how to get a lasting YouTube without Shorts.",
            'body': [
                ('big', "YouTube is a little more generous than Instagram: there is a setting to hide Shorts. It lasts <strong>thirty days</strong>, then everything comes back."),
                ('p', "That's something, and it's worth turning on. But if this is your third visit to a page like this in six months, you already know it isn't a solution."),

                ('h2', "The two settings that genuinely exist"),
                ('steps', [
                    ("Hide the Shorts shelf",
                     "On the home page, next to the “Shorts” header, the “…” menu offers to <strong>hide</strong> the shelf. YouTube then tells you it won't be back for thirty days. So it's a monthly chore — and it doesn't remove the Shorts tab from the bottom bar."),
                    ("Turn off watch history",
                     "In your Google account settings, pausing watch history empties the home page of recommendations. It's blunt and it works — at the cost of losing the suggestions you actually liked, and resume-where-you-left-off."),
                ]),
                ('note', ("The web version", "On desktop, a content blocker with the right CSS rule removes Shorts permanently. On mobile, the native app accepts no extensions — which is the whole difficulty.")),

                ('h2', "Why Shorts always come back"),
                ('p', "Short form is YouTube's answer to TikTok, and the home-page shelf is its best entry point. Hiding it permanently would cost YouTube its main retention lever on mobile; thirty days is the compromise between letting you breathe and not letting you leave."),
                ('pull', "Thirty days is long enough that you forget, and short enough that it returns."),

                ('h2', "A YouTube without Shorts, for good"),
                ('p', "Slowcial opens YouTube in a web view and strips Shorts on every load: the thumbnails in the feed, the home-page shelves, and the tab in the navigation bar. Subscriptions, history, playlists and comments are untouched."),
                ('p', "Unlike the native setting, there's nothing to redo every month: the rule applies on every open, and it's verified before each release. The most recent audit counted eight thumbnails, two shelves and the navigation tab — all removed."),
                ('ul', [
                    "Videos from your subscriptions open normally",
                    "Search works exactly as before",
                    "A Short someone sends you as a link still plays — you just can't swipe to the next one",
                ]),
            ],
            'faq': [
                ("Can you disable YouTube Shorts permanently?",
                 "Not from the app itself. Hiding the Shorts shelf lasts thirty days, then it reappears, and the Shorts tab in the bottom bar is never affected. Only a tool that strips the elements on every load gives a lasting result."),
                ("Is turning off watch history enough?",
                 "It empties the home page of recommendations, and therefore of the Shorts it carried — but you also lose useful suggestions, resume playback, and the Shorts tab stays put."),
                ("Does this work with YouTube Premium?",
                 "Yes. Filtering applies to how pages are displayed, not to your account: a Premium subscription keeps working normally."),
            ],
        },
    },
    # ————————————————————————————————————————————————— 3. Explorer Instagram
    {
        'id': 'ig-explore', 'img': 'p2', 'net': 'Instagram',
        'fr': {
            'slug': 'enlever-explore-instagram',
            'title': "Enlever la page Explorer d'Instagram (2026)",
            'h1': "Enlever <em>Explorer</em> d'Instagram",
            'eyebrow': 'Guide · Instagram',
            'lede': "La loupe, c'est la porte d'entrée du scroll sans fin. Instagram ne permet pas de la retirer — voici ce qu'on peut faire à la place.",
            'desc': "Instagram ne permet pas de supprimer l'onglet Explorer. Voici comment en réduire l'effet, pourquoi le réinitialiser ne suffit pas, et comment le faire disparaître.",
            'body': [
                ('big', "Explorer est la page la plus efficace d'Instagram : une grille infinie de contenus choisis par l'algorithme, sans un seul compte que tu as demandé à suivre. <strong>Elle ne peut pas être désactivée.</strong>"),
                ('p', "Elle est pourtant, pour beaucoup de gens, l'endroit exact où les vingt minutes passent. On ouvre pour chercher quelque chose, on touche la loupe, et on ressort ailleurs."),

                ('h2', "Le piège de la loupe"),
                ('p', "Le détail qui rend Explorer si redoutable : l'onglet sert à la fois à <em>chercher</em> et à <em>découvrir</em>. Tu le touches avec une intention précise — retrouver un compte, une recette, un lieu — et avant le champ de recherche, tu reçois une grille conçue pour te retenir. L'intention est détournée à la seconde où tu arrives."),
                ('pull', "On ne va pas sur Explorer. On y tombe en allant chercher autre chose."),

                ('h2', "Ce que permettent les réglages d'Instagram"),
                ('steps', [
                    ("Réinitialiser les suggestions",
                     "Dans Paramètres → Contenus suggérés, il est possible de remettre à zéro ce qu'Instagram croit savoir de tes goûts. La grille redevient générique quelques jours, puis se reconstruit — elle apprend vite."),
                    ("Marquer « Pas intéressé »",
                     "Sur chaque vignette, un appui long propose de ne plus voir ce type de contenu. Utile pour sortir d'un thème envahissant ; sans effet sur l'existence de la page."),
                    ("Passer le compte en privé",
                     "Ça change ce que les autres voient de toi, pas ce que tu vois. Contrairement à une idée répandue, aucun effet sur Explorer."),
                ]),
                ('note', ("Ce qu'on lit souvent et qui est faux", "Non, se désabonner de comptes ne vide pas Explorer : la page ne se nourrit pas de tes abonnements mais de ce que regardent des gens jugés semblables à toi. C'est pour ça qu'elle reste pleine même sur un compte neuf.")),

                ('h2', "Retirer la page plutôt que la subir"),
                ('p', "Slowcial retire l'accès à Explorer d'Instagram : l'onglet disparaît de la barre de navigation, et avec lui la grille. La recherche par nom de compte, elle, reste disponible — c'est la partie utile de la loupe, et il n'y a aucune raison de s'en priver."),
                ('p', "Chaque filtre est indépendant : tu peux retirer Explorer et garder les Reels, ou l'inverse. Rien n'est imposé en bloc."),
            ],
            'faq': [
                ("Peut-on supprimer l'onglet Explorer d'Instagram ?",
                 "Pas depuis l'application. Instagram permet de réinitialiser les suggestions et de masquer des thèmes, mais l'onglet et sa grille restent en place. Seul un outil qui retire l'élément à l'affichage le fait disparaître."),
                ("Réinitialiser les contenus suggérés, ça dure combien de temps ?",
                 "Quelques jours en pratique. La page se reconstruit à partir de ce que tu regardes ensuite, et regarder une seule vidéo suffit à relancer la machine."),
                ("Est-ce que je perds la recherche ?",
                 "Non. La recherche de comptes, de lieux et de hashtags continue de fonctionner : c'est la grille de découverte qui est retirée, pas le champ de recherche."),
            ],
        },
        'en': {
            'slug': 'remove-instagram-explore',
            'title': "How to Remove the Explore Page from Instagram (2026)",
            'h1': "Remove <em>Explore</em> from Instagram",
            'eyebrow': 'Guide · Instagram',
            'lede': "The magnifying glass is the front door to endless scrolling. Instagram won't let you remove it — here's what you can do instead.",
            'desc': "Instagram gives you no way to delete the Explore tab. Here's how to blunt it, why resetting suggestions isn't enough, and how to make it disappear.",
            'body': [
                ('big', "Explore is Instagram's most effective page: an infinite grid picked by the algorithm, without a single account you asked to follow. <strong>It cannot be turned off.</strong>"),
                ('p', "And for a lot of people it's exactly where the twenty minutes go. You open the app to look something up, you tap the magnifier, and you come out somewhere else entirely."),

                ('h2', "The magnifier trap"),
                ('p', "Here's what makes Explore so potent: the tab is both <em>search</em> and <em>discovery</em>. You tap it with a precise intention — find an account, a recipe, a place — and before the search field, you get a grid built to hold you. The intention is hijacked the second you arrive."),
                ('pull', "Nobody goes to Explore. You land there on your way somewhere else."),

                ('h2', "What Instagram's settings allow"),
                ('steps', [
                    ("Reset your suggestions",
                     "Under Settings → Suggested content, you can reset what Instagram thinks it knows about your taste. The grid goes generic for a few days, then rebuilds — it learns fast."),
                    ("Mark “Not interested”",
                     "Long-press any tile to stop seeing that kind of content. Useful for escaping one invasive theme; no effect on the page existing at all."),
                    ("Switch to a private account",
                     "That changes what others see of you, not what you see. Despite a widespread belief, it has no effect on Explore."),
                ]),
                ('note', ("A common claim that's simply false", "No, unfollowing accounts does not empty Explore: the page isn't fed by who you follow but by what people it considers similar to you are watching. That's why it stays full even on a brand-new account.")),

                ('h2', "Remove the page instead of enduring it"),
                ('p', "Slowcial strips Instagram's access to Explore: the tab disappears from the navigation bar, and the grid with it. Searching for an account by name still works — that's the useful half of the magnifier, and there's no reason to give it up."),
                ('p', "Every filter is independent: remove Explore and keep Reels, or the other way round. Nothing is imposed as a block."),
            ],
            'faq': [
                ("Can you delete the Explore tab on Instagram?",
                 "Not from the app. Instagram lets you reset suggestions and hide topics, but the tab and its grid stay put. Only a tool that strips the element at display time makes it disappear."),
                ("How long does resetting suggested content last?",
                 "A few days in practice. The page rebuilds from whatever you watch next, and a single video is enough to restart the machine."),
                ("Do I lose search?",
                 "No. Searching for accounts, places and hashtags keeps working: it's the discovery grid that's removed, not the search field."),
            ],
        },
    },

    # ————————————————————————————————————————————————— 4. Reels Facebook
    {
        'id': 'fb-reels', 'img': 'p6', 'net': 'Facebook',
        'fr': {
            'slug': 'enlever-les-reels-facebook',
            'title': "Enlever les Reels de Facebook (2026)",
            'h1': "Enlever les Reels de <em>Facebook</em>",
            'eyebrow': 'Guide · Facebook',
            'lede': "Facebook a un onglet « Flux » qui montre vos amis et rien d'autre. Presque personne ne le connaît, et il ne reste jamais sélectionné.",
            'desc': "Comment retirer les Reels et le contenu suggéré de Facebook : l'onglet Flux, ses limites, et comment obtenir un Facebook qui ne montre que vos amis.",
            'body': [
                ('big', "Facebook a une particularité : <strong>un fil « Amis » existe vraiment</strong>, et il fait exactement ce qu'on lui demande. Il est simplement rangé là où personne ne le cherche."),
                ('p', "Il s'appelle « Flux » selon les versions, et il se trouve dans le menu, pas dans la barre principale. Il affiche les publications de tes amis, en ordre chronologique, sans suggestions ni Reels."),

                ('h2', "Le fil « Flux », et pourquoi il ne suffit pas"),
                ('steps', [
                    ("Le trouver",
                     "Dans le menu de l'application, cherche <strong>Flux</strong> (ou « Feeds »). Il propose plusieurs vues, dont <em>Amis</em> : uniquement les publications des gens que tu as ajoutés."),
                    ("L'épingler",
                     "Sur certaines versions, il peut être ajouté aux raccourcis. Ça réduit le nombre de gestes ; ça ne change pas ce qui s'ouvre quand tu touches l'icône Facebook."),
                ]),
                ('p', "Et c'est là que ça coince : <strong>Facebook ne garde pas ton choix</strong>. L'application s'ouvre toujours sur le fil algorithmique, avec ses Reels, ses groupes suggérés et ses pages que tu n'as jamais aimées. Le bon fil existe, mais il faut le demander à chaque fois."),
                ('pull', "Le réglage que tu cherches existe. Il ne reste simplement jamais coché."),

                ('h2', "Ce que Slowcial retire sur Facebook"),
                ('p', "L'onglet Reels de l'en-tête, les étagères de Reels intercalées dans le fil, et les publications sponsorisées. Le dernier audit en relevait l'onglet, deux étagères dans le fil et un post sponsorisé — tous neutralisés."),
                ('ul', [
                    "Messenger et tes conversations ne sont pas touchés",
                    "Tes groupes restent accessibles",
                    "Les événements et les pages que tu suis ne bougent pas",
                ]),
                ('note', ("Un défaut connu, dit franchement", "Sur Facebook, l'emplacement de l'onglet Reels masqué laisse parfois un rectangle gris dans l'en-tête. C'est cosmétique, c'est relevé dans notre audit, et c'est en cours de correction — autant que tu le saches avant de l'installer.")),
            ],
            'faq': [
                ("Facebook a-t-il un fil sans Reels ?",
                 "Oui : le fil « Flux », vue « Amis », n'affiche que les publications de tes amis, sans suggestions ni Reels. Son défaut est qu'il ne reste pas sélectionné — l'application rouvre toujours sur le fil algorithmique."),
                ("Peut-on supprimer l'onglet Reels de Facebook ?",
                 "Aucun réglage de l'application ne le permet. Il peut en revanche être retiré à l'affichage par un outil de filtrage."),
                ("Est-ce que Messenger est affecté ?",
                 "Non. Le filtrage porte sur les pages de Facebook ; les messages, qu'ils soient dans l'application ou dans Messenger, ne sont pas concernés."),
            ],
        },
        'en': {
            'slug': 'remove-facebook-reels',
            'title': "How to Remove Reels from Facebook (2026)",
            'h1': "Remove Reels from <em>Facebook</em>",
            'eyebrow': 'Guide · Facebook',
            'lede': "Facebook has a Feeds tab that shows your friends and nothing else. Almost nobody knows it exists, and it never stays selected.",
            'desc': "How to remove Reels and suggested content from Facebook: the Feeds tab, its limits, and how to get a Facebook that only shows your friends.",
            'body': [
                ('big', "Facebook is a special case: <strong>a Friends-only feed genuinely exists</strong>, and it does exactly what you'd want. It's just filed where nobody looks."),
                ('p', "It's called Feeds, and it lives in the menu rather than the main bar. It shows posts from your friends, in chronological order, with no suggestions and no Reels."),

                ('h2', "The Feeds tab, and why it isn't enough"),
                ('steps', [
                    ("Find it",
                     "In the app menu, look for <strong>Feeds</strong>. It offers several views, one of them <em>Friends</em>: only posts from people you actually added."),
                    ("Pin it",
                     "On some versions it can be added to your shortcuts. That cuts the number of taps; it doesn't change what opens when you tap the Facebook icon."),
                ]),
                ('p', "And that's the catch: <strong>Facebook doesn't remember your choice</strong>. The app always opens on the algorithmic feed, with its Reels, its suggested groups and its pages you never liked. The right feed exists, but you have to ask for it every single time."),
                ('pull', "The setting you're looking for exists. It just never stays ticked."),

                ('h2', "What Slowcial strips on Facebook"),
                ('p', "The Reels tab in the header, the Reels shelves wedged into the feed, and sponsored posts. The last audit counted the tab, two in-feed shelves and one sponsored post — all neutralised."),
                ('ul', [
                    "Messenger and your conversations are untouched",
                    "Your groups stay reachable",
                    "Events and the pages you follow don't move",
                ]),
                ('note', ("A known flaw, stated plainly", "On Facebook, the hidden Reels tab sometimes leaves a grey rectangle in the header. It's cosmetic, it's logged in our own audit, and it's being fixed — you may as well know before you install.")),
            ],
            'faq': [
                ("Does Facebook have a feed without Reels?",
                 "Yes: the Feeds tab, Friends view, shows only posts from your friends, with no suggestions and no Reels. Its flaw is that it doesn't stay selected — the app always reopens on the algorithmic feed."),
                ("Can you delete the Reels tab on Facebook?",
                 "No app setting allows it. It can, however, be stripped at display time by a filtering tool."),
                ("Is Messenger affected?",
                 "No. Filtering applies to Facebook's pages; messages, whether in the app or in Messenger, are not touched."),
            ],
        },
    },

    # ————————————————————————————————————————————————— 5. Fil « Pour vous » de X
    {
        'id': 'x-following', 'img': 'p7', 'net': 'X',
        'fr': {
            'slug': 'x-fil-abonnements',
            'title': "X (Twitter) : garder le fil « Abonnements » (2026)",
            'h1': "X sans le fil <em>« Pour vous »</em>",
            'eyebrow': 'Guide · X',
            'lede': "L'onglet « Abonnements » existe. Le problème, c'est que X revient sur « Pour vous » dès que tu as le dos tourné.",
            'desc': "Comment rester sur le fil « Abonnements » de X (Twitter) : ce que permet l'application, pourquoi le choix ne tient pas, et comment le rendre permanent.",
            'body': [
                ('big', "Sur X, le bon réglage existe et il est à un centimètre du pouce : l'onglet <strong>Abonnements</strong>, juste à côté de « Pour vous ». Il affiche les comptes que tu suis, sans recommandation."),
                ('p', "Et pourtant tu finis toujours sur « Pour vous ». Ce n'est pas ton imagination."),

                ('h2', "Pourquoi le choix ne tient pas"),
                ('p', "Selon les versions et les plateformes, X reprend l'onglet « Pour vous » par défaut — au redémarrage de l'application, après une notification, ou en revenant d'un lien externe. Le choix n'est pas mémorisé de façon fiable, ce qui revient à devoir le refaire plusieurs fois par jour."),
                ('p', "Ajoute les publications sponsorisées glissées entre deux tweets, et les « suggestions de comptes à suivre » au milieu du fil, et le fil chronologique que tu croyais avoir choisi n'en est plus vraiment un."),
                ('pull', "Un réglage qu'il faut refaire six fois par jour n'est pas un réglage."),

                ('h2', "Ce qu'on peut faire dans X"),
                ('steps', [
                    ("Sélectionner « Abonnements »",
                     "En haut du fil, touche <strong>Abonnements</strong>. Sur certaines versions, un appui long sur l'onglet permet de gérer les onglets affichés et parfois de détacher « Pour vous »."),
                    ("Utiliser les listes",
                     "Une liste ne contient que les comptes que tu y mets et reste strictement chronologique, sans suggestion. C'est la meilleure partie de X, et la plus ignorée — mais il faut la construire à la main."),
                    ("Signaler les publicités",
                     "Le menu « … » d'un post sponsorisé permet de le masquer. Un par un, sans fin."),
                ]),

                ('h2', "Rendre le choix permanent"),
                ('p', "Slowcial rejoue la bascule vers « Abonnements » à chaque ouverture, retire les accès à Explorer et neutralise les publications sponsorisées. Le dernier audit a relevé <strong>vingt éléments publicitaires</strong> neutralisés sur une seule session, les trois accès à Explorer retirés et la bascule effectuée — c'est le réseau où le filtrage mord le plus fort."),
                ('ul', [
                    "Tes messages privés restent accessibles",
                    "Tes listes fonctionnent normalement",
                    "Tu peux toujours publier, répondre et rechercher",
                ]),
            ],
            'faq': [
                ("Peut-on supprimer l'onglet « Pour vous » sur X ?",
                 "Selon les versions, un appui long sur les onglets permet parfois d'en gérer l'affichage, mais rien ne garantit que « Abonnements » reste sélectionné. En pratique, X y revient régulièrement."),
                ("Les listes sont-elles une meilleure solution ?",
                 "Pour la qualité du fil, oui : une liste est strictement chronologique et ne contient que ce que tu y mets. Mais elle demande d'être construite, et elle ne remplace pas le fil d'accueil que tu ouvres par réflexe."),
                ("Est-ce que les publicités disparaissent complètement ?",
                 "Les publications sponsorisées repérées dans le fil sont neutralisées — vingt sur une session lors du dernier audit. Comme les réseaux changent leur balisage sans prévenir, les règles sont revérifiées et republiées régulièrement."),
            ],
        },
        'en': {
            'slug': 'x-following-feed',
            'title': "X (Twitter): How to Stay on the Following Feed (2026)",
            'h1': "X without the <em>For You</em> feed",
            'eyebrow': 'Guide · X',
            'lede': "The Following tab exists. The problem is that X snaps back to For You the moment you look away.",
            'desc': "How to stay on X's Following feed: what the app allows, why the choice doesn't stick, and how to make it permanent.",
            'body': [
                ('big', "On X the right setting exists and sits an inch from your thumb: the <strong>Following</strong> tab, right next to For You. It shows the accounts you follow, with no recommendations."),
                ('p', "And yet you always end up back on For You. That isn't your imagination."),

                ('h2', "Why the choice doesn't stick"),
                ('p', "Depending on version and platform, X reverts to For You by default — on app restart, after a notification, or when you come back from an external link. The choice isn't reliably remembered, which means remaking it several times a day."),
                ('p', "Add the sponsored posts slipped between tweets, and the “who to follow” suggestions mid-feed, and the chronological timeline you thought you'd picked isn't quite one any more."),
                ('pull', "A setting you have to redo six times a day isn't a setting."),

                ('h2', "What you can do inside X"),
                ('steps', [
                    ("Select Following",
                     "At the top of the timeline, tap <strong>Following</strong>. On some versions, long-pressing the tab bar lets you manage which tabs show, and sometimes unpin For You."),
                    ("Use lists",
                     "A list contains only the accounts you put in it and stays strictly chronological, with no suggestions. It's the best part of X and the most ignored — but you have to build it by hand."),
                    ("Report the ads",
                     "The “…” menu on a sponsored post lets you hide it. One at a time, forever."),
                ]),

                ('h2', "Making the choice permanent"),
                ('p', "Slowcial replays the switch to Following on every open, strips the routes into Explore, and neutralises sponsored posts. The last audit counted <strong>twenty ad elements</strong> neutralised in a single session, all three Explore entry points removed and the switch performed — it's the network where filtering bites hardest."),
                ('ul', [
                    "Your direct messages stay reachable",
                    "Your lists work normally",
                    "You can still post, reply and search",
                ]),
            ],
            'faq': [
                ("Can you delete the For You tab on X?",
                 "On some versions, long-pressing the tabs lets you manage what's shown, but nothing guarantees Following stays selected. In practice, X keeps coming back to For You."),
                ("Are lists a better answer?",
                 "For feed quality, yes: a list is strictly chronological and contains only what you put in it. But it has to be built, and it doesn't replace the home timeline you open by reflex."),
                ("Do ads disappear completely?",
                 "Sponsored posts detected in the timeline are neutralised — twenty in one session at the last audit. Because networks change their markup without notice, the rules are re-verified and republished regularly."),
            ],
        },
    },

    # ————————————————————————————————————————————————— 6. Supprimer ou pas
    {
        'id': 'delete-or-not', 'img': 'p9', 'net': None,
        'fr': {
            'slug': 'supprimer-instagram-ou-pas',
            'title': "Faut-il supprimer Instagram ? La réponse honnête",
            'h1': "Faut-il <em>supprimer</em> Instagram ?",
            'eyebrow': 'Réflexion',
            'lede': "Tout le monde te dit de le supprimer. Presque personne ne tient plus d'une semaine. Voilà pourquoi — et ce qui marche à la place.",
            'desc': "Supprimer Instagram échoue presque toujours, et ce n'est pas un problème de volonté. Voici pourquoi la détox ne tient pas, et l'alternative qui fonctionne.",
            'body': [
                ('big', "La suppression est le conseil le plus donné et le moins suivi d'internet. Ce n'est pas parce que les gens manquent de discipline. C'est parce que <strong>le conseil demande de choisir entre son temps et ses gens</strong>."),

                ('h2', "Ce que tu perds vraiment en supprimant"),
                ('ul', [
                    "Tes messages, souvent le seul canal avec certaines personnes",
                    "Les groupes où s'organisent des choses réelles",
                    "Les photos que ta famille poste et ne t'enverra jamais autrement",
                    "Pour beaucoup, une part de leur travail — clients, portfolio, contacts",
                ]),
                ('p', "Mis bout à bout, ça fait un prix que personne ne paie longtemps. Les trois jours de détox se terminent par une réinstallation, souvent honteuse, et la conviction d'avoir échoué à quelque chose de simple."),

                ('h2', "Ce n'est pas une question de volonté"),
                ('p', "En face de ta décision du soir, il y a des milliers de personnes payées à plein temps, des tests menés sur des centaines de millions d'utilisateurs, et des modèles qui savent quelle vidéo te retiendra avant que tu l'aies vue. Le fil est sans fin parce qu'une fin est un endroit où l'on s'arrête. Le geste de tirer vers le bas reproduit exactement celui d'une machine à sous : récompense imprévisible, geste répété."),
                ('pull', "Tu n'es pas accro. Tu es visé."),
                ('p', "Dit autrement : ce n'est pas un match. Et se juger sur le résultat d'un match truqué est la meilleure façon de recommencer le mois suivant."),

                ('h2', "La question qu'il faut poser à la place"),
                ('p', "Pas « est-ce que je supprime ? », mais <strong>« qu'est-ce qui, précisément, me fait perdre ce temps ? »</strong>. Pose-toi la question honnêtement et la réponse tient en trois éléments : les vidéos courtes qui s'enchaînent, le fil de recommandations, et la page de découverte."),
                ('p', "Aucun des trois n'est ce pour quoi tu as installé l'application. Retire ces trois-là, il reste une messagerie avec des photos d'amis — c'est-à-dire ce que c'était au début."),

                ('h2', "Ce que ça donne en pratique"),
                ('compare', ("La détox", [
                    "Tout ou rien",
                    "Tu perds le contact",
                    "Elle tient trois jours",
                    "Elle finit en sentiment d'échec",
                ], "Retirer les mécaniques", [
                    "Tu gardes les messages et les gens",
                    "Tu enlèves ce qui te retient",
                    "Rien à retenir chaque jour",
                    "Le réglage tient tout seul",
                ])),
                ('p', "C'est ce que fait Slowcial : ouvrir les réseaux en retirant les vidéos courtes, les suggestions et les pages de découverte, et laisser le reste intact. Un réseau est gratuit, sans publicité, et rien ne quitte ton téléphone."),
            ],
            'faq': [
                ("Est-ce que supprimer Instagram fonctionne vraiment ?",
                 "Pour une minorité de gens, oui, durablement. Pour la plupart, non : le coût social est immédiat et le bénéfice diffus, si bien que la réinstallation arrive en quelques jours. Ce n'est pas un défaut de caractère, c'est une question de rapport coût/bénéfice."),
                ("Combien de temps faut-il pour voir une différence ?",
                 "En retirant les vidéos courtes et les suggestions, la différence se voit dès la première session : il n'y a simplement plus rien à faire défiler après les publications de tes abonnés."),
                ("Et si je veux quand même supprimer ?",
                 "Alors fais-le, c'est la solution la plus radicale et elle a ses mérites. Garde simplement en tête que rien ne t'oblige à choisir entre tout garder et tout perdre."),
            ],
        },
        'en': {
            'slug': 'should-i-delete-instagram',
            'title': "Should You Delete Instagram? The Honest Answer",
            'h1': "Should you <em>delete</em> Instagram?",
            'eyebrow': 'Essay',
            'lede': "Everyone tells you to delete it. Almost nobody lasts a week. Here's why — and what works instead.",
            'desc': "Deleting Instagram almost always fails, and it isn't a willpower problem. Here's why the detox doesn't hold, and the alternative that does.",
            'body': [
                ('big', "Deleting is the most given and least followed advice on the internet. Not because people lack discipline. Because <strong>the advice asks you to choose between your time and your people</strong>."),

                ('h2', "What you actually lose by deleting"),
                ('ul', [
                    "Your messages — often the only channel you have with certain people",
                    "The groups where real things get organised",
                    "The photos your family posts and will never send you any other way",
                    "For many, part of their work — clients, portfolio, contacts",
                ]),
                ('p', "Add it up and it's a price nobody pays for long. The three-day detox ends in a reinstall, usually a sheepish one, and the belief that you failed at something simple."),

                ('h2', "It is not a willpower problem"),
                ('p', "Facing your evening decision are thousands of people paid full-time, tests run on hundreds of millions of users, and models that know which video will hold you before you've seen it. The feed is endless because an end is a place where you stop. Pulling down to refresh reproduces a slot machine exactly: unpredictable reward, repeated gesture."),
                ('pull', "You're not addicted. You're targeted."),
                ('p', "Put another way: it was never a fair match. And judging yourself on the result of a rigged one is the surest way to try again next month."),

                ('h2', "The question to ask instead"),
                ('p', "Not “should I delete it?” but <strong>“what precisely is taking the time?”</strong>. Answer honestly and it comes down to three things: short videos that autoplay one after another, the recommendation feed, and the discovery page."),
                ('p', "None of the three is why you installed the app. Remove those three and what's left is a messaging app with photos from friends — which is what it was in the first place."),

                ('h2', "What that looks like in practice"),
                ('compare', ("The detox", [
                    "All or nothing",
                    "You lose contact",
                    "It lasts three days",
                    "It ends in a sense of failure",
                ], "Removing the mechanics", [
                    "You keep the messages and the people",
                    "You remove what holds you",
                    "Nothing to sustain every day",
                    "The setting holds by itself",
                ])),
                ('p', "That's what Slowcial does: it opens the networks with the short videos, the suggestions and the discovery pages stripped out, and leaves the rest intact. One network is free, there are no ads, and nothing leaves your phone."),
            ],
            'faq': [
                ("Does deleting Instagram actually work?",
                 "For a minority of people, yes, lastingly. For most, no: the social cost is immediate and the benefit diffuse, so the reinstall comes within days. That isn't a character flaw, it's a cost-benefit ratio."),
                ("How long before I notice a difference?",
                 "With short videos and suggestions stripped out, you notice in the first session: there is simply nothing left to scroll once you've seen the posts from people you follow."),
                ("What if I want to delete it anyway?",
                 "Then do — it's the most radical option and it has its merits. Just keep in mind that nothing forces you to choose between keeping everything and losing everything."),
            ],
        },
    },
    # ————————————————————————————————————————————————— 7. Comparatif des méthodes
    {
        'id': 'methodes', 'img': 'p5', 'net': None,
        'fr': {
            'slug': 'comment-moins-scroller-methodes-comparees',
            'title': "Moins scroller : les 6 méthodes comparées (2026)",
            'h1': "Les <em>six</em> façons de moins scroller",
            'eyebrow': 'Comparatif',
            'lede': "Bloqueurs, minuteurs, suppression, écran en gris, comptes secondaires, filtrage. Ce que chacune fait vraiment, et pourquoi la plupart ne tiennent pas.",
            'desc': "Comparatif honnête des méthodes pour réduire le scroll : bloqueurs d'applications, Temps d'écran, suppression, écran en niveaux de gris, second compte, filtrage. Ce qui tient dans la durée et ce qui ne tient pas.",
            'body': [
                ('big', "Toutes ces méthodes marchent. La question n'est pas leur efficacité sur le moment — c'est <strong>combien de temps on les garde</strong>. Une méthode abandonnée au bout de quatre jours a une efficacité réelle de zéro."),
                ('p', "Voilà les six, avec ce que chacune coûte et ce qui la fait lâcher."),

                ('h2', "1. Supprimer l'application"),
                ('p', "<strong>Ce que ça fait :</strong> tout disparaît, d'un coup. C'est la méthode la plus efficace pendant qu'elle dure."),
                ('p', "<strong>Pourquoi ça lâche :</strong> les messages partent avec le reste. Les groupes, les photos de famille, parfois une part du travail. Le coût social est immédiat et le bénéfice diffus — c'est exactement le rapport qui fait réinstaller en trois jours."),
                ('p', "<strong>Pour qui ça marche :</strong> ceux dont la vie sociale ne passe pas par ce réseau. C'est une minorité, et elle le sait déjà."),

                ('h2', "2. Les bloqueurs d'applications"),
                ('p', "<strong>Ce que ça fait :</strong> l'accès est coupé à heure fixe, ou après un quota."),
                ('p', "<strong>Pourquoi ça lâche :</strong> le problème n'a jamais été d'ouvrir l'application — c'est ce qui se passe une fois dedans. Un bloqueur traite l'accès, pas le contenu. Et il bloque aussi les cinq minutes légitimes où tu voulais répondre à quelqu'un, ce qui pousse à le désactiver « juste cette fois »."),
                ('p', "<strong>Le piège :</strong> plus le blocage est strict, plus vite on apprend à le contourner. La plupart des gens connaissent le code de leur propre restriction par cœur."),

                ('h2', "3. Temps d'écran et limites natives"),
                ('p', "<strong>Ce que ça fait :</strong> iOS et Android mesurent et avertissent, puis limitent."),
                ('p', "<strong>Pourquoi ça lâche :</strong> « Ignorer la limite » est un bouton. Il est à un centimètre du pouce, au moment exact où la volonté est la plus basse. La mesure, elle, reste utile — c'est sa meilleure partie."),

                ('h2', "4. L'écran en niveaux de gris"),
                ('p', "<strong>Ce que ça fait :</strong> retirer la couleur rend les vignettes moins attirantes. L'effet est réel et documenté."),
                ('p', "<strong>Pourquoi ça lâche :</strong> ça dégrade tout le téléphone, y compris les photos, la carte, l'appareil photo. On le remet en couleur pour une raison précise, et on oublie de le recouper."),

                ('h2', "5. Le second compte, ou le téléphone secondaire"),
                ('p', "<strong>Ce que ça fait :</strong> un compte neuf n'a pas d'historique, donc un fil de recommandation pauvre."),
                ('p', "<strong>Pourquoi ça lâche :</strong> l'algorithme apprend vite. Quelques jours suffisent à reconstituer un fil aussi captif que l'ancien — et tu as désormais deux comptes à surveiller au lieu d'un."),

                ('h2', "6. Retirer les mécaniques, garder le réseau"),
                ('p', "<strong>Ce que ça fait :</strong> le réseau s'ouvre normalement, mais les fils de vidéos courtes, les recommandations et les pages de découverte n'y sont plus. Les messages, les abonnements et les profils ne bougent pas."),
                ('p', "<strong>Pourquoi ça tient :</strong> il n'y a rien à tenir. Aucun quota à respecter, aucune heure à attendre, aucun bouton « ignorer » à ne pas toucher. Le réglage se pose une fois et ne demande plus rien — et il ne coupe jamais ce pour quoi tu avais installé l'application."),
                ('p', "<strong>Sa limite, dite franchement :</strong> les règles décrivent le balisage de sites que personne ne contrôle. Quand un réseau refait son interface, un filtre cesse de mordre jusqu'à ce que la règle soit corrigée. C'est le prix de cette approche, et c'est pour ça que le jeu de règles de Slowcial est servi à part de l'application, réparable en quelques minutes plutôt qu'en quelques jours."),

                ('h2', "Le tableau"),
                ('compare', ("Ce qui coupe l'accès", [
                    "Suppression : tu perds les messages",
                    "Bloqueurs : tu perds aussi les usages légitimes",
                    "Limites natives : un bouton « ignorer » suffit",
                    "Demande un effort chaque jour",
                ], "Ce qui retire les mécaniques", [
                    "Les messages et les abonnements restent",
                    "Seul le fil conçu pour retenir disparaît",
                    "Rien à ignorer, rien à contourner",
                    "Se règle une fois",
                ])),

                ('h2', "Que choisir"),
                ('ul', [
                    "<strong>Si le réseau ne te sert à rien socialement</strong> — supprime-le. C'est plus simple et c'est gratuit.",
                    "<strong>Si le problème est le soir</strong> — une plage horaire suffit, et beaucoup d'outils en proposent, Slowcial compris.",
                    "<strong>Si tu y perds du temps mais que tu ne peux pas partir</strong> — retirer les mécaniques est la seule méthode de cette liste qui ne te demande pas de choisir entre ton temps et tes gens.",
                ]),
                ('pull', "La meilleure méthode n'est pas la plus stricte. C'est celle que tu auras encore dans six mois."),
            ],
            'faq': [
                ("Quelle est la méthode la plus efficace pour moins scroller ?",
                 "Sur le moment, supprimer l'application. Dans la durée, retirer les mécaniques d'engagement en gardant le réseau — parce que c'est la seule qui ne coûte pas l'accès aux messages, et qu'on n'abandonne donc pas au bout de quelques jours."),
                ("Les bloqueurs d'applications fonctionnent-ils ?",
                 "Ils coupent l'accès, ce qui règle un problème différent : le problème n'est pas d'ouvrir l'application, c'est le fil sans fin qu'on y trouve. Et parce qu'ils bloquent aussi les usages légitimes, ils finissent désactivés."),
                ("Le mode niveaux de gris réduit-il vraiment le temps d'écran ?",
                 "L'effet existe : un fil sans couleur attire moins. Sa faiblesse est qu'il s'applique à tout le téléphone, y compris aux photos et à l'appareil photo, si bien qu'on le désactive pour une raison ponctuelle et qu'on oublie de le remettre."),
                ("Peut-on garder ses messages tout en supprimant les reels ?",
                 "Oui. C'est précisément ce que fait le filtrage : le réseau s'ouvre avec ton compte, tes conversations et tes abonnements intacts, mais sans les fils de vidéos courtes, les suggestions ni les pages de découverte."),
            ],
        },
        'en': {
            'slug': 'how-to-scroll-less-methods-compared',
            'title': "Scrolling Less: 6 Methods Compared (2026)",
            'h1': "The <em>six</em> ways to scroll less",
            'eyebrow': 'Comparison',
            'lede': "Blockers, timers, deleting, greyscale, second accounts, filtering. What each one actually does, and why most of them don't last.",
            'desc': "An honest comparison of ways to cut scrolling: app blockers, Screen Time, deleting the app, greyscale, a second account, filtering. What holds over time and what doesn't.",
            'body': [
                ('big', "All of these work. The question isn't whether they work in the moment — it's <strong>how long you keep them</strong>. A method abandoned after four days has a real-world effectiveness of zero."),
                ('p', "Here are the six, with what each one costs and what makes people quit."),

                ('h2', "1. Deleting the app"),
                ('p', "<strong>What it does:</strong> everything goes at once. It's the most effective method for as long as it lasts."),
                ('p', "<strong>Why it fails:</strong> your messages go with it. The groups, the family photos, sometimes part of your work. The social cost is immediate and the benefit diffuse — exactly the ratio that gets it reinstalled within three days."),
                ('p', "<strong>Who it works for:</strong> people whose social life doesn't run through that network. That's a minority, and they already know it."),

                ('h2', "2. App blockers"),
                ('p', "<strong>What it does:</strong> access is cut at a set hour, or after a quota."),
                ('p', "<strong>Why it fails:</strong> opening the app was never the problem — what happens once you're inside is. A blocker treats access, not content. It also blocks the legitimate five minutes where you wanted to reply to someone, which is what pushes people to disable it “just this once”."),
                ('p', "<strong>The trap:</strong> the stricter the block, the faster you learn to route around it. Most people know their own restriction passcode by heart."),

                ('h2', "3. Screen Time and built-in limits"),
                ('p', "<strong>What it does:</strong> iOS and Android measure, warn, then limit."),
                ('p', "<strong>Why it fails:</strong> “Ignore limit” is a button. It sits an inch from your thumb, at exactly the moment willpower is lowest. The measuring, though, stays genuinely useful — it's the best part."),

                ('h2', "4. Greyscale"),
                ('p', "<strong>What it does:</strong> removing colour makes thumbnails less pulling. The effect is real and documented."),
                ('p', "<strong>Why it fails:</strong> it degrades the whole phone, photos, maps and camera included. You turn colour back on for one specific reason, and forget to turn it off again."),

                ('h2', "5. A second account, or a second phone"),
                ('p', "<strong>What it does:</strong> a fresh account has no history, so a thin recommendation feed."),
                ('p', "<strong>Why it fails:</strong> the algorithm learns fast. A few days is enough to rebuild a feed as gripping as the old one — and now you have two accounts to watch instead of one."),

                ('h2', "6. Removing the mechanics, keeping the network"),
                ('p', "<strong>What it does:</strong> the network opens normally, but the short-video feeds, the recommendations and the discovery pages aren't there. Messages, the accounts you follow and profiles don't move."),
                ('p', "<strong>Why it holds:</strong> there's nothing to hold. No quota to respect, no hour to wait for, no “ignore” button to avoid pressing. The setting is made once and asks nothing more — and it never cuts off the thing you installed the app for."),
                ('p', "<strong>Its limitation, stated plainly:</strong> the rules describe the markup of sites nobody controls. When a network redesigns, a filter stops biting until the rule is fixed. That's the price of this approach, and it's why Slowcial's rule set is served separately from the app — repairable in minutes rather than days."),

                ('h2', "The table"),
                ('compare', ("Methods that cut access", [
                    "Deleting: you lose the messages",
                    "Blockers: you lose legitimate use too",
                    "Built-in limits: one “ignore” button is enough",
                    "Requires effort every day",
                ], "Methods that remove mechanics", [
                    "Messages and the people you follow stay",
                    "Only the feed built to hold you goes",
                    "Nothing to ignore, nothing to route around",
                    "Set once",
                ])),

                ('h2', "What to choose"),
                ('ul', [
                    "<strong>If the network does nothing for you socially</strong> — delete it. It's simpler and free.",
                    "<strong>If the problem is evenings</strong> — a time window is enough, and plenty of tools offer one, Slowcial included.",
                    "<strong>If it costs you time but you can't leave</strong> — removing the mechanics is the only method here that doesn't ask you to choose between your time and your people.",
                ]),
                ('pull', "The best method isn't the strictest. It's the one you'll still have in six months."),
            ],
            'faq': [
                ("What's the most effective way to scroll less?",
                 "In the moment, deleting the app. Over time, removing the engagement mechanics while keeping the network — because it's the only one that doesn't cost you access to your messages, and so doesn't get abandoned after a few days."),
                ("Do app blockers work?",
                 "They cut off access, which solves a different problem: the problem isn't opening the app, it's the endless feed you find inside. And because they block legitimate use too, they end up switched off."),
                ("Does greyscale actually reduce screen time?",
                 "The effect is real: a feed without colour pulls less. Its weakness is that it applies to the entire phone, photos and camera included, so you disable it for one specific reason and forget to re-enable it."),
                ("Can you keep your messages while removing reels?",
                 "Yes. That's precisely what filtering does: the network opens with your account, your conversations and the people you follow intact, but without short-video feeds, suggestions or discovery pages."),
            ],
        },
    },
]
