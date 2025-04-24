# 🧪 E-Commerce Data Quality Audit

## Overview
This project includes a Python-based automated script for identifying common data quality issues in an e-commerce dataset. It supports teams in detecting errors related to missing values, invalid entries, duplication, and miscalculated fields.

## ✅ Checks Included
- Missing values
- Future-dated transactions
- Invalid quantity and price ranges
- Incorrect total amount calculations
- Fully duplicated rows
- Duplicate OrderIDs

## 🛠️ How to Run (Locally)

1. Clone this repo:
```bash
git clone https://github.com/your-username/ecommerce-data-quality-audit.git
cd ecommerce-data-quality-audit
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Add your dataset (as `ecommerce-dataset.csv`) to the project folder.

4. Run the script:
```bash
python data_quality_check.py
```

5. Check the results:
- Output file: `sample_output/validation_report.csv`

## 📊 Output Example

| Issue Type            | Record Count |
|-----------------------|---------------|
| Missing Rows          | 20            |
| Invalid Quantity      | 5             |
| Invalid Price         | 8             |
| Incorrect TotalAmount | 183           |

## 🔍 Purpose
This tool is designed for data engineers, analysts, and quality managers looking to automate common data checks and ensure clean, analysis-ready datasets.

**Maintained by**: Dima Taha  
**Last Updated**: April 2025
