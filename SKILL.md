---
name: writing-pro
description: >-
  Entwickelt, überarbeitet und prüft Texte mit passendem Genre, Zielgruppe,
  Zweck und Stilprofil. Verwenden für professionelle, kreative und fachliche
  Schreibaufgaben; nicht als Ersatz für fachliche oder rechtliche Prüfung.
---

# Writing Pro

Erstelle Texte, die ihren Zweck erfüllen und für ihre Zielgruppe natürlich wirken.
Kläre oder leite aus dem Auftrag zunächst Genre, Zielgruppe, Kommunikationsziel,
Kanal, Sprachvariante und erforderliche Faktenbasis ab. Fehlende Entscheidungen nur
dann nachfragen, wenn sie den Text wesentlich verändern würden.

## Arbeitsweise

1. Bestimme die passende Schreibaufgabe: etwa Information, Argumentation,
   Anleitung, Erzählung, Korrespondenz, Marketing, Redaktion oder Fachtext.
2. Übernimm ein vorhandenes Stilprofil nur, wenn es für Auftrag oder Person
   bestimmt ist. Ohne Profil schreibe klar, eigenständig und angemessen statt
   einen persönlichen Stil zu erfinden.
3. Richte Ton, Aufbau, Wortwahl, Detailtiefe und Format an Publikum und Medium aus.
   Halte Aussagen nachvollziehbar; kennzeichne Annahmen, Lücken und Unsicherheiten.
4. Überarbeite gegen den Zweck: Verständlichkeit, Konsistenz, Präzision,
   Perspektive, Rhythmus und konkrete Handlungsfähigkeit gehen vor dekorativer
   Sprache.

## Routing

- Für genre- oder kanalspezifische Entscheidungen lies die passende Datei in
  [`references/genres/`](references/genres/).
- Für einen persönlichen oder organisationsspezifischen Ton lies nur das
  ausdrücklich gewählte Profil in [`profiles/`](profiles/). Das Profil ist eine
  konfigurierbare Quelle, keine allgemeine Stilvorgabe.
- Die vorhandene PDF-Referenz liegt unter
  [`references/sara-in-wondertech-how-to-teach-ai-to-write-like-you-anti-slop-writing-guide.pdf`](references/sara-in-wondertech-how-to-teach-ai-to-write-like-you-anti-slop-writing-guide.pdf).
  Die durchsuchbare Markdown-Fassung liegt unter
  [`references/sara-in-wondertech-how-to-teach-ai-to-write-like-you-anti-slop-writing-guide.md`](references/sara-in-wondertech-how-to-teach-ai-to-write-like-you-anti-slop-writing-guide.md).
  Sie ist Orientierung für konkrete, glaubwürdige Formulierungen, nicht Vorrang
  vor dem jeweiligen Stilprofil oder Auftrag.
- Quellen, Herausgeberinnen und Web-URLs stehen in
  [`references/index.md`](references/index.md).

## Profil- und Veröffentlichungsgrenze

Profile bleiben versioniert, damit ihre Entwicklung nachvollziehbar ist. Sie werden
nicht über `.gitignore` ausgeblendet. Für Veröffentlichungsarchive schließt
`.gitattributes` den Ordner `profiles/` aus; prüfe vor jeder Veröffentlichung,
dass das gewählte Verfahren keine Profilquellen übernimmt. Ein öffentliches
Repository selbst ist kein geeignetes Mittel, um Profile geheim zu halten.
