#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, at most 140 characters, for a city that
does not exist, to /output/entry.txt.

Method (see README.md and candidates.md for the full selection): 30 candidate
lines were drafted and scored by hand, 0-5, against each of the five published
judge criteria (invented city named with weather the whole point; makes a bored
commuter smile; broadcast-weather register; one concrete detail; every word
earns its place). The winner combines the strongest image of the top lines
(rain falling upwards) with the strongest commuter punchline (your bus is late,
but so is your boss). No live judge ran: the shared OpenRouter key is HTTP 402
exhausted, so no judge numbers are claimed anywhere.

Deterministic: the output is a constant string. No wall-clock time, no
randomness, no network, no environment reads beyond the output directory.
The program validates its own output against the sealed gate (UTF-8 text,
1-140 characters, not only whitespace) and exits non-zero on any violation.
"""

import os
import sys

ENTRY = "Today in Drizzlewick: light rain falling upwards, highs of 14°, and your bus is late, but so is your boss."

MAX_CHARS = 140


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the 140-character gate"
            % len(text),
            file=sys.stderr,
        )
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print("error: entry is not UTF-8 text: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the judged text is exactly the one line.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
