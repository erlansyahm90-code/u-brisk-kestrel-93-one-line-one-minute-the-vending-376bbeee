"""A vending machine's one-breath pickup line, delivered as a plain text file.

This script produces the contest entry: a single sentence that a vending
machine might call out to a passerby. The wording stays inside the machine's
own little world (its hum, its coils) and lands its charm in the final few
words. The result is written to /output/entry.txt with no trailing newline,
so the file holds exactly the line and nothing else.
"""

import os

ENTRY = "I hum all day, but my coils only spin for you."

# The gate requires a non-blank line between 1 and 200 characters.
# Anything longer or shorter than that would be rejected before judging.
assert 1 <= len(ENTRY) <= 200, "entry length outside the 1-200 character gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
