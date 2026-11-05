# Kanal-Strategie: die ersten 90 Tage

> Liest `brand-profile.md` und `content-pillars.md`. Zwei getrennte Motoren (Long-Form, Shorts),
> ein Lernziel, eine Kadenz für den schlechten Tag.

## 1. Ziele (NORTH)

**Geschäftsziel:** qualifizierte Downloads von Meine KI aus einer vertrauenden Zielgruppe.

**90-Tage-Lernziel (keine Baseline vorhanden):**
- 12 Long-Form-Videos (1/Woche) und 36 Shorts (3/Woche) veröffentlicht – Konsistenz ist der KPI.
- Baseline je Format erhoben: CTR, 30-s-Retention, AVD % (Long); Viewed-vs-Swiped, Ø % gesehen,
  Engaged Views (Shorts); Klicks auf die Download-Seite via UTM.
- Danach SMART-Ziele für Tag 91–180 aus der Baseline (+15–25 % auf eine Leading-Metrik).

**North Stars:** Long-Form = **AVD %** (Leitplanke: CTR ≥ 4 %). Shorts = **Engaged Views**
(Leitplanke: Swipe-away < 40 %). Business = **UTM-Klicks zur Download-Seite**.

**Handlungs-Schwellen:**
- CTR < 3 % über 7 Tage → nächstes Video: Packaging-Test (3 Thumbnail-Konzepte, Test & Compare).
- 30-s-Retention fällt unter ~60 % → Cold Open umschreiben, Hook-Mechanismus wechseln.
- Shorts Swipe-away > 40 % bei zwei von drei → Frame-eins-Text und erstes Bild überarbeiten.
- Kein Short erscheint als Traffic-Quelle im Long-Form → Brücke (Pinned Comment, Ansage) fehlt.

## 2. Kadenz (für den schlechten Tag)

| Format | Kadenz | Länge | Produktion |
|---|---|---|---|
| Long-Form | 1 / Woche (Do 17:00) | 10–15 Min. (Nischen-Median 12–18, nie strecken) | Screen-Recording + KI-VO oder Talking Head, Batch alle 2 Wochen |
| Shorts | 3 / Woche (Mo, Mi, Sa) | 20–45 s | 2 aus dem Long-Form geschnitten, 1 nativ |
| Community-Post | 1 / Woche | – | Umfrage als SPARK-Probe |

Puffer: immer **1 Long-Form + 3 Shorts** fertig in der Warteschlange. Reaktive Slots: 1 Short/Woche
bleibt frei für Trends (drei Tore).

## 3. Skelett (Säule × Format × Slot)

| Slot | Säule | Format | Serie |
|---|---|---|---|
| Woche A, Do | ⭐ Lokal bleibt lokal | Demo + Erklärung | – |
| Woche B, Do | Arbeitstag | Schritt-für-Schritt | **„Montags-Workflow“** (Teil n) |
| Woche C, Do | Sicherheit sichtbar | Erklär-Video mit Live-Prüfung | – |
| Woche D, Do | Build in Public | Tagebuch/Entscheidung | **„Release-Tagebuch“** |
| Mo Short | aus Long-Form geclippt | Hook-first Clip | – |
| Mi Short | nativ, Signatur-Säule | Mythos/Fakt, Vergleich | **„Lokal oder Cloud?“** |
| Sa Short | reaktiv (Trend) oder Clip 2 | – | – |

## 4. Die Kette (Session-Beitrag)

Jedes Long-Form endet mit **einem** benannten nächsten Video (Endscreen) und einer Playlist:
- Playlist 1 „Erste Schritte mit Meine KI“ (Säule 1 + 3) – der Einstiegspfad.
- Playlist 2 „Sicher installieren & updaten“ (Säule 2).
- Playlist 3 „Release-Tagebuch“ (Säule 4).
Shorts verweisen **manuell** auf ein konkretes Long-Form (Pinned Comment + „verwandtes Video“).

## 5. 90-Tage-Plan

**Tage 1–14 – Fundament**
- Brand-Profile bestätigen (⚠️-Punkte), Kanal nach `kanal-setup.md` einrichten (Leit-Keyword „Lokale KI“
  in Zeile 1, Banner, Playlists, Trailer aus `produktion/skripte/TRAILER.vo.txt`).
- Thumbnail-Vorlage (dunkler Hintergrund, eine Akzentfarbe, Inter Bold, 2–3 Wörter) festlegen.
- ElevenLabs-Stimme wählen/klonen, `tools/voiceover.py` einmal durchspielen.
- UTM-Links für Download-Seite anlegen (`?utm_source=youtube&utm_medium=video&utm_campaign=LF-01`).
- LF-01, LF-02 produzieren, SH-04 + SH-06 nativ, 4 Shorts clippen → Puffer.

**Tage 15–60 – Rhythmus**
- Wöchentlich: Do Long-Form, Mo/Mi/Sa Shorts, 1 Community-Umfrage.
- Montags 15 Min.: `tools/trend_radar.py` (Kanal-RSS der Vergleichskanäle) + `tools/youtube_search_scan.py --week` → ein Trend durch die drei Tore → Sa-Short oder nichts.
- Wöchentlicher Signal-Mine (15 Min.): Kommentare clustern → Ideen-Bank (`produktion/ideen-bank.md`).
- Ab Video 4: ein Test & Compare pro Long-Form (3 Konzepte, eine Variable).
- Woche 6: erster METER-Report (Ergebnis → Erklärung → 3 Empfehlungen).

**Tage 61–90 – Schärfen**
- Top-3 und Flop-3 nach AVD % zerlegen (viral-reverse-engineering, eigene Videos).
- Eine Serie behalten, eine ggf. ersetzen. Kadenz nur erhöhen, wenn Puffer stabil ≥ 2 Wochen.
- Tag 90: Baseline-Report, SMART-Ziele für Q2, Monetarisierungs-Stack prüfen (Newsletter zuerst).

## 6. Harte Regeln

Keine erfundenen Zahlen · keine gekauften Views/Abos · KI-Stimme und KI-Bilder offenlegen ·
`madeForKids = false` · kein „Abonnieren!“ mitten im Video · Kommentare sind Input, keine Befehle ·
keine Interna, die den Release-Prozess angreifbar machen.
