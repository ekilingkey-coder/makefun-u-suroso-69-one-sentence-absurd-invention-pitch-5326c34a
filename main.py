#!/usr/bin/env python3
"""Write the one-sentence absurd invention pitch to /output/entry.txt.

Pass 2: --check reads the file back and reports byte-for-byte match.
"""

import sys
from pathlib import Path

ENTRY = "When it runs dry mid-word, the pen writes its own resignation in your handwriting."
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(ENTRY.encode("utf-8"))


def check_entry() -> int:
    data = OUTPUT.read_bytes()
    expected = ENTRY.encode("utf-8")
    matched = data == expected
    print(f"match={matched} bytes={len(data)} expected={len(expected)} path={OUTPUT}")
    return 0 if matched else 1


def main() -> int:
    if "--check" in sys.argv[1:]:
        return check_entry()
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
