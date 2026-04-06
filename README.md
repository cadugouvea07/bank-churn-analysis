# 🏦 Bank Customer Churn Analysis: A Data-Driven Retention Strategy

## 📌 Project Overview

Customer attrition (churn) is one of the most critical metrics for financial institutions. This project aims to identify the root causes of customer churn in a European bank and quantify the financial impact of these lost accounts. By moving from isolated metrics to multivariate analysis, this project uncovers the "perfect storm" of churn drivers and provides actionable business recommendations to improve retention.

## 🎯 Business Objectives

* Identify demographic and geographic segments with the highest risk of churn.
* Discover behavioral patterns (e.g., account activity) that accelerate customer exit.
* Quantify the financial impact (Capital at Risk) to prioritize marketing and retention budgets.
* Build an interactive Executive Dashboard to monitor these KPIs.

## 🛠️ Tech Stack & Tools

* **Python:** Data Cleaning, Transformation, and EDA (Pandas, NumPy).
* **Jupyter Notebook:** Statistical validation and Multivariate Analysis.
* **Data Visualization:** Seaborn & Matplotlib (Heatmaps, Bar Charts).
* **Power BI:** Interactive Executive Dashboard, DAX Measures, and Data Modeling.

## 💡 Key Business Insights (The "Golden Nuggets")

1. **The Global Baseline:** The bank has an overall churn rate of **20.37%**.
2. **The Structural Flaw (Age):** Customers between **51-60 years old** represent a critical risk, with a churn rate exceeding **56%** globally.
3. **The Perfect Storm (Germany):** While Germany represents only 25% of the customer base, it acts as an accelerator for churn. The churn rate for **Inactive German customers** hits an alarming **41.08%**. When cross-referencing Country and Age, the churn rate for **German clients aged 51-60** skyrockets to **70.04%**.
4. **Financial Impact (Capital at Risk):** The analysis revealed a severe financial vulnerability. German customers not only churn at higher rates but also hold **almost double the average account balance** (~$118k) compared to clients in France and Spain (~$65k). The bank is losing its highest-value clients.

## 📊 Executive Dashboard![Power BI Executive Dashboard](dashboards/dashboard_bank_churns.png)

## 📁 Repository Structure

├── data/
│   ├── raw/
│   │   └── Churn_Modelling.csv          # Original dataset
│   └── processed/
│       └── bank_churn_processed.csv     # Cleaned dataset ready for Power BI
├── notebooks/
│   └── 02_eda_bank_churn.ipynb          # Exploratory Data Analysis & Statistical Validation
├── scripts/

│   └── 01_data_preparation.py           # Python script for data cleaning and feature engineering
├── dashboards/
│   ├── data_analysis.pbix               # Power BI Executive Dashboard
│   ├── data_analysis.pdf                # Static PDF version of the dashboard
│   └── dashboard_bank_churns.png        # Dashboard preview image
└── README.md
