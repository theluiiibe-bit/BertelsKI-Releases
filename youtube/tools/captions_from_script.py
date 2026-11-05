#!/usr/bin/env python3
"""
captions_from_script.py – SRT-Untertitel aus Skript + fertiger Audiodatei (z. B. aus Artlist AI-Voiceover).

Artlist liefert MP3/WAV, aber keine Wort-Zeitstempel. Dieses Werkzeug verteilt die Sätze des
Skripts proportional zu ihrer Länge über die Audiodauer und schreibt Blöcke à max. 2 Zeilen ×
42 Zeichen (Shorts-Spezifikation aus `wissen/01-…`). Das Timing ist eine gute erste Näherung;
Feinschliff (±0,3 s) machst du in CapCut/HitFilm/DaVinci am Wellenbild.

Skript-Format wie bei voiceover.py: reiner Text fürs Ohr, Leerzeile = Pause, '#'-Zeilen ignoriert.
Markierte Pausen "..." bekommen etwas zusätzliche Zeit.

Nutzung:
  python3 captions_from_script.py skript.txt --audio vo.mp3 --out ../output/SH-04.srt
  python3 captions_from_script.py skript.txt --duration 28.5 --out ../output/SH-04.srt   # ohne ffprobe

Benötigt: ffprobe (für --audio) – sonst --duration angeben.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

LEAD_IN = 0.15        # Sekunden vor dem ersten Wort
PAUSE_PARAGRAPH = 0.45
PAUSE_ELLIPSIS = 0.35
MAX_CHARS = 42
MAX_LINES = 2


def read_script(path: Path) -> list[list[str]]:
    """Liste von Absätzen; jeder Absatz = Liste von Sätzen."""
    paragraphs, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("#"):
            continue
        if not line.strip():
            if buf:
                paragraphs.append(" ".join(buf))
                buf = []
        else:
            buf.append(line.strip())
    if buf:
        paragraphs.append(" ".join(buf))
    out = []
    for p in paragraphs:
        # Satzgrenzen: . ! ? gefolgt von Leerzeichen; "..." bleibt im Satz
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ„\"(0-9])", p) if s.strip()]
        out.append(sents or [p])
    return out


def audio_duration(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
                         capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def weight(sentence: str) -> float:
    """Sprechdauer-Gewicht: Buchstaben zählen, Satzzeichen leicht, '...' extra."""
    letters = sum(1 for c in sentence if c.isalnum())
    return letters + 2.0 * sentence.count("...") + 0.5 * len(re.findall(r"[,;:]", sentence))


def wrap_block(text: str) -> list[str]:
    lines, cur = [], ""
    for w in text.split():
        cand = f"{cur} {w}".strip()
        if len(cand) <= MAX_CHARS:
            cur = cand
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def srt_time(sec: float) -> str:
    ms = int(round(max(sec, 0) * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def build(paragraphs: list[list[str]], duration: float) -> list[tuple[float, float, str]]:
    sentences = [(pi, s) for pi, sents in enumerate(paragraphs) for s in sents]
    pauses = PAUSE_PARAGRAPH * max(len(paragraphs) - 1, 0) + PAUSE_ELLIPSIS * sum(s.count("...") for _, s in sentences)
    speech = max(duration - LEAD_IN - pauses - 0.2, 1.0)
    total_w = sum(weight(s) for _, s in sentences) or 1.0
    cues, t, last_p = [], LEAD_IN, 0
    for pi, s in sentences:
        if pi != last_p:
            t += PAUSE_PARAGRAPH
            last_p = pi
        dur = speech * weight(s) / total_w + PAUSE_ELLIPSIS * s.count("...")
        # Satz in Blöcke à MAX_LINES Zeilen teilen, Zeit proportional zu Zeichen
        lines = wrap_block(s)
        blocks = [lines[i:i + MAX_LINES] for i in range(0, len(lines), MAX_LINES)]
        chars = sum(len(l) for l in lines) or 1
        bt = t
        for b in blocks:
            bd = dur * sum(len(l) for l in b) / chars
            cues.append((bt, bt + bd, "\n".join(b)))
            bt += bd
        t += dur
    return cues


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("script")
    ap.add_argument("--audio", type=Path, help="fertige Sprachdatei (Dauer per ffprobe)")
    ap.add_argument("--duration", type=float, help="Dauer in Sekunden, falls kein ffprobe")
    ap.add_argument("--out", type=Path, help="Ziel-SRT (Standard: ../output/<skript>.srt)")
    args = ap.parse_args()
    if not args.audio and not args.duration:
        ap.error("--audio oder --duration angeben.")
    duration = args.duration or audio_duration(args.audio)
    paragraphs = read_script(Path(args.script))
    cues = build(paragraphs, duration)
    out = args.out or Path(__file__).resolve().parent.parent / "output" / (Path(args.script).stem + ".srt")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for n, (s, e, text) in enumerate(cues, 1):
            f.write(f"{n}\n{srt_time(s)} --> {srt_time(e)}\n{text}\n\n")
    words = sum(len(s.split()) for p in paragraphs for s in p)
    print(f"{out}  ·  {len(cues)} Blöcke · {words} Wörter auf {duration:.1f} s = {words / (duration / 60):.0f} W/Min. (Ziel 120–140)")


if __name__ == "__main__":
    main()
