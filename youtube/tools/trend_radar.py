#!/usr/bin/env python3
"""
trend_radar.py – Live-Trendscan für die Nische „lokale KI / Windows / Datenschutz“.

Zieht ohne API-Keys:
  * Google Trends – tägliche Trends (RSS, Region DE)
  * YouTube-RSS der Vergleichskanäle (letzte Uploads, Titel-Muster)
  * Reddit – optional (--reddit); blockt Skripte meist mit 403, dann manuell lesen
  * Hacker News – Algolia-Suche nach Nischen-Keywords

und schreibt einen Markdown-Report mit der Drei-Tore-Checkliste (FIT, SAFETY, TIMING)
aus `wissen/05-trends-finden-und-ideen.md`. Das Skript findet Kandidaten; **bewerten
musst du** – kein Modell weiß, was gerade trendet.

Nutzung:
  python3 trend_radar.py                 # Report nach ../output/trend-report-YYYY-MM-DD.md
  python3 trend_radar.py --out report.md
  python3 trend_radar.py --channels UCxxxx,UCyyyy   # eigene Kanal-IDs ergänzen

Benötigt: Python 3.10+, `requests` (pip install requests). Internetzugang.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("Bitte zuerst: pip install requests")

UA = {"User-Agent": "bertelski-trend-radar/1.0 (+github.com/theluiiibe-bit/BertelsKI-Releases)"}
TIMEOUT = 20

# Nischen-Keywords: ein Treffer in Titel/Text markiert einen Kandidaten als FIT-verdächtig.
NICHE_KEYWORDS = [
    "ki", "ai", "künstliche intelligenz", "llm", "ollama", "lm studio", "gpt4all", "jan ",
    "lokal", "local", "offline", "datenschutz", "privacy", "dsgvo", "gdpr", "windows", "copilot",
    "chatgpt", "claude", "gemini", "llama", "mistral", "qwen", "open source", "open-source",
    "smartscreen", "signatur", "signature", "update", "desktop", "assistent", "assistant",
]

# Vergleichskanäle (YouTube-RSS braucht die Kanal-ID "UC…", nicht den Handle).
# Stand 05.11.2026; weitere IDs: Kanalseite → „Kanal teilen“ → „Kanal-ID kopieren“.
DEFAULT_CHANNELS: dict[str, str] = {
    "c't 3003": "UC1t9VFj-O6YUDPQxaVg-NkQ",
    "The Morpheus": "UCLGY6_j7kZfA1dmmjR1J_7w",
    "Digitale Profis": "UCv90NdTyTp7ZPPRvvSZaS5w",
    "NetworkChuck (EN)": "UC9x0AN7BWHpCDHSm9NiJFJQ",
    # weitere Nischen-Kanäle (IDs über Kanalseite → Teilen → Kanal-ID kopieren):
    # "KI-Wissen mit Harald Frey", "Daniel Klozbücher", "Giorgi Lomidze – Souveräne KI",
    # "Lokale KI mit Andreas Nürenberg", "AI mit Arnie", "Marco Franz"
}

# Reddit blockt Skript-Zugriffe ohne OAuth meist mit 403 – nur mit --reddit versuchen, sonst im Browser lesen.
SUBREDDITS = ["LocalLLaMA", "ollama", "de_EDV", "selfhosted", "PrivacyGuides"]
HN_QUERIES = ["local llm", "ollama", "on-device ai", "privacy ai assistant"]


def _get(url: str, **kw) -> requests.Response | None:
    try:
        r = requests.get(url, headers=UA, timeout=TIMEOUT, **kw)
        r.raise_for_status()
        return r
    except Exception as exc:  # noqa: BLE001
        print(f"  ! {url.split('/')[2]}: {exc}", file=sys.stderr)
        return None


def niche_hits(text: str) -> list[str]:
    t = text.lower()
    return [k for k in NICHE_KEYWORDS if re.search(r"(?<![a-zäöüß])" + re.escape(k.strip()) + r"(?![a-zäöüß])", t)]


# ---------------------------------------------------------------- Google Trends (DE)
def google_trends_de() -> list[dict]:
    r = _get("https://trends.google.com/trending/rss?geo=DE")
    if not r:
        return []
    out = []
    root = ET.fromstring(r.content)
    ns = {"ht": "https://trends.google.com/trending/rss"}
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        traffic = (item.findtext("ht:approx_traffic", namespaces=ns) or "").strip()
        news = item.find("ht:news_item", ns)
        news_title = news.findtext("ht:news_item_title", namespaces=ns) if news is not None else ""
        out.append({"title": title, "traffic": traffic, "context": news_title or "", "hits": niche_hits(f"{title} {news_title}")})
    return out


# ---------------------------------------------------------------- YouTube RSS
def youtube_channel_feed(channel_id: str) -> list[dict]:
    r = _get(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
    if not r:
        return []
    ns = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015", "media": "http://search.yahoo.com/mrss/"}
    root = ET.fromstring(r.content)
    out = []
    for e in root.findall("a:entry", ns)[:8]:
        title = e.findtext("a:title", namespaces=ns) or ""
        published = (e.findtext("a:published", namespaces=ns) or "")[:10]
        vid = e.findtext("yt:videoId", namespaces=ns) or ""
        views = ""
        stats = e.find(".//media:statistics", ns)
        if stats is not None:
            views = stats.attrib.get("views", "")
        out.append({"title": title, "date": published, "url": f"https://youtu.be/{vid}", "views": views, "hits": niche_hits(title)})
    return out


# ---------------------------------------------------------------- Reddit
def reddit_top(sub: str, limit: int = 8) -> list[dict]:
    r = _get(f"https://www.reddit.com/r/{sub}/top.json?t=week&limit={limit}")
    if not r:
        return []
    out = []
    for child in r.json().get("data", {}).get("children", []):
        d = child["data"]
        out.append({
            "title": d.get("title", ""),
            "score": d.get("score", 0),
            "comments": d.get("num_comments", 0),
            "url": "https://www.reddit.com" + d.get("permalink", ""),
            "hits": niche_hits(d.get("title", "")),
        })
    return out


# ---------------------------------------------------------------- Hacker News
def hn_search(query: str, days: int = 7, limit: int = 6) -> list[dict]:
    since = int((dt.datetime.now(dt.UTC) - dt.timedelta(days=days)).timestamp())
    r = _get("https://hn.algolia.com/api/v1/search", params={"query": query, "tags": "story", "numericFilters": f"created_at_i>{since}", "hitsPerPage": limit})
    if not r:
        return []
    return [{"title": h.get("title", ""), "points": h.get("points", 0), "comments": h.get("num_comments", 0),
             "url": h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}"} for h in r.json().get("hits", [])]


# ---------------------------------------------------------------- Report
GATES = """
### Drei-Tore-Check (für jeden Kandidaten, in dieser Reihenfolge)

| Tor | Frage | Antwort |
|---|---|---|
| 1 FIT | Habe ich einen echten Blickwinkel aus unserer Nische (lokale KI, Sicherheit, Arbeitstag, Build-in-Public)? | |
| 2 SAFETY | Tragödie / Krise / spaltendes Thema / Spott? → **nicht anfassen** | |
| 3 TIMING | Steigt es noch (emerging/rising) oder ist es gesättigt? | |

Ein Fail = nicht machen. Remix = Struktur des Trends + unsere Wahrheit, in unserer Stimme.
Output geht als Short (Sa-Slot) über `produktion/skripte/`.
"""


def md_table(rows: list[dict], cols: list[tuple[str, str]]) -> str:
    if not rows:
        return "_keine Daten (Quelle nicht erreichbar oder leer)_\n"
    head = "| " + " | ".join(c[1] for c in cols) + " |\n|" + "---|" * len(cols) + "\n"
    body = ""
    for r in rows:
        cells = []
        for key, _ in cols:
            v = r.get(key, "")
            if key == "hits":
                v = ", ".join(v) if v else ""
            cells.append(str(v).replace("|", "\\|"))
        body += "| " + " | ".join(cells) + " |\n"
    return head + body


def build_report(channels: dict[str, str], with_reddit: bool = False) -> str:
    today = dt.date.today().isoformat()
    parts = [f"# Trend-Radar · {today}\n",
             "> Kandidaten, keine Empfehlungen. Jede Zeile mit Nischen-Treffer (Spalte „Nische“) durch die drei Tore schicken.\n"]

    print("· Google Trends DE …", file=sys.stderr)
    gt = google_trends_de()
    parts.append("## Google Trends (DE, täglich)\n" + md_table(gt, [("title", "Suchbegriff"), ("traffic", "Volumen"), ("context", "Kontext"), ("hits", "Nische")]))

    parts.append("## Vergleichskanäle (YouTube-RSS, letzte Uploads)\n")
    if not channels:
        parts.append("_Keine Kanal-IDs konfiguriert – `DEFAULT_CHANNELS` im Skript oder `--channels` setzen._\n")
    for name, cid in channels.items():
        print(f"· YouTube {name} …", file=sys.stderr)
        parts.append(f"### {name}\n" + md_table(youtube_channel_feed(cid), [("date", "Datum"), ("title", "Titel"), ("views", "Views"), ("url", "Link"), ("hits", "Nische")]))

    parts.append("## Reddit (Top der Woche)\n")
    if with_reddit:
        for sub in SUBREDDITS:
            print(f"· r/{sub} …", file=sys.stderr)
            parts.append(f"### r/{sub}\n" + md_table(reddit_top(sub), [("score", "Score"), ("comments", "Komm."), ("title", "Titel"), ("url", "Link")]))
    else:
        parts.append("_Übersprungen (Reddit blockt Skripte meist mit 403). Manuell lesen: " + ", ".join(f"[r/{s}](https://www.reddit.com/r/{s}/top/?t=week)" for s in SUBREDDITS) + " – oder `--reddit` versuchen._\n")

    parts.append("## Hacker News (7 Tage)\n")
    for q in HN_QUERIES:
        print(f"· HN „{q}“ …", file=sys.stderr)
        parts.append(f"### „{q}“\n" + md_table(hn_search(q), [("points", "Punkte"), ("comments", "Komm."), ("title", "Titel"), ("url", "Link")]))

    parts.append(GATES)
    parts.append("\n## Manuell prüfen (keine API)\n- YouTube-Suche „KI lokal“ / „KI offline“ mit Filter *Diese Woche* → Titel-Muster notieren\n- Release-Notes: Ollama, LM Studio, Windows Copilot – neue Features = Plattform-Trend\n- eigene Kommentare clustern (Verwirrung / Einwand / Wunsch) → `produktion/ideen-bank.md`\n")
    return "\n".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", help="Zieldatei (Standard: ../output/trend-report-<Datum>.md)")
    ap.add_argument("--channels", help="Kommagetrennte YouTube-Kanal-IDs (UC…), zusätzlich zu DEFAULT_CHANNELS")
    ap.add_argument("--reddit", action="store_true", help="Reddit-JSON trotzdem versuchen (meist 403)")
    args = ap.parse_args()

    channels = dict(DEFAULT_CHANNELS)
    if args.channels:
        for cid in args.channels.split(","):
            cid = cid.strip()
            if cid:
                channels[cid] = cid

    report = build_report(channels, with_reddit=args.reddit)
    out = Path(args.out) if args.out else Path(__file__).resolve().parent.parent / "output" / f"trend-report-{dt.date.today().isoformat()}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"Report: {out}")


if __name__ == "__main__":
    main()
