#!/usr/bin/env python3
"""One-word answer to the make.fun bounty 'The Internet in One Word'.

The program answers with a single word for the whole internet and
stores that answer in /output/entry.txt while also echoing it on
stdout. Every run produces exactly the same bytes: the word is a
constant, there is no input, no randomness, and no network access.
"""

import os
import sys

WORD = "Cookies"
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(word: str) -> str:
    """Check the entry against the bounty rules and return it unchanged.

    Rules enforced here:
      * the entry is a single word (no whitespace anywhere),
      * its length is between 1 and 30 characters inclusive,
      * it contains only printable, non-space characters.
    """
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(word) <= 30:
        raise ValueError(f"entry length {len(word)} is outside the 1-30 gate")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no whitespace")
    if any(not ch.isprintable() for ch in word):
        raise ValueError("entry must contain only printable characters")
    return word


def verify_output(path: str, expected: str) -> bool:
    """Re-read the written file and confirm it matches the entry exactly."""
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        content = handle.read()
    return content == expected + "\n"


def main() -> int:
    word = validate_entry(WORD)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(word + "\n")

    if not verify_output(OUTPUT_PATH, word):
        print(f"error: {OUTPUT_PATH} does not match the entry", file=sys.stderr)
        return 1

    print(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
