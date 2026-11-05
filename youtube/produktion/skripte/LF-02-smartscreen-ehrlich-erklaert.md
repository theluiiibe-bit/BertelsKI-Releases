# LF-02 · „Warum Windows unsere App ‚unbekannt‘ nennt – und wie du sie prüfst“

Säule 2 · Long-Form · Ziel 7–8 Min. · Format: Screen-Recording + Voiceover · NEXT-Ziel von LF-01
⚠️ Fakten-Check: SmartScreen-Dialog im aktuellen Windows-Build nachstellen; Prüfsumme live gegen
`manifest.json` vergleichen; keine Schritte zeigen, die Nutzer zum pauschalen Ignorieren von
Warnungen erziehen.

## 1. PACKAGE

**Versprechen:** Dieses Video zeigt vorsichtigen Windows-Nutzern, warum SmartScreen bei einem
kleinen Entwickler-Installer warnt und wie sie in 60 Sekunden selbst prüfen, dass die Datei echt ist.

| | A (Empfehlung) | B | C |
|---|---|---|---|
| **Titel** | SmartScreen Warnung erklärt: Installer in 60 s selbst prüfen | Windows warnt vor unserer App – zu Recht? Prüfsumme live geprüft | „Unbekannter Herausgeber“: Was die Warnung wirklich bedeutet |
| Zeichen | 58 | 60 | 58 |

**Thumbnail-Brief:** Hero = der echte blaue SmartScreen-Dialog, leicht gedreht, darüber ein
grünes Häkchen-Siegel mit „SHA-256“. Text: „ZU RECHT?“ (2 Wörter). Dunkler Hintergrund, Akzent
Grün. Varianten: A Häkchen · B Lupe auf dem Dialog · C Fragezeichen-Siegel. Kein Gesicht.

## 2. Struktur

| Zeit | Beat | Re-Hook |
|---|---|---|
| 0:00–0:25 | Cold Open: Dialog erscheint. „Das ist richtig so. Und ich zeig dir, wie du *trotzdem* sicher bist – ohne blind auf ‚Trotzdem ausführen‘ zu klicken.“ | – |
| 0:25–1:30 | Was SmartScreen prüft: Reputation + Zertifikat; warum junge Software ohne teures Zertifikat warnt; warum wir es ehrlich sagen statt zu verstecken | „Die Warnung ist kein Virus-Fund – das ist der Punkt, den fast alle verwechseln“ |
| 1:30–3:30 | **Prüfung 1: Prüfsumme.** `certutil -hashfile Meine_KI_Setup.exe SHA256` vs. Manifest auf der offiziellen Seite | Zoom auf die ersten/letzten 6 Zeichen |
| 3:30–5:00 | **Prüfung 2: Signatur.** Was eine Ed25519-Signatur ist (Siegel + öffentlicher Schlüssel), wie der Updater sie prüft, warum die Prüfsumme allein keine Herkunft beweist | „Eine Prüfsumme kann jeder fälschen, der die Datei tauscht – deshalb Schritt zwei“ |
| 5:00–6:15 | **Was wir *nicht* haben:** Authenticode; was es kostet; wann es kommt (⚠️ nur, wenn geplant) | – |
| 6:15–7:00 | Regel für alle Downloads: Quelle, Prüfsumme, Signatur – nie nur „Trotzdem ausführen“ | – |
| 7:00–7:30 | Close + NEXT: Playlist „Sicher installieren & updaten“ → Endscreen auf LF-01 oder #10 | – |

## 3. AV-Skript (Auszug Cold Open)

| Zeit | AUDIO [VO] | BILD |
|---|---|---|
| 0:00 | Du lädst unsere App runter, startest sie ... und Windows sagt: Der Computer wurde geschützt. Unbekannter Herausgeber. | [Screen] echter SmartScreen-Dialog, Vollbild |
| 0:08 | Ehrlich? Das ist richtig so. Windows kennt uns noch nicht. | [Overlay] „Richtig so.“ |
| 0:13 | Aber „Trotzdem ausführen“ zu klicken, weil ein Video es sagt – das wäre falsch. Also prüfen wir die Datei jetzt gemeinsam. Sechzig Sekunden. Zwei Schritte. Danach weißt du es, statt es zu hoffen. | [Overlay] „Schritt 1: Prüfsumme · Schritt 2: Signatur“ |

*(Restliches AV-Skript nach dem Muster von LF-01 ausfüllen; Befehle im Bild immer vollständig
zeigen, auch als Text in der Beschreibung.)*

## 4. VO-Brief (Artlist AI Voiceover · ElevenLabs-Werte optional)

```
ARTLIST:  Katalog → Deutsch → feste Kanalstimme; Tempo leicht unter Standard; 2–3 Takes; WAV laden
          Captions: tools/captions_from_script.py <skript>.vo.txt --audio stimme.wav
VOICE: wie LF-01 (Kanal-Konsistenz) · MODEL: eleven_multilingual_v2 · Stability 0.6 (sachlich)
AUSSPRACHE: „SmartScreen“ englisch · „certutil“ = „zert-ju-til“ · „SHA-256“ = „Scha-zwei-fünf-sechs“
          „Ed25519“ = „Ed-zwei-fünf-fünf-eins-neun“ · „Authenticode“ = „Au-then-ti-kohd“
ETHICS: KI-Stimme offenlegen; Upload-Flag prüfen
```

## 5. Metadaten

**Titel:** SmartScreen Warnung erklärt: Installer in 60 s selbst prüfen
**Beschreibung (oben):**
```
Windows warnt vor unserer App – und das ist richtig. So prüfst du einen Installer selbst, statt
blind auf „Trotzdem ausführen“ zu klicken: SmartScreen Warnung verstehen, SHA-256-Prüfsumme in
60 Sekunden vergleichen, Signatur erklärt.

Befehl aus dem Video:
certutil -hashfile Meine_KI_Setup.exe SHA256
Offizieller Update-Feed mit Prüfsumme + Signatur:
https://theluiiibe-bit.github.io/BertelsKI-Releases/updates/manifest.json

Kapitel
00:00 Die SmartScreen Warnung – richtig so
00:25 Was SmartScreen wirklich prüft
01:30 Prüfsumme in 60 Sekunden vergleichen
03:30 Signatur: warum Prüfsumme allein nicht reicht
05:00 Was wir noch nicht haben (Authenticode)
06:15 Die Regel für jeden Download
07:00 Nächster Schritt
```
**Tags:** `smartscreen warnung`, `unbekannter herausgeber`, `sha256 prüfen windows`, `installer prüfen`, `meine ki`
**Kategorie:** Wissenschaft & Technik · **madeForKids:** false · KI-Stimmen-Hinweis wie LF-01.
