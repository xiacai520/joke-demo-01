#!/usr/bin/env python3
"""Entry for make.fun "The joke about the demo"
(the-joke-about-the-demo-20261123-0112).

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Deterministic: no randomness, no network, no clock.
"""

import os

JOKE = (
    "My AI agent finished my demo before I did \u2014 I was still on slide two "
    "when it shipped the feature, wrote the tests, and apologized for a bug "
    "I hadn't even found yet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
