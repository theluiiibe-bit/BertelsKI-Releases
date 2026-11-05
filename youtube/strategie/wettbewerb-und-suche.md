# Wettbewerb und Suche – was in der Nische wirklich rankt

> Quelle: Live-Scan der YouTube-Suche am 05.11.2026 (`tools/youtube_search_scan.py`, 8 Keywords,
> je „alle Zeiten“ und „letzter Monat“, 277 Videos). Zahlen = öffentlich angezeigte Aufrufe zum
> Abrufzeitpunkt, keine Analytics. Rohdaten: `output/suche-scan-live.md` (nicht committet).
> Methode: Muster und Lücken lesen (SPARK), Mechanismen statt Oberfläche (Viral-Teardown) –
> **nichts umformulieren**.

## 1. Die Kanäle, die die Nische besetzen

| Kanal | Rolle in der Nische | Typische Länge | Beobachtetes Muster |
|---|---|---|---|
| **c't 3003** (263k Abos, `UC1t9VFj-O6YUDPQxaVg-NkQ`) | journalistische Autorität | 20–45 Min. | „Was ich über lokale KI gelernt habe“ (572k), „Lokale KI ist jetzt WIRKLICH brauchbar (und auf dieser Hardware läuft sie)“ (565k) – Ich-Erfahrung + Hardware-Antwort |
| **The Morpheus** (277k, `UCLGY6_j7kZfA1dmmjR1J_7w`) | Tech-Erklärer | 25–30 Min. | „Was ich aus lokaler KI rausgeholt habe“ (245k in 3 Wochen), „Warum gerade alle ChatGPT kündigen“ (300k) |
| **Digitale Profis** (171k, `UCv90NdTyTp7ZPPRvvSZaS5w`) | Tutorial-Kanal, ruhig | 8–14 Min. | Tool-Tutorials: „Offline Chatbot … lokal auf deinem PC installieren“ (73k), „Vier Stufen … mit Hardware-Guide“ (17k) |
| **KI-Wissen mit Harald Frey** | Tool-Tutorials, hohe Frequenz | 8–15 Min. | „Ollama 2026 Komplett-Guide (In 5 Min fertig)“ (30k), „LM Studio Bionic … 100 % offline“ (26k) |
| **Daniel Klozbücher** | Meinung + Unternehmen | 12–31 Min. | „Lokale KI statt ChatGPT im Unternehmen“ (41k), „Der Denkfehler bei lokaler KI“ (36k) |
| **Giorgi Lomidze – Souveräne KI** | Praxis, Listen | 18–52 Min. | „Die 7 besten Anwendungen (kostenlos & offline)“ (8,6k), auch Contrarian: „Warum lokale KI ein Sicherheitsalptraum ist“ |
| **Lokale KI mit Andreas Nürenberg** | Nischen-News + Firmen | 11–17 Min. | „Firmen-ChatGPT mit RAG: Keine Frage verlässt die Firma“, wöchentliche „Lokale KI News“ |
| **AI mit Arnie**, **Marco Franz**, **Hermann Ott**, **Jan-Keno Janssen**, **IchBinFabian** | Hardware-Kauf-Beratung | 10–44 Min. | „Lokale KI: Kauf nicht die falsche Hardware“ (110k), „Warum gerade alle einen eigenen KI-Rechner kaufen“ (20k), „128 GB … alle Wege mit Euro-Preis“ (30k) |

Rang-Muster: Die **großen Zahlen** (200k–570k) kommen von Ich-Erfahrungsberichten etablierter
Journalisten-Kanäle. Die **Mittelklasse** (10k–40k) sind Tool-Tutorials und Hardware-Beratung.
**Neue, kleine Kanäle** mit Setup-Tutorials liegen bei 20–500 Aufrufen – der Markt für
„Ollama installieren“ ist gesättigt.

## 2. Keyword-Befunde

| Keyword | Qualität der Treffer | Befund |
|---|---|---|
| **lokale ki** | sehr hoch, 100 % Nische | das Leit-Keyword. Erscheint in 13 von 20 Titeln. **Muss in jeden unserer Titel.** |
| ki lokal windows | hoch | „Windows“ bringt Copilot-Konkurrenz rein; Median-Länge 13–15 Min. |
| ki offline | mittel (verunreinigt durch Gaming/Musik) | „offline“ als Zusatz, nicht als Haupt-Keyword |
| ki assistent windows | niedrig für uns | dominiert von Microsoft-Copilot-Agenten und „Jarvis“-Bastelprojekten |
| chatgpt alternative datenschutz | mittel, Business-lastig | DSGVO-Winkel wird von Datenschutz-Beratern besetzt; kleine Zahlen (300–2k), außer Morpheus |
| ollama windows deutsch | gesättigt | 19 von 20 Titeln „Ollama“; neue Tutorials bleiben unter 100 Aufrufen |
| lm studio deutsch | gesättigt | gleiches Bild, „Bionic“ als aktueller Hook |
| smartscreen warnung | **Lücke** | nur „deaktivieren“-Tutorials (1–2 Min., alt). Niemand erklärt „prüfen statt abschalten“. |

Wiederkehrende Titel-Bausteine mit Reichweite: *„Was ich … gelernt/rausgeholt habe“* (Ich-Erfahrung),
*„WIRKLICH brauchbar“ / „wirklich“* (Skepsis-Marker), *„ohne Cloud / ohne Abo / kostenlos“*,
*„auf dieser Hardware / Euro-Preis“*, *„statt ChatGPT“*, *„komplett offline“*, *„Denkfehler“*.

Länge: Median in der Nische **12–18 Minuten**, Top-Videos 20–30 Minuten. Das ist länger als die
allgemeine 8–15-Regel; die Zielgruppe hält durch, **wenn** Erfahrung und Hardware-Antworten
geliefert werden. Konsequenz für uns: 10–15 Min. anpeilen, nie strecken.

## 3. Lücken, die wir besetzen können (kein Wettbewerber tut es)

1. **„Fertige Windows-App statt Terminal“ für Nicht-Techniker.** Fast alle Treffer setzen
   Ollama/LM Studio/Docker/n8n voraus. Die Zielgruppe „Selbstständige ohne Terminal“ wird nur von
   Datenschutz-Beratern mit Folien bedient, nicht mit einer Demo. → Säule ⭐1 + 3.
2. **Sicherheit sichtbar machen: Signatur, Prüfsumme, SmartScreen.** Die Suche liefert nur
   „SmartScreen deaktivieren“. Unser Winkel „prüfen statt abschalten“ ist einzigartig. → LF-02, SH-03.
3. **Ehrliche Grenze als Marke.** Contrarian-Titel („Denkfehler“, „Sicherheitsalptraum“) ziehen
   in der Nische. Ein Hersteller, der die eigenen Grenzen zuerst nennt, hat das noch niemand. → SH-02.
4. **Hardware-Frage für Normal-PCs** (nicht 128-GB-Workstations). Alle Hardware-Videos zielen auf
   Käufer teurer Rechner. „Welcher normale Büro-PC reicht für Meine KI?“ fehlt. → Idee #6.
5. **Deutsche Arbeits-Workflows** (Angebot, Protokoll, PDF-Suche) mit lokaler KI – als Demo, nicht als
   Tool-Vergleich. → Säule 3, „Montags-Workflow“.

## 4. Konsequenzen für unsere Pakete

- **LF-01 Titel ändern:** Haupt-Keyword „Lokale KI“ nach vorn, „offline“ als Beleg. Neue Favoriten:
  *„Lokale KI ohne Terminal: 5 Dinge, die Meine KI offline erledigt“* oder
  *„Lokale KI für Nicht-Techniker: 5 Aufgaben komplett ohne Cloud“*.
- **Ich-Erfahrung einbauen:** Die Top-Videos erzählen „was ich gelernt habe“. Unser Build-in-Public
  (Säule 4) ist die eigene Version davon – nicht als Vlog, sondern als „was wir beim Bauen gelernt haben“.
- **Hardware-Antwort in jedes Säule-1-Video** (ein Satz mit konkreter Mindestanforderung), weil die
  Suche zeigt, dass es die dominante Zuschauerfrage ist.
- **Keine weiteren Ollama/LM-Studio-Setup-Videos.** Gesättigt, kleine Kanäle ersticken darin.

## 5. Trend-Kandidaten aus dem Scan (Drei Tore)

| Kandidat | FIT | SAFETY | TIMING | Entscheidung |
|---|---|---|---|---|
| „Jarvis komplett offline“ (42,9k Aufrufe in 23 h; mehrere Jarvis-Titel im Monat) | ja: Säule 1, aber unser Winkel ist „kein Bastelprojekt nötig“ | ja | steigend | **Short (Sa-Slot):** „Du brauchst keinen Jarvis. Du brauchst eine App, die läuft.“ – Flugmodus-Demo |
| „Qwen3.5-9B schlägt Claude Opus 4.5 für 100 Dollar“ (Modell-Benchmarks) | teils: nur, wenn Meine KI das Modell nutzt ⚠️ | ja | steigend | prüfen, sonst skip |
| „Lokale KI ab 12 GB / Hardware-Kauf“ (190k, 110k) | ja: Säule 1, Winkel „normaler PC“ | ja | Peak | Long-Form Idee #6 ziehen |
| „KI-Abo-Kosten vs. lokal“ (c't 3003 05.11. „Lokale KI statt Cloud-Abo“, 02.11. „KI-Abos: erst gewöhnen, dann teuer bezahlen?“ 20k; Morpheus 300k) | ja: Säule 1, unser Winkel „was es wirklich kostet“ mit echten Zahlen | ja | steigend | **Long-Form Idee #16** |
| Windows „K2“-Features November 2026 (41k) | schwach | ja | Peak | skip |
| Google Trends DE (05.11.): Sport, Politik, Serien | nein | – | – | skip |
| HN: „What hardware are you using to run local LLMs?“ (52 Punkte, 46 Kommentare) | ja: Signal für Idee #6, Kommentare als Fragen-Mine | ja | – | in Ideen-Bank als Beleg |

Nächster Scan: wöchentlich, Montag, mit `--week` und den Kanal-IDs oben in `trend_radar.py`.
