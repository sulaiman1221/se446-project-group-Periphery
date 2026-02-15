import csv
import sys


def extract_year(date_value: str) -> str | None:
    parts = date_value.strip().split()
    if not parts:
        return None

    mmddyyyy = parts[0].split("/")
    if len(mmddyyyy) != 3:
        return None

    year = mmddyyyy[2].strip()
    if len(year) != 4 or not year.isdigit():
        return None

    return year


def main() -> None:
    reader = csv.reader(sys.stdin)
    for row in reader:
        if not row:
            continue

        if row[0].strip() == "ID":
            continue

        if len(row) <= 2:
            continue

        year = extract_year(row[2])
        if not year:
            continue

        print(f"{year}\t1")


if __name__ == "__main__":
    main()
