# BertelsKI – offizielle Windows-Updates

Dies ist der **öffentliche Downloadkanal** für BertelsKI / Meine KI.

Der **Quellcode bleibt privat** im Repository `theluiiibe-bit/BertelsKI`.

## Aktueller Stand

Noch **kein veröffentlichtes Update**. Installationsdateien werden erst nach erfolgreichem Windows-Build, doppelten Tests, Installations-/Startprüfung und Ed25519-signiertem Update-Manifest veröffentlicht.

## Sicherheitsregeln

- Nur `Meine_KI_Setup.exe` und signierte Metadaten werden veröffentlicht.
- Keine Quellcodedateien, privaten Schlüssel, API-Schlüssel, Chats oder lokalen Projektdateien.
- Eine SHA-256-Prüfsumme allein beweist nicht die Herkunft. Der Desktop-Updater muss die Ed25519-Signatur gegen einen separat geprüften öffentlichen Schlüssel verifizieren.
- Vor der Installation muss der Nutzer ausdrücklich zustimmen.
- Es ist **noch keine** Windows-Authenticode-Codesignatur vorhanden.

Der geplante Feed lautet: `https://theluiiibe-bit.github.io/BertelsKI-Releases/updates/manifest.json` (erst nach Aktivierung von GitHub Pages und einer erfolgreichen Veröffentlichung).
