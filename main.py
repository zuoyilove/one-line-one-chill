#!/usr/bin/env python3
"""One Line, One Chill — a single sentence of horror.

Writes one line (under 200 characters) to /output/entry.txt.
The line is a fixed, hand-written sentence: no input, no network,
no randomness, so every run produces byte-identical output.
"""

import os

LINE = (
    "The dentist found a second row of teeth growing behind mine, "
    "small and patient, already practising my smile."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
