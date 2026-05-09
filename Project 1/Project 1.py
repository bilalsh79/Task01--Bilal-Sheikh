import pandas as pd
# Load an Excel file
df = pd.read_excel('Dataset for Data Analytics.xlsx')
# 2. Inspect the data to find errors
print(df.info())               # Checks data types and overall non-null counts
print(df.isnull().sum())       # Counts exactly how many missing values are in each column
print(df.duplicated().sum())   # Counts how many completely duplicated rows exist
# Fill missing values in the CouponCode column
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')
# Drop any duplicate rows
df = df.drop_duplicates()
# Convert the Date column to actual datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Optional: Extract just the date part (YYYY-MM-DD) so it looks clean in Excel 
# without adding unnecessary timestamp (00:00:00) tails
df['Date'] = df['Date'].dt.date

# Ensure numeric columns are strictly typed
df['Quantity'] = df['Quantity'].astype(int)
df['UnitPrice'] = df['UnitPrice'].astype(float)
df['TotalPrice'] = df['TotalPrice'].astype(float)

#Validity checks
# Check for any remaining missing values
print(df.isnull().sum())
# Check data types
print(df.dtypes)
# Check the minimum and maximum values of your numbers
print(df.describe())
# Check categories for hidden typos
print(df['OrderStatus'].unique())
print(df['PaymentMethod'].unique())


# Save the cleaned dataframe as an Excel file
output_filename = 'Cleaned_Dataset.xlsx'
df.to_excel(output_filename, index=False, engine='openpyxl')

print(f"Success! Data cleaned and saved to {output_filename}")

