#!/usr/bin/env python3
"""
voiceover.py – Skript → ElevenLabs-Sprachausgabe (MP3) + Untertitel (SRT).

Umsetzung des VOICE-Frameworks aus `wissen/03-vertonung-ki-voiceover.md`:
  * Entwurf auf Flash (billig), Final auf eleven_v3 / eleven_multilingual_v2
  * Stability/Similarity als Regie-Regler
  * SRT aus den zeichen-genauen Timestamps der API → Captions sitzen exakt
  * Offenlegungs-Hinweis wird als .disclosure.txt neben die Ausgabe gelegt

Nutzung:
  export ELEVENLABS_API_KEY=...            # nie ins Repo, nie in die Beschreibung
  python3 voiceover.py skript.txt --voice <voice_id> --final
  python3 voiceover.py skript.txt --voice <voice_id>            # Entwurf (Flash)
  python3 voiceover.py --list-voices                            # verfügbare Stimmen

Skript-Format: reiner Text fürs Ohr. Leerzeile = Pause (wird als Absatz gesendet).
Zeilen, die mit '#' beginnen, sind Regie-Notizen und werden nicht gesprochen.

Lizenz-Hinweis: Der Free-Tarif erlaubt keine kommerzielle Nutzung und verlangt Attribution.
Für monetarisierte Videos mindestens Starter.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("Bitte zuerst: pip install requests")

API = "https://api.elevenlabs.io/v1"
MODELS = {
    "draft": "eleven_flash_v2_5",
    "final": "eleven_multilingual_v2",
    "expressive": "eleven_v3",
}
MAX_CHARS_PER_REQUEST = 4500  # unter dem 5.000-Zeichen-Limit von v3 bleiben


def api_key() -> str:
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY ist nicht gesetzt (export ELEVENLABS_API_KEY=...).")
    return key


def read_script(path: Path) -> list[str]:
    """Absätze fürs Ohr; '#'-Zeilen sind Regie-Notizen."""
    text = path.read_text(encoding="utf-8")
    paragraphs, buf = [], []
    for line in text.splitlines():
        if line.strip().startswith("#"):
            continue
        if not line.strip():
            if buf:
                paragraphs.append(" ".join(buf).strip())
                buf = []
        else:
            buf.append(line.strip())
    if buf:
        paragraphs.append(" ".join(buf).strip())
    return paragraphs


def chunk_paragraphs(paragraphs: list[str]) -> list[str]:
    chunks, cur = [], ""
    for p in paragraphs:
        if len(p) > MAX_CHARS_PER_REQUEST:
            sys.exit(f"Ein Absatz ist länger als {MAX_CHARS_PER_REQUEST} Zeichen – bitte teilen (Leerzeile).")
        if len(cur) + len(p) + 2 > MAX_CHARS_PER_REQUEST and cur:
            chunks.append(cur)
            cur = p
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        chunks.append(cur)
    return chunks


def list_voices() -> None:
    r = requests.get(f"{API}/voices", headers={"xi-api-key": api_key()}, timeout=30)
    r.raise_for_status()
    for v in r.json().get("voices", []):
        labels = ", ".join(f"{k}={val}" for k, val in (v.get("labels") or {}).items())
        print(f"{v['voice_id']}  {v['name']:<24} {labels}")


def tts_with_timestamps(text: str, voice: str, model: str, stability: float, similarity: float, lang: str | None) -> tuple[bytes, list[str], list[float], list[float]]:
    body: dict = {
        "text": text,
        "model_id": model,
        "voice_settings": {"stability": stability, "similarity_boost": similarity},
    }
    if lang and model != "eleven_v3":
        body["language_code"] = lang  # v3 erkennt die Sprache selbst
    r = requests.post(
        f"{API}/text-to-speech/{voice}/with-timestamps",
        headers={"xi-api-key": api_key(), "Content-Type": "application/json"},
        json=body,
        timeout=300,
    )
    if r.status_code != 200:
        sys.exit(f"ElevenLabs {r.status_code}: {r.text[:400]}")
    data = r.json()
    audio = base64.b64decode(data["audio_base64"])
    al = data.get("alignment") or data.get("normalized_alignment") or {}
    return audio, al.get("characters", []), al.get("character_start_times_seconds", []), al.get("character_end_times_seconds", [])


def srt_time(sec: float) -> str:
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def build_srt(chars: list[str], starts: list[float], ends: list[float], offset: float, max_chars: int = 42, max_lines: int = 2) -> list[tuple[float, float, str]]:
    """Wörter aus Zeichen-Alignment bauen, dann Blöcke à max_lines × max_chars (Shorts-Spezifikation)."""
    words: list[tuple[float, float, str]] = []
    cur, w_start = "", None
    for ch, s, e in zip(chars, starts, ends):
        if ch.isspace():
            if cur:
                words.append((w_start, e, cur))
                cur, w_start = "", None
        else:
            if w_start is None:
                w_start = s
            cur += ch
    if cur:
        words.append((w_start, ends[-1] if ends else 0.0, cur))

    cues: list[tuple[float, float, str]] = []
    lines: list[str] = []
    line = ""
    cue_start = None
    cue_end = 0.0
    for s, e, w in words:
        if cue_start is None:
            cue_start = s
        candidate = f"{line} {w}".strip()
        if len(candidate) <= max_chars:
            line = candidate
        else:
            lines.append(line)
            line = w
            if len(lines) == max_lines:
                cues.append((cue_start + offset, cue_end + offset, "\n".join(lines)))
                lines, cue_start = [], s
        cue_end = e
        if w.endswith((".", "!", "?")) and (lines or len(line) > max_chars * 0.6):
            lines.append(line)
            cues.append((cue_start + offset, cue_end + offset, "\n".join(lines)))
            lines, line, cue_start = [], "", None
    if line:
        lines.append(line)
    if lines and cue_start is not None:
        cues.append((cue_start + offset, cue_end + offset, "\n".join(lines)))
    return cues


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("script", nargs="?", help="Textdatei fürs Ohr")
    ap.add_argument("--voice", help="ElevenLabs voice_id (siehe --list-voices)")
    ap.add_argument("--final", action="store_true", help="eleven_multilingual_v2 statt Flash-Entwurf")
    ap.add_argument("--expressive", action="store_true", help="eleven_v3 (Audio-Tags wie [warm])")
    ap.add_argument("--model", help="Modell-ID explizit")
    ap.add_argument("--stability", type=float, default=0.55)
    ap.add_argument("--similarity", type=float, default=0.8)
    ap.add_argument("--lang", default="de", help="Sprachcode für v2/Flash (v3 erkennt selbst)")
    ap.add_argument("--out", help="Zielpfad ohne Endung (Standard: ../output/<skriptname>)")
    ap.add_argument("--list-voices", action="store_true")
    args = ap.parse_args()

    if args.list_voices:
        list_voices()
        return
    if not args.script or not args.voice:
        ap.error("Skript und --voice sind nötig (oder --list-voices).")

    model = args.model or (MODELS["expressive"] if args.expressive else MODELS["final"] if args.final else MODELS["draft"])
    script_path = Path(args.script)
    paragraphs = read_script(script_path)
    if not paragraphs:
        sys.exit("Skript ist leer.")
    chunks = chunk_paragraphs(paragraphs)
    total_chars = sum(len(c) for c in chunks)
    words = sum(len(c.split()) for c in chunks)
    print(f"Modell {model} · {len(chunks)} Anfrage(n) · {total_chars} Zeichen (≈ Credits) · {words} Wörter ≈ {words/130:.1f} Min.", file=sys.stderr)

    out_base = Path(args.out) if args.out else Path(__file__).resolve().parent.parent / "output" / script_path.stem
    out_base.parent.mkdir(parents=True, exist_ok=True)

    audio_all = bytearray()
    cues_all: list[tuple[float, float, str]] = []
    offset = 0.0
    for i, chunk in enumerate(chunks, 1):
        print(f"  Teil {i}/{len(chunks)} …", file=sys.stderr)
        audio, chars, starts, ends = tts_with_timestamps(chunk, args.voice, model, args.stability, args.similarity, args.lang)
        audio_all += audio
        cues_all += build_srt(chars, starts, ends, offset)
        if ends:
            offset += ends[-1] + 0.35  # kleine Pause zwischen Teilen (MP3-Konkatenation ist näherungsweise)

    mp3 = out_base.with_suffix(".mp3")
    mp3.write_bytes(audio_all)
    srt = out_base.with_suffix(".srt")
    with srt.open("w", encoding="utf-8") as f:
        for n, (s, e, text) in enumerate(cues_all, 1):
            f.write(f"{n}\n{srt_time(s)} --> {srt_time(max(e, s + 0.4))}\n{text}\n\n")
    disclosure = out_base.with_suffix(".disclosure.txt")
    disclosure.write_text(
        "Hinweis für Beschreibung + Upload: Die Sprecherstimme in diesem Video ist KI-generiert "
        f"(ElevenLabs, Modell {model}, lizenzierte Nutzung). Beim Upload das Feld „veränderter oder "
        "synthetischer Inhalt“ wahrheitsgemäß prüfen.\n", encoding="utf-8")
    meta = out_base.with_suffix(".json")
    meta.write_text(json.dumps({"model": model, "voice": args.voice, "stability": args.stability, "similarity": args.similarity, "chars": total_chars, "words": words, "chunks": len(chunks)}, indent=2), encoding="utf-8")
    print(f"MP3: {mp3}\nSRT: {srt}\nOffenlegung: {disclosure}")
    if len(chunks) > 1:
        print("Hinweis: Mehrere MP3-Teile wurden aneinandergehängt; für sauberes Timing in der Schnittsoftware prüfen oder mit ffmpeg neu encodieren.", file=sys.stderr)


if __name__ == "__main__":
    main()
