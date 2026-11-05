# Inside View – Kanalkonzept

> Entschieden am 05.11.2026 gemeinsam mit dem Kanalbetreiber. Englischsprachig, gesichtslos,
> Blender-3D, Artlist-Stimme. Ersetzt für diesen Kanal die produktbezogenen Annahmen in
> `../strategie/` (die bleiben als Beispiel liegen). Das allgemeine Handwerk in `../wissen/` gilt.

## Das Versprechen

**Inside View zeigt, was man nie sehen kann: das Innere der Dinge im Moment, in dem etwas passiert.**
Jeder Short beantwortet eine Frage, die ohne 3D nicht beantwortbar ist.

## Format

| | |
|---|---|
| Länge | 25–40 s, 9:16, Shorts zuerst; später Zusammenschnitte als Long-Form |
| Look | **Schnittmodell-Ästhetik:** Objekte und Körper werden sauber aufgeschnitten wie im Lehrbuch. Feste Palette (Hintergrund tiefes Blaugrau #1B2430, Haut/Objekt warmes Beige, Hervorhebung Orange #FF8A3D, Sekundär Türkis #3DD6C8). Weiches Studiolicht, leichte Tiefenschärfe, keine Texturen-Flut. Kamera: langsamer Push-in, ein Schnitt pro Beat. |
| Stimme | eine feste Artlist-Stimme, ruhig, neutral-amerikanisch oder britisch; Tempo leicht unter Standard; als KI offengelegt |
| Titel | Frage oder „Why/How X …“, 40–60 Zeichen, ein Emoji am Ende als Emotions-Vorschau |
| Serie | Jeder Short beginnt mit demselben 0,5-s-Marker: Schnittlinie fährt durch das Objekt, Titel-Text erscheint |
| Themen | Körper · Alltagsobjekte · Tiere · Physik · „Was wäre wenn“ (markiert) |

## Die Retention-Leiter, angewandt

- **STOP (0–3 s):** Frame 1 zeigt das Objekt bereits aufgeschnitten, Text-Overlay mit der Frage, Stimme stellt die Frage.
- **HOLD:** ein Beat pro 2–4 s, jeder Beat ein neuer Schnitt oder eine neue Bewegung im Modell; Zahlen sparsam; Captions eingebrannt.
- **ANGLE:** Der Schnittmodell-Look und die „im Moment, in dem es passiert“-Erzählung – nicht „Fakten über X“, sondern „das passiert gerade in X“.
- **BRIDGE:** letzter Satz lädt den ersten neu auf (Loop); Pinned Comment mit Quelle und Verweis auf den nächsten Short.

## Regeln

1. Jede Aussage mit Quelle im Skript und im Pinned Comment. Keine Zahl ohne Beleg.
2. Keine medizinischen Ratschläge; Körperthemen erklären, nicht empfehlen.
3. Fiktion/„Was wäre wenn“ wird im Titel markiert (wie bei Zack D Films).
4. Keine echten Personen, keine fremden Marken/Figuren.
5. KI-Stimme in Beschreibung + Upload-Flag offenlegen.
6. Keine erfundenen Zahlen über Performance; Studio-Daten nach 48 h lesen.

## Kadenz (Start)

3 Shorts pro Woche (Mo, Mi, Sa). Puffer: drei fertige Shorts vor dem ersten Upload. Nach 12 Shorts
Baseline lesen (Viewed vs. Swiped, Ø % gesehen, Engaged Views) und eine Variable ändern.

## Produktionskette

Idee (Bank) → Fakten + Quellen → Zwei-Spalten-Skript mit Blender-Shot-Briefs → Blender-Szenen
(Claude baut per Skript, Mensch prüft) → Render 1080×1920 → Artlist-Stimme → `tools/captions_from_script.py`
→ Schnitt (Stimme, SFX aus Artlist, Captions) → Metadaten → Upload mit Offenlegung → Pinned Comment.

## Ideen-Bank (Start)

| # | Titel (EN) | Thema | Status |
|---|---|---|---|
| 1 | What happens inside your ear when a plane takes off 😮 | Körper | **Skript fertig → IV-01** |
| 2 | Why a cat always lands on its feet 🐈 | Tiere | neu |
| 3 | What a hiccup actually is 🤔 | Körper | neu |
| 4 | How a zipper really works 🤯 | Objekt | neu |
| 5 | What happens inside a battery when it dies 🔋 | Physik | neu |
| 6 | Why bread goes stale 🍞 | Alltag | neu |
| 7 | What a mosquito bite does under your skin 😨 | Körper | neu |
| 8 | How a toilet flushes without a pump 🚽 | Objekt | neu |
| 9 | What happens in your spine when you crack your back 😬 | Körper | neu |
| 10 | Why ice floats 🧊 | Physik | neu |
