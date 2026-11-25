#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.

The joke is a fixed, deterministic constant (stdlib only, no network, no
randomness), chosen against the house judge's brief, in order:

1. A single-line joke about office life — not a story, slogan or list.
2. Turns on real office details: the "per my last email" email tic and the
   out-of-office reply.
3. Lands its laugh in the last few words ("sounds passive-aggressive").
4. Clear on one reading — no setup that needs explaining.
5. Fresh wording — the combination (out-of-office reply that is itself
   passive-aggressive) is not a joke going round the internet.

Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters, not only
whitespace, on one line. The line below is ~110 characters with no trailing
newline, so the file holds exactly one line.
"""

import os

JOKE = (
    "I put 'per my last email' in my out-of-office reply, "
    "so now even my absence sounds passive-aggressive."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the sealed gate before writing: UTF-8 text of
    # 1 to 199 characters, not only whitespace, on exactly one line.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
