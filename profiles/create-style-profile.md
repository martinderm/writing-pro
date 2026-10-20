# Ein Stilprofil erstellen

Ein Stilprofil beschreibt beobachtbares Schreiben einer Person oder Organisation.
Es soll keine Idealversion der Stimme erfinden und keine einzelnen Beispiele zu
allgemeinen Regeln aufblasen.

## 1. Material wählen

Sammle Texte, die von der Person selbst stammen und zum künftigen Einsatzzweck
passen. Nutze mindestens zehn aussagekräftige Beispiele, aber höchstens 20–30
repräsentative — mehr Material verlangsamt ohne Mehrwert. Für längere Formate
sind vollständige längere Texte hilfreicher als einzelne Sätze oder Captions.

Trenne dabei nach Genre und Kanal. Ein Newsletter, ein Fachbeitrag und eine
LinkedIn-Notiz können dieselbe Stimme unterschiedlich realisieren. Nimm keine
Texte, die bereits stark von KI oder anderen Redaktionen umgeschrieben wurden,
ohne das kenntlich zu machen.

Leichteinstieg bei wenig Material: Genügen 3–5 starke Beispiele, lässt sich
statt der Vollanalyse ein Starter-Profil per Interview bauen — die KI stellt
eine Frage nach der anderen zu Ton, Struktur, Rhythmus und Hassmustern und
legt stattdessen Kontrastbeispiele zur Reaktion vor. Dazu eine Blacklist mit
5–10 verhassten KI-Mustern und 2–3 Fremdbeispielen als Zielmarke. Reicht für
den Anfang, ersetzt die Vollanalyse bei regelmäßigem Gebrauch nicht. Fällt
das Interview aus (Batch-Modus, keine Antworten), ordne die vorhandenen
Samples selbst zu und markiere offene Fragen im Feld „Vertrauensgrad und
offene Fragen“.

## 2. Muster statt Etiketten erfassen

Arbeite mit konkreten Beobachtungen und Beispielen. Prüfe insbesondere:

- Wie Texte eröffnen und schließen
- Wie Argumente oder Erzählungen aufgebaut werden
- Satz- und Absatzlänge sowie Rhythmus
- Wiederkehrende Wörter, Wendungen und Bilder
- Direktheit, Humor, Haltung und Umgang mit Unsicherheit
- Art, komplexe Sachverhalte zu erklären
- Wörter, Formeln, Tonlagen und Behauptungen, die nicht passen
- Rechtschreibung und Sprachvariante (etwa de-DE, de-CH, en-US)
- Leseransprache: wann „ich“, „wir“, „man“ oder direkte Anrede
- Enthusiasmusmodus: Superlative, Tiefe oder Detailfreude
- Interpunktion: Gedankenstriche, Klammern, Semikolons, Ausrufezeichen

Eine Aussage wie „klar und nahbar" ist nur nützlich, wenn sie durch beobachtbare
Merkmale ergänzt wird, etwa: „beginnt ohne Begrüßungsfloskel mit einer konkreten
Situation; verwendet kurze Absätze; vermeidet Superlative".

Sprachvarianten: Die Sektionen „Sprachliche Muster", „Blacklist" und
„Exemplar-Paare" werden in der Zielsprache des Profils verfasst; alle
Meta-Sektionen (Geltung, Evidenzbasis, Protokoll) bleiben in der Arbeits- und
Dokumentationssprache. Die Exemplar-Paare (Do/Don't-Sätze) sind dabei der
schnellste Few-shot-Kontext — ihre Muster leben direkt in der Zielsprache.

## 3. Erstfassung erstellen

Kopiere [`style-profile.template.md`](style-profile.template.md) in einen
eigenen Unterordner im konsumierenden Workspace:
`<workspace>/writing-profiles/<profile-id>/style-profile.md`. Halte Herkunft,
Anwendungsgrenzen und Unsicherheiten fest. Beispiele dürfen nur abgelegt werden,
wenn ihre Nutzung dafür erlaubt ist.

Dazu gehören zwei weitere Artefakte:

- **`provenance.json`** im selben Ordner (Schema:
  [`references/schemas/profile-provenance.schema.json`](../references/schemas/profile-provenance.schema.json)):
  Quellenliste mit `source_sha256`, Ausschlüsse mit Begründung pro Eintrag,
  optional `receipt_ref` auf bestehende cloud-atlas-Curation-Receipts statt
  Doppel-Hashing. Die Prosa-Evidenzbasis in der style-profile.md bleibt
  interpretierend und referenziert das Sidecar.
- **Eintrag in der `writing-profiles/index.md`** (Schema:
  [`references/schemas/writing-profiles-index.schema.json`](../references/schemas/writing-profiles-index.schema.json)):
  die Discovery-Karteikarte (id, Titel, Inhaber, Sprachvarianten, Genres,
  Version, Status, Pfade). Der Index ist eine gewollte Projektion des
  Profil-Frontmatters; der Profilordner trägt zusätzlich das Mini-Protokoll,
  damit Profile auch ohne geladenen Skill korrekt angewendet werden.

Versionierung: `profile_version` (semantisch: MAJOR bei inkompatibler
Stimm-Änderung, MINOR bei neuen Regeln, PATCH bei Korrekturen), Status im
Frontmatter (`draft`/`tested`/`deprecated`), Changelog im
Test- und Korrekturprotokoll. Bestehende Profile nie überschreiben — neue
Versionen werden als eigene Version neben der alten gepflegt und die alte auf
`deprecated` gesetzt. Prüfen mit
[`scripts/profile_validate.py`](../scripts/profile_validate.py)
(Frontmatter, Sidecar, Index-Projektion, Quellen-Hashes).

## 4. An einem neuen Auftrag testen

Lass einen neuen, sachlich passenden Textentwurf erstellen. Markiere konkret,
was nicht passt: fremde Wörter, zu glatte Sätze, erfundene Positionen oder
Details, untypische Witze, generische Einstiege oder Wiederholungen.

Jeder Test läuft gegen ein Testprotokoll-Artefakt
([`test-report.template.md`](test-report.template.md)), abgelegt unter
`writing-profiles/<profile-id>/tests/YYYY-MM-DD-<auftrag>.md`: Frozen Draft
(oder Verweis), Belegmarken mit Profilzitaten und Blacklist-Treffern, Edit-Plan,
dann genau einmal rewriten, gefolgt vom Differenz-Log Entwurf ↔ Korrektur —
das ist die Kern-Evidenz für die nächste Profilversion. Ein abgeschlossener
Test setzt den Profil-Status auf `tested` und erneuert `next_review`.
Wenn kein getrennter Prüfdurchgang möglich ist (etwa Batch-Modus), arbeitest
du die Prüfkriterien als Checkliste vor dem Rewrite ab und vermerkst das im
Testprotokoll.

Die Profilinhaberin bzw. der Profilinhaber überarbeitet problematische
Stellen selbst; wenn die KI korrigieren muss, markiert sie jede Änderung als
unbestätigt. Die Differenz zwischen Entwurf und Korrektur ist die beste
Evidenz für eine anschließende Profiländerung. Jede Anwendung dokumentiert die
genutzte `profile_version` (im Testprotokoll; bei längeren Texten optional im
Dokumentkopf), damit Profiländerungen auf Tests rückführbar bleiben.

## 5. Profil iterativ pflegen

Ergänze nur Regeln, die mehrfach beobachtet oder im Test bestätigt wurden. Notiere
Gegenbeispiele und Kontexte, in denen eine Regel nicht gilt. Stimmen altern:
nimm bei alten Samples immer etwas Aktuelles dazu, sonst konserviert das Profil
ein früheres Ich. Ein Profil ist ein versioniertes Arbeitsartefakt: Es darf
wachsen, soll aber nachvollziehbar bleiben.

## Verwendung und Schutz

Ein Stilprofil wird nur verwendet, wenn Auftrag und Profil zueinander passen —
Details in `SKILL.md`, Schritt 2 und Routing. Es steuert Ausdruck und Form,
nicht Fakten oder fachliche Beurteilungen. Live-Profile liegen in der Ablage
aus `SKILL.md` (Abschnitt „Profilablage und Schutz“); der Skill-Ordner
`profiles/` enthält nur Template, Methode und fiktives Beispiel.

Fremdprofile nur auf ausdrücklichen Auftrag; aus Samples Muster übernehmen,
keine wörtlichen Passagen. Profile können persönliche Daten und
urheberrechtlich geschützte Beispiele enthalten.
