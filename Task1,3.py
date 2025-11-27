import pandas as pd
import numpy as np

# Load the real CSV file
df = pd.read_csv("data/weather_data.csv")

# Rename column names
df.columns = ["Date", "TmaxNormal", "TminNormal", "Rainfall", "Humidity"]

# Convert date format
df["Date"] = pd.to_datetime(df["Date"], format="%d-%b")

# Convert numeric values
df["TmaxNormal"] = pd.to_numeric(df["TmaxNormal"])
df["TminNormal"] = pd.to_numeric(df["TminNormal"])
df["Rainfall"] = pd.to_numeric(df["Rainfall"])
df["Humidity"] = pd.to_numeric(df["Humidity"])

# Display data
print("Cleaned Data:")
print(df.head())

print("\nInformation:")
print(df.info())

print("\nSummary:")
print(df.describe())

print("\nStatistical Analysis using NumPy:\n")

tmax = np.array(df["TmaxNormal"])
tmin = np.array(df["TminNormal"])
rain = np.array(df["Rainfall"])
humid = np.array(df["Humidity"])

print("Mean Maximum Temperature:", np.mean(tmax))
print("Minimum Maximum Temperature:", np.min(tmax))
print("Maximum Maximum Temperature:", np.max(tmax))
print("Standard Deviation of Maximum Temperature:", np.std(tmax))
print("Mean Humidity:", np.mean(humid))
