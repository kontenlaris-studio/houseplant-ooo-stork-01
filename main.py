"""The Houseplant Out-of-Office entry: an OOO auto-reply from the plant.

Writes the entry line to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "I'm out of office, busy being a plant. Your email will be watered, "
    "ignored, and possibly eaten by the cat."
)


def main():
    # Contract: one funny line, under 120 characters.
    assert 30 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of band"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
