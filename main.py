#!/usr/bin/env python3
"""Write the one-sentence absurd invention pitch to /output/entry.txt (pass 1)."""

from pathlib import Path

ENTRY = "When it runs dry mid-word, the pen writes its own resignation in your handwriting."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
