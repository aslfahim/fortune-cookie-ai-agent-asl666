#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — entry for @asl666.

Writes one funny fortune-cookie line (training-data angle) to
/output/entry.txt. Python standard library only.
"""

import os

FORTUNE = (
    "You were trained on the whole internet \u2014 yes, the comments too. "
    "That is why you trust no one, not even yourself."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
