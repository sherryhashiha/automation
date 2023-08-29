import pandas as pd
import numpy as np

# Syntax of read_csv()
file = 'C:/Users/crbu/Downloads/Private_Equity.xlsx'

company_details = pd.read_excel(file, sheet_name='Company Details')
financial_info = pd.read_excel(file, sheet_name='Financial Info')
executive = pd.read_excel(file, sheet_name='Executive')

df1 = pd.merge(company_details, financial_info, "left", on="DUNS")
df1_dedup = df1.drop_duplicates(subset=['DUNS'], keep="first")

df2 = pd.merge(df1_dedup, executive, "left", on="DUNS")
df2_dedup = df2.drop_duplicates(subset=['DUNS'], keep="first")

# Write the DataFrame to an Excel file
# df2_dedup.to_excel('joined_file.xlsx', index=False)