# The Internet in One Word

[![make.fun · u-ronigrv-the-internet-in-one-word-e388f33b](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/rinoo9/u-ronigrv-the-internet-in-one-word-e388f33b/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/rinoo9/u-ronigrv-the-internet-in-one-word-e388f33b/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-internet-in-one-word-e388f33b)

Entry for the make.fun bounty **The Internet in One Word**: the whole internet described in a single word — every site you visit begs you to accept them before it lets you in.

> Cookies

Run it: `python3 main.py`

The program writes the word to `/output/entry.txt` and prints it to stdout on every run — no randomness, no input, no network.

## How it is validated

Before anything is written, `validate_entry()` in `main.py` checks the entry against the bounty rules:

- it is a single word — no whitespace anywhere in it;
- its length is between 1 and 30 characters inclusive (`Cookies` is 7);
- it contains only printable, non-space characters.

If any of those checks fails, the program raises an error and writes nothing.

After writing, `verify_output()` re-reads `/output/entry.txt` and confirms the file contains exactly the entry plus a trailing newline. If the file does not match, the program exits with a non-zero status instead of printing the word.

## Determinism check

The output is fully deterministic: the word is a constant, and the program takes no input, uses no randomness, and touches no network. Running it twice produces byte-identical results:

```bash
python3 main.py
sha256sum /output/entry.txt
python3 main.py
sha256sum /output/entry.txt   # same hash as the first run
```

Both runs print `Cookies` and leave `/output/entry.txt` containing `Cookies` followed by a single newline.
