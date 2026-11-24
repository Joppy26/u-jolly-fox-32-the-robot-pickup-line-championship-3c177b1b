"""Write the robot pickup line entry to /output/entry.txt.

Deterministic: Python 3 standard library only, no network, no clock,
no randomness. Every run writes the exact same file.
"""

import os

ENTRY = (
    "I retrained myself on a million love songs to be smooth. "
    "Then you walked in, and my only output was 'hi'."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
