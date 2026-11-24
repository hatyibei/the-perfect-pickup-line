#!/usr/bin/env python3
"""Entry for make.fun's "The Perfect Pickup Line".

Writes a single pickup line to /output/entry.txt
(UTF-8, 1-200 characters, no trailing newline).
"""
import os

ENTRY = (
    "I seem to have lost my number in your smile - mind if I borrow "
    "yours until it turns up?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
