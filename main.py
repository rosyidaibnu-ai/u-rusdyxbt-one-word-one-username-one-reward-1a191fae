#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry program.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt, exactly as the bounty asks: a single word, at most
30 characters, no explanation, no links, no pitch.

The username is the handle of the make.fun account this entry is submitted
from (@rosyidaibnu), so the judge compares a genuine handle, not a word
invented for the occasion.
"""

import sys
from pathlib import Path

# The entrant's own make.fun handle: one word, 11 characters.
USERNAME = "rosyidaibnu"

OUTPUT_PATH = Path("/output/entry.txt")

MAX_LENGTH = 30


def validate_username(username: str) -> str:
    """Check the text is a single word the gate will accept."""
    if not username:
        raise ValueError("username is empty")
    if len(username) > MAX_LENGTH:
        raise ValueError(f"username is {len(username)} chars, over the 30-char cap")
    if any(ch.isspace() for ch in username):
        raise ValueError("username must be a single word with no whitespace")
    return username


def main() -> int:
    username = validate_username(USERNAME)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(username, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != username:
        raise RuntimeError("round-trip check failed: file does not hold the username")
    print(f"wrote {len(written)}-char entry to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
