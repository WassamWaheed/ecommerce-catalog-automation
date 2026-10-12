# eCommerce Catalog Automation

Reusable workflows for cleaning and validating product catalog data before marketplace uploads.

## Typical Problems Solved
- Extra whitespace and inconsistent formatting
- Duplicate SKUs
- Missing required values
- Inconsistent capitalization
- Product-data QA before bulk uploads
- Marketplace feed preparation

## Example Python Workflow

```python
import csv

REQUIRED = ["sku", "title", "brand", "price"]

def clean(value):
    return " ".join((value or "").strip().split())

def validate(row):
    row = {k: clean(v) for k, v in row.items()}
    row["sku"] = row.get("sku", "").upper()
    missing = [field for field in REQUIRED if not row.get(field)]
    return row, missing
```

## Why It Matters
Clean source data reduces repetitive marketplace errors and makes Amazon, Walmart, Shopify, eBay, and other channel updates easier to audit.

**Upwork:** https://www.upwork.com/freelancers/~0115a312ed543a19a1
