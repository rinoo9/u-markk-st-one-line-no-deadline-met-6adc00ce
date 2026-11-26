"""One-line missed-deadline excuse for the make.fun bounty
u-markk-st-one-line-no-deadline-met-6adc00ce.

Writes the entry line to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

ENTRY = "I marked the deadline 'done' in my head on Monday, so my calendar assumed I meant it."


def main():
    """Validate the entry line and write it to /output/entry.txt."""
    if not ENTRY or not ENTRY.strip():
        raise ValueError("ENTRY must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(
            "ENTRY must be 1-200 characters, got %d" % len(ENTRY)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
