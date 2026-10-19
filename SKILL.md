---
name: writing-pro
description: >-
  Entwickelt, überarbeitet und prüft Texte mit passendem Genre, Zielgruppe,
  Zweck und Stilprofil. Verwenden für professionelle, kreative und fachliche
  Schreibaufgaben; nicht als Ersatz für fachliche oder rechtliche Prüfung.
---

# Writing Pro

Erstelle Texte, die ihren Zweck erfüllen und für ihre Zielgruppe natürlich wirken.

## Arbeitsweise

1. Kläre aus dem Auftrag in je einem Satz: Schreibaufgabe (etwa Information,
   Argumentation, Anleitung, Erzählung, Korrespondenz, Marketing, Redaktion
   oder Fachtext), Zielgruppe, Kommunikationsziel, Kanal, Sprachvariante und
   erforderliche Faktenbasis. Fehlende Entscheidungen nur dann nachfragen, wenn
   sie den Text wesentlich verändern würden.
2. Übernimm ein vorhandenes Stilprofil nur, wenn es für Auftrag oder Person
   bestimmt ist. Ohne Profil schreibe klar, eigenständig und angemessen statt
   einen persönlichen Stil zu erfinden.
3. Richte Ton, Aufbau, Wortwahl, Detailtiefe und Format an Publikum und Medium aus.
   Halte Aussagen nachvollziehbar; kennzeichne Annahmen, Lücken und Unsicherheiten.
4. Überarbeite gegen den Zweck: Verständlichkeit, Konsistenz, Präzision,
   Perspektive, Rhythmus und konkrete Handlungsfähigkeit gehen vor dekorativer
   Sprache.

## Routing

- Für einen persönlichen oder organisationsspezifischen Ton lies nur das
  ausdrücklich gewählte Profil aus dem konsumierenden Workspace. Das Profil
  ist eine konfigurierbare Quelle, keine allgemeine Stilvorgabe.
- Zum Anlegen oder Überarbeiten eines Profils lies
  [`profiles/create-style-profile.md`](profiles/create-style-profile.md) und
  nutze [`profiles/style-profile.template.md`](profiles/style-profile.template.md).
  Ein fiktives, ausgefülltes Beispiel liegt unter
  [`profiles/example/style-profile.md`](profiles/example/style-profile.md).
- Die Sara-Referenz (nach Bootstrap, siehe
  [`references/index.md`](references/index.md)) ist Orientierung für konkrete,
  glaubwürdige Formulierungen, nicht Vorrang vor dem jeweiligen Stilprofil
  oder Auftrag.
- Quellen, Bezug, Bootstrap und Lizenz stehen in
  [`references/index.md`](references/index.md).

## Profilablage und Schutz

Gelebte Stilprofile gehören in den konsumierenden Workspace (dort versioniert,
etwa `<workspace>/profiles/<name>/style-profile.md`). Dieser Skill enthält
absichtlich keine echten Profile, nur Template, Methode und ein fiktives
Beispiel. Für skill-lokale Wiederverwendung gibt es den gitignorierten Overlay
`profiles/local/`; dort abgelegte Dateien werden nie committet. Hinweis: Was
einmal in Git landet und gepusht wird, ist praktisch öffentlich — ein
Repository ist kein Geheimhaltungsmechanismus.
