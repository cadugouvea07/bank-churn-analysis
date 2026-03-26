# 1. libraries imports

import pandas as pd


# 2. load raw dataset

bank_df = pd.read_csv(r"J:\2.Estudos\Portfolio\bank_churn_project\data\raw\Churn_Modelling.csv", sep=",")

# 3. data inspection

print("--- Dataset Shape ---")
print(bank_df.shape)

print("\n--- Data Types & Info ---")
print(bank_df.info())

print("\n--- Missing Values ---")
print(bank_df.isnull().sum())

# 4. display options

pd.set_option('display.max_columns', None)
pd.set_option('display.width',1000)

# 5. initial data exploration

print("\n--- First 5 Rows ---")
print(bank_df.head())

print("\n--- Descriptive Statistics ---")
print(bank_df.describe(include='all'))

# 6. feature selection (drop unnecessary columns) and column standardization

bank_df.drop(columns=['RowNumber', 'CustomerId', 'Surname'], inplace=True)

bank_df.columns = bank_df.columns.str.upper()

print("\n--- Dataset Shape After Feature Selection ---")
print(bank_df.shape)

print("\n--- First 5 Rows After Feature Selection ---")
print(bank_df)

# 7. column renaming (for a better understanding and consistency)

bank_df.rename(columns={
    'CREDITSCORE': 'CREDIT_SCORE',
    'NUMOFPRODUCTS': 'NUM_OF_PRODUCTS',
    'HASCRCARD': 'HAS_CR_CARD',
    'ISACTIVEMEMBER': 'IS_ACTIVE_MEMBER',
    'ESTIMATEDSALARY': 'ESTIMATED_SALARY'
}, inplace=True)

print("\n--- Dataset After Column Renaming ---")
print(bank_df)


# 8. feature engineering (creating business values)

# 8.1 mapping booleans to readable strings for visual charts (PBI, Tableau, etc.)

bank_df['HAS_CR_CARD_STATUS'] = bank_df['HAS_CR_CARD'].map({0: 'No', 1: 'Yes'})
bank_df['IS_ACTIVE_MEMBER_STATUS'] = bank_df['IS_ACTIVE_MEMBER'].map({0: 'Inactive', 1: 'Active'})
bank_df['CHURN_STATUS'] = bank_df['EXITED'].map({0: 'Retained', 1: 'Churned'})

# 8.2 creating age groups (age bins) to facilitate demographic analysis

age_bins = [17, 30, 40, 50, 60, 100]
age_labels = ['18-30', '31-40', '41-50', '51-60', '60+']
bank_df['AGE_GROUP'] = pd.cut(bank_df['AGE'], bins=age_bins, labels=age_labels, right=False)

# 8.3 creating financial KPI (balance to salary ratio)

bank_df['BALANCE_SALARY_RATIO'] = round(bank_df['BALANCE'] / bank_df['ESTIMATED_SALARY'], 2)

# 9. data export

processed_data_path = r"J:\2.Estudos\Portfolio\bank_churn_project\data\processed\bank_churn_processed.csv"
bank_df.to_csv(processed_data_path, index=False)

print(f"\n--- Processed data saved to {processed_data_path} ---")
print(bank_df)