#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line (1-140 chars) to /output/entry.txt and prints it.
"""

import os

LINE = "My map says that corner is a cliff, my bumper says it is a wall, and my battery says it is quitting time. I believe all three."

def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line must be 1-140 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
