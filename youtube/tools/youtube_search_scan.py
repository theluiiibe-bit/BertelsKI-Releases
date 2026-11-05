#!/usr/bin/env python3
"""
youtube_search_scan.py – Packaging-Scan der YouTube-Suche für Nischen-Keywords (ohne API-Key).

Lädt die öffentliche Suchergebnisseite, liest das eingebettete `ytInitialData` und listet pro
Keyword die Ergebnisse: Titel, Kanal, Aufrufe, Alter, Länge, Link. Daraus liest du ab, welche
Titel-Muster und Längen in der Nische ranken (CLICK/INDEX aus `wissen/04-…`) und welche Lücke
offen ist (SPARK: Wettbewerber-Muster + Lücke, nie umformulieren).

Nutzung:
  python3 youtube_search_scan.py "ki offline" "ki lokal windows" --out ../output/suche.md
  python3 youtube_search_scan.py "smartscreen warnung" --month        # nur letzter Monat
  python3 youtube_search_scan.py --from-html ordner/                   # bereits gespeicherte Seiten

Honest scope: Zahlen sind die öffentlich angezeigten Aufrufe zum Abrufzeitpunkt – keine Analytics.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.parse
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("Bitte zuerst: pip install requests")

HEADERS = {"Accept-Language": "de-DE,de;q=0.9", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) bertelski-search-scan/1.0"}
SP_MONTH = "EgIIBA%3D%3D"   # Upload-Datum: diesen Monat
SP_WEEK = "EgIIAw%3D%3D"    # Upload-Datum: diese Woche


def fetch(query: str, sp: str | None) -> str:
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}&hl=de&gl=DE"
    if sp:
        url += f"&sp={sp}"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.text


def extract_initial_data(html: str) -> dict:
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not m:
        m = re.search(r'window\["ytInitialData"\] = (\{.*?\});', html, re.S)
    if not m:
        raise ValueError("ytInitialData nicht gefunden (Seite geändert oder Consent-Wall).")
    return json.loads(m.group(1))


def runs_text(obj: dict | None) -> str:
    if not obj:
        return ""
    if "simpleText" in obj:
        return obj["simpleText"]
    return "".join(r.get("text", "") for r in obj.get("runs", []))


def walk(node, out: list[dict]) -> None:
    if isinstance(node, dict):
        if "videoRenderer" in node:
            v = node["videoRenderer"]
            out.append({
                "id": v.get("videoId", ""),
                "title": runs_text(v.get("title")),
                "channel": runs_text(v.get("ownerText")) or runs_text(v.get("longBylineText")),
                "views": runs_text(v.get("viewCountText")),
                "age": runs_text(v.get("publishedTimeText")),
                "length": runs_text(v.get("lengthText")),
                "short": any("reelItemRenderer" in str(k) for k in v.get("navigationEndpoint", {}).keys()) or ("shorts" in str(v.get("navigationEndpoint", {}))),
            })
        elif "reelItemRenderer" in node:
            v = node["reelItemRenderer"]
            out.append({"id": v.get("videoId", ""), "title": runs_text(v.get("headline")), "channel": "", "views": runs_text(v.get("viewCountText")), "age": "", "length": "Short", "short": True})
        for val in node.values():
            walk(val, out)
    elif isinstance(node, list):
        for item in node:
            walk(item, out)


def parse_results(html: str) -> list[dict]:
    data = extract_initial_data(html)
    out: list[dict] = []
    walk(data, out)
    seen, uniq = set(), []
    for r in out:
        if r["id"] and r["id"] not in seen:
            seen.add(r["id"])
            uniq.append(r)
    return uniq


def views_num(s: str) -> int:
    m = re.search(r"([\d.,]+)\s*(Mio|Mrd|M|B|K|Tsd)?", s.replace(" ", " "))
    if not m:
        return 0
    num = m.group(1).replace(".", "").replace(",", ".")
    try:
        n = float(num)
    except ValueError:
        return 0
    mult = {"Mio": 1e6, "M": 1e6, "Mrd": 1e9, "B": 1e9, "K": 1e3, "Tsd": 1e3}.get(m.group(2) or "", 1)
    return int(n * mult)


def length_sec(s: str) -> int:
    parts = [int(p) for p in s.split(":")] if re.fullmatch(r"[\d:]+", s or "") else []
    sec = 0
    for p in parts:
        sec = sec * 60 + p
    return sec


def md_section(query: str, results: list[dict], label: str) -> str:
    rows = [f"## „{query}“ – {label} ({len(results)} Treffer)\n", "| # | Titel | Kanal | Aufrufe | Alter | Länge |", "|---|---|---|---|---|---|"]
    for i, r in enumerate(results[:20], 1):
        t = r["title"].replace("|", "\\|")
        rows.append(f"| {i} | [{t}](https://youtu.be/{r['id']}) | {r['channel']} | {r['views']} | {r['age']} | {r['length']} |")
    longs = [r for r in results if not r["short"] and length_sec(r["length"]) >= 60]
    if longs:
        secs = sorted(length_sec(r["length"]) for r in longs)
        med = secs[len(secs) // 2]
        rows.append(f"\nLong-Form: {len(longs)} · Median-Länge {med // 60}:{med % 60:02d} · Shorts: {sum(1 for r in results if r['short'] or length_sec(r['length']) < 60)}")
    # Titel-Muster: häufigste Wörter (grob)
    words = re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", " ".join(r["title"] for r in results).lower())
    stop = {"und", "oder", "mit", "für", "das", "der", "die", "den", "dem", "ein", "eine", "auf", "von", "wie", "was", "nicht", "ist", "sind", "deutsch", "video", "2026", "2025", "deine", "dein", "jetzt", "ohne", "auch", "noch", "aber"}
    freq: dict[str, int] = {}
    for w in words:
        if w not in stop:
            freq[w] = freq.get(w, 0) + 1
    top = sorted(freq.items(), key=lambda kv: -kv[1])[:12]
    rows.append("Häufige Titelwörter: " + ", ".join(f"{w} ({n})" for w, n in top))
    return "\n".join(rows) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("queries", nargs="*")
    ap.add_argument("--month", action="store_true", help="nur Uploads des letzten Monats")
    ap.add_argument("--week", action="store_true", help="nur Uploads der letzten Woche")
    ap.add_argument("--from-html", type=Path, help="Ordner mit gespeicherten Ergebnisseiten (*.html)")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    sections = [f"# YouTube-Suche Packaging-Scan · {dt.date.today().isoformat()}\n", "> Öffentlich angezeigte Zahlen zum Abrufzeitpunkt. Muster lesen, nicht kopieren.\n"]
    if args.from_html:
        for f in sorted(args.from_html.glob("*.html")):
            label = "letzter Monat" if ".month" in f.name else "alle Zeiten"
            q = f.name.replace(".month", "").replace(".html", "").replace("_", " ")
            try:
                sections.append(md_section(q, parse_results(f.read_text(encoding="utf-8", errors="ignore")), label))
            except Exception as exc:  # noqa: BLE001
                sections.append(f"## „{q}“ – Fehler: {exc}\n")
    else:
        if not args.queries:
            ap.error("Keywords angeben oder --from-html.")
        sp = SP_WEEK if args.week else SP_MONTH if args.month else None
        label = "letzte Woche" if args.week else "letzter Monat" if args.month else "alle Zeiten"
        for q in args.queries:
            print(f"· {q} …", file=sys.stderr)
            try:
                sections.append(md_section(q, parse_results(fetch(q, sp)), label))
            except Exception as exc:  # noqa: BLE001
                sections.append(f"## „{q}“ – Fehler: {exc}\n")
    report = "\n".join(sections)
    out = args.out or Path(__file__).resolve().parent.parent / "output" / f"suche-scan-{dt.date.today().isoformat()}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"Report: {out}")


if __name__ == "__main__":
    main()
