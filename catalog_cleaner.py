import csv
import sys

REQUIRED = ["sku", "title", "brand", "price"]

def clean(value):
    return " ".join((value or "").strip().split())

def normalize_row(row):
    cleaned = {k: clean(v) for k, v in row.items()}
    cleaned["sku"] = cleaned.get("sku", "").upper()
    return cleaned

def validate(row):
    return [field for field in REQUIRED if not row.get(field)]

if len(sys.argv) != 3:
    print("Usage: python catalog_cleaner.py input.csv output.csv")
    raise SystemExit(1)

source, output = sys.argv[1], sys.argv[2]
seen = set()
issues = []

with open(source, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

cleaned_rows = []
for index, row in enumerate(rows, start=2):
    row = normalize_row(row)
    missing = validate(row)

    if missing:
        issues.append(f"Row {index}: missing {', '.join(missing)}")

    sku = row.get("sku", "")
    if sku and sku in seen:
        issues.append(f"Row {index}: duplicate SKU {sku}")

    if sku:
        seen.add(sku)

    cleaned_rows.append(row)

with open(output, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(cleaned_rows)

print(f"Wrote {len(cleaned_rows)} rows to {output}")
for issue in issues:
    print("WARNING:", issue)
