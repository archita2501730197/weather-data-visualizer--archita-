import pandas as pd

# Load dataset again
df = pd.read_csv("data/weather_data.csv")

# Convert date column into datetime
df["date"] = pd.to_datetime(df["date"], format="%d-%b")

# Handle missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display cleaned dataset
print("\nCleaned DataFrame:")
print(df.head())
