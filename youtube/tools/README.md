# Werkzeuge

Alle Skripte laufen lokal auf deinem Rechner (Python 3.10+, `pip install requests Pillow`,
ffmpeg im PATH). Ausgaben landen in `../output/` (von Git ignoriert).

| Skript | Was es tut | Beispiel |
|---|---|---|
| `trend_radar.py` | Google Trends (DE), Reddit-Nischen, Hacker News, YouTube-RSS von Vergleichskanälen → Markdown-Report mit Drei-Tore-Checkliste | `python3 trend_radar.py --channels UCxxxx,UCyyyy` |
| `youtube_search_scan.py` | YouTube-Suche je Keyword → Titel, Kanal, Aufrufe, Alter, Länge, häufige Titelwörter, Median-Länge (Packaging-Muster + Lücken) | `python3 youtube_search_scan.py "lokale ki" "smartscreen warnung" --week` |
| `captions_from_script.py` | Skript fürs Ohr + Artlist-Audio → SRT (2 Zeilen × 42 Zeichen, proportionales Timing) | `python3 captions_from_script.py ../produktion/skripte/SH-04.vo.txt --audio stimme.wav` |
| `build_video.py` | Folien-Datei + Audio + SRT → MP4 in 16:9 und/oder 9:16 mit eingebrannten Untertiteln | `python3 build_video.py ../produktion/skripte/SH-04.slides.md --audio stimme.wav --srt ../output/SH-04.vo.srt --format both` |
| `voiceover.py` | optional: ElevenLabs-API → MP3 + wortgenaue SRT (`ELEVENLABS_API_KEY` als Umgebungsvariable) | `python3 voiceover.py skript.vo.txt --voice <id> --final` |

Schnelltest ohne Stimme (Animatic): `python3 build_video.py ../produktion/skripte/SH-04.slides.md --silent 18 --format short`

Regeln: keine API-Keys im Repo oder in Video-Beschreibungen · Ausgaben nicht committen · KI-Stimme
und KI-Bilder immer offenlegen.
