# Website mulligan-playgolf.com

Statische Coming-Soon-Seite für Mulligan. Wissen zu Inhalt, Texten, QR-Codes und offenen Punkten steht in `HANDOVER.md`. Kein Framework, kein Build-Schritt, kein JavaScript, keine Cookies, kein Tracking, Schriften selbst gehostet. Gehostet bei Vercel, Domain und Postfach bei STRATO.

## Was wo liegt
| Pfad | Inhalt | URL |
|---|---|---|
| `index.html`, `en/index.html` | Startseite Deutsch und Englisch | `/`, `/en` |
| `partner.html`, `en/partner.html` | Partnerseite für Clubs, Anlagen, Trainer und Marken | `/partner`, `/en/partner` |
| `impressum.html`, `datenschutz.html`, `agb.html` | Rechtstexte Deutsch (verbindlich) | `/impressum`, `/datenschutz`, `/agb` |
| `en/imprint.html`, `en/privacy.html`, `en/terms.html` | Rechtstexte Englisch | `/en/imprint`, `/en/privacy`, `/en/terms` |
| `assets/` | CSS, Schriften (SIL OFL), Logos, Screenshots, QR-Code | |
| `vercel.json` | saubere URLs, Weiterleitungen, Sicherheits-Header | |
| `_quellen/` | Erzeugungsskript und Rechtstexte als Fragmente. Wird nicht veröffentlicht (`.vercelignore`) | |

## Der QR-Code
`assets/img/qr-app.svg` zeigt auf `https://mulligan-playgolf.com/app`. Diese Adresse leitet per `vercel.json` weiter, im Moment auf die Startseite. Zum Launch nur das Ziel tauschen, der Code bleibt gleich und funktioniert auch auf Flyern und Merch:

```json
{ "source": "/app", "destination": "https://apps.apple.com/de/app/<eure-app-id>", "permanent": false }
```

Zum Launch außerdem in `_quellen/build.py` die Texte "Bald im App Store" anpassen und in den `<head>` beider Startseiten das Smart App Banner setzen: `<meta name="apple-itunes-app" content="app-id=<eure-app-id>">`.

## Erstmals veröffentlichen (einmalig, etwa 15 Minuten)

### 1. Vercel-Projekt aus GitHub anlegen
1. Auf vercel.com mit GitHub anmelden ("Continue with GitHub").
2. "Add New..." > "Project" > bei "Import Git Repository" GitHub verbinden und der Vercel-App Zugriff auf `LoBecker/Mulligan-Play-Golf-Website` geben ("Only select repositories").
3. `Mulligan-Play-Golf-Website` > "Import". Einstellungen:
   - Project Name: `mulligan-website`
   - Framework Preset: `Other`
   - Root Directory: leer lassen (das Repo enthält nur die Website)
   - Build Command und Output Directory leer lassen
4. "Deploy". Danach steht die Seite unter einer `*.vercel.app`-Adresse.

Ab dann veröffentlicht jeder Push auf `main` die Seite automatisch. Pull Requests bekommen eine Vorschau-Adresse.

Wichtig zum Tarif: Vercels kostenloser Hobby-Tarif ist laut Fair-Use-Regeln nur für nicht kommerzielle, private Nutzung. Eine Seite für ein Startup fällt nach Vercels Definition darunter, sobald jemand damit Geld verdienen will. Sauber ist der Pro-Tarif (20 US-Dollar im Monat). Kostenlose Alternativen mit erlaubter gewerblicher Nutzung sind Cloudflare Pages oder Netlify. Die Seite läuft dort unverändert, nur der Abschnitt "Hosting" in der Datenschutzerklärung muss dann angepasst werden.

### 2. Domain in Vercel verbinden
Vercel > Projekt `mulligan-website` > Settings > Domains:
- `mulligan-playgolf.com` hinzufügen
- `www.mulligan-playgolf.com` hinzufügen und auf `mulligan-playgolf.com` weiterleiten lassen (Vercel bietet das beim Hinzufügen an)

Vercel zeigt danach die Werte, die bei STRATO eingetragen werden müssen: eine IP-Adresse für den A-Record (meist `76.76.21.21`, bei neueren Projekten z. B. `216.198.79.1`) und ein Ziel für den CNAME von www. Immer die Werte aus Vercel nehmen.

### 3. DNS bei STRATO umstellen
STRATO Kunden-Login > Domains > Domainverwaltung:
1. Bei `mulligan-playgolf.com` aufs Zahnrad > Reiter DNS > **A-Record verwalten** > "Eigene IP-Adresse" > IP aus Vercel > Einstellungen übernehmen.
2. **AAAA-Record**: Falls dort eine IPv6-Adresse von STRATO hinterlegt ist, entfernen bzw. deaktivieren. Vercel unterstützt für eigene Domains über fremdes DNS kein IPv6.
3. Subdomain `www` anlegen, falls es sie noch nicht gibt. Dann bei `www` > DNS-Verwaltung > **CNAME-Record verwalten** > Ziel aus Vercel > speichern.
4. **MX-Records nicht anfassen.** Die Postfächer bleiben bei STRATO.

Es kann bis zu 24 Stunden dauern, meist geht es in unter einer Stunde. Das SSL-Zertifikat stellt Vercel automatisch aus.

### 4. Postfach anlegen
Im Impressum und in den Rechtstexten steht `contact@mulligan-playgolf.com`. Dieses Postfach muss existieren und regelmäßig gelesen werden (Impressum, Datenschutzanfragen, DSA-Kontaktstelle, Meldungen aus der App). STRATO > E-Mail > Postfach anlegen.

### 5. Prüfen
- `https://mulligan-playgolf.com`, `/en`, `/impressum`, `/datenschutz`, `/agb` laden
- `https://www.mulligan-playgolf.com` leitet auf die Hauptdomain
- `https://mulligan-playgolf.com/app` leitet auf die Startseite
- QR-Code mit dem iPhone scannen

## Später ändern
- Inhalte der Startseite und Rechtstexte stehen in `_quellen/`. Nach einer Änderung: `python3 _quellen/build.py` im Repo-Ordner ausführen, committen und pushen. Vercel veröffentlicht automatisch.
- Rechtstexte müssen angepasst werden, sobald sich etwas an der Datenverarbeitung ändert: bezahlte Events oder Trainerpakete (Stripe), neuer E-Mail-Dienst, Analyse- oder Absturz-SDKs, anderer Hoster, Wechsel von der GbR zur UG.

## Für App Store Connect
- Datenschutzrichtlinie-URL: `https://mulligan-playgolf.com/datenschutz`
- Support-URL: `https://mulligan-playgolf.com` (Kontakt steht auf der Seite)
- Marketing-URL: `https://mulligan-playgolf.com`
