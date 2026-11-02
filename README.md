# writing-pro

Ein Shared Skill für längere Texte: Auftrag klären, zielgruppengerecht
schreiben, gegen den Zweck überarbeiten. Optional mit einem Stilprofil, das
Stimme und Form einer Person oder Organisation abbildet.

Der Skill liefert Methode und Werkzeuge, keine fertigen Texte und keine echten
Profile: Er enthält Template, Leitfaden, ein fiktives Beispiel und einen
Validator. Gelebte Profile bleiben im konsumierenden Workspace.

## Was der Skill abdeckt

- **Auftragsklärung**: Schreibaufgabe, Zielgruppe, Kommunikationsziel, Kanal,
  Sprachvariante und Faktenbasis — nur nachfragen, was den Text wirklich ändert.
- **Überarbeitung**: Verständlichkeit, Konsistenz, Präzision und
  Handlungsfähigkeit vor dekorativer Sprache; Tell-Check gegen KI-Floskeln als
  Heuristik, nicht als Detektor.
- **Stilprofile**: kompatibles Profil nur bei passendem Inhaber, Genre, Kanal
  und Sprachvariante; sonst klar und eigenständig ohne Profil schreiben.
- **Profilpflege**: Evidenzbasis mit Quellen-Hashes, Testprotokolle,
  semantische Versionierung und Index als Discovery-Karteikarte.

Nicht gedacht für Code, Commit-Messages, Chat-Antworten, Übersetzungen und
kurze Transaktionstexte. Recht, Medizin und Finanzen liefert der Skill nur als
Entwurf und Struktur; die fachliche Prüfung bleibt bei Fachexpertise.

## Quick Start

Skill im Ziel-Workspace verlinken (Junction unter Windows, Symlink unter *nix):

```powershell
New-Item -ItemType Junction -Path ".agents/skills/writing-pro" -Target "D:/users/dagobert/agents/skills/writing-pro"
```

```bash
ln -s ../skills/writing-pro .agents/skills/writing-pro
```

Danach genügt der Verweis in der `AGENTS.md` des Workspace:

```markdown
## writing-pro

Dieser Workspace nutzt den Skill `writing-pro` (Checkout z. B. unter
`.agents/skills/writing-pro/`) für zielgruppen- und stilgerechtes Schreiben.
Siehe dort `SKILL.md` für Routing und Regeln. Live-Stilprofile liegen in
`<workspace>/writing-profiles/` (Discovery über
`<workspace>/writing-profiles/index.md`).
```

## Verzeichnis

```text
writing-pro/
├── SKILL.md                       # Arbeitsweise, Tell-Check, Routing
├── profiles/
│   ├── create-style-profile.md    # Profil bauen, testen, pflegen
│   ├── style-profile.template.md  # Vorlage für style-profile.md
│   ├── test-report.template.md    # Vorlage für Testprotokolle
│   ├── example/                   # fiktives, ausgefülltes Beispiel
│   └── local/                     # gitignored: wiederverwendbare Profile
├── references/
│   ├── index.md                   # Quellen, Bootstrap, Lizenz
│   └── schemas/                   # JSON Schemas für Profil, Index, Provenance
└── scripts/
    └── profile_validate.py        # Validator (Python 3, stdlib only)
```

## Stilprofile im Workspace

Profile liegen nicht im Skill, sondern im konsumierenden Workspace:

```text
<workspace>/writing-profiles/
├── index.md                       # Discovery-Karteikarte (Projektion)
└── <profile-id>/
    ├── style-profile.md           # Stimme, Muster, Grenzen, Exemplar-Paare
    ├── provenance.json            # Quellen mit SHA-256, Ausschlüsse
    └── tests/                     # Testprotokolle je Auftrag
```

Zum Anlegen oder Überarbeiten: `profiles/create-style-profile.md` folgen und
`profiles/style-profile.template.md` kopieren. Bestehende Profile nie
überschreiben, neue Version daneben anlegen und die alte auf `deprecated`
setzen. Versionen semantisch: MAJOR bei inkompatibler Stimmänderung, MINOR bei
neuen Regeln, PATCH bei Korrekturen.

## Validator

```bash
python -B scripts/profile_validate.py <path> [<path> ...] \
  [--workspace <workspace-root>] [--no-hashes] [--json]
```

`<path>` ist ein Profilordner, eine `style-profile.md`, eine
`provenance.json` oder ein `writing-profiles/`-Ordner mit `index.md`. Geprüft
werden Frontmatter, Provenance-Sidecar, Index-Projektion, die Konsistenz
zwischen allen drei und optional die Quellen-Hashes.

- Exit-Codes: `0` gültig, `1` ungültig, `2` Aufruf- oder IO-Fehler.
- `--json` liefert das Standard-Envelope (`action`, `success`, `state`,
  `message`, `data`, `error`) statt Text.
- `--workspace` löst relative Quellenpfade für die Hash-Prüfung auf; ohne
  Angabe wird ein Workspace-Root mit `data/cloud/` aufwärts gesucht.

## Quellen und Lizenz

Der Skill-Code steht unter MIT, siehe [`LICENSE.txt`](LICENSE.txt).

Fremdtexte der Referenzquellen liegen nicht im Repository: Sie werden bei
Bedarf manuell bezogen und bleiben gitignored unter `references/local/`.
Übersicht, Bezugswege und Lizenzhinweise stehen in
[`references/index.md`](references/index.md). Ohne lokale Kopien arbeitet der
Skill mit den Links und dem Musterkatalog im `SKILL.md`.

Profile im Workspace können personenbezogene Daten und geschützte Beispiele
enthalten. Sie gehören nie in dieses Repository; `profiles/local/` ist nur für
wiederverwendbare, nicht-sensible Profile gedacht und bleibt ebenfalls
gitignored.
