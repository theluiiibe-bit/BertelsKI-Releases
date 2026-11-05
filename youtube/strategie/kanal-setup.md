# Kanal-Setup – einmalig, vor dem ersten Upload

> Liest `brand-profile.md`, `content-pillars.md`, `wettbewerb-und-suche.md`. Alles mit ⚠️ bestätigen.

## Name, Handle, Beschreibung

- **Kanalname:** ⚠️ „BertelsKI“ (Markenname) oder „Meine KI – lokal auf Windows“ (Keyword-Name).
  Empfehlung: **„BertelsKI“** als Name, Keyword in der Kanal-Beschreibung und im Tagline-Zusatz.
- **Handle:** ⚠️ `@BertelsKI` (prüfen, ob frei).
- **Kanal-Beschreibung (Keywords in den ersten zwei Zeilen):**
  ```
  Lokale KI auf Windows, die auf deinem Rechner bleibt. Wir bauen „Meine KI“ und zeigen hier,
  was lokale KI im Arbeitsalltag wirklich kann – ohne Cloud, ohne Terminal, mit ehrlichen Grenzen.

  Jeden Donnerstag ein Video: Demos im Flugmodus, Sicherheit zum Nachprüfen (Signaturen,
  Prüfsummen, SmartScreen), Workflows für Selbstständige und kleine Teams, und das
  Release-Tagebuch hinter der App.

  Download (signierter Installer): https://theluiiibe-bit.github.io/BertelsKI-Releases/
  Sprecherstimme in Videos: KI-generiert und als solche gekennzeichnet.
  ```
- **Links:** Download-Seite (UTM `utm_source=youtube&utm_medium=channel`), ⚠️ Newsletter, ⚠️ Impressum/Kontakt.

## Banner (2560×1440, sicherer Bereich 1546×423 mittig)

Dunkler Grund (#10141C), eine Akzentfarbe (Gelb-Orange #FFB830), Inter Bold. Links: Produkt-Fenster
von Meine KI (echter Screenshot ohne Nutzerdaten). Rechts drei Wörter: **„Lokal. Signiert. Ehrlich.“**
Darunter klein: „Neue Videos donnerstags“. Kein Gesicht nötig. Lesbar auf dem Handy prüfen.

## Trailer (60 s, für Nicht-Abonnenten)

Aus LF-01 Cold Open plus Versprechen des Kanals. VO-Text: `../produktion/skripte/TRAILER.vo.txt`.
Struktur: 0–8 s Flugmodus-Beweis · 8–30 s was der Kanal zeigt (drei Säulen in je einem Satz) ·
30–45 s die ehrliche Grenze (Vertrauensanker) · 45–60 s „Donnerstags. Abonnieren, wenn du KI
willst, die bei dir bleibt.“ Eingebrannte Untertitel, KI-Stimme offengelegt.

## Playlists (Kette für Session-Beitrag)

| Playlist | Inhalt | Erstes Video |
|---|---|---|
| Erste Schritte mit Meine KI | Säule 1 + 3, Einstiegspfad | LF-01 |
| Sicher installieren & updaten | Säule 2 | LF-02 |
| Montags-Workflow | Säule 3 Serie | Idee #7 |
| Release-Tagebuch | Säule 4 Serie | Idee #9 |
| Lokal oder Cloud? (Shorts) | Shorts-Serie | SH-02 |

## Standard-Texte

**Pinned Comment unter jedem Short:**
```
Das ganze Video dazu (mit Hardware-Antwort und ehrlicher Grenze): [Link LF-xx]
Was bleibt bei dir, was nicht – steht in der Beschreibung.
```
**Endscreen-Regel:** genau ein nächstes Video (das in der Kette) + die Playlist. Kein „Zufällig“.

**UTM-Schema:** `?utm_source=youtube&utm_medium=video&utm_campaign=<LF-xx|SH-xx>` für Videos,
`utm_medium=channel` für Kanal-Links, `utm_medium=short` für Pinned Comments.

## Einstellungen

- Standard-Sichtbarkeit: privat → nach Qualitäts-Tor öffentlich.
- `madeForKids` = false (Kanal-Standard).
- Kommentare: moderiert halten, Links in Kommentaren zur Prüfung zurückhalten (Schutz vor Fake-Download-Links –
  das ist bei einem Installer-Kanal ein echtes Risiko).
- Community-Tab: wöchentliche Umfrage (SPARK-Probe).
- Untertitel: automatische zulassen, aber eigene SRT hochladen (Namen, Zahlen korrekt).
- „Veränderter oder synthetischer Inhalt“: bei jedem Upload mit KI-Stimme wahrheitsgemäß setzen.

## Checkliste

```
[ ] Name/Handle gesetzt, Beschreibung mit „Lokale KI auf Windows“ in Zeile 1
[ ] Banner hochgeladen, auf Handy geprüft
[ ] Trailer veröffentlicht, als Kanaltrailer gesetzt
[ ] 5 Playlists angelegt (leer ist ok)
[ ] Links + UTM gesetzt
[ ] Kommentar-Moderation (Links zurückhalten) aktiv
[ ] Erster Community-Post: Umfrage „Was willst du mit KI auf deinem PC erledigen?“ (4 Optionen aus Säule 3)
```
