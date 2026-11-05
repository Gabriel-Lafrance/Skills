"""Export JSON orders on stdin as CSV on stdout."""
import csv
import json
import sys


def main():
    rows = json.load(sys.stdin)
    if not rows:
        return
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(["id", "total"])
    for row in rows:
        writer.writerow([row["id"], row["total"]])


if __name__ == "__main__":
    main()
