#!/usr/bin/env python3
"""
build_video.py – Slide-Video aus Skript + Audio + Untertiteln, in 16:9 (Long-Form) und 9:16 (Short).

Für gesichtslose Erklär-Passagen, Trailer, Shorts mit Text-Beats oder als Vorschau-Animatic,
bevor du Screen-Recordings schneidest. Nutzt Pillow für die Folien, ffmpeg für Mux + eingebrannte
Captions. Kein Upload, keine Analytics – nur die Datei.

Folien-Format (Markdown-ähnlich, eine Datei):
    ---                      Folien-Trenner
    # Große Überschrift      (max. ~5 Wörter, Hook-Text)
    Untertext in normaler Größe, mehrere Zeilen erlaubt.
    @12.5                    optionale Startzeit in Sekunden (sonst gleichmäßig über das Audio verteilt)

Nutzung:
  python3 build_video.py slides.md --audio vo.mp3 --srt vo.srt --out ../output/LF-01-trailer
  python3 build_video.py slides.md --audio vo.mp3 --format short      # 1080x1920
  python3 build_video.py slides.md --silent 20 --format both            # Test ohne Stimme, 20 s

Benötigt: ffmpeg im PATH, Pillow (pip install Pillow). Schrift: Inter (falls installiert), sonst DejaVu.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # pragma: no cover
    sys.exit("Bitte zuerst: pip install Pillow")

# Marken-Defaults (siehe strategie/brand-profile.md): dunkler Grund, eine Akzentfarbe, Inter Bold.
BG = (16, 20, 28)
FG = (240, 242, 246)
ACCENT = (255, 184, 48)
MUTED = (150, 158, 172)
FORMATS = {"long": (1920, 1080), "short": (1080, 1920)}

FONT_CANDIDATES_BOLD = [
    "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
    "/usr/share/fonts/truetype/inter/Inter-Bold.ttf",
    "C:/Windows/Fonts/Inter-Bold.ttf",
    "C:/Windows/Fonts/segoeuib.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
FONT_CANDIDATES_REG = [
    "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
    "/usr/share/fonts/truetype/inter/Inter-Regular.ttf",
    "C:/Windows/Fonts/Inter-Regular.ttf",
    "C:/Windows/Fonts/segoeui.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def pick_font(cands: list[str], size: int) -> ImageFont.FreeTypeFont:
    for c in cands:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default(size)


@dataclass
class Slide:
    title: str = ""
    body: list[str] = field(default_factory=list)
    start: float | None = None


def parse_slides(path: Path) -> list[Slide]:
    slides: list[Slide] = []
    cur = Slide()
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.strip() == "---":
            if cur.title or cur.body:
                slides.append(cur)
            cur = Slide()
        elif line.startswith("# "):
            cur.title = line[2:].strip()
        elif m := re.match(r"^@([\d.]+)\s*$", line.strip()):
            cur.start = float(m.group(1))
        elif line.strip():
            cur.body.append(line.strip())
    if cur.title or cur.body:
        slides.append(cur)
    if not slides:
        sys.exit("Keine Folien gefunden.")
    return slides


def wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        cand = f"{cur} {w}".strip()
        if draw.textlength(cand, font=font) <= max_w:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render_slide(s: Slide, size: tuple[int, int], idx: int, total: int, caption_safe: bool) -> Image.Image:
    w, h = size
    img = Image.new("RGB", size, BG)
    d = ImageDraw.Draw(img)
    margin = int(w * 0.08)
    vertical = h > w
    title_size = int(w * (0.085 if vertical else 0.06))
    body_size = int(w * (0.042 if vertical else 0.028))
    f_title = pick_font(FONT_CANDIDATES_BOLD, title_size)
    f_body = pick_font(FONT_CANDIDATES_REG, body_size)
    f_small = pick_font(FONT_CANDIDATES_REG, int(w * 0.018))

    # Akzent-Balken links oben (Marken-Signatur)
    d.rectangle([margin, int(h * 0.12), margin + int(w * 0.012), int(h * 0.12) + title_size], fill=ACCENT)

    max_text_w = w - 2 * margin - int(w * 0.03)
    y = int(h * 0.12)
    # Im Hochformat: Text im oberen Drittel halten (Augen/Hook-Zone), Captions-Zone unten frei.
    if vertical:
        y = int(h * 0.18)
    x = margin + int(w * 0.03)
    for line in wrap(d, s.title, f_title, max_text_w):
        d.text((x, y), line, font=f_title, fill=FG)
        y += int(title_size * 1.15)
    y += int(body_size * 0.8)
    for para in s.body:
        for line in wrap(d, para, f_body, max_text_w):
            d.text((x, y), line, font=f_body, fill=MUTED if para.startswith("(") else FG)
            y += int(body_size * 1.35)
        y += int(body_size * 0.5)
    if caption_safe:
        # untere ~22 % für eingebrannte Untertitel reservieren – hier nichts zeichnen
        pass
    d.text((margin, h - margin // 2 - int(w * 0.018)), f"{idx}/{total}", font=f_small, fill=MUTED)
    return img


def ffmpeg(*args: str) -> None:
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args]
    subprocess.run(cmd, check=True)


def audio_duration(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)], capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def build(slides: list[Slide], fmt: str, audio: Path | None, silent_secs: float | None, srt: Path | None, out_base: Path, fps: int = 30) -> Path:
    size = FORMATS[fmt]
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        if audio is None:
            audio = tdp / "silence.m4a"
            ffmpeg("-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", str(silent_secs or 10), "-c:a", "aac", str(audio))
        total = audio_duration(audio)

        # Startzeiten: explizit (@) oder gleichmäßig verteilt
        starts = [s.start for s in slides]
        if any(st is None for st in starts):
            step = total / len(slides)
            starts = [i * step if st is None else st for i, st in enumerate(starts)]
        starts = sorted(starts)
        ends = starts[1:] + [total]

        concat = tdp / "list.txt"
        with concat.open("w", encoding="utf-8") as f:
            for i, (s, st, en) in enumerate(zip(slides, starts, ends), 1):
                png = tdp / f"slide{i:03}.png"
                render_slide(s, size, i, len(slides), caption_safe=srt is not None).save(png)
                f.write(f"file '{png.name}'\nduration {max(en - st, 0.1):.3f}\n")
            f.write(f"file 'slide{len(slides):03}.png'\n")  # letzte Folie halten

        out = out_base.with_name(out_base.name + ("-short" if fmt == "short" else "-long")).with_suffix(".mp4")
        out.parent.mkdir(parents=True, exist_ok=True)
        vf = [f"scale={size[0]}:{size[1]}", "format=yuv420p"]
        if srt:
            # libass rechnet force_style-Werte im Skript-Raster (SRT → PlayRes 384x288), nicht in Pixeln.
            play_w, play_h = 384, 288
            margin_v = int(play_h * (0.20 if fmt == "short" else 0.08))
            font_size = 15 if fmt == "long" else 12
            style = (f"FontName=Inter,Bold=1,FontSize={font_size},PrimaryColour=&H00FFFFFF,OutlineColour=&H00101418,"
                     f"Outline=2,Shadow=0,Alignment=2,MarginV={margin_v},MarginL={int(play_w*0.06)},MarginR={int(play_w*0.06)}")
            srt_escaped = str(srt).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")
            vf.append(f"subtitles='{srt_escaped}':force_style='{style}'")
        ffmpeg("-f", "concat", "-safe", "0", "-i", str(concat), "-i", str(audio),
               "-vf", ",".join(vf), "-r", str(fps), "-c:v", "libx264", "-preset", "medium", "-crf", "20",
               "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out))
        return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slides", help="Folien-Datei (siehe Format oben)")
    ap.add_argument("--audio", type=Path, help="Voiceover (MP3/WAV/M4A), z. B. aus voiceover.py")
    ap.add_argument("--silent", type=float, help="Stattdessen Stille mit N Sekunden (Test/Animatic)")
    ap.add_argument("--srt", type=Path, help="Untertitel zum Einbrennen (aus voiceover.py)")
    ap.add_argument("--format", choices=["long", "short", "both"], default="long")
    ap.add_argument("--out", type=Path, help="Zielbasis ohne Endung (Standard: ../output/<slides-name>)")
    args = ap.parse_args()

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        sys.exit("ffmpeg/ffprobe nicht gefunden – bitte installieren und in den PATH legen.")
    if not args.audio and not args.silent:
        ap.error("--audio oder --silent angeben.")

    slides_path = Path(args.slides)
    slides = parse_slides(slides_path)
    out_base = args.out or Path(__file__).resolve().parent.parent / "output" / slides_path.stem
    fmts = ["long", "short"] if args.format == "both" else [args.format]
    for fmt in fmts:
        out = build(slides, fmt, args.audio, args.silent, args.srt, out_base)
        print(f"{fmt}: {out}")
    print("Erinnerung: Bei KI-Stimme/KI-Bild Offenlegung in Beschreibung + Upload-Flag.")


if __name__ == "__main__":
    main()
