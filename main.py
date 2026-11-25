#!/usr/bin/env python3
"""Honest appliance error: one line a fridge could plausibly show.

The program writes a single error line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, then verifies the written file against
the competition gate: UTF-8 text, 1 to 200 characters, one line, not
only whitespace.
"""

import os

# The entry: a fridge whose cooling has failed but whose light still
# works. The humour comes from the truth of the fault, in the machine's
# own flat voice.
LINE = (
    "E5: Cooling failed. The light still works. "
    "I am now a cupboard that hums, and I am sorry about the milk."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    text.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("written entry does not match the entry line")
    # Re-check the gate on the file as written, not just on the string.
    if not 1 <= len(written) <= 200:
        raise SystemExit(f"written entry is {len(written)} chars, must be 1-200")
    if "\n" in written or "\r" in written:
        raise SystemExit("written entry must be a single line")
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
