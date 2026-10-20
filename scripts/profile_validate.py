#!/usr/bin/env python3
"""Validator for writing-pro profiles.

Validates:
  - the YAML frontmatter of a style-profile.md (style-profile-frontmatter schema)
  - the provenance.json sidecar (profile-provenance schema)
  - the frontmatter of a writing-profiles/index.md (writing-profiles-index schema)
  - consistency between index, profile frontmatter and provenance (three-way)
  - optionally the source hashes referenced by provenance.json

Usage:
  python profile_validate.py <path> [more paths...]
      Each path may be a profile directory (containing style-profile.md),
      a style-profile.md, a provenance.json, or a writing-profiles directory
      (containing index.md).

  python profile_validate.py <path> --json
      Structured CLI envelope (see authoring-guide.md).

Options:
  --workspace PATH   Root used to resolve relative source paths for hash
                     checking. Defaults to the parent of the writing-profiles
                     directory (or the profile directory's parent when the
                     layout is nested deeper; walk up while an index.md or a
                     data/cloud directory is not found -- see --workspace).
  --no-hashes        Skip recomputing source_sha256 of referenced files.
  --json             Print the standard envelope instead of human text.

Exit codes: 0 valid, 1 invalid, 2 error (usage or IO failure).

Only Python 3 standard library is used (see authoring-guide.md). The JSON
Schema support is a deliberate subset: type, const, enum, required,
properties, additionalProperties (false), items, minItems, pattern, oneOf.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

PROVENANCE_SCHEMA = Path(__file__).resolve().parent.parent / "references" / "schemas" / "profile-provenance.schema.json"
FRONTMATTER_SCHEMA = Path(__file__).resolve().parent.parent / "references" / "schemas" / "style-profile-frontmatter.schema.json"
INDEX_SCHEMA = Path(__file__).resolve().parent.parent / "references" / "schemas" / "writing-profiles-index.schema.json"

ENVELOPE_ACTIONS = {
    "profile": "validate-profile",
    "provenance": "validate-provenance",
    "index": "validate-index",
}


# ---------------------------------------------------------------------------
# JSON Schema subset
# ---------------------------------------------------------------------------

def schema_error(doc, schema, path: str) -> str | None:
    """Return the first schema violation as a human-readable string, or None."""
    if "oneOf" in schema:
        matches = sum(1 for sub in schema["oneOf"] if schema_error(doc, sub, path) is None)
        if matches != 1:
            return f"{path or 'document'}: expected exactly one match for oneOf, got {matches}"
        return None

    expected = schema.get("type")
    if expected:
        checks = {
            "object": lambda v: isinstance(v, dict),
            "string": lambda v: isinstance(v, str),
            "array": lambda v: isinstance(v, list),
            "null": lambda v: v is None,
        }
        check = checks.get(expected)
        if check is None:
            return f"{path or 'schema'}: unsupported type '{expected}'"
        if not check(doc):
            return f"{path or 'document'}: expected type '{expected}', got {type(doc).__name__}"
        return None

    if "const" in schema and doc != schema["const"]:
        return f"{path}: expected const {json.dumps(schema['const'])}, got {json.dumps(doc)}"

    if "enum" in schema and doc not in schema["enum"]:
        return f"{path}: value {json.dumps(doc)} not in enum {json.dumps(schema['enum'])}"

    if isinstance(doc, dict):
        for key in schema.get("required", []):
            if key not in doc:
                return f"{path or 'document'}: missing required property '{key}'"
        props = schema.get("properties", {})
        for key, value in doc.items():
            if key in props:
                error = schema_error(value, props[key], f"{path}.{key}" if path else key)
                if error:
                    return error
            elif schema.get("additionalProperties") is False:
                return f"{path or 'document'}: unexpected property '{key}'"
        return None

    if isinstance(doc, list):
        if len(doc) < schema.get("minItems", 0):
            return f"{path}: expected at least {schema['minItems']} items, got {len(doc)}"
        item_schema = schema.get("items")
        if item_schema:
            for i, value in enumerate(doc):
                error = schema_error(value, item_schema, f"{path}[{i}]")
                if error:
                    return error
        return None

    if isinstance(doc, str):
        pattern = schema.get("pattern")
        if pattern and not re.search(pattern, doc):
            return f"{path}: value does not match pattern {pattern}"
        return None

    return None


# ---------------------------------------------------------------------------
# Minimal YAML subset (flat mappings, inline lists, inline flow mappings)
# ---------------------------------------------------------------------------

def _parse_scalar(raw: str):
    text = raw.strip()
    if text == "" or text == "~":
        return None
    if text.lower() == "null":
        return None
    if (text.startswith('"') and text.endswith('"') and len(text) >= 2) or (
        text.startswith("'") and text.endswith("'") and len(text) >= 2
    ):
        return text[1:-1]
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(part) for part in _split_flow(inner)]
    if text.startswith("{") and text.endswith("}"):
        mapping: dict = {}
        for part in _split_flow(text[1:-1].strip()):
            key, _, value = part.partition(":")
            mapping[key.strip()] = _parse_scalar(value)
        return mapping
    return text


def _split_flow(text: str) -> list[str]:
    parts, depth, current, quote = [], 0, "", None
    for char in text:
        if quote:
            current += char
            if char == quote:
                quote = None
        elif char in {'"', "'"}:
            quote = char
            current += char
        elif char in "[{":
            depth += 1
            current += char
        elif char in "]}":
            depth -= 1
            current += char
        elif char == "," and depth == 0:
            parts.append(current)
            current = ""
        else:
            current += char
    if current.strip():
        parts.append(current)
    return parts


def parse_frontmatter(md_path: Path) -> dict:
    """Parse the YAML frontmatter block of a markdown file (flat keys plus
    `profiles:` lists of inline flow mappings as used by writing-profiles/index.md)."""
    lines = md_path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{md_path}: no frontmatter block found (file must start with '---')")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError(f"{md_path}: unterminated frontmatter block")

    result: dict = {}
    current_list_key: str | None = None
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            if current_list_key is None:
                raise ValueError(f"{md_path}: list item without a preceding key: {stripped}")
            result[current_list_key].append(_parse_scalar(stripped[2:]))
            continue
        key, separator, raw = line.partition(":")
        if not separator:
            raise ValueError(f"{md_path}: cannot parse frontmatter line: {line!r}")
        key = key.strip()
        current_list_key = None
        if raw.strip() == "":
            result[key] = []
            current_list_key = key
        else:
            result[key] = _parse_scalar(raw)
    return result


# ---------------------------------------------------------------------------
# Validation targets
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def inclusion_hash_of(sources: list[dict]) -> str:
    digest = hashlib.sha256()
    for source in sorted(sources, key=lambda item: item.get("path", "")):
        digest.update(f"{source.get('path', '')}\n{source.get('source_sha256', '')}\n".encode("utf-8"))
    return digest.hexdigest()


def collect_errors(doc, schema, context: str) -> list[str]:
    error = schema_error(doc, schema, "")
    return [f"{context}: {error}"] if error else []


def find_profile_dir(start: Path) -> tuple[Path, str]:
    """Classify a start path and return (profile_dir, target)."""
    if start.is_file():
        name = start.name
        if name == "provenance.json":
            return start.parent, "provenance"
        if name == "index.md":
            return start.parent, "index"
        return start.parent, "profile"
    if (start / "index.md").is_file():
        return start, "index"
    if (start / "provenance.json").is_file() and not (start / "style-profile.md").is_file():
        return start, "provenance"
    return start, "profile"


def validate_profile_dir(profile_dir: Path, workspace: Path | None, check_hashes: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    profile_path = profile_dir / "style-profile.md"
    provenance_path = profile_dir / "provenance.json"
    if not profile_path.is_file():
        return [f"{profile_dir}: missing style-profile.md"], warnings
    if not provenance_path.is_file():
        errors.append(f"{profile_dir}: missing provenance.json sidecar")
        return errors, warnings

    frontmatter_schema = json.loads(FRONTMATTER_SCHEMA.read_text(encoding="utf-8"))
    provenance_schema = json.loads(PROVENANCE_SCHEMA.read_text(encoding="utf-8"))

    try:
        frontmatter = parse_frontmatter(profile_path)
    except ValueError as exc:
        errors.append(str(exc))
        return errors, warnings
    errors.extend(collect_errors(frontmatter, frontmatter_schema, f"{profile_path.name} frontmatter"))

    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    errors.extend(collect_errors(provenance, provenance_schema, provenance_path.name))

    if frontmatter.get("profile_id") != provenance.get("profile_id"):
        errors.append(
            "profile_id mismatch: "
            f"frontmatter={frontmatter.get('profile_id')!r} provenance={provenance.get('profile_id')!r}"
        )

    if check_hashes and workspace is not None:
        for source in provenance.get("sources", []):
            source_path = workspace / source["path"]
            if not source_path.is_file():
                warnings.append(f"source file not found (hash not checked): {source['path']}")
                continue
            actual = sha256_of(source_path)
            if actual != source["source_sha256"]:
                errors.append(
                    f"source hash mismatch for {source['path']}: "
                    f"documented={source['source_sha256']} actual={actual}"
                )
        if "inclusion_hash" in provenance:
            expected = inclusion_hash_of(provenance.get("sources", []))
            if expected != provenance["inclusion_hash"]:
                errors.append("inclusion_hash does not match the canonical sources list")
    return errors, warnings


def validate_index_dir(index_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    index_path = index_dir / "index.md"
    index_schema = json.loads(INDEX_SCHEMA.read_text(encoding="utf-8"))
    frontmatter_schema = json.loads(FRONTMATTER_SCHEMA.read_text(encoding="utf-8"))
    provenance_schema = json.loads(PROVENANCE_SCHEMA.read_text(encoding="utf-8"))

    try:
        index = parse_frontmatter(index_path)
    except ValueError as exc:
        return [str(exc)], warnings
    errors.extend(collect_errors(index, index_schema, "index.md frontmatter"))

    for card in index.get("profiles", []):
        profile_path = index_dir.parent / card.get("profile_path", "")
        if not profile_path.is_file():
            errors.append(f"index entry points to missing profile: {card.get('profile_path')}")
            continue
        try:
            frontmatter = parse_frontmatter(profile_path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        errors.extend(collect_errors(frontmatter, frontmatter_schema, f"{card.get('profile_path')} frontmatter"))
        for field in ("profile_id", "profile_version", "status", "language_variants", "genres"):
            if card.get(field) != frontmatter.get(field):
                errors.append(
                    f"index projection mismatch for {card.get('profile_id')} field '{field}': "
                    f"index={card.get(field)!r} profile={frontmatter.get(field)!r}"
                )
        provenance_path = profile_path.parent / "provenance.json"
        if provenance_path.is_file():
            provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
            errors.extend(collect_errors(provenance, provenance_schema, provenance_path.name))
            if frontmatter.get("profile_id") != provenance.get("profile_id"):
                errors.append(f"provenance profile_id mismatch for {frontmatter.get('profile_id')}")
        else:
            warnings.append(f"missing provenance.json for {card.get('profile_id')}")
    return errors, warnings


def find_workspace_root(start: Path) -> Path | None:
    """Walk up from start looking for a data/cloud directory (workspace root)."""
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "data" / "cloud").is_dir():
            return candidate
    return None


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_envelope(action: str, success: bool, state: str, message: str, data: dict) -> dict:
    return {
        "action": action,
        "success": success,
        "state": state,
        "message": message,
        "data": data,
        "error": None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="+", help="profile directories, style-profile.md files, provenance.json or writing-profiles directories")
    parser.add_argument("--workspace", help="workspace root for resolving relative source paths (auto-detected when omitted)")
    parser.add_argument("--no-hashes", action="store_true", help="skip recomputing source_sha256 of referenced files")
    parser.add_argument("--json", action="store_true", help="print the standard envelope (see authoring-guide.md)")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    actions: set[str] = set()
    targets: list[str] = []

    for raw_path in args.paths:
        start = Path(raw_path)
        if not start.exists():
            errors.append(f"path not found: {raw_path}")
            continue
        target_dir, target = find_profile_dir(start)
        actions.add(ENVELOPE_ACTIONS[target])
        targets.append(str(start).replace("\\", "/"))
        workspace = Path(args.workspace) if args.workspace else find_workspace_root(target_dir)
        if target == "index":
            target_errors, target_warnings = validate_index_dir(target_dir)
        else:
            target_errors, target_warnings = validate_profile_dir(target_dir, workspace, not args.no_hashes)
        errors.extend(target_errors)
        warnings.extend(target_warnings)

    if errors:
        success, state = False, "invalid"
        message = f"{len(errors)} validation error(s); {len(warnings)} warning(s)"
    else:
        success, state = True, "valid"
        message = "all targets valid" if warnings else "all targets valid, no warnings"

    if args.json:
        action = actions.pop() if len(actions) == 1 else "validate"
        envelope = build_envelope(action, success, state, message, {"targets": targets, "errors": errors, "warnings": warnings})
        print(json.dumps(envelope, indent=2, ensure_ascii=False))
    else:
        for line in warnings:
            print(f"warning: {line}")
        for line in errors:
            print(f"error: {line}")
        print(message)

    return 1 if errors else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except OSError as exc:
        print(json.dumps(build_envelope("validate", False, "error", str(exc), {}), ensure_ascii=False))
        sys.exit(2)
