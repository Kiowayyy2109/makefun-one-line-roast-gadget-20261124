"""One-Line Roast: The Gadget You Use Every Day.

Writes a single roast line about an everyday gadget to /output/entry.txt.
The target is the smartwatch: it tracks everything, congratulates you for
standing up at the least dignified moments, and still manages to be the
most encouraging voice in the house.
"""

from pathlib import Path

LINE = (
    "My smartwatch congratulated me for standing up while I was sitting "
    "on the toilet, and honestly it's the only positive feedback I've had "
    "all week."
)

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly rather than write an entry the gate would refuse."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(line)}")


def main() -> None:
    validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    written = OUTPUT_PATH.read_bytes()
    if written != LINE.encode("utf-8"):
        raise RuntimeError("written bytes do not match the entry line")


if __name__ == "__main__":
    main()
