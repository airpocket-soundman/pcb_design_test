from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path


def patch_source(source: str, config: dict[str, object]) -> str:
    if "records" not in config:
        records = [
            {"type": "STRING", "id": record_id, "set": values}
            for record_id, values in config.items()
        ]
        additions: list[dict[str, object]] = []
    else:
        records = list(config.get("records", []))
        additions = list(config.get("additions", []))

    edits = {
        (str(edit["type"]), str(edit["id"])): dict(edit["set"])
        for edit in records
    }
    additions_by_anchor: dict[tuple[str, str], list[dict[str, object]]] = {}
    for addition in additions:
        anchor = addition["after"]
        key = (str(anchor["type"]), str(anchor["id"]))
        additions_by_anchor.setdefault(key, []).append(addition)

    patched: list[str] = []
    seen: set[tuple[str, str]] = set()
    inserted: set[tuple[str, str]] = set()

    for line in source.splitlines():
        divider = line.find("||")
        if divider < 0:
            patched.append(line)
            continue

        envelope = json.loads(line[:divider])
        record_type = str(envelope.get("type", ""))
        record_id = str(envelope.get("id", ""))
        record_key = (record_type, record_id)
        if record_key not in edits:
            patched.append(line)
        else:
            payload_text = line[divider + 2 :]
            suffix = "|" if payload_text.endswith("|") else ""
            if suffix:
                payload_text = payload_text[:-1]
            payload = json.loads(payload_text)
            payload.update(edits[record_key])
            patched.append(
                json.dumps(envelope, ensure_ascii=False, separators=(",", ":"))
                + "||"
                + json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
                + suffix
            )
            seen.add(record_key)

        if record_key in additions_by_anchor:
            for addition in additions_by_anchor[record_key]:
                patched.append(
                    json.dumps(
                        addition["envelope"],
                        ensure_ascii=False,
                        separators=(",", ":"),
                    )
                    + "||"
                    + json.dumps(
                        addition["payload"],
                        ensure_ascii=False,
                        separators=(",", ":"),
                    )
                    + "|"
                )
            inserted.add(record_key)

    missing = sorted(set(edits) - seen)
    if missing:
        formatted = ", ".join(f"{kind}:{record_id}" for kind, record_id in missing)
        raise ValueError(f"Records not found: {formatted}")
    missing_anchors = sorted(set(additions_by_anchor) - inserted)
    if missing_anchors:
        formatted = ", ".join(
            f"{kind}:{record_id}" for kind, record_id in missing_anchors
        )
        raise ValueError(f"Addition anchors not found: {formatted}")

    return "\n".join(patched) + ("\n" if source.endswith("\n") else "")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply a review patch to an EasyEDA .epro2/.eprj2 archive."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("edits", type=Path, help="JSON patch configuration")
    args = parser.parse_args()

    edits = json.loads(args.edits.read_text(encoding="utf-8"))
    args.destination.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(args.source, "r") as source_zip:
        entries = {info.filename: source_zip.read(info) for info in source_zip.infolist()}
        project_sources = [
            name for name in entries if name.lower().endswith(".epru")
        ]
        if len(project_sources) != 1:
            raise ValueError(
                f"Expected one .epru entry, found {len(project_sources)}"
            )
        project_source = project_sources[0]
        entries[project_source] = patch_source(
            entries[project_source].decode("utf-8"), edits
        ).encode("utf-8")
        if "projectTitle" in edits and "project2.json" in entries:
            project_data = json.loads(entries["project2.json"].decode("utf-8"))
            project_data["title"] = str(edits["projectTitle"])
            entries["project2.json"] = (
                json.dumps(project_data, ensure_ascii=False, indent=2) + "\n"
            ).encode("utf-8")

        with zipfile.ZipFile(
            args.destination, "w", compression=zipfile.ZIP_DEFLATED
        ) as destination_zip:
            for name, data in entries.items():
                destination_zip.writestr(name, data)


if __name__ == "__main__":
    main()
