#!/usr/bin/env python3
"""Baut die statische Mulligan-Website: Startseite DE/EN, Rechtstexte DE/EN, 404.
Rechtstexte kommen als HTML-Fragmente aus LEGAL_DIR."""
import html
import os
import re
import sys

# Aufruf aus website/:  python3 _quellen/build.py
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)
LEGAL_DIR = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "rechtstexte")
DOMAIN = "https://mulligan-playgolf.com"
MAIL = "contact@mulligan-playgolf.com"
OWNER = "Becker &amp; Groß GbR"
YEAR = "2026"

ICONS = {
    "people": '<svg class="ico" viewBox="0 0 28 28" fill="none" stroke="#C6BC93" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="10.5" cy="9" r="4"/><path d="M3 23.5c0-4.2 3.3-7.5 7.5-7.5s7.5 3.3 7.5 7.5"/><circle cx="20.5" cy="10" r="3"/><path d="M19.5 16.2c3.4.3 5.5 3 5.5 6.3"/></svg>',
    "chart": '<svg class="ico" viewBox="0 0 28 28" fill="none" stroke="#C6BC93" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 24.5h21"/><path d="M4 19.5l6-6.5 4.5 3.5L23 7"/><path d="M17.5 7H23v5.5"/></svg>',
    "bolt": '<svg class="ico" viewBox="0 0 28 28" fill="none" stroke="#C6BC93" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15.5 3 6 16h7.5l-1.5 9L21.5 12H14l1.5-9z"/></svg>',
    "trophy": '<svg class="ico" viewBox="0 0 28 28" fill="none" stroke="#C6BC93" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8.5 4h11v6.5a5.5 5.5 0 0 1-11 0V4z"/><path d="M8.5 6.5H5v1.5a4 4 0 0 0 4 4"/><path d="M19.5 6.5H23v1.5a4 4 0 0 1-4 4"/><path d="M14 16v4.5"/><path d="M9.5 24.5h9l-1-4h-7z"/></svg>',
    "flag": '<svg class="ico" viewBox="0 0 28 28" fill="none" stroke="#C6BC93" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7.5 25V3.5"/><path d="M7.5 4.5h13l-3 4.75 3 4.75h-13"/><path d="M4 25h8"/></svg>',
}

T = {
    "de": {
        "lang": "de",
        "locale": "de_DE",
        "home": "/",
        "other_home": "/en",
        "switch_label": "EN",
        "switch_aria": "English version",
        "title": "Mulligan · Social Golf Club Düsseldorf",
        "desc": "Mulligan ist der Social Golf Club aus Düsseldorf: 9-Loch-Matches gegen Leute auf deinem Niveau, ein Rating, das sich nach jeder Runde bewegt, neue Leute im Flight und Events. Kostenlos, bald im App Store.",
        "skip": "Zum Inhalt springen",
        "logo_alt": "Mulligan, zur Startseite",
        "legal": {"impressum": ("/impressum", "Impressum"), "datenschutz": ("/datenschutz", "Datenschutz"), "agb": ("/agb", "AGB")},
        "foot_other": ("/en", "English"),
        "foot_brand": "Mulligan · Social Golf Club Düsseldorf",
        "kicker": "Bald im App Store",
        "h1": "Spiel um Punkte.<br>Lern Leute kennen.<br><em>Steig im Rang auf.</em>",
        "lead": "Mulligan macht aus jeder Runde ein Match. Du spielst 9 Loch gegen Leute auf deinem Niveau, dein Rating bewegt sich nach jeder Runde, und im Flight lernst du neue Leute kennen. Ohne Startgeld, kostenlos in der App.",
        "get_title": "Bald im App Store",
        "get_text": "Scan den Code mit deinem iPhone. Sobald die App erscheint, führt er direkt dorthin. Für iPhone, kostenlos.",
        "qr_alt": "QR-Code: führt zum Start der App in den App Store, bis dahin auf diese Seite",
        "pill": "Bald im App Store",
        "get_note": "Für iPhone. Kostenlos, ohne Startgeld.",
        "screen": "/assets/img/screen-spiele-de.webp",
        "screen_alt": "Die Mulligan App: Tab Spiele mit Tagesleiste, Filtern und offenen Matches",
        "caption": "Beispielansicht mit erfundenen Daten",
        "app_kicker": "So funktioniert's",
        "app_h2": "Ein Tipp, und du bist <em>im Flight.</em>",
        "app_p": "Jedes Match ist eine 9-Loch-Runde mit zwei bis vier Leuten. Die Startzeit beim Club bucht, wer das Match eröffnet. Das Greenfee zahlt jeder vor Ort.",
        "steps": [
            ("01", "Finden", "Match finden oder eröffnen", "Offene Matches in deiner Nähe, mit Club, Uhrzeit und Spielmodus. Du siehst vorher, wer mitspielt und auf welchem Niveau. Oder du eröffnest selbst und lädst Freunde ein."),
            ("02", "Spielen", "Ergebnis eintragen", "Nach der Runde trägt jeder seine Schläge ein, ein Mitspieler bestätigt. Treffpunkt und Anfahrt klärt ihr vorher im Flight-Chat."),
            ("03", "Aufsteigen", "Rating und Rang", "Wer gewinnt, bekommt Punkte, gegen Stärkere mehr. So landest du bei den nächsten Matches bei Leuten, die zu dir passen."),
            ("04", "Vernetzen", "Freunde, Clubs und Events", "Folge Leuten aus deinem Flight, gib Applaus für gute Runden und entdecke Clubs, Rangeabende und Events in deiner Umgebung."),
        ],
        "soon": "In Vorbereitung: Trainerstunden buchen und der Mulligan Shop.",
        "why_kicker": "Warum Mulligan",
        "why_h2": "Ein Club ohne Clubhaus. <em>Dafür mit Rivalen.</em>",
        "why": [
            ("bolt", "Jede Runde zählt", "Dein Mulligan Rating ändert sich nach jeder gewerteten Runde. Es zählt, wen du schlägst, nicht um wie viele Schläge. Du musst nicht aufs nächste Turnier warten, um zu sehen, ob du besser wirst."),
            ("trophy", "Wettkampf ohne Startgeld", "Jeder gegen jeden oder 2 gegen 2, die Ergebnisse bestätigt der Flight. Die App kostet nichts. Du zahlst nur dein Greenfee vor Ort."),
            ("people", "Neue Leute auf deinem Level", "In jedem Flight triffst du Leute, die so spielen wie du. Dazu Rangeabende und Events, bei denen aus Mitspielern Freunde werden. Oder mehr."),
            ("chart", "Zeig, was du draufhast", "Dein Profil zeigt Rang, Rating, Bestmarke und Meilensteine. Etwa fünf Siege gegen Gleichstarke bringen dich einen Rang weiter, von Rookie bis Albatros."),
        ],
        "demo_label": "Beispiele aus der App",
        "match": {"time": "09:40", "date": "Sa 24. Okt", "place": "Neuss", "mode": "2 gegen 2", "avg": "Ø 1.175", "rank": "Bogey", "free": "2 frei", "aria": "Match in Neuss am Samstag, 24. Oktober, 09:40 Uhr, 2 gegen 2, zwei Plätze frei"},
        "chat": [("other", "Jonas", "Moin, wer fährt am Samstag?"), ("other", "Maja", "Ich kann zwei mitnehmen."), ("me", "", "Ich bin dabei. 09:20 bei dir?"), ("sys", "", "Anna ist beigetreten")],
        "chat_aria": "Flight-Chat",
        "rating": {"label": "Mulligan Rating", "num": "1.160", "delta": "+20", "rank": "Bogey", "note": "Noch 40 Punkte bis Par"},
        "cta_kicker": "Mitmachen",
        "cta_h2": "Wir starten in <em>Düsseldorf.</em>",
        "cta_p": "Mulligan erscheint bald für iPhone. Du betreibst einen Golfclub oder eine Indoor-Anlage, gibst Trainerstunden oder willst dein Produkt zeigen? Dann werde Partner und mach mit uns Events.",
        "back": "Zur Startseite",
        "nav_partner": ("/partner", "Partner werden"),
        "cta_button": "Partner werden",
        "stand": "Stand: Oktober 2026",
        "toc": "Inhalt",
        "nf_title": "Seite nicht gefunden · Mulligan",
        "nf_h1": "Diese Seite gibt es nicht.",
        "nf_p": "Vielleicht ein Tippfehler. Auf der Startseite geht es weiter.",
    },
    "en": {
        "lang": "en",
        "locale": "en_GB",
        "home": "/en",
        "other_home": "/",
        "switch_label": "DE",
        "switch_aria": "Deutsche Version",
        "title": "Mulligan · Social Golf Club Düsseldorf",
        "desc": "Mulligan is the social golf club from Düsseldorf: 9-hole matches against people at your level, a rating that moves after every round, new people in every flight and events. Free, coming soon to the App Store.",
        "skip": "Skip to content",
        "logo_alt": "Mulligan, back to home",
        "legal": {"impressum": ("/en/imprint", "Imprint"), "datenschutz": ("/en/privacy", "Privacy"), "agb": ("/en/terms", "Terms")},
        "foot_other": ("/", "Deutsch"),
        "foot_brand": "Mulligan · Social Golf Club Düsseldorf",
        "kicker": "Coming soon to the App Store",
        "h1": "Play for points.<br>Meet new people.<br><em>Climb the ranks.</em>",
        "lead": "Mulligan turns every round into a match. You play 9 holes against people at your level, your rating moves after every round, and you meet new people in every flight. No entry fee, free in the app.",
        "get_title": "Coming soon to the App Store",
        "get_text": "Scan the code with your iPhone. Once the app is out, it takes you straight there. For iPhone, free.",
        "qr_alt": "QR code: leads to the app in the App Store once it launches, to this page until then",
        "pill": "Coming soon to the App Store",
        "get_note": "For iPhone. Free, no entry fee.",
        "screen": "/assets/img/screen-feed-en.webp",
        "screen_alt": "The Mulligan app: the Feed tab with this week's rounds and a scored round",
        "caption": "Sample view with made-up data",
        "app_kicker": "How it works",
        "app_h2": "One tap and you're <em>in the flight.</em>",
        "app_p": "Every match is a 9-hole round for two to four players. Whoever opens the match books the tee time with the club. Everyone pays their green fee on site.",
        "steps": [
            ("01", "Find", "Find or open a match", "Open matches nearby with club, tee time and game mode. You see who's playing and at what level before you join. Or open one yourself and invite friends."),
            ("02", "Play", "Enter your score", "After the round, everyone enters their strokes and another player confirms them. Where to meet and who's driving gets sorted in the flight chat beforehand."),
            ("03", "Climb", "Rating and rank", "Win and you gain points, more against stronger players. That way your next matches put you with people who fit your game."),
            ("04", "Connect", "Friends, clubs and events", "Follow people from your flight, give applause for good rounds and discover clubs, range nights and events near you."),
        ],
        "soon": "In the works: booking lessons and the Mulligan shop.",
        "why_kicker": "Why Mulligan",
        "why_h2": "A club without a clubhouse. <em>But with rivals.</em>",
        "why": [
            ("bolt", "Every round counts", "Your Mulligan Rating changes after every scored round. What counts is who you beat, not by how many strokes. No waiting for the next tournament to see if you're getting better."),
            ("trophy", "Competition without entry fees", "Everyone vs everyone or 2 vs 2, with scores confirmed by the flight. The app is free. You only pay your green fee on site."),
            ("people", "New people at your level", "Every flight brings people who play like you. Plus range nights and events where playing partners become friends. Or more."),
            ("chart", "Show what you've got", "Your profile shows your rank, rating, personal best and milestones. About five wins against equally strong players move you up a rank, from Rookie to Albatross."),
        ],
        "demo_label": "Examples from the app",
        "match": {"time": "09:40", "date": "Sat 24 Oct", "place": "Neuss", "mode": "2 vs 2", "avg": "avg 1,175", "rank": "Bogey", "free": "2 open", "aria": "Match in Neuss on Saturday 24 October at 09:40, 2 vs 2, two open spots"},
        "chat": [("other", "Jonas", "Morning, who's driving on Saturday?"), ("other", "Maja", "I can take two."), ("me", "", "I'm in. 09:20 at yours?"), ("sys", "", "Anna joined")],
        "chat_aria": "Flight chat",
        "rating": {"label": "Mulligan Rating", "num": "1,160", "delta": "+20", "rank": "Bogey", "note": "40 points to Par"},
        "cta_kicker": "Get involved",
        "cta_h2": "We're starting in <em>Düsseldorf.</em>",
        "cta_p": "Mulligan is coming soon for iPhone. Do you run a golf club or an indoor facility, give lessons or want to show your product? Become a partner and host events with us.",
        "back": "Back to home",
        "nav_partner": ("/en/partner", "Become a partner"),
        "cta_button": "Become a partner",
        "stand": "Last updated: October 2026",
        "toc": "Contents",
        "nf_title": "Page not found · Mulligan",
        "nf_h1": "This page doesn't exist.",
        "nf_p": "Maybe a typo. Head back to the home page.",
    },
}

# Seitenpaare für Sprachumschalter und hreflang
PAIRS = {
    "home": ("/", "/en"),
    "impressum": ("/impressum", "/en/imprint"),
    "datenschutz": ("/datenschutz", "/en/privacy"),
    "agb": ("/agb", "/en/terms"),
    "partner": ("/partner", "/en/partner"),
}

PARTNER_SUBJECT = {"de": "Partneranfrage%20Mulligan", "en": "Partner%20request%20Mulligan"}

P = {
    "de": {
        "title": "Partner werden · Mulligan",
        "desc": "Partner von Mulligan werden: Events in der App erstellen, den eigenen Club sichtbar machen und Produkte bei jungen Golferinnen und Golfern in Düsseldorf zeigen.",
        "kicker": "Partner werden",
        "h1": "Zeigt euch dort, wo <em>Flights entstehen.</em>",
        "lead": "Mulligan bringt Golferinnen und Golfer in Düsseldorf und Umgebung zusammen, die öfter spielen wollen und gegen Leute auf ihrem Niveau antreten. Als Partner macht ihr mit uns Events, zeigt euren Club oder stellt euer Produkt dort vor, wo die nächste Runde geplant wird.",
        "button": "Partneranfrage senden",
        "alt_mail": "Oder direkt an",
        "demo_label": "Beispiele, wie Partner in der App erscheinen",
        "caption": "Beispielansicht",
        "event": {"kicker": "Event", "title": "Rangeabend", "when": "Freitag · 19:00", "where": "Driving Range, Düsseldorf", "desc": "Bälle und Bier inklusive. Bring jemanden mit.", "going": "+28 Zusagen", "sponsor": "Gesponsert von eurer Marke", "button": "Zusagen"},
        "club": {"name": "Euer Club", "new": "Neu", "news": "Schnupperabend für Neue am Donnerstag", "matches": "4 offene Matches"},
        "who_kicker": "Für wen",
        "who_h2": "Für alle, die Golf <em>in Düsseldorf machen.</em>",
        "who": [
            ("Golfclubs und Anlagen", "Rangeabende, Schnuppertage und offene Turniere bei euch. Spielerinnen und Spieler sehen in der App eure News und die offenen Matches an eurem Platz."),
            ("Indoor und Simulatoren", "Simulator-Abende, Wintertermine und Turniere unter dem Dach. So bleibt eure Anlage auch in der Saisonpause im Gespräch."),
            ("Trainerinnen und Trainer", "Schnupperstunden und Kurse als Event. Trainerstunden direkt in der App sind in Vorbereitung. Ihr könnt euch dafür schon vormerken lassen."),
            ("Marken und Produkte", "Testtage, Goodies und gesponserte Events. Euer Name steht am Event, gekennzeichnet als Sponsor."),
        ],
        "get_kicker": "Was ihr bekommt",
        "get_h2": "Euer Event in der App. <em>Eure Leute am Platz.</em>",
        "get": [
            ("flag", "Events, die gesehen werden", "Wir legen euer Event in der App an, mit Titel, Ort, Zeit, Plätzen, Beschreibung und Bild. Es steht in der Eventliste, erscheint als Karte im Feed und am Tag selbst in der Match-Suche. Zusagen geht mit einem Tipp. Zum Start ist das Zusagen kostenlos, Tickets über die App folgen."),
            ("people", "Sichtbarkeit für euren Club", "Partnerclubs bekommen in der App eine eigene Beschreibung, Bilder und News. Wer euren Club als Favorit markiert, sieht eure neueste News direkt auf der Startseite."),
            ("trophy", "Klar gekennzeichnet, ohne Datenhandel", "Gesponserte Events tragen den Hinweis \"Gesponsert von\" mit eurem Namen. Personenbezogene Daten der Nutzer geben wir nicht an Partner weiter. Nach dem Event bekommt ihr anonyme Zahlen, zum Beispiel wie viele zugesagt haben."),
        ],
        "how_kicker": "So läuft es ab",
        "how_h2": "In drei Schritten <em>in der App.</em>",
        "how": [
            ("01", "Anfrage", "Schreibt uns", "Kurz, wer ihr seid und was ihr vorhabt: Event, Clubprofil oder Produkt."),
            ("02", "Gespräch", "Wir planen gemeinsam", "Wir klären Idee, Termin, Rahmen und Konditionen."),
            ("03", "Live", "Ab in die App", "Wir legen Event oder Clubprofil an und stimmen alles vorher mit euch ab."),
        ],
        "end_kicker": "Partner werden",
        "end_h2": "Wir starten in <em>Düsseldorf.</em>",
        "end_p": "Die ersten Partner prägen, wie Mulligan in Düsseldorf und Umgebung startet. Schreibt uns, wir melden uns persönlich.",
    },
    "en": {
        "title": "Become a partner · Mulligan",
        "desc": "Become a Mulligan partner: create events in the app, make your club visible and show your products to young golfers in Düsseldorf.",
        "kicker": "Become a partner",
        "h1": "Show up where <em>flights come together.</em>",
        "lead": "Mulligan brings together golfers in and around Düsseldorf who want to play more and compete against people at their level. As a partner, you host events with us, show off your club or present your product where the next round gets planned.",
        "button": "Send a partner request",
        "alt_mail": "Or write directly to",
        "demo_label": "Examples of how partners appear in the app",
        "caption": "Sample view",
        "event": {"kicker": "Event", "title": "Range night", "when": "Friday · 19:00", "where": "Driving range, Düsseldorf", "desc": "Balls and beer included. Bring someone along.", "going": "+28 going", "sponsor": "Sponsored by your brand", "button": "Join"},
        "club": {"name": "Your club", "new": "New", "news": "Taster evening for newcomers on Thursday", "matches": "4 open matches"},
        "who_kicker": "Who it's for",
        "who_h2": "For everyone who makes golf <em>happen in Düsseldorf.</em>",
        "who": [
            ("Golf clubs and courses", "Range nights, taster days and open tournaments at your place. Players see your news and the open matches at your course in the app."),
            ("Indoor and simulators", "Simulator nights, winter dates and indoor tournaments. That keeps your facility on people's minds in the off-season too."),
            ("Coaches", "Taster lessons and courses as events. Booking lessons directly in the app is in the works. You can already sign up for it."),
            ("Brands and products", "Test days, goodies and sponsored events. Your name is on the event, labelled as sponsor."),
        ],
        "get_kicker": "What you get",
        "get_h2": "Your event in the app. <em>Your people on the course.</em>",
        "get": [
            ("flag", "Events people see", "We create your event in the app with title, place, time, spots, description and image. It appears in the events list, as a card in the feed and on the day itself in the match search. Joining takes one tap. At launch, joining is free, tickets in the app will follow."),
            ("people", "Visibility for your club", "Partner clubs get their own description, images and news in the app. Anyone who marks your club as a favourite sees your latest news right on the home screen."),
            ("trophy", "Clearly labelled, no data trading", "Sponsored events carry the note \"Sponsored by\" with your name. We do not pass on users' personal data to partners. After the event you get anonymous numbers, for example how many people joined."),
        ],
        "how_kicker": "How it works",
        "how_h2": "Three steps <em>into the app.</em>",
        "how": [
            ("01", "Request", "Write to us", "Tell us briefly who you are and what you have in mind: an event, a club profile or a product."),
            ("02", "Talk", "We plan together", "We sort out the idea, date, setup and terms."),
            ("03", "Live", "Into the app", "We create the event or club profile and agree everything with you beforehand."),
        ],
        "end_kicker": "Become a partner",
        "end_h2": "We're starting in <em>Düsseldorf.</em>",
        "end_p": "The first partners shape how Mulligan launches in and around Düsseldorf. Write to us and we'll get back to you personally.",
    },
}


def head(t, title, desc, path, key, noindex=False):
    de, en = PAIRS.get(key, ("/", "/en"))
    canonical = DOMAIN + (path if path != "/" else "/")
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">{robots}
<meta name="theme-color" content="#0B1C11">
<meta name="color-scheme" content="dark">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="de" href="{DOMAIN}{de}">
<link rel="alternate" hreflang="en" href="{DOMAIN}{en}">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}{de}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/InstrumentSerif-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/Archivo-Medium.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mulligan">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
</head>
"""


def header(t, key):
    de, en = PAIRS.get(key, ("/", "/en"))
    other = en if t["lang"] == "de" else de
    return f"""<body>
<a class="skip" href="#inhalt">{t['skip']}</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{t['home']}" aria-label="{t['logo_alt']}"><img src="/assets/img/logo.svg" alt="Mulligan" width="525" height="190"></a>
    <nav class="head-nav" aria-label="Navigation">
      <a class="nav-link" href="{t['nav_partner'][0]}"{' aria-current="page"' if key == 'partner' else ''}>{t['nav_partner'][1]}</a>
      <a class="lang" href="{other}" hreflang="{'en' if t['lang'] == 'de' else 'de'}" lang="{'en' if t['lang'] == 'de' else 'de'}" aria-label="{t['switch_aria']}">{t['switch_label']}</a>
    </nav>
  </div>
</header>
"""


def footer(t, current=None):
    links = []
    ph, pl = t["nav_partner"]
    links.append(f'<li><a href="{ph}"{' aria-current="page"' if current == 'partner' else ''}>{pl}</a></li>')
    for k in ("impressum", "datenschutz", "agb"):
        href, label = t["legal"][k]
        cur = ' aria-current="page"' if current == k else ""
        links.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    oh, ol = t["foot_other"]
    links.append(f'<li><a href="{oh}" lang="{"en" if t["lang"] == "de" else "de"}">{ol}</a></li>')
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-brand"><img src="/assets/img/zeichen.svg" alt="" width="209" height="132"><span>{t['foot_brand']}</span></div>
    <ul class="foot-links">{''.join(links)}</ul>
    <p class="copy">© {YEAR} {OWNER}</p>
  </div>
</footer>
</body>
</html>
"""


def home(t):
    m = t["match"]
    r = t["rating"]
    steps = "\n".join(
        f'<li class="step"><div class="step-num"><span>{n}</span>{k}</div><h3>{h}</h3><p>{p}</p></li>'
        for n, k, h, p in t["steps"]
    )
    why = "\n".join(
        f'<li>{ICONS[i]}<div><h3>{h}</h3><p>{p}</p></div></li>' for i, h, p in t["why"]
    )
    chat = []
    for kind, name, text in t["chat"]:
        if kind == "other":
            chat.append(f'<div class="bubble other"><b>{name}</b>{text}</div>')
        elif kind == "me":
            chat.append(f'<div class="bubble me">{text}</div>')
        else:
            chat.append(f'<div class="sys">{text}</div>')
    body = f"""<main id="inhalt">
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <p class="kicker">{t['kicker']}</p>
      <h1>{t['h1']}</h1>
      <p class="lead">{t['lead']}</p>
      <div class="get">
        <div class="qr"><img src="/assets/img/qr-app.svg" alt="{t['qr_alt']}" width="132" height="132"></div>
        <div class="get-text"><strong>{t['get_title']}</strong><p>{t['get_text']}</p></div>
        <span class="pill">{t['pill']}</span>
        <p class="get-note">{t['get_note']}</p>
      </div>
    </div>
    <figure class="device">
      <div class="phone"><img src="{t['screen']}" alt="{t['screen_alt']}" width="640" height="1391" fetchpriority="high"></div>
      <figcaption>{t['caption']}</figcaption>
    </figure>
  </div>
</section>

<section class="section why" id="warum" aria-labelledby="why-h">
  <div class="wrap">
    <div>
      <p class="kicker">{t['why_kicker']}</p>
      <h2 id="why-h">{t['why_h2']}</h2>
      <ul class="why-list">
{why}
      </ul>
    </div>
    <div class="stack" role="group" aria-label="{t['demo_label']}">
      <div class="match" role="img" aria-label="{m['aria']}">
        <div class="match-time"><strong>{m['time']}</strong><span>{m['date']}</span></div>
        <div class="match-rule"></div>
        <div>
          <div class="match-place">{m['place']}</div>
          <div class="match-mode">{m['mode']}</div>
          <div class="slots"><span class="slot a">JK</span><span class="slot b">AN</span><span class="slot free"></span><span class="slot free"></span></div>
        </div>
        <div class="match-side"><span>{m['avg']}</span><span>{m['rank']}</span><span class="free-count">{m['free']}</span></div>
      </div>
      <div class="chat" aria-label="{t['chat_aria']}">
        {''.join(chat)}
      </div>
      <div class="rating">
        <div class="rating-label"><img src="/assets/img/zeichen-khaki.svg" alt="" width="209" height="132">{r['label']}</div>
        <div class="rating-row"><div><span class="rating-num">{r['num']}</span><span class="badge">{r['delta']}</span></div><span class="rating-rank">{r['rank']}</span></div>
        <div class="bar"><span></span></div>
        <p class="rating-note">{r['note']}</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="app" aria-labelledby="app-h">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">{t['app_kicker']}</p>
      <h2 id="app-h">{t['app_h2']}</h2>
      <p>{t['app_p']}</p>
    </div>
    <ol class="steps">
{steps}
    </ol>
    <p class="soon">{t['soon']}</p>
  </div>
</section>

<section class="section cta" id="kontakt" aria-labelledby="cta-h">
  <div class="wrap">
    <div>
      <p class="kicker">{t['cta_kicker']}</p>
      <h2 id="cta-h">{t['cta_h2']}</h2>
      <p>{t['cta_p']}</p>
    </div>
    <a class="mail" href="{t['nav_partner'][0]}">{t['cta_button']}</a>
  </div>
</section>
</main>
"""
    return head(t, t["title"], t["desc"], t["home"], "home") + header(t, "home") + body + footer(t)


def legal_page(t, key, h1, frag_file, path, title_suffix, toc=True):
    src = os.path.join(LEGAL_DIR, frag_file)
    if not os.path.exists(src):
        print("fehlt:", src)
        return None
    frag = open(src, encoding="utf-8").read().strip()
    # Sicherheitsnetz: keine Platzhalter durchlassen
    left = re.findall(r"\{\{[A-Z_]+\}\}|\[[^\]]*(einfügen|insert|Platzhalter|TODO)[^\]]*\]", frag, re.I)
    if left:
        raise SystemExit(f"Platzhalter in {frag_file}: {left}")
    toc_html = ""
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', frag, re.S)
    if toc and len(heads) >= 4:
        items = "".join(f'<li><a href="#{i}">{re.sub("<[^>]+>", "", txt).strip()}</a></li>' for i, txt in heads)
        toc_html = f'<nav class="toc" aria-label="{t["toc"]}"><p>{t["toc"]}</p><ul>{items}</ul></nav>'
    desc = f"{h1} der Mulligan App und der Website mulligan-playgolf.com." if t["lang"] == "de" else f"{h1} for the Mulligan app and the website mulligan-playgolf.com."
    body = f"""<main id="inhalt" class="legal">
  <div class="wrap">
    <a class="back" href="{t['home']}">← {t['back']}</a>
    <h1>{h1}</h1>
    <p class="stand">{t['stand']}</p>
    {toc_html}
    <div class="prose">
{frag}
    </div>
  </div>
</main>
"""
    return head(t, f"{h1} · Mulligan", desc, path, key) + header(t, key) + body + footer(t, current=key)


def partner(t, lang):
    q = P[lang]
    e = q["event"]
    c = q["club"]
    mailto = f"mailto:{MAIL}?subject={PARTNER_SUBJECT[lang]}"
    who = "\n".join(f'<li class="step"><h3>{h}</h3><p>{p}</p></li>' for h, p in q["who"])
    get = "\n".join(f'<li>{ICONS[i]}<div><h3>{h}</h3><p>{p}</p></div></li>' for i, h, p in q["get"])
    how = "\n".join(f'<li class="step"><div class="step-num"><span>{n}</span>{k}</div><h3>{h}</h3><p>{p}</p></li>' for n, k, h, p in q["how"])
    body = f"""<main id="inhalt">
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <p class="kicker">{q['kicker']}</p>
      <h1>{q['h1']}</h1>
      <p class="lead">{q['lead']}</p>
      <div class="ask">
        <a class="mail" href="{mailto}">{q['button']}</a>
        <p class="mail-alt">{q['alt_mail']} <span class="addr">{MAIL}</span></p>
      </div>
    </div>
    <figure class="stack partner-demo" aria-label="{q['demo_label']}">
      <div class="event-card">
        <div class="event-top"><span class="event-kicker">{e['kicker']}</span><span class="event-sponsor">{e['sponsor']}</span></div>
        <div class="event-title">{e['title']}</div>
        <div class="event-when">{e['when']}</div>
        <div class="event-where">{e['where']}</div>
        <p class="event-desc">{e['desc']}</p>
        <div class="event-foot"><div class="slots"><span class="slot a">JK</span><span class="slot b">AN</span><span class="slot c">MS</span></div><span class="event-going">{e['going']}</span><span class="event-btn">{e['button']}</span></div>
      </div>
      <div class="club-card">
        <div class="club-art" aria-hidden="true"></div>
        <div class="club-body">
          <div class="club-name">{c['name']}</div>
          <div class="club-new">{c['new']}</div>
          <p class="club-news">{c['news']}</p>
          <p class="club-matches">{c['matches']}</p>
        </div>
      </div>
      <figcaption>{q['caption']}</figcaption>
    </figure>
  </div>
</section>

<section class="section" id="fuer-wen" aria-labelledby="who-h">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">{q['who_kicker']}</p>
      <h2 id="who-h">{q['who_h2']}</h2>
    </div>
    <ul class="steps cards">
{who}
    </ul>
  </div>
</section>

<section class="section why" id="leistungen" aria-labelledby="get-h">
  <div class="wrap">
    <div>
      <p class="kicker">{q['get_kicker']}</p>
      <h2 id="get-h">{q['get_h2']}</h2>
    </div>
    <ul class="why-list">
{get}
    </ul>
  </div>
</section>

<section class="section" id="ablauf" aria-labelledby="how-h">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">{q['how_kicker']}</p>
      <h2 id="how-h">{q['how_h2']}</h2>
    </div>
    <ol class="steps three">
{how}
    </ol>
  </div>
</section>

<section class="section cta" id="kontakt" aria-labelledby="end-h">
  <div class="wrap">
    <div>
      <p class="kicker">{q['end_kicker']}</p>
      <h2 id="end-h">{q['end_h2']}</h2>
      <p>{q['end_p']}</p>
    </div>
    <div class="ask">
      <a class="mail" href="{mailto}">{q['button']}</a>
      <p class="mail-alt">{q['alt_mail']} <span class="addr">{MAIL}</span></p>
    </div>
  </div>
</section>
</main>
"""
    path = "/partner" if lang == "de" else "/en/partner"
    return head(t, q["title"], q["desc"], path, "partner") + header(t, "partner") + body + footer(t, current="partner")


def notfound(t):
    body = f"""<main id="inhalt" class="notfound">
  <div class="wrap">
    <p class="kicker">404</p>
    <h1>{t['nf_h1']}</h1>
    <p>{t['nf_p']}</p>
    <a class="mail" href="{t['home']}">{t['back']}</a>
  </div>
</main>
"""
    return head(t, t["nf_title"], t["nf_p"], "/404", "home", noindex=True) + header(t, "home") + body + footer(t)


def write(rel, content):
    if content is None:
        return
    p = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print("geschrieben:", rel)


de, en = T["de"], T["en"]
write("index.html", home(de))
write("en/index.html", home(en))
write("impressum.html", legal_page(de, "impressum", "Impressum", "impressum.html", "/impressum", "", toc=False))
write("datenschutz.html", legal_page(de, "datenschutz", "Datenschutzerklärung", "datenschutz.html", "/datenschutz", ""))
write("agb.html", legal_page(de, "agb", "Allgemeine Geschäftsbedingungen", "agb.html", "/agb", ""))
write("en/imprint.html", legal_page(en, "impressum", "Imprint", "impressum.html", "/en/imprint", "", toc=False))
write("en/privacy.html", legal_page(en, "datenschutz", "Privacy Policy", "privacy-en.html", "/en/privacy", ""))
write("en/terms.html", legal_page(en, "agb", "Terms of Use", "terms-en.html", "/en/terms", ""))
write("partner.html", partner(de, "de"))
write("en/partner.html", partner(en, "en"))
write("404.html", notfound(de))
