# 📊 E-Commerce Data Quality Audit

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

3. The dataset is already included in the project as `ecommerce-dataset.csv`.


4. Run the script:
```bash
python data_quality_check.py
```

5. After running the script, a summary report will be saved to:
   sample_output/validation_report.csv


📁 Note: The sample_output folder is part of the project and includes a small placeholder file to make sure it remains visible when the project is cloned using Git



## 📊 Output Example

| Issue Type            | Record Count |
|-----------------------|---------------|
| Missing Rows          | 21            |
| Future-Dated Orders   | 0             |
| Invalid Quantity      | 5             |
| Invalid Price         | 8             |
| Incorrect TotalAmount | 203           |
| Fully Duplicated Rows | 2             |
| Duplicate OrderIDs    | 6             |

📌 The validation results shown in this README reflect the included dataset. Output may vary if the dataset is modified.



## 🔍 Purpose
This tool provides a lightweight and repeatable way to audit e-commerce data before using it in reports or dashboards. It can be extended easily for use in larger pipelines or scheduled checks.

**Maintained by**: Dima Taha  
**Last Updated**: April 2025

Update README to reflect pre-included dataset and output folder
