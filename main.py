"""Funniest Cat Voicemail Greeting - make.fun entry.

Writes one line, the funniest voicemail greeting a cat would record,
to entry.txt in the output directory.
"""

import os
import sys

MAX_CHARS = 120

LINE = (
    "Hi, it's Miso. I knocked your phone off the table, "
    "so meow after the beep - I'll call you back at 4 a.m. for food."
)


def _check_printable(text):
    """Reject control characters; tabs are the only exception allowed."""
    bad = [ch for ch in text if ord(ch) < 0x20 and ch != "\t"]
    if bad:
        raise ValueError(
            "entry must not contain control characters, found %r" % bad[0]
        )


def _check_single_line(text):
    """The gate counts one line; newlines or carriage returns fail it."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def validate(text):
    """Check the entry line against the competition gate.

    The gate requires UTF-8 text of 1 to 120 characters, not only
    white space, on a single line, with no control characters.
    Returns the validated text unchanged so callers can write it
    exactly as authored.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    _check_single_line(text)
    _check_printable(text)
    text.encode("utf-8")
    return text


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
