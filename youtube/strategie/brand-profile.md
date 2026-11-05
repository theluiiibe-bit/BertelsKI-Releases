# Brand Profile – BertelsKI / „Meine KI“ auf YouTube

> **Vorläufig.** Abgeleitet aus dem öffentlichen Release-Repo (README, docs/) und der Nische
> „lokale KI auf Windows“. Alles mit ⚠️ ist eine Annahme, die du bestätigen oder korrigieren
> solltest. Jeder andere Baustein (Skripte, Thumbnails, Kalender) liest diese Datei zuerst.

## Identität (ein Satz)

BertelsKI baut **„Meine KI“**, einen KI-Assistenten als Windows-Desktop-App, der signiert
ausgeliefert wird und dem Nutzer die Kontrolle lässt – ⚠️ lokal/offline-fähig, datensparsam,
auf Deutsch.

## Positionierung und Haltung

- **Kategorie:** KI-Assistent für den eigenen Windows-PC (nicht Browser-Chatbot, nicht Cloud-Abo).
- **Das eine Anders:** ⚠️ Kontrolle beim Nutzer – eigene Daten bleiben auf dem Rechner, Updates
  werden kryptografisch signiert (Ed25519) und nur nach ausdrücklicher Zustimmung installiert.
- **Haltungen, für die der Kanal steht (Hügel, auf denen wir sterben):**
  1. „KI, die du nicht kontrollierst, kontrolliert dich.“ – Datenhoheit ist kein Nerd-Thema.
  2. „Sicherheit ist ein Feature, das man sehen kann.“ – Signaturen, Prüfsummen, Zustimmung
     werden gezeigt, nicht versteckt.
  3. „Ehrlich über Grenzen.“ – Wo Cloud-Modelle besser sind, sagen wir es.
- **Haltung, die wir ablehnen:** KI-Hype ohne Beleg, „10 geheime Prompts“-Clickbait, Angstmache.

## Zielgruppen auf YouTube

1. **Primär – der datenbewusste Windows-Nutzer (30–55):** ⚠️ Selbstständige, kleine Betriebe,
   Lehrkräfte, Verwaltungsnahe, technikaffine Privatpersonen in DACH. Will KI nutzen, aber ohne
   Kundendaten, Verträge oder private Dokumente in US-Clouds zu laden. Sucht nach „KI offline“,
   „ChatGPT Alternative Datenschutz“, „KI lokal Windows“.
2. **Sekundär – der Bastler (18–40):** ⚠️ kennt Ollama/LM Studio, vergleicht Modelle, schaut
   Benchmarks und Setups, teilt Videos in r/LocalLLaMA und Discord.

Nicht Zielgruppe: Enterprise-IT mit Beschaffungsprozess (zu lang), Kinder (madeForKids = false).

## Stimme

| Dimension | Position |
|---|---|
| Förmlich ↔ locker | locker-sachlich, „du“ |
| Nüchtern ↔ begeistert | ruhig überzeugt; Begeisterung nur bei echten Belegen |
| Lehrer ↔ Kumpel | erfahrener Kollege, der dir am Schreibtisch etwas zeigt |
| Ernst ↔ witzig | trockener Humor erlaubt, kein Clown |

**Lexikon (benutzen):** „auf deinem Rechner“, „bleibt bei dir“, „zeig ich dir in zwei Minuten“,
„ehrlich gesagt“, „signiert“, „Prüfsumme“, „ohne Cloud“, „Schritt für Schritt“.
**Verboten:** „revolutionär“, „bahnbrechend“, „Game-Changer“, „du MUSST“, „Geheimnis“,
„niemand sagt dir“, „KI ersetzt …“, Ausrufezeichen-Ketten, unbelegte Prozentzahlen.

**Signatur-Elemente:** Bildschirmaufnahme mit sichtbarem Cursor; ein Satz „Was du gleich siehst,
läuft komplett lokal“ als Running Gag/Trust-Marker; am Ende immer „Was bleibt bei dir, was nicht“.

## Belege und Angebote

- **Belege (real, prüfbar):** signierte Installer über GitHub Pages; SHA-256 + Ed25519-Signatur
  im Manifest; Updater verifiziert gegen separaten Public Key; Nutzer stimmt vor Installation zu.
  ⚠️ Weitere Belege (Nutzerzahlen, Benchmarks) erst, wenn messbar – nichts erfinden.
- **Angebote / CTAs:** Download-Seite `https://theluiiibe-bit.github.io/BertelsKI-Releases/`;
  ⚠️ Newsletter/Community (noch anzulegen); Abo + Glocke nur einmal am Ende, nie mitten im Video.

## Leitplanken

- Keine Versprechen zu Sicherheit, die wir nicht belegen („100 % sicher“ ist verboten).
- Noch **keine** Windows-Authenticode-Signatur → SmartScreen-Warnung ehrlich zeigen und erklären.
- Keine Vergleiche mit Konkurrenz, die wir nicht selbst getestet haben.
- Keine Gesundheits-, Rechts- oder Finanz-Ratschläge durch die KI im Video als Fakt präsentieren.
- Keine fremden Stimmen/Gesichter klonen. Keine Screenshots mit echten Nutzerdaten.
- Deutsch zuerst; englische Fachwörter nur mit Erklärung beim ersten Vorkommen.

## Betriebs-Defaults

- **KI-Stimme:** erlaubt, **immer offengelegt** (Beschreibung + Upload-Flag „veränderter Inhalt“,
  wenn realistisch). Bevorzugt eigener Klon oder designte Stimme, Lizenz ab Starter-Tarif.
- **KI-Bilder/B-Roll:** erlaubt für abstrakte Illustration, deklariert; nie für „Produkt-Screenshots“.
- **Sprachen:** DE primär; EN-Untertitel optional ab Monat 3.
- **Aussprache:** „BertelsKI“ = „Bertels-Ka-I“; „Ollama“ = „O-lama“; „Ed25519“ = „Ed-zwei-fünf-fünf-eins-neun“.
- **Barrierefreiheit:** immer Untertitel; Kontrast-Check bei Overlays.

## Vorbilder (Zeigen statt Beschreiben)

⚠️ Hier 3–5 Videos eintragen, die du gut findest, und 1–2, die du hasst – mit je einem Satz
warum. Beispiele zum Prüfen: *Digitale Profis* (DE, KI-Tutorials, ruhiger Lehrton), *NetworkChuck*
(EN, Energie + Screen-Demo), *c't 3003* (DE, journalistisch-skeptisch). Hass-Beispiel: alles mit
„KI macht dich REICH“-Thumbnail.
