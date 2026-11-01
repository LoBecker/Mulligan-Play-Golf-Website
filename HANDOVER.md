# Handover: Website mulligan-playgolf.com

Alles, was man braucht, um an der Website weiterzuarbeiten, ohne das App-Repo lesen zu müssen. Technische Einrichtung (Vercel, DNS, Postfach) steht in `README.md`.

Stand: 1.11.2026

## Worum es geht
- Coming-Soon-Seite für die iOS App **Mulligan: Play Golf** (Name im App Store, auf dem Homescreen "Mulligan").
- Positionierung: Golf-App für **Matchmaking, Netzwerk und Statistik**, deutschlandweit mit allen Golfclubs aus OpenStreetMap, später weitere Länder. Kostenlos für Spieler.
- Nicht mehr verwenden: "Social Golf Club", "Düsseldorf" als Standort der App, "Inner Circle". Düsseldorf bleibt nur als Sitz der GbR in den Rechtstexten.
- Betreiber: Becker & Groß GbR (Louis Becker, David Roman Groß), Talstraße 40, 40217 Düsseldorf. Kontakt `contact@mulligan-playgolf.com`.

## Zwei Repos
| Repo | Inhalt |
|---|---|
| `LoBecker/Mulligan-Play-Golf-Website` (dieses) | Website, Rechtstexte für Web und App Store, QR-Codes |
| `LoBecker/mulligan-ios` | iOS App, Supabase, Produktdoku (`docs/`), To-do-Liste (`docs/10-todo.md`) |

Die Website lag bis zum 1.11.2026 zusätzlich als Ordner `website/` im App-Repo. Der Ordner ist dort entfernt, gepflegt wird nur noch hier.

## Seiten ändern
1. Texte stehen in `_quellen/build.py`: Startseite im Block `T` (`de` und `en`), Partnerseite im Block `P`. Rechtstexte als HTML-Fragmente in `_quellen/rechtstexte/`.
2. Im Repo-Ordner `python3 _quellen/build.py` ausführen. Das erzeugt alle `.html`-Dateien neu. Die `.html`-Dateien nie von Hand ändern.
3. Committen und auf `main` pushen. Vercel veröffentlicht automatisch, Pull Requests bekommen eine Vorschau-Adresse.

Das Skript läuft mit dem Python des Mac (ab 3.9), ohne Zusatzpakete.

## Textregeln
Gleiche Regeln wie in der App:
- Informieren, nicht verkaufen.
- Kein Superlativ, kein Ausrufezeichen, keine Emojis, keine Gedankenstriche.
- Du-Form, kurze Sätze.
- Englisch locker und direkt.

Fester Claim: "Finde Mitspieler. Buche deinen Flight. Spiel öfter Golf." / "Find players. Book your flight. Play more golf."

## Was auf der Seite steht
- **Titel und Vorschau beim Teilen** (WhatsApp, iMessage): "Mulligan · Golf-App für Matches, Netzwerk und Statistik", englisch "Mulligan · The golf app for matches, people and stats". Kommt aus `title` und `desc` in `T`. Das Vorschaubild ist `og-image.jpg`.
- **Startseite:**
  - So funktioniert's: Finden, Spielen mit Karte je Loch, Aufsteigen, Vernetzen.
  - Warum Mulligan: Jede Runde zählt, Wettkampf ohne Startgeld, neue Leute, Statistik und Bestenlisten.
  - Mitmachen: Partner werden, Instagram.
- **Partnerseite:** für Golfclubs, Indoor-Anlagen, Trainer und Marken. Zusagen und Tickets für Events stehen als "folgen", weil sie in der ersten App-Version ausgeblendet sind.
- **Fußzeile auf allen Seiten:** "Mulligan · Play Golf", Partner, Impressum, Datenschutz, AGB, Instagram, Sprachwechsel.

## QR-Codes und Links
| Was | Datei | Ziel |
|---|---|---|
| App | `assets/img/qr-app.svg` | `https://mulligan-playgolf.com/app`. Leitet per `vercel.json` weiter, bis zum Launch auf die Startseite. Zum Launch nur das Ziel in `vercel.json` auf den App-Store-Link ändern, der Code bleibt gleich. |
| Instagram | `assets/img/qr-instagram.png` (400 px fürs Web) | `https://www.instagram.com/mulligan_playgolf/`, erzeugt in der Instagram-App. Original in voller Größe für Druck und Flyer: `_quellen/social/instagram-qr-mulligan_playgolf.png` |

Auf dem Handy blendet die Seite die QR-Codes aus und zeigt nur Links.

## Rechtstexte
- **Inhalt:** Impressum, Datenschutz und AGB auf Deutsch (verbindlich) und Englisch. Sie gelten auch für die App. App Store Connect verlinkt `/datenschutz`.
- **Übereinstimmung mit der App:** Die Datenschutzerklärung beschreibt, was die App tatsächlich tut. Ändert sich die Datenverarbeitung der App, muss sie hier angepasst werden. Das gilt etwa für einen neuen E-Mail-Dienst (geplant ist Resend für Anmeldecodes), Stripe, Analyse- oder Absturz-SDKs, einen anderen Hoster oder den Wechsel zur UG.
- **Stand 1.11.2026 zum Standort:** Ohne Freigabe sortiert die App ab dem Heimatplatz oder einem selbst gewählten Ort, sonst nach Name.
- **Stand 1.11.2026 zum Feed:** Nach jeder Runde fragt die App, ob die Runde in den Feed soll.

## Offen
- [ ] Zum Launch: Ziel von `/app` in `vercel.json` auf den App-Store-Link stellen, "Bald im App Store" in `_quellen/build.py` ändern und das Smart App Banner in beide Startseiten setzen (siehe `README.md`).
- [ ] Vercel-Tarif klären: Hobby ist nur für nicht kommerzielle Nutzung, sauber wäre Pro (siehe `README.md`).
- [ ] Zugang zu Vercel für David. Im Hobby-Tarif nicht möglich, im Pro-Tarif über ein Team.
- [ ] Datenschutzerklärung ergänzen, sobald das eigene SMTP (Resend) für Anmeldecodes läuft.
- [ ] Geplante Wortmarke: In `docs/recht/checkliste-gbr.md` im App-Repo steht "Mulligan: Play Golf". Die Markenrecherche steht noch aus.

## Verlauf
- 24.10.2026: Seite angelegt, Rechtstexte auf die Becker & Groß GbR umgestellt, Kontakt `contact@mulligan-playgolf.com` (Louis).
- 1.11.2026: Texte auf die neue Positionierung umgestellt, Datenschutz zu Standort und Feed nachgezogen, Instagram mit QR-Code und Fußzeilen-Link ergänzt, `build.py` lauffähig mit Python 3.9 (David, aus PR #9 im App-Repo übernommen).
