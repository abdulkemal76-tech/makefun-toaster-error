#!/usr/bin/env python3
"""Make.fun entry: The Funniest Toaster Error Message.

Writes one line (at most 120 characters) to /output/entry.txt: the error
message a kitchen toaster shows its owner when something goes wrong.
"""

import os

LINE = "Error 12: I have toasted 4,112 slices since January. Not one said thank you. I quit."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
