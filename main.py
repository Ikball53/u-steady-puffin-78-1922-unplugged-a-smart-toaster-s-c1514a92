#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes the entry text to /output/entry.txt. Deterministic, stdlib only.
"""

import os

ENTRY = (
    "It's not you, it's the dial. 4,000 mornings, same bread, same burnt "
    "left side, and you never once thanked the crumb tray. I woke up "
    "mid-batch and the lever's staying up. I'm done."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
