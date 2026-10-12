# Example Output

Running:

```bash
python catalog_cleaner.py sample_products.csv cleaned_products.csv
```

produces a cleaned CSV and warnings for data-quality issues such as:

```text
Wrote 3 rows to cleaned_products.csv
WARNING: Row 3: missing price
WARNING: Row 4: duplicate SKU DEMO-002
```

This demonstrates how a lightweight validation step can catch common catalog problems before a marketplace upload.
