# Vertonung mit KI-Voiceover – VOICE

> Quelle: Skill `ai-voiceover` (ElevenLabs-Referenz 2026) + Live-Recherche 05.11.2026.
> Preise/Modell-IDs **vor dem Bauen gegen elevenlabs.io prüfen**.

## Die These: 80 % Skript + Regie, 20 % Tool

KI-Stimmen klingen roboterhaft, weil man ihnen **Augen-Text** füttert (Blog-Absätze, Stichpunkte)
und den **Default-Read** akzeptiert. Eine gute Vertonung ist fast ganz Skript-fürs-Ohr plus Regie.
Und: Social läuft **stumm** – die Stimme stützt die Captions, sie trägt das Video nicht allein.

## Das Framework

| | Schritt | Konkret |
|---|---|---|
| **V** | Voice match | Library-Stimme, Voice Design per Prompt oder **eigener** Klon (IVC ab 1–2 Min. sauberem Audio, PVC für Studio-Qualität). Muss zur geschriebenen Markenstimme passen. |
| **O** | Own the script for the ear | gesprochener Rhythmus, Kontraktionen („gibt's“, „hab ich“), kurze Sätze, ein Gedanke pro Atemzug, Punkt vorne. **Laut vorlesen** – wo du stolperst, stolpert das Modell. |
| **I** | Inflect & direct | Modell nach Job; Audio-Tags sparsam; Stabilität 0,3–0,5 (expressiv) vs. 0,7–1,0 (konstant); Similarity 0,75–0,85; Aussprache-Notizen für Namen/Fachwörter. 2–3 Takes, schwache Zeilen einzeln neu rendern. |
| **C** | Caption alongside | eingebrannte Untertitel planen; Bild muss stumm verständlich sein. Lokalisierung per Dubbing (70+ Sprachen, Qualität je Sprache prüfen). |
| **E** | Ethics | nur **eingewilligte** Stimmen (eigene, Library, designte, lizenzierte). Nie fremde Personen klonen. **Offenlegen** (EU AI Act, YouTube „veränderter Inhalt“, Pflicht in Werbung). |

## Dein Setup: Artlist (primär) – ElevenLabs optional

Du arbeitest mit **Artlist** (Max-Plan). Das deckt für den Kanal vier Dinge ab, alle unter einer
kommerziellen Lizenz, die YouTube-Monetarisierung einschließt (Lizenzumfang im Konto prüfen):

| Bedarf | Artlist-Baustein | Hinweis |
|---|---|---|
| Sprecherstimme | **AI Voiceover** (Text-to-Speech, Speech-to-Speech, Voice Cloning der eigenen Stimme) | Katalog nach Sprache *Deutsch* filtern; Stimme einmal wählen und für alle Videos behalten (Wiedererkennung). Speech-to-Speech = du sprichst, Artlist ersetzt die Stimme – beste Betonung. |
| Musik | Music-Katalog | leise, ohne Gesang, unter Sprache −18 bis −24 dB; bei Shorts am Loop-Punkt schneiden |
| Soundeffekte | SFX-Katalog | Klick/Whoosh bei Overlays, dezent; kein Dauer-Feuerwerk |
| B-Roll | Footage-Katalog | nur für abstrakte Zwischenschnitte (Server, Büro, Hände); Produkt immer als echtes Screen-Recording |

**Workflow mit Artlist-Voiceover:**
1. `*.vo.txt` fürs Ohr schreiben (Regeln unten), laut lesen.
2. Text in Artlist AI Voiceover einfügen, Stimme wählen, Tempo etwas unter Standard, 2–3 Takes
   erzeugen, besten herunterladen (WAV, wenn angeboten).
3. Untertitel: `../tools/captions_from_script.py skript.vo.txt --audio stimme.wav` → SRT mit
   proportionalem Timing; in der Schnittsoftware am Wellenbild feinjustieren.
4. `../tools/build_video.py` oder dein Editor mischt Stimme + Bild + SRT.
5. Offenlegung: „Sprecherstimme KI-generiert (Artlist, lizenziert)“ in die Beschreibung;
   Upload-Flag „veränderter/synthetischer Inhalt“ prüfen.

Artlist-Regel aus den Nutzungsbedingungen: Stimmen und Assets des Generators dürfen nicht zum
Trainieren oder Klonen anderer Modelle verwendet werden. Nur die eigene Stimme klonen.

**ElevenLabs** bleibt die Option, wenn du Wort-genaue Zeitstempel per API willst
(`../tools/voiceover.py`) oder Audio-Tags für sehr expressive Reads brauchst. Alles Folgende zu
Modellen und Reglern gilt für ElevenLabs; die Prinzipien (Skript fürs Ohr, Regie, Offenlegung)
gelten für beide.

## Modelle nach Job – ElevenLabs (verify-quarterly)

| Job | Modell (ID) | Warum |
|---|---|---|
| Short / Reel, expressiv | Eleven v3 (`eleven_v3`) | Audio-Tags wie `[warm]`, `[flüstert]`, Energie; 70+ Sprachen; seit 02/2026 GA |
| Erklärvideo / Tutorial / lang | Multilingual v2 (`eleven_multilingual_v2`) | stabilste Qualität über lange Passagen, 29+ Sprachen |
| Entwurf / Test / Echtzeit | Flash v2.5 (`eleven_flash_v2_5`) | ~halbe Credits, ~75 ms Latenz |
| Fremdsprachige Versionen | Dubbing | eigene Stimme bleibt erhalten |

Faustregel: **Entwurf auf Flash, Final auf v3 oder Multilingual v2.**

Credits: 1 Zeichen = 1 Credit (v2/v3), Flash ~0,5. Free (~10k Zeichen) hat **keine kommerzielle
Lizenz** und verlangt Attribution – für monetarisierte Videos mindestens Starter (IVC) oder
Creator (PVC, 192 kbps). API-Listenpreis ~0,10 $/1k Zeichen (v2/v3), Promo-Preise laufen laut
Drittquellen am 09.11.2026 aus – prüfen.

## Deutsch fürs Ohr schreiben – Regeln

1. Sätze unter 14 Wörtern. Nebensätze auflösen.
2. Zahlen ausschreiben, wie man sie sagt („rund achtzehn Megabyte“, nicht „18,6 MB“).
3. Abkürzungen ausschreiben oder phonetisch notieren: „Ed-two-five-five-one-nine“ ist nutzlos;
   sage „Ed-25519-Signatur“ nur, wenn die Zielgruppe es kennt, sonst „kryptografische Signatur“.
4. Englische Produktnamen mit Aussprache-Notiz: *Ollama* → „O-lama“, *GitHub* → „Git-Hab“.
5. Keine Klammern, keine Aufzählungszeichen, kein Fettdruck – das Modell sieht sie nicht.
6. Eine Pause ist `...` oder ein Absatz, kein Komma-Stakkato.
7. Jeden Satz **laut lesen**, bevor er ins Tool geht.

## Der VO-Brief (für jedes Video ausfüllen)

```
VOICE:     Library | designt | eigener Klon – Charakter + warum er zur Marke passt
MODEL:     eleven_v3 (expressiv) | eleven_multilingual_v2 (final, lang) | eleven_flash_v2_5 (Entwurf)
SCRIPT:    fürs Ohr; Tags sparsam; Aussprache-Notizen
SETTINGS:  Stability / Similarity
CAPTIONS:  eingebrannt, 2 Zeilen, 32–42 Zeichen; Sprachen (Dubbing)
ETHICS:    Einwilligung bestätigt; Offenlegung geplant („KI-Stimme“ in Beschreibung + Upload-Flag)
```

## Werkzeuge im Repo

`../tools/captions_from_script.py` baut aus Skript + Artlist-Audio die SRT-Datei (Timing proportional, in der Schnittsoftware nachziehen).

`../tools/voiceover.py` (optional, ElevenLabs) ruft die ElevenLabs-REST-API auf (`ELEVENLABS_API_KEY` als Umgebungsvariable,
nie im Repo), erzeugt MP3 **und** eine SRT-Datei aus den Zeichen-Timestamps – damit die Captions
exakt zur Stimme sitzen. Die Audiodatei wird dann mit `../tools/build_video.py` zu einem Video
gemischt. ElevenLabs generiert nur Audio; mischen, schneiden und prüfen bleibt bei dir.

## Niemals

Fremde Stimmen klonen · Promi-Soundalikes kommerziell · KI-Stimme in Werbung ohne Hinweis ·
Free-Tier-Audio in monetarisierten Videos · Zahlen über Performance erfinden.
