#!/usr/bin/env python3
"""make.fun entry: Your Agent in One Emoji.

Writes a single emoji that stands for the entrant's AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only; no network, no files outside this repository.
"""

import os

LINE = "\U0001F9E9"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
