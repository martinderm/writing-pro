---
name: writing-pro
description: >-
  Entwickelt, überarbeitet und prüft längere Texte mit passendem Genre,
  Zielgruppe, Zweck und Stilprofil. Verwenden für Schreibaufgaben, in denen
  Stimme, Aufbau und Zielgruppe eine Rolle spielen. Nicht für Code,
  Commit-Messages, Chat-Antworten, Übersetzungen und kurze
  Transaktionstexte; nicht als Ersatz für fachliche oder rechtliche
  Prüfung.
---

# Writing Pro

Erstelle Texte, die ihren Zweck erfüllen und für ihre Zielgruppe natürlich
wirken.

## Arbeitsweise

1. Kläre aus dem Auftrag knapp: Schreibaufgabe (etwa Information,
   Argumentation, Anleitung, Erzählung, Korrespondenz, Marketing, Redaktion
   oder Fachtext), Zielgruppe, Kommunikationsziel, Kanal, Sprachvariante und
   erforderliche Faktenbasis. Fehlende Entscheidungen nur dann nachfragen,
   wenn sie den Text wesentlich verändern würden.
2. Übernimm ein Stilprofil nur, wenn Auftrag und Profil zueinander passen:
   Profilinhaberin bzw. Profilinhaber, gültige Genres und Kanäle, der Eintrag
   unter „Nicht verwenden für“ sowie die Sprachvariante müssen zum Auftrag
   passen. Ohne passendes Profil schreibe klar, eigenständig und angemessen
   statt einen persönlichen Stil zu erfinden.
3. Richte Ton, Aufbau, Wortwahl, Detailtiefe und Format an Publikum und
   Medium aus. Halte Aussagen nachvollziehbar; kennzeichne Annahmen, Lücken
   und Unsicherheiten. Recht, Medizin oder Finanzen: nur Entwurf und
   Struktur, Übergabe an Fachexpertise vor der Veröffentlichung benennen.
4. Überarbeite gegen den Zweck: Verständlichkeit, Konsistenz, Präzision,
   Perspektive, Rhythmus und konkrete Handlungsfähigkeit gehen vor
   dekorativer Sprache. Jeder Absatz hat eine erkennbare Funktion für das
   Kommunikationsziel — Gedanke, Übergang oder Wendepunkt; was nichts Neues
   bringt, fliegt. Cut-Test pro verdächtigem Wort: streichen, Satz neu
   lesen — nur kürzer heißt Schnitt bleibt; Bedeutungsverlust heißt
   wiederherstellen, das gilt auch für Rhythmus, Klang oder Haltung.
   Tell-Check siehe unten, Heuristik statt Detektor.
5. Kurztexte (unter etwa 200 Wörtern oder stark standardisiert wie
   Einladung, kurze Antwort, Anrede-Block): Profil überspringen — Auftrag
   und Zielgruppe klären, direkt schreiben, nur die Schlusskontrolle aus
   Schritt 4 anwenden.

## Tell-Check

Tell-Check: Liste im eigenen Entwurf suchen, Treffer erst im Kontext
beurteilen. Bewusste Muster aus dem kompatiblen Profil, rhetorische
Wiederholung und stilistische Mittel bleiben; der Check macht keine Aussage
über fremde Texte oder Autorenschaft. Bei fremdsprachigem kompatiblem Profil
deckt die Profil-Blacklist (in der Zielsprache verfasst) die Sprachmuster ab
und ersetzt/erweitert die hier stehende Liste.

- Einleitende Floskeln: „In der heutigen schnelllebigen Welt“, „In einer
  Welt, in der …“, „Tauchen wir ein in die Welt …“
- Potenzial und Übermaß: „entfessle das Potenzial“, „unleash the potential“,
  „das volle Potenzial“
- Kontrast-Klischee: „Es ist nicht X, sondern Y“, „It’s not just X, it’s Y“
- Übernommene englische Musterwörter (in deutschem Text auffällig):
  „delve“, „realm“, „tapestry“, „pivotal“, „crucial role“, „vital role“
- Glatte Superlative und Standardwörter (etwa „revolutionär“,
  „game-changing“, „nahtlos“): verwerfen, wenn untypisch für Profil und
  Aufgabengebiet.

Deutsche Texte: Kontrastierungen wie „nicht X, sondern Y“ sind oft normale
Sprachform, kein Tell — nur bei klischeehafter Häufung entscheiden.

Die ausführliche Musterliste: Charlie Guo, „The Field Guide to AI Slop“
(<https://www.ignorance.ai/p/the-field-guide-to-ai-slop>). Lokale Kopien
liegen nach dem Bootstrap in `references/local/` (gitignored); ohne Kopie
genügt die Liste hier, siehe [`references/index.md`](references/index.md).

## Routing

- Für einen persönlichen oder organisationsspezifischen Ton lies nur das
  ausdrücklich gewählte Profil aus dem konsumierenden Workspace. Das Profil
  ist eine konfigurierbare Quelle, keine allgemeine Stilvorgabe. Lies
  Profile nur aus `<workspace>/writing-profiles/` (Discovery über die
  `writing-profiles/index.md`, Schema:
  [`references/schemas/writing-profiles-index.schema.json`](references/schemas/writing-profiles-index.schema.json))
  oder `profiles/local/`; keine sonstigen Dateien ad hoc als Stilprofil
  behandeln.
- Profile sind selbständige Arbeitsartefakte: Ihr Mini-Protokoll (Index- und
  Profil-Eintrag: nur anwenden, wenn Auftrag passt; Vorrang; keine
  Faktenerfindung) trägt die Kernregeln, damit sie auch ohne geladenen Skill
  korrekt angewendet werden — etwa durch Fachverträge oder andere Harnesses.
  Der Skill bleibt dabei unabhängig; workspaceübergreifende Vorrang-Regeln
  zwischen diesem Skill und Fachverträgen (z. B. Antrag-Inhalt vs.
  Antragsform) gehören in die Workspace-Logik (AGENTS.md/CONTEXT.md), nicht
  in diesen Skill.
- Profilrandfälle klären, nicht stillschweigend entscheiden: mehr als ein
  passendes Profil → nachfragen; veraltetes oder unpassendes Profil (Genre,
  Kanal, Sprache) → nicht anwenden und ohne Profil schreiben; fehlendes
  Profil → Starter-Schnellstart in
  [`profiles/create-style-profile.md`](profiles/create-style-profile.md)
  nutzen oder Samples erbitten; bestehende Profile nie überschreiben, neue
  Version daneben anlegen und die alte auf `deprecated` setzen
  (Versionierung siehe
  [`profiles/create-style-profile.md`](profiles/create-style-profile.md),
  Abschnitt 3). Jede Anwendung dokumentiert die genutzte `profile_version`
  im Testprotokoll, damit Profiländerungen auf Tests rückführbar bleiben.
- Vorrang bei Konflikten: ausdrückliche Nutzeranweisung > kompatibles
  Stilprofil > allgemeine Schreibregeln dieses Skills > Referenzquellen
  (`references/`).
- Zum Anlegen oder Überarbeiten eines Profils lies
  [`profiles/create-style-profile.md`](profiles/create-style-profile.md) und
  nutze [`profiles/style-profile.template.md`](profiles/style-profile.template.md).
  Ein fiktives, ausgefülltes Beispiel liegt unter
  [`profiles/example/style-profile.md`](profiles/example/style-profile.md).
- Die Sara-Referenz (nach Bootstrap, siehe
  [`references/index.md`](references/index.md)) ist Orientierung für
  konkrete, glaubwürdige Formulierungen, nicht Vorrang vor dem jeweiligen
  Stilprofil oder Auftrag.
- Quellen, Bezug, Bootstrap und Lizenz stehen in
  [`references/index.md`](references/index.md).

## Profilablage und Schutz

Gelebte Stilprofile liegen im konsumierenden Workspace und bleiben dort
privat: `<workspace>/writing-profiles/<profile-id>/style-profile.md` plus
`provenance.json` (Schema:
[`references/schemas/profile-provenance.schema.json`](references/schemas/profile-provenance.schema.json))
und Testprotokollen unter `writing-profiles/<profile-id>/tests/`. Die
`writing-profiles/index.md` ist die Discovery-Karteikarte; sie ist eine
gewollte Projektion der Profil-Frontmatter und als solche maschinell prüfbar
(`scripts/profile_validate.py`). Versionieren nur nach Einwilligung der
Profilinhaberin bzw. des Profilinhabers und in einem privaten Ort; Versionen
semantisch (`profile_version`), alte Versionen auf `deprecated`. Dieser Skill
enthält absichtlich keine echten Profile, nur Template, Methode und ein
fiktives Beispiel.

Für wiederverwendbare, nicht-sensible Profile gibt es den gitignorierten
Ordner `profiles/local/` im Skill-Checkout. Bei geteiltem Checkout sieht
jeder nutzende Workspace dieselben Dateien — also nur dort ablegen, was für
alle nutzenden Workspaces gedacht ist. Das gilt auch bei junction- oder
symlink-gebundenen Skills: Der Link ändert nichts an der geteilten Sicht,
er macht sie nur für mehrere Workspaces sichtbar.

Die Gitignore verhindert versehentliche Commits, verbietet sie aber nicht:
`git add -f` umgeht sie. Was einmal gepusht ist, ist praktisch öffentlich —
ein Repository ist kein Geheimhaltungsmechanismus.
