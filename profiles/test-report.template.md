---
type: writing-profile-test-report
profile_id: <kebab-case-id>
profile_version: <x.y.z>
tested_at: <YYYY-MM-DD>
assignment_genre: <kebab-case-genre>
language_variants: [<z. B. en-GB>]
outcome: passed | passed-with-changes | failed
---

# Testprotokoll: [Profil-ID] am [Auftrag, Datum]

## Auftrag und Kontext

- Schreibaufgabe, Genre, Zielgruppe, Kanal:
- Warum passt das Profil (Inhaber, Genres, Sprachvariante):
- Verwendete Profil-Quellen (nur das kompatible Profil):

## Frozen Draft

Der Entwurf wird vor der Prüfung eingefroren und nicht mehr angepasst. Entweder
hier vollständig einfügen oder auf die archivierte Datei verweisen:

- Entwurf: <Pfad oder eingefügter Text>

## Prüfdurchgang (Belegmarken)

Jede kritische Stelle mit Zitat und Fundstelle; Blacklist-Treffer einzeln
listen. Heuristik, kein Detektor: Treffer erst im Kontext beurteilen.

| # | Stelle (Zitat) | Befund | Profilregel / Blacklist-Treffer |
| --- | --- | --- | --- |
| 1 | … | … | … |

## Edit-Plan

Der kurze Plan aus dem Prüfdurchgang — welche Stellen, welche Änderung, warum.
Genau **ein** Rewrite folgt diesem Plan; kein zweiter Durchlauf.

1. …

## Differenz-Log (Entwurf ↔ Korrektur)

Die Kern-Evidenz für die nächste Profilversion. Jede Änderung, die die
Profilinhaberin bzw. der Profilinhaber selbst vornahm, gilt als bestätigt;
Änderungen, die die KI vornahm, werden als **unbestätigt** markiert.

| # | Vorher (Frozen Draft) | Nachher | Wer geändert hat (Profilinhaber / KI, unbestätigt) | Regel-Konsequenz |
| --- | --- | --- | --- | --- |
| 1 | … | … | … | … |

## Konsequenzen für das Profil

- Bestätigte Regeln (mit Beobachtungszählung):
- Regeländerungsvorschläge für die nächste Version (MAJOR/MINOR/PATCH-Einordnung):
- Gegenbeispiele und Kontexte, in denen eine Regel nicht gilt:
- Neuer Profil-Status: `tested` (bei abgeschlossenem Test); `next_review` erneuert auf: <YYYY-MM-DD>
