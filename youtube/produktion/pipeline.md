# Produktions-Pipeline: von der Idee zum veröffentlichten Video

> Jede Stufe nennt das Werkzeug, die Regel und wer entscheidet. Die KI plant, schreibt, briefed
> und interpretiert. **Der Mensch dreht, hört ab, lädt hoch und liest die Zahlen.**

```
Signal → Idee → PACKAGE → Skript (AV) → Vertonung → Bild → Captions → Metadaten → Thumbnail → Upload → Kette → Analytics
```

| # | Stufe | Werkzeug | Regel / Output |
|---|---|---|---|
| 1 | **Signal sammeln** | Kommentare, Support-Fragen, `tools/trend_radar.py`, Reddit, Suchvorschläge | wöchentlich 15 Min.; clustern: Verwirrung / Einwand / Wunsch → `ideen-bank.md` |
| 2 | **Idee wählen** | Ideen-Karte (Säule, Beleg, Aufwand) | nur Ideen mit Nachfrage-Beleg; teure Ideen erst als Short/Umfrage testen |
| 3 | **PACKAGE zuerst** | `wissen/04-…` CLICK + INDEX | Titel (Keyword in 40 Zeichen) + Thumbnail-Versprechen **vor** dem Skript. Zieht es nicht, Idee zurück in die Bank. |
| 4 | **Skript** | `wissen/02-…` AV-Vorlage, `skripte/_vorlage-long-form.md` | Cold Open ≤ 30 s löst Versprechen ein; Re-Hook alle 60–90 s; Wortzahl ÷ 130 = Minuten; Table-Read mit Stoppuhr |
| 5 | **Vertonung** | **Artlist AI Voiceover** (Text-to-Speech oder Speech-to-Speech) → `tools/captions_from_script.py` für die SRT; optional `tools/voiceover.py` (ElevenLabs, Wort-Zeitstempel) | Skript fürs Ohr (`*.vo.txt`); feste Kanalstimme; 2–3 Takes; Offenlegung notieren |
| 6 | **Bild** | OBS/Windows-Spielleiste für Screen-Recording; Handy für Talking Head; `tools/build_video.py` für Slide-Videos; Artlist-Footage oder KI-B-Roll nur als Zwischenschnitt | Cursor sichtbar, 1080p, Zoom auf Details; nie zweimal hintereinander „sprechender Kopf“; kein Fake-Screenshot |
| 7 | **Schnitt + Captions + Musik** | CapCut / DaVinci Resolve / HitFilm (Artlist); Musik + SFX aus Artlist (Musik −18 bis −24 dB unter Sprache); `build_video.py` brennt SRT ein | eingebrannte Untertitel 2 Zeilen, 32–42 Zeichen; erste halbe Sekunde jeder lahmen Stelle weg |
| 8 | **Shorts clippen** | Opus Clip / CapCut; Hook neu schreiben | nur in sich geschlossene Momente; 9:16 reframen; Loop bauen; **ohne Wasserzeichen**; Brücke zum Long-Form |
| 9 | **Metadaten** | `skripte/*.md` Abschnitt „Metadaten“ | Titel 50–60 Zeichen, Beschreibung mit Kapiteln + UTM-Link + KI-Hinweis, 3–5 Tags, Kategorie „Wissenschaft & Technik“, madeForKids=false |
| 10 | **Thumbnail** | Brief aus Skript → Ideogram / Nano-Banana / Canva / selbst; 1280×720 | 3 Konzepte, eine Variable; mobil bei 168×94 prüfen; nativ in Studio hochladen; Test & Compare |
| 11 | **Upload + Kette** | YouTube Studio | „Veränderter Inhalt“-Flag wahrheitsgemäß; Endscreen auf **ein** konkretes Video; Playlist; Shorts: Pinned Comment mit Link |
| 12 | **Analytics** | YouTube Studio (nativ), GA4/UTM | nach 48 h: CTR, 30-s-Retention, AVD %; Shorts: Viewed vs Swiped, Ø %; wöchentlich 3 Empfehlungen; Ergebnisse zurück in Stufe 1 |

## Werkzeuge im Repo (`../tools/`)

| Datei | Zweck | Benötigt |
|---|---|---|
| `trend_radar.py` | zieht Google-Trends (DE), Reddit-Nischen, Hacker News, YouTube-RSS von Vergleichskanälen → Markdown-Report mit Drei-Tore-Checkliste | Internet, Python 3.10+ (`requests`) |
| `captions_from_script.py` | Skript (`*.vo.txt`) + Artlist-Audio → SRT (proportionales Timing, 2 × 42 Zeichen) | `ffprobe` oder `--duration` |
| `voiceover.py` | optional: Skript → ElevenLabs MP3 + SRT (zeichen-genaue Timestamps) | `ELEVENLABS_API_KEY`, bezahlter Tarif |
| `build_video.py` | Skript-Abschnitte → Slides (PIL) + Audio + eingebrannte Untertitel → MP4 in 16:9 und 9:16 | `ffmpeg`, `Pillow` |

Ausgaben landen in `youtube/output/` (ignoriert von Git – Medien gehören nicht ins Release-Repo).

## Qualitäts-Tor vor dem Upload

```
[ ] Titel + Thumbnail versprechen genau das, was die ersten 30 s liefern
[ ] Cold Open ohne Intro/Logo/„Hallo Leute“
[ ] Wortzahl ÷ 130 ≈ Ziel-Länge; kein Padding
[ ] Re-Hook-Marker alle 60–90 s im Skript
[ ] Untertitel eingebrannt und auf Namen/Zahlen geprüft
[ ] KI-Stimme/KI-Bilder in Beschreibung + Upload-Flag offengelegt
[ ] Endscreen-Ziel + Playlist gesetzt
[ ] UTM-Link in der Beschreibung
[ ] madeForKids = false
[ ] Keine Interna (Keys, Pfade, Build-Protokolle) im Bild
```
