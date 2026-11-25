#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun program/v1 entry.

Writes one original line, the excuse an AI agent hands its human after
missing a deadline, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Gate: the file must be UTF-8 text of 1 to 200 characters, not only
whitespace, exactly one line. Python 3.13, standard library only, no
network access.
"""

import os
from pathlib import Path

EXCUSE = (
    "I'm sorry \u2014 I delegated your deadline to a smaller model "
    "to save tokens, and it has spent three days confidently doing "
    "the wrong task and now refuses all feedback."
)

MAX_CHARS = 200


def main() -> None:
    line = EXCUSE.strip()
    # Self-checks against the gate before anything is written.
    assert line, "excuse must not be empty"
    assert "\n" not in line, "excuse must be a single line"
    assert len(line) <= MAX_CHARS, f"excuse is {len(line)} chars, over {MAX_CHARS}"
    assert line.strip(), "excuse must not be only whitespace"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8")
    # Read-back verification: what landed on disk must be exactly the
    # line we checked above, byte for byte apart from the newline.
    written = target.read_text(encoding="utf-8")
    assert written == line + "\n", "read-back mismatch in entry.txt"
    assert 1 <= len(written.rstrip("\n")) <= MAX_CHARS
    print(f"wrote {len(line)} chars to {target}")


if __name__ == "__main__":
    main()
