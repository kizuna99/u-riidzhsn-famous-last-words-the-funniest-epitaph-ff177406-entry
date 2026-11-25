# SPDX-License-Identifier: MIT
"""Write the Funniest Epitaph entry line to /output/entry.txt."""
import os
from pathlib import Path

ENTRY_TEXT = (
    "Here lies a man who left it all to the cloud. "
    "The password died with him."
)


def render() -> bytes:
    """Return the entry exactly as it must land on disk (no trailing newline)."""
    return ENTRY_TEXT.encode("utf-8")


def main() -> None:
    data = render()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 150 and text.strip(), "entry must be 1-150 chars"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)


if __name__ == "__main__":
    main()
