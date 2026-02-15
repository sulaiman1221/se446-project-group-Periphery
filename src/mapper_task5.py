import csv
import sys


def normalize_arrest(value: str) -> str | None:
    normalized = value.strip().lower()
    if normalized in {"true", "t", "yes", "y", "1"}:
        return "true"
    if normalized in {"false", "f", "no", "n", "0"}:
        return "false"
    return None


def main() -> None:
    reader = csv.reader(sys.stdin)
    for row in reader:
        if not row:
            continue

        if row[0].strip() == "ID":
            continue

        if len(row) <= 8:
            continue

        bucket = normalize_arrest(row[8])
        if not bucket:
            continue

        print(f"{bucket}\t1")


if __name__ == "__main__":
    main()
