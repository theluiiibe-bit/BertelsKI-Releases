# Trends finden, Virales zerlegen, Ideen-System

> Quelle: Skills `trend-jacking`, `viral-reverse-engineering`, `idea-generation-and-ideation`.
> Ehrliche Grenze: **Kein Modell weiß, was gerade trendet.** Trends sind Echtzeit. Die KI
> bewertet und setzt um; die Entdeckung kommt aus Live-Quellen (siehe `../tools/trend_radar.py`).

## 1. Trend-Jacking: drei Tore, in dieser Reihenfolge

| Tor | Frage | Fail = nicht machen |
|---|---|---|
| **1 FIT** | Kann ich einen echten Blickwinkel beisteuern, oder klebe ich nur mein Logo auf fremden Moment? | einziger Grund ist „ist populär“; ich müsste den Trend verbiegen |
| **2 SAFETY** | Wirkt eine Marke hier opportunistisch, taktlos, ausbeuterisch? | Tragödien, Krisen, Todesfälle; politisch/gesellschaftlich spaltende Momente für Reichweite; Spott nach unten; harmlose Herkunft unklar |
| **3 TIMING** | Steigt der Trend noch (emerging → rising → peak → saturated → dead)? | gesättigt/tot – spät wirkt abgehängt |

Ein Fail reicht. Fit und Safety **vor** Timing prüfen: ein schneller Post auf unpassendem Trend
ist nur ein schneller Fehler. Der Remix nimmt **Struktur/Format** des Trends und füllt sie mit der
**eigenen Nischen-Wahrheit** – keine Logo-Kopie, kein erzwungener Jugendslang. Trends sind
~20–30 % des Mix (reaktive Slots im Kalender), nie die Identität.

### Trend-Typen und wo man sie findet

- **Formate/Memes/Templates** – markenfreundlichster Typ; Struktur übernehmen, Nische einfüllen.
- **Themen/Hashtags** – eigene Meinung dazu, nicht nur taggen.
- **News / Produkt-Launches in der eigenen Nische** (z. B. neues lokales Modell, Windows-Update,
  Datenschutz-Urteil) – höchste Reichweite, höchstes Risiko, SAFETY-Tor am strengsten.
- **Plattform-Features** – frühe Nutzung wird belohnt.
- **Saisonal / planbar** – gehört in den Kalender statt in die Reaktion.

Live-Quellen (Reihenfolge nach Nutzen für diese Nische): eigener YouTube-Feed und Abo-Kanäle ·
YouTube-Suche mit Filter „diese Woche“ · Google Trends (DE) · Reddit (r/LocalLLaMA, r/de_EDV,
r/ollama) · Hacker News · Release-Notes von Ollama/LM Studio/Windows · Heise/Golem/t3n · Trend-
Newsletter. **Der Vorteil liegt darin, in der eigenen Ecke früh zu sein**, nicht plattformweite
Mega-Trends zu jagen.

## 2. Virales rückwärts zerlegen: Mechanismus statt Oberfläche

Die meisten „lerne vom Viralen“-Versuche floppen, weil die **Oberfläche** kopiert wird (Sound,
Thema, Format) statt des **Mechanismus** (tragender Hook, emotionaler Auslöser, Teil-Trigger).

Ablauf:
1. **Material beschaffen** – Transkript (siehe Skill `youtube-transcriber`, braucht Browser),
   Screenshots, Top-Kommentare, sichtbare Zahlen, Kanalgröße. Nichts erfinden, Lücken benennen.
   Ein virales Video ist eine Anekdote; **Muster brauchen mehrere Beispiele.**
2. **Schichten zerlegen** – Hook · emotionaler/Teil-Treiber · Retention-Struktur · Format/
   Packaging · Thema/Angle · Teil-Trigger · Verteilungsfaktoren. Eine Zeile pro Schicht.
3. **Kontrafaktisch testen** – „Nimm X weg – knallt es noch?“ Was nicht wegfallen kann, ist
   **Treiber** (meist 1–2: Hook + Emotion). Rest ist Beiwerk.
4. **Teil-Trigger benennen** – Identität („das bin ich“), hohe Erregung (Staunen, Ärger, Humor,
   Inspiration), soziale Währung, praktischer Nutzen, Relatability, Story. Top-Kommentare sind der
   beste Beleg. Ohne Teil-Trigger: Views, aber keine Viralität.
5. **Replizierbarkeit prüfen** – Kanalgröße, Glück, Einmal-Moment, Survivorship-Bias, kleine
   Stichprobe. Wenn der Erfolg vor allem Confound ist: **als nicht replizierbar markieren**, keine
   falsche Formel ableiten.
6. **Prinzip extrahieren und auf die eigene Nische anwenden** – „Der Hebel ist X; hier ist X für
   uns.“ Nie eine Kopie. Swipe-File wiederkehrender Muster aufbauen.

## 3. Ideen-System SPARK: echte Signale rein, KI als Multiplikator

74 % der Marketer nutzen KI für Ideenfindung, 71 % klagen über generische Ergebnisse – weil
Modelle **Konsens-Maschinen** sind: „Gib mir 10 Ideen zu X“ liefert allen dieselbe Mittelwert-Liste.
Die Umkehr: **echte Daten für Entdeckung, KI für Ausbau.**

| | Schritt |
|---|---|
| **S – Stock** | Input-Diät: zuerst Publikums-Signale (Kommentare, DMs, FAQs, Support-Fragen zu Meine KI, Umfragen) in Themen geclustert: Verwirrung / Einwände / Wünsche. Dann Nischen-Communities, Wettbewerber-Muster **und Lücken** (nie umformulieren), Suchnachfrage, fachfremde Lektüre. **Proprietäre Inputs sind der Burggraben.** |
| **P – Produce** | reibungslose Erfassung (ein Tool, Sekunden); KI erweitert **konkrete echte Signale** in angewinkelte Varianten; Denken und Machen trennen (wöchentlicher Ideen-Block, Produktionstage produzieren nur). |
| **A – Angle** | Matrix Säule × Format × Blickwinkel; POV-Filter: „Könnte ein Wettbewerber das posten? Dann ist es noch nicht unseres.“ Trends timen Säulen, ersetzen sie nicht. |
| **R – Rank + bank** | Score: Säulen-Fit + Publikums-Beleg + Ziel + Aufwand; Bank mit 100+ Ideen (3–5 Säulen × 20–30); wöchentlich sichten, monatlich ausmisten, quartalsweise Säulen prüfen. |
| **K – Kick-test** | teure Ideen erst billig testen: Community-Post/Umfrage → Short → Long-Form → Serie. Stille = neu anwinkeln, nicht zwingend töten. |

Der Erweiterungs-Prompt (Muster): *„Hier sind N echte Zuschauer-Signale dieser Woche: [geclusterte
Kommentare]. Schlage je Thema 3 Video-Ideen vor, die Saves oder Shares für [Zielgruppe] verdienen,
in [Markenstimme], je einer Säule und einem Format zugeordnet.“* Niemals das nackte „10 Ideen zu X“.

Ideen-Karte: Idee · Quell-Signal (echt, verlinkt) · Säule · Segment · Format(e) · Aufwand S/M/L ·
Nachfrage-Beleg (keiner / einmal gefragt / wiederholt gefragt) · Status (neu / getestet / geplant / geparkt).

Niemals: am Produktionstag ideieren · generische KI-Listen · Wettbewerber umformulieren ·
Publikumsfragen erfinden · Dringlichkeit fabrizieren · 200 ungescorte Ideen horten · teure Ideen
ohne Probe freigeben · Testergebnisse erfinden.
