#!/usr/bin/env python3
"""Make the AI Judge Laugh -- one office-life one-liner.

Writes a single joke about office life to /output/entry.txt.
The line is fixed, so every run produces byte-identical output.
"""

import os

JOKE = (
    "I keep a plant on my desk so when my boss asks how my workload "
    "is going, I can point at something else dying quietly."
)


def main() -> None:
    # Gate mirrors the competition rule: 1 to 200 characters, not blank.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
