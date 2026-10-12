# eCommerce Catalog Automation

Reusable Python workflows for cleaning and validating product catalog data before marketplace uploads.

## Typical Problems Solved
- Extra whitespace and inconsistent formatting
- Duplicate SKUs
- Missing required values
- Inconsistent capitalization
- Product-data QA before bulk uploads
- Marketplace feed preparation

## Included Files
- [Catalog Cleaner](catalog_cleaner.py)
- [Demo Product Data](sample_products.csv)
- [Example Output](EXAMPLE_OUTPUT.md)

## Run the Demo

```bash
python catalog_cleaner.py sample_products.csv cleaned_products.csv
```

No third-party Python packages are required.

## Core Logic

```python
REQUIRED = ["sku", "title", "brand", "price"]

def clean(value):
    return " ".join((value or "").strip().split())
```

## Why It Matters
Clean source data reduces repetitive marketplace errors and makes Amazon, Walmart, Shopify, eBay, and other channel updates easier to audit.

**Upwork:** https://www.upwork.com/freelancers/~0115a312ed543a19a1
