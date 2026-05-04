import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("/content/DSA 210 PROJECT DATA.xlsx")

# Basic overview
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)
print("\nInfo:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())
print("\nFirst 5 rows:")
print(df.head())

# Convert duration columns to minutes
def time_to_minutes(x):
    if pd.isnull(x):
        return np.nan
    
    if isinstance(x, str):
        x = pd.to_datetime(x, errors="coerce").time()
    
    return x.hour * 60 + x.minute + x.second / 60

df["actual_duration_min"] = df["actual_duration"].apply(time_to_minutes)
df["estimated_duration_min"] = df["estimated_duration"].apply(time_to_minutes)

# Convert date and departure
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["departure"] = pd.to_datetime(df["departure"].astype(str), errors="coerce")

# Rush hour (hour kolonunu tutmadan)
departure_hour = df["departure"].dt.hour

df["rush_hour"] = departure_hour.apply(
    lambda x: "Yes" if (7 <= x <= 9) or (17 <= x <= 19) else "No"
)

# Show date without time
df["date"] = df["date"].dt.date

# Delay
df["delay_min"] = df["actual_duration_min"] - df["estimated_duration_min"]

# Distance cleaning
df["distance"] = df["distance"].astype(str).str.replace("km", "", regex=False)
df["distance"] = df["distance"].str.replace(",", ".", regex=False)
df["distance"] = pd.to_numeric(df["distance"], errors="coerce")

# Traffic level
df["trafic_level"] = df["trafic_level"].astype(str).str.strip()

# Summary statistics
print("\nSummary statistics:")
print(df[[
    "actual_duration_min",
    "estimated_duration_min",
    "delay_min",
    "distance",
    "num_lights"
]].describe())

print("\nTraffic level counts:")
print(df["trafic_level"].value_counts())

print("\nRush hour counts:")
print(df["rush_hour"].value_counts())

# EDA VISUALIZATIONS

# Duration histogram
print()
plt.figure()
df["actual_duration_min"].hist()
plt.title("Distribution of Actual Travel Duration")
plt.show()

# Distance histogram
print()
plt.figure()
df["distance"].hist()
plt.title("Distribution of Distance")
plt.show()

# Delay histogram
print()
plt.figure()
df["delay_min"].hist()
plt.title("Distribution of Delay")
plt.show()

# CORRELATIONS & PLOTS

# Distance vs Actual Duration
print()
corr1 = df["distance"].corr(df["actual_duration_min"])
print("\nCorrelation (Distance vs Duration):", corr1)
print()
plt.figure()
plt.scatter(df["distance"], df["actual_duration_min"])
plt.title("Actual Distance vs Duration")
plt.xlabel("Distance")
plt.ylabel("Duration")
plt.show()

# Traffic lights vs Duration
print()
corr2 = df["num_lights"].corr(df["actual_duration_min"])
print("\nCorrelation (Traffic Lights vs Duration):", corr2)
print()
plt.figure()
plt.scatter(df["num_lights"], df["actual_duration_min"])
plt.title("Traffic Lights vs Duration")
plt.xlabel("Number of Lights")
plt.ylabel("Duration")
plt.show()

# Estimated vs Actual
print()
corr3 = df["estimated_duration_min"].corr(df["actual_duration_min"])
print("\nCorrelation (Estimated vs Actual):", corr3)
print()
plt.figure()
plt.scatter(df["estimated_duration_min"], df["actual_duration_min"])
plt.title("Estimated vs Actual")
plt.xlabel("Estimated")
plt.ylabel("Actual")

max_val = max(df["estimated_duration_min"].max(), df["actual_duration_min"].max())
plt.plot([0, max_val], [0, max_val])

plt.show()

# BOXPLOTS

print()
plt.figure()
df.boxplot(column="actual_duration_min", by="trafic_level")
plt.title("Traffic Level vs Duration")
plt.suptitle("")
plt.show()
print()
plt.figure()
df.boxplot(column="actual_duration_min", by="rush_hour")
plt.title("Rush Hour vs Duration")
plt.suptitle("")
plt.show()

# GROUP ANALYSIS

print()
print("\nAverage duration by traffic level:")
print(df.groupby("trafic_level")["actual_duration_min"].mean())
print()
print("\nAverage delay by traffic level:")
print(df.groupby("trafic_level")["delay_min"].mean())

# Final preview
print()
print("\nFinal Data:")
print(df.head())
