# Blender-Skripte für Inside View

`iv01_ear.py` baut die komplette IV-01-Szene per Python und rendert sie (Blender 4.2 oder neuer).

**Auf dem PC ausführen (Windows, Eingabeaufforderung im Ordner InsideView):**
```
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" -b -P iv01_ear.py -- --out C:/InsideView/render/IV-01 --fps 30 --seconds 42
ffmpeg -framerate 30 -i C:/InsideView/render/IV-01_%04d.png -c:v libx264 -pix_fmt yuv420p IV-01-raw.mp4
```
Nur Szene bauen und in Blender ansehen: `--no-render` anhängen, dann `IV-01.blend` öffnen.

**Dann:** Artlist-Stimme als WAV → `youtube/tools/captions_from_script.py` für die SRT →
Stimme + `IV-01-raw.mp4` + SRT + SFX in CapCut/DaVinci/HitFilm mischen → Upload mit KI-Hinweis.

Timing: Die `SHOTS`-Tabelle im Skript trägt Richtwerte für 42 s. Nach der Sprachaufnahme die
Sekundenwerte an die echten Pausen anpassen und neu rendern.

Hinweis: Das Skript ist ein stilisiertes Schnittmodell, keine medizinische Darstellung. Die Geometrie
ist bewusst einfach; Look entsteht über Palette, Licht und Bewegung. Das erste Rendering zeigt, was
noch nachgeschärft werden muss (Materialien, Kamera-Pfade).
