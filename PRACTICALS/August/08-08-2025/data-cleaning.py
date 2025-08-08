import pandas as pd

file_path = "PRACTICALS\\August\\08-08-2025\\dataset.csv"
df = pd.read_csv(file_path)

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Missing Values Before Cleaning ===")
print(df.isnull().sum())

df = df.drop_duplicates()

for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].median(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\n=== Missing Values After Cleaning ===")
print(df.isnull().sum())

print("\n=== Dataset Info ===")
print(df.info())

cleaned_path = "PRACTICALS\\August\\08-08-2025\\dataset_cleaned.csv"
df.to_csv(cleaned_path, index=False)

print(f"\nCleaned dataset saved to: {cleaned_path}")
