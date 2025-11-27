import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned weather data
df = pd.read_csv("data/weather_data.csv")
df.columns = ["Date", "TmaxNormal", "TminNormal", "Rainfall", "Humidity"]
df["Date"] = pd.to_datetime(df["Date"], format="%d-%b")

# Temperature Trend (Line Chart)
plt.figure(figsize=(8,4))
plt.plot(df["Date"], df["TmaxNormal"])
plt.title("Daily Maximum Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/temperature_trend.png")
plt.show()

# Monthly Rainfall (Bar Chart)
df["Month"] = df["Date"].dt.strftime("%b")
monthly_rainfall = df.groupby("Month")["Rainfall"].sum()

plt.figure(figsize=(6,4))
plt.bar(monthly_rainfall.index, monthly_rainfall.values)
plt.title("Monthly Rainfall Total")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("images/monthly_rainfall.png")
plt.show()

# Humidity vs Temperature (Scatter Plot)
plt.figure(figsize=(6,4))
plt.scatter(df["TmaxNormal"], df["Humidity"])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.savefig("images/humidity_vs_temperature.png")
plt.show()

# Combined Figure:Temperature Trend+Rainfall
fig, ax1 = plt.subplots(figsize=(8,4))

# Line chart for temperature
ax1.plot(df["Date"], df["TmaxNormal"])
ax1.set_xlabel("Date")
ax1.set_ylabel("Temperature (°C)")
ax1.tick_params(axis='x', rotation=45)

# Second axis for rainfall
ax2 = ax1.twinx()
ax2.bar(df["Date"], df["Rainfall"], alpha=0.3)
ax2.set_ylabel("Rainfall (mm)")

plt.title("Combined Chart: Temperature vs Rainfall")
plt.tight_layout()
plt.savefig("images/combined_chart.png")
plt.show()