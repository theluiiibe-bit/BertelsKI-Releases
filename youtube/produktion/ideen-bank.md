# Ideen-Bank

> Wöchentlich sichten, monatlich ausmisten. Jede Idee braucht ein **echtes** Quell-Signal –
> keine erfundenen Zuschauerfragen. Status: neu / getestet / geplant / geparkt / produziert.
> Aufwand: S (Short) / M (Long-Form Screen-Recording) / L (Long-Form mit Dreh + B-Roll).

| # | Idee (Arbeitstitel) | Quell-Signal | Säule | Format | Aufwand | Nachfrage | Status |
|---|---|---|---|---|---|---|---|
| 1 | Diese 5 Dinge erledigt Meine KI komplett ohne Internet | Nischen-Suche „KI offline Windows“ (Recherche 05.11.2026, hohe Ratgeber-Dichte) | ⭐1 | LF | M | Suchnachfrage | **produziert → LF-01** |
| 2 | Warum Windows unsere App „unbekannt“ nennt – SmartScreen ehrlich erklärt | README: noch keine Authenticode-Signatur; Such-Scan bestätigt Lücke (siehe #19) | 2 | LF | M | erwartbar + Suchlücke | **produziert → LF-02** |
| 3 | Lokal oder Cloud? Wo lokale KI verliert | Ratgeber-Konsens „für komplexe Aufgaben ist Cloud meist besser“ | ⭐1 | Short/LF | S | mittel | geplant (SH-02) |
| 4 | Prüfsumme in 60 Sekunden selbst prüfen | manifest.json enthält SHA-256; Standardfrage sicherheitsbewusster Nutzer | 2 | Short | S | mittel | geplant (SH-03) |
| 5 | Was eine Cloud-KI über dich weiß | Datenschutz-Suchthema | ⭐1 | Short | S | hoch | geplant (SH-01) |
| 6 | Welcher normale Büro-PC reicht für lokale KI? (nicht 128 GB) | Such-Scan 05.11.: „Kauf nicht die falsche Hardware“ 110k, „Lokale KI ab 12 GB“ 190k, „128 GB … Euro-Preis“ 30k; HN „What hardware for local LLMs“ 46 Kommentare | ⭐1 | LF | M | **hoch (belegt)** | neu – Lücke: Normal-PC statt Workstation |
| 7 | Angebot in 3 Minuten aus Stichpunkten (Montags-Workflow #1) | Zielgruppe Selbstständige | 3 | LF | M | ⚠️ zu belegen (Umfrage) | neu |
| 8 | 50 PDFs durchsuchen, ohne sie zu lesen | Standard-Use-Case lokaler Dokumenten-Chats (GPT4All-Vergleich in Recherche) | 3 | LF | M | mittel | neu |
| 9 | Warum Version 0.69 fast nicht rausging (Release-Tagebuch #1) | Commit-Historie zeigt mehrere Release-Anläufe | 4 | LF | L | gering, Community | neu |
| 10 | Auto-Update ohne Hintertür: so prüft der Updater | README Sicherheitsregeln | 2 | LF | M | mittel | neu |
| 11 | Ollama vs. Meine KI – ehrlicher Vergleich für Nicht-Techniker | Such-Scan: 19 von 20 Treffern zu „ollama windows deutsch“ sind Setup-Tutorials, neue bleiben < 100 Aufrufe → kein Setup-Video, sondern Vergleich „Terminal vs. App“ | ⭐1 | LF | M | mittel | neu – erst nach eigenem Test |
| 12 | „Das läuft gerade komplett offline“ – Flugmodus-Demo | Signatur-Trust-Marker aus dem Brand-Profile | ⭐1 | Short | S | – | geplant (SH-04) |
| 13 | Was ihr euch gewünscht habt – und was wir bauen | Community-Post-Rückläufer (noch zu sammeln) | 4 | LF | M | – | geparkt bis Signale |
| 14 | KI-Stimme im Video – warum wir es sagen | eigene Offenlegungspflicht; Meta-Thema | 4 | Short | S | gering | geplant (SH-05) |
| 15 | „Du brauchst keinen Jarvis“ – Trend-Remix | Such-Scan: „JARVIS komplett offline“ 42,9k in 23 h, 4 Jarvis-Titel im Monat; Drei Tore bestanden | ⭐1 | Short | S | Trend | **geplant (SH-06, Sa-Slot)** |
| 16 | Was uns lokale KI im Betrieb wirklich kostet (Abo vs. Strom vs. Hardware) | c't 3003 05.11.: „Lokale KI statt Cloud-Abo“, 02.11.: „KI-Abos: erst gewöhnen, dann teuer“ 20k; Morpheus „Warum alle ChatGPT kündigen“ 300k | ⭐1 | LF | M | hoch (belegt) | neu – Rechnung mit echten Zahlen, keine Schätzung |
| 17 | Firmen-Wissen durchsuchen, ohne dass eine Frage die Firma verlässt | Nürenberg „Firmen-ChatGPT mit RAG“ (2,4k in 1 Tag); Klozbücher „Lokale KI statt ChatGPT im Unternehmen“ 41k | 3 | LF | M | hoch (belegt) | neu – ⚠️ nur, wenn Dokumenten-Suche im Build existiert |
| 18 | „Der Denkfehler bei lokaler KI“ – unsere Antwort | Klozbücher 35k in 2 Wochen; Contrarian zieht in der Nische | ⭐1 | LF/Short | M | mittel | neu – eigene These, nicht Reaktion |
| 19 | SmartScreen: prüfen statt deaktivieren | Such-Scan: „smartscreen warnung“ liefert nur „deaktivieren“-Tutorials (1–2 Min., 3–5 Jahre alt) → unbesetzte Lücke | 2 | LF | M | Suchlücke | **produziert → LF-02** |

## Wöchentlicher Signal-Mine (15 Min.)

```
[ ] Kommentare + Community-Post-Antworten seit letzter Woche geclustert (Verwirrung / Einwand / Wunsch)
[ ] beste Frage aus Support/E-Mail notiert
[ ] ein Forum-Thread mit wiederholtem Engagement (r/LocalLLaMA, r/de_EDV, Heise-Forum)
[ ] Top-3 Videos von 2 Vergleichskanälen: Muster + Lücke (nicht umformulieren)
[ ] tools/trend_radar.py (Montag, mit Kanal-RSS) und tools/youtube_search_scan.py --week gelaufen, Drei-Tore-Check für max. 1 Trend
[ ] alles Zwischendurch-Erfasste eingetragen
```
