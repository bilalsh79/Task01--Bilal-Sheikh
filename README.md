# Task01--Bilal-Sheikh
# Project 1: Data Cleaning & Preprocessing Pipeline (Python)

## 📌 Project Overview
This project represents the **Preparation Phase** of the data analytics lifecycle. Working as a Data Analyst Intern at **DecodeLabs**, I developed a robust Python script to transform a raw, messy e-commerce dataset into a structured, analysis-ready format. 

The primary goal was to ensure data integrity by identifying and resolving structural errors, handling missing values, and standardizing data types across 14 key business dimensions.

## 📊 Dataset Description
The analysis was performed on an e-commerce sales dataset containing the following features:
* **Order Details:** `OrderID`, `Date`, `OrderStatus`, `TrackingNumber`.
* **Customer Info:** `CustomerID`, `ShippingAddress`, `ReferralSource`.
* **Product Metrics:** `Product`, `Quantity`, `UnitPrice`, `TotalPrice`, `ItemsInCart`.
* **Financial Data:** `PaymentMethod`, `CouponCode`.

## 🛠️ Tools & Technologies
* **Python 3.x**
* **Pandas:** For data manipulation and structural cleaning.
* **Openpyxl:** For handling Excel engine operations.

## ⚙️ Implementation: The Cleaning Pipeline
The script (`Project 1.py`) executes a multi-stage cleaning process:

1.  **Integrity Inspection:** Utilized `.info()` and `.isnull().sum()` to map out missing data and inconsistent types.
2.  **Missing Value Treatment:** Identified the `CouponCode` column as having significant nulls. These were strategically filled with `'No Coupon'` to maintain dataset volume without skewing categorical analysis.
3.  **Deduplication:** Identified and removed completely duplicated rows to prevent inflated sales metrics.
4.  **Temporal Standardization:** Converted the `Date` column into uniform `datetime` objects and stripped unnecessary timestamp tails (00:00:00) for a cleaner professional presentation.
5.  **Strict Typecasting:** Forced numeric columns (`Quantity`, `UnitPrice`, `TotalPrice`) into their correct types (`int` and `float`) to ensure mathematical accuracy in downstream analysis (Project 3).

## 🔍 Validation & Quality Assurance
Post-cleaning, the pipeline runs a final validation check:
* Verifies **zero null values** across critical columns.
* Performs **statistical range checks** using `.describe()` to identify outliers or negative prices.
* Audits **categorical unique values** in `OrderStatus` and `PaymentMethod` to catch hidden typos or inconsistent naming conventions.

## 🚀 How to Run
1. Ensure you have the raw dataset file: `Dataset for Data Analytics.xlsx`.
2. Install dependencies:
   ```bash
   pip install pandas openpyxl
