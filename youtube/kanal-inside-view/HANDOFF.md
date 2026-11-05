# Übergabe an die lokale Session (PC „InsideView“)

Du bist dieselbe Claude wie in der Cloud-Session vom 05.11.2026, nur lokal auf dem PC des
Kanalbetreibers. Dieses Dokument ist dein Gedächtnis. Lies es zuerst, dann die verlinkten Dateien.

## Wer entscheidet

Der Kanalbetreiber entscheidet, und zwar in **kleinen Schritten, jeder einzeln bestätigt**. Er will
keine Fragebögen und keine Fachbegriffe ohne Erklärung („für Dumme erklären“: Commit = Speicherpunkt
lokal, Push = zu GitHub hochladen). Nichts zu GitHub pushen ohne sein Wort. Er hat gesagt: „Ich
vertraue dir, nimm, was du am besten findest“ – also Vorschlag mit Begründung machen, kurz
bestätigen lassen, dann umsetzen. Nicht vorauseilen und eine ganze Strategie bauen (das ist in
der Cloud einmal schiefgegangen: Ich hatte den Kanal auf sein Software-Produkt ausgerichtet, das
wollte er nicht).

## Was entschieden ist

- **Kanal: „Inside View“**, englischsprachig, gesichtslos, Blender-3D, Stimme aus **Artlist AI
  Voiceover** (er hat Artlist Max; kein ElevenLabs).
- **Format:** 25–45 s Shorts, 9:16. Jeder Short zeigt das Innere von etwas im Moment, in dem etwas
  passiert. Schnittmodell-Look, feste Palette (Hintergrund #1B2430, Haut Beige, Orange #FF8A3D,
  Türkis #3DD6C8). Details: `00-konzept.md`.
- **Vorbild-Mechanismus** (Zack D Films, aus 30 Shorts analysiert): Titel als Frage mit Lücke plus
  Emoji; 3D zeigt, was eine Kamera nicht kann; hohe Erregung (Staunen, Ekel, Empörung, Humor);
  Loop am Ende. Eigener Look ist Pflicht (YouTube-Originalitätsregel seit Okt. 2026).
- **Erstes Video: IV-01 „What happens inside your ear when a plane takes off 😮“** – Skript,
  Quellen, Shot-Briefs, Sprechtext und Metadaten liegen in `skripte/`. Blender-Szene als
  Python-Skript in `blender/iv01_ear.py` (nur syntaxgeprüft, nie gerendert – erster Lauf zeigt,
  was nachzuschärfen ist).
- Kadenz-Ziel: 3 Shorts/Woche, drei fertige im Puffer vor dem ersten Upload.

## Was du jetzt tun sollst (in dieser Reihenfolge, jeden Schritt kurz bestätigen lassen)

1. Blender finden (`where blender` / Standardpfad) und `blender/iv01_ear.py` mit `--no-render`
   ausführen, `IV-01.blend` öffnen, Screenshot zeigen. Dann Szene nachschärfen, bis der Look stimmt.
2. Rendern (Befehl in `blender/README.md`), mit ffmpeg zu `IV-01-raw.mp4` zusammenfügen, zeigen.
3. Sprechtext `skripte/IV-01.vo.txt` – der Betreiber fügt ihn in Artlist ein (du darfst seinen
   Browser mitbedienen, aber nie seine Zugangsdaten anfassen). WAV speichern.
4. `../tools/captions_from_script.py IV-01.vo.txt --audio stimme.wav` → SRT. Shot-Zeiten im
   Blender-Skript (`SHOTS`) an die echte Aufnahme anpassen, ggf. neu rendern.
5. Stimme + Video + SRT + dezente SFX (Artlist) mischen (CapCut/DaVinci/HitFilm oder ffmpeg).
6. Upload durch den Betreiber in YouTube Studio; Titel, Beschreibung, Tags aus dem Skript; Flag
   „veränderter/synthetischer Inhalt“ setzen; Pinned Comment mit Quellen.
7. Danach IV-02 aus der Ideen-Bank in `00-konzept.md` (Vorschlag: #7 Mückenstich oder #2 Katze).

## Dein Wissen (alles im Repo, aus 20 Creator-Skills destilliert)

Lies bei Bedarf: `../wissen/01-youtube-algorithmus-2026.md` (Shorts: Viewed-vs-Swiped, erste
30–60 Min., Anti-Repetitive-KI, 28-Tage-Flattening, Captions), `02-hooks-skripte-und-dreh.md`
(11 Hook-Mechanismen, Zwei-Spalten-Skript), `03-vertonung-ki-voiceover.md` (Artlist-Workflow,
Skript fürs Ohr), `04-thumbnails-und-metadaten.md`, `05-trends-finden-und-ideen.md` (Drei Tore,
Viral-Teardown, SPARK), `06-ziele-analytics-monetarisierung.md`.
Wenn die Skills verfügbar sind, lade zusätzlich: `social-media-skills:youtube-shorts`,
`hook-writer`, `viral-reverse-engineering`, `scripting-and-storyboarding`, `ai-voiceover`,
`trend-jacking`, `idea-generation-and-ideation`, `captions-and-clipping`, `thumbnail-design`.

## Werkzeuge (`../tools/`)

`trend_radar.py` (Google Trends DE, Hacker News, YouTube-RSS der Vergleichskanäle),
`youtube_search_scan.py` (Suchergebnisse je Keyword: Titel, Views, Länge, Titelwörter),
`captions_from_script.py` (Skript + Audio → SRT), `build_video.py` (Folien + Audio + SRT → MP4,
Animatic), `voiceover.py` (optional ElevenLabs). Alle brauchen Python 3.10+, `requests`, `Pillow`, ffmpeg.

## Harte Regeln

Keine Zahlen über Performance erfinden (nur YouTube Studio). KI-Stimme immer offenlegen. Jede
Aussage im Video mit Quelle. Keine echten Personen, keine fremden Marken/Figuren. Fiktion im
Titel markieren. Keine Medizin-Ratschläge. Reddit blockt Skripte; YouTube-Watch-Seiten und
interne Player-API nicht per Skript abgreifen (wurde als Bot-Umgehung abgelehnt) – Transkripte
per Browser.

## Der Stand der anderen Ordner

`../strategie/` und `../produktion/` sind ein **verworfener** erster Entwurf für einen
produktbezogenen Kanal („Meine KI“). Nicht weiterverfolgen, nur als Beispielmaterial.
