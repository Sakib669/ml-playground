import pandas as pd

# Define the 14 standard column names for the Boston Housing dataset
columns = [
    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 
    'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'
]

# Read the raw text file
# sep=r'\s+' tells pandas to split on any amount of whitespace (spaces/tabs)
df = pd.read_csv('housing.data.txt', sep=r'\s+', header=None, names=columns)

# Save it as a proper CSV file
df.to_csv('boston_housing.csv', index=False)

# Print the first 5 rows to verify
print(df.head())
print(f"\nTotal rows: {len(df)}")