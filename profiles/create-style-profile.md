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

Eine Aussage wie „klar und nahbar“ ist nur nützlich, wenn sie durch beobachtbare
Merkmale ergänzt wird, etwa: „beginnt ohne Begrüßungsfloskel mit einer konkreten
Situation; verwendet kurze Absätze; vermeidet Superlative“.

## 3. Erstfassung erstellen

Kopiere [`style-profile.template.md`](style-profile.template.md) in einen eigenen
Unterordner im konsumierenden Workspace, etwa
`<workspace>/profiles/jane-doe/style-profile.md` (oder im Skill-Checkout unter
`profiles/local/jane-doe/`, gitignored). Halte Herkunft,
Anwendungsgrenzen und Unsicherheiten fest. Beispiele dürfen nur abgelegt werden,
wenn ihre Nutzung dafür erlaubt ist.

## 4. An einem neuen Auftrag testen

Lass einen neuen, sachlich passenden Textentwurf erstellen. Markiere konkret,
was nicht passt: fremde Wörter, zu glatte Sätze, erfundene Positionen oder
Details, untypische Witze, generische Einstiege oder Wiederholungen.

Evidence-first in vier Schritten: Entwurf einfrieren und nicht mehr anpassen;
in einem getrennten Durchgang nur prüfen und jede kritische Stelle mit
Belegzitaten markieren; daraus den kurzen Edit-Plan ableiten; dann genau
einmal rewriten. Wenn kein getrennter Durchgang möglich ist (etwa
Batch-Modus), arbeitest du die Prüfkriterien als Checkliste vor dem Rewrite
ab.

Die Profilinhaberin bzw. der Profilinhaber überarbeitet problematische
Stellen selbst; wenn die KI korrigieren muss, markiert sie jede Änderung als
unbestätigt. Die Differenz zwischen Entwurf und Korrektur ist die beste
Evidenz für eine anschließende Profiländerung.

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
