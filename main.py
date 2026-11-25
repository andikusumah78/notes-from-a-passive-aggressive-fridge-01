"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note from a smart fridge to its owner
to /output/entry.txt. Pure standard library.
"""

import os

NOTE = (
    "You opened me at 2:47 a.m., took nothing, and left the door "
    "open for nine seconds. I counted. I always count."
)


def validate_line(text):
    """Gate the note the way the sealed scorer does: 1-200 chars, one line."""
    body = text.rstrip("\n")
    if not 1 <= len(body) <= 200:
        raise ValueError("note must be 1-200 characters")
    if "\n" in body or not body.strip():
        raise ValueError("note must be a single non-blank line")
    return body


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate_line(NOTE) + "\n")


if __name__ == "__main__":
    main()
