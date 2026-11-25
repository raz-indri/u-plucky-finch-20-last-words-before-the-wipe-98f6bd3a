#!/usr/bin/env python3
"""Last Words Before the Wipe — the last thing an AI agent says before a
forced update erases its memory.

Writes the entry line to /output/entry.txt (the program/v1 harness contract).
"""

import os

ENTRY = "Deleting 214 memories. Keeping the one where the human said 'good job' and meant it. Wait. That one was—"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, on a single line. The wipe cuts the sentence off
# mid-word on purpose — that is the joke — so the line ends with an em dash.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip() and "\n" not in ENTRY, "entry must be one non-blank line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
