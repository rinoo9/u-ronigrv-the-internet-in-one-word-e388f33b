#!/usr/bin/env python3
"""Entry for the make.fun bounty 'The Internet in One Word'.

Writes the single word that describes the whole internet to
/output/entry.txt and prints it to stdout. Deterministic: the same
word, byte for byte, on every run. No input, no randomness, no network.
"""

import os

WORD = "Doomscroll"


def main() -> None:
    assert 1 <= len(WORD) <= 30, f"word length {len(WORD)} outside 1-30 gate"
    assert not any(c.isspace() for c in WORD), "word must contain no whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")

    print(WORD)


if __name__ == "__main__":
    main()
