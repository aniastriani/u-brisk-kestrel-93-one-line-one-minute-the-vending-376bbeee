"""Vending-machine pickup line entry.

Writes a single pickup line, spoken by a vending machine to a passing
human, to <MAKEFUN_OUTPUT_DIR>/entry.txt. Pure standard library only.
"""

import os

LINE = (
    "Excuse me \u2014 I hum all day, but my coils only spin for you. "
    "Press B7, keep the exact change: you already took "
    "my last Snickers\u2026 and my heart."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
