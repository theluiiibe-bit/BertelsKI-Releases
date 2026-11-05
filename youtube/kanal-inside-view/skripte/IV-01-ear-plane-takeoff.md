# IV-01 · What happens inside your ear when a plane takes off 😮

Kanal Inside View · Short · Ziel 40–45 s · 9:16 · Blender-Schnittmodell + Artlist-Stimme (offengelegt)

## Fakten und Quellen (vor dem Bau geprüft)

| Aussage im Video | Beleg |
|---|---|
| Die Kabine wird nicht auf Meereshöhe gehalten, sondern auf einen Druck, der etwa 1.800–2.400 m Höhe entspricht. | FAA, Aerospace Medicine: cabin altitude typically 6,000–8,000 ft |
| Hinter dem Trommelfell liegt das luftgefüllte Mittelohr; sein einziger Ausgleichsweg ist die Eustachische Röhre zum Rachen. | Standard-Anatomie (z. B. Gray's Anatomy; NIH/NIDCD) |
| Beim Steigflug sinkt der Kabinendruck; die Luft im Mittelohr hat dann den höheren Druck und drückt das Trommelfell leicht nach außen. | NIDCD / Mayo Clinic „Airplane ear“ |
| Die Röhre öffnet sich meist von selbst und lässt Luft entweichen – das ist das „Plopp“. Schlucken und Gähnen spannen einen Gaumenmuskel an, der sie aktiv öffnet. | Mayo Clinic; Physiologie (Tensor veli palatini) |
| Beim Sinkflug ist es umgekehrt: Außendruck steigt, Trommelfell wird nach innen gedrückt, die Röhre öffnet schwerer – deshalb tut der Sinkflug öfter weh. | Mayo Clinic „Airplane ear“ |

⚠️ Vor dem Upload: Quellen-Links im Pinned Comment ausschreiben; keine Zahl ohne Link.

## Zwei-Spalten-Skript mit Blender-Shot-Briefs

| Zeit | AUDIO [VO, englisch] | BILD [Blender-Shot-Brief] | ON-SCREEN |
|---|---|---|---|
| 0:00 | *Your ears pop on takeoff. Here's what's actually happening inside.* | **Shot 1 – Serien-Marker + Hook.** Kopf von der Seite, halbtransparent; eine Schnittlinie fährt in 0,5 s von oben durch das Ohr, die vordere Hälfte klappt weg und gibt den Schnitt durch Außenohr, Trommelfell, Mittelohr, Röhre frei. Kamera: leichter Push-in auf das Mittelohr. Palette: Haut Beige, Mittelohr-Luft Türkis leuchtend, Trommelfell Orange. | „Why your ears POP on takeoff“ |
| 0:04 | *Behind your eardrum is a tiny pocket of air. Sealed. Its only exit is a narrow tube down to your throat.* | **Shot 2.** Push-in auf das Mittelohr; die Luftkammer pulsiert kurz türkis; die Eustachische Röhre wird als dünner Schlauch nach unten zum Rachen nachgezeichnet (Linie wächst in 1 s). | „sealed air pocket“ · „tube to your throat“ |
| 0:10 | *As the plane climbs, the cabin pressure drops. Not to sea level — the cabin is kept like you're standing on a 2,000-metre mountain.* | **Shot 3.** Schnitt nach außen: Flugzeug-Silhouette steigt links im Bild; rechts ein Druck-Balken „CABIN“, der sinkt. Kurz, 3 s. | „cabin ≈ 2,000 m altitude“ |
| 0:15 | *So now the air trapped in your ear is pushing harder than the air outside. It bulges your eardrum outward.* | **Shot 4.** Zurück zum Schnitt; Pfeile (orange) drücken von innen gegen das Trommelfell; Trommelfell wölbt sich sichtbar nach außen (Shape Key 0 → 1 in 1,5 s). Leichter Zoom. | „pressure inside > outside“ |
| 0:21 | *Then the tube opens for a split second. Air escapes. That's the pop.* | **Shot 5 – Payoff.** Die Röhre weitet sich kurz, türkise Luftpartikel strömen nach unten in den Rachen, Trommelfell schnappt zurück in Ruhelage. SFX: dezentes „pop“ (Artlist SFX). Kamera-Shake minimal. | „POP“ (0,4 s groß) |
| 0:25 | *Swallowing or yawning pulls a small muscle in your palate that forces that tube open. That's why it works.* | **Shot 6.** Unten im Schnitt: Gaumenmuskel zieht (kurze Kontraktion, orange Highlight), Röhre öffnet sich erneut, Partikel fließen. | „swallow · yawn“ |
| 0:29 | *Landing is the reverse — and that's the one that hurts.* | **Shot 7 – Loop.** Flugzeug sinkt; Trommelfell wölbt sich nach innen; Bild friert kurz, Schnittlinie fährt zurück → Frame 1. | „landing: next video“ |

Laufzeit: 119 Wörter ≈ 42 s bei ~165 W/Min. (englisch, ruhig). Die Zeitmarken oben sind Richtwerte für 32 s; die
echte Artlist-Aufnahme setzt die Schnittzeiten. Jeder Beat ≤ 7 s, Bildwechsel alle 2–4 s. Wird es länger als 45 s,
Streiche zuerst den Kabinen-Vergleich (Shot 3), nie den Payoff.

## Blender-Bau (Reihenfolge)

1. Grundszene: Kamera 1080×1920, 30 fps, Eevee Next, Studio-HDRI weich, Hintergrund #1B2430.
2. Kopf: Low-Poly-Basismesh (eigenes oder CC0), Boolean-Schnitt mit Ebene; Schnittfläche als eigenes Material (helles Beige, leichte Kontur).
3. Ohr-Anatomie stilisiert: Gehörgang (Zylinder), Trommelfell (Scheibe mit Shape Key „bulge_out“ und „bulge_in“), Mittelohr-Kammer (Hohlraum, Volumen-Material türkis, Emission 0,3), Eustachische Röhre (Kurve mit Bevel, Radius-Keyframes für „öffnen“), Rachen (einfache Röhre).
4. Partikel: Luftströmung als kleine Kugeln entlang der Kurve (Partikelsystem oder Geometry Nodes „Curve to Points“ + Offset-Animation).
5. Pfeile: Instanzen eines Pfeil-Meshes, orange Emission, Keyframes Scale 0 → 1.
6. Overlays/Text: im Schnitt, nicht in Blender (Caption-Zone unten 22 % freihalten).
7. Render: Eevee, 32 Samples, Motion Blur aus, PNG-Sequenz → ffmpeg H.264.

## Sprechtext (fürs Ohr, Artlist)

`IV-01.vo.txt` – Stimme ruhig, leicht unter Standardtempo, Pausen an den „...“.

## Metadaten

**Titel:** What happens inside your ear when a plane takes off 😮
**Beschreibung:**
```
Your ears pop on takeoff — here's what's actually happening inside your ear, cut open in 3D.
The sealed air pocket behind your eardrum, the tube to your throat, and the split second the pop happens.

Inside View shows what you can't see: the inside of things, in the moment something happens.

Sources: Mayo Clinic (Airplane ear), NIDCD, FAA cabin altitude guidance — links in the pinned comment.
Narration is an AI voice (Artlist), disclosed. Animation made in Blender.
#insideview #ear #airplane #3danimation #science
```
**Tags:** `what happens inside your ear`, `why do ears pop on a plane`, `airplane ear`, `3d animation`, `inside view`
**Kategorie:** Science & Technology · **madeForKids:** false · Upload-Flag „altered or synthetic“: ja (KI-Stimme).
**Pinned Comment:** Quellen-Links + „Landing is worse — that's the next one.“

## Qualitäts-Tor vor Upload

```
[ ] Frame 1 zeigt den Schnitt und die Frage, funktioniert stumm
[ ] jeder Beat ≤ 6 s, neuer Bildreiz alle 2–4 s
[ ] Loop: letzter Frame führt zu Frame 1
[ ] alle fünf Fakten mit Link im Pinned Comment
[ ] Captions eingebrannt, 2 Zeilen, Zone unten frei
[ ] KI-Stimme offengelegt; Blender-Look konsistent mit Konzept-Palette
```
