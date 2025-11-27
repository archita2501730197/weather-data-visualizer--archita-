import pandas as pd

# Load data
df = pd.read_csv("data/weather_data.csv")
df.columns = ["Date", "TmaxNormal", "TminNormal", "Rainfall", "Humidity"]
df["Date"] = pd.to_datetime(df["Date"], format="%d-%b")

# Create Month column
df["Month"] = df["Date"].dt.strftime("%b")

# Group by Month
monthly_summary = df.groupby("Month").agg({
    "TmaxNormal": "mean",
    "TminNormal": "mean",
    "Rainfall": "sum",
    "Humidity": "mean"
}).reset_index()

# Rename columns for clarity
monthly_summary.columns = ["Month", "AvgTmax", "AvgTmin", "TotalRainfall", "AvgHumidity"]

# Display summary
print("Monthly Summary:")
print(monthly_summary)

# Export to CSV
monthly_summary.to_csv("data/monthly_summary.csv", index=False)
print("\nMonthly summary saved as 'data/monthly_summary.csv'")
