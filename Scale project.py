
import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv("sales_data_basic.csv")

# Step 2: View first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Get basic info
print("\nData Info:")
print(df.info())

# Step 4: Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Drop missing values (if any)
df = df.dropna()

# Step 6: Access and modify data
print("\nRevenue Column:")
print(df['Revenue'])

# Add new column (e.g., Profit = Revenue * 0.2)
df['Profit'] = df['Revenue'] * 0.2
print("\nData with Profit column added:")
print(df.head())

# Step 7: Save modified DataFrame
df.to_csv("sales_data_cleaned.csv", index=False)
