import csv
import sys


def main() -> None:
    reader = csv.reader(sys.stdin)
    for row in reader:
        if not row:
            continue

        if row[0].strip() == "ID":
            continue

        if len(row) <= 7:
            continue

        key = row[7].strip()
        if not key:
            continue

        print(f"{key}\t1")


if __name__ == "__main__":
    main()
