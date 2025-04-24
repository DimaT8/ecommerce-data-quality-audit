"""
E-Commerce Data Quality Check Script
Author: Dima Taha
Date: April 2025

This script performs basic automated data validation checks on an e-commerce dataset.
The goal is to identify common data quality issues in a clear, repeatable way.
"""

import pandas as pd
import numpy as np
from datetime import datetime

# Load dataset
try:
    df = pd.read_csv("ecommerce-dataset.csv")
except FileNotFoundError:
    raise FileNotFoundError("Dataset not found. Please make sure 'ecommerce-dataset.csv' is in the same folder as this script.")

# Create a summary dictionary to store findings
summary = {}

# 1. Check for missing values
missing_rows = df[df.isnull().any(axis=1)]
summary['Missing Rows'] = len(missing_rows)

# 2. Check for future-dated OrderDate values
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
future_dates = df[df['OrderDate'] > pd.Timestamp.now()]
summary['Future-Dated Orders'] = len(future_dates)

# 3. Check for invalid Quantity values
invalid_quantity = df[(df['Quantity'] < 1) | (df['Quantity'] >= 100)]
summary['Invalid Quantity'] = len(invalid_quantity)

# 4. Check for invalid Price values
invalid_price = df[(df['Price'] <= 0) | (df['Price'] > 1000)]
summary['Invalid Price'] = len(invalid_price)

# 5. Check for TotalAmount calculation mismatch
df['ExpectedTotal'] = df['Quantity'] * df['Price']
invalid_total = df[~np.isclose(df['TotalAmount'], df['ExpectedTotal'], atol=1)]
summary['Incorrect TotalAmount'] = len(invalid_total)

# 6. Check for duplicate rows and duplicate OrderIDs
duplicate_rows = df[df.duplicated()]
duplicate_order_ids = df[df['OrderID'].duplicated(keep=False)]
summary['Fully Duplicated Rows'] = len(duplicate_rows)
summary['Duplicate OrderIDs'] = len(duplicate_order_ids)

# Convert findings to DataFrame
report_df = pd.DataFrame(list(summary.items()), columns=["Issue Type", "Record Count"])

# Save report to output folder
output_path = "sample_output/validation_report.csv"
report_df.to_csv(output_path, index=False)

print("✅ Data quality check completed. Report saved to:", output_path)
