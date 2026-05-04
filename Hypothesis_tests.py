import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_excel("/content/DSA 210 PROJECT DATA.xlsx")

def time_to_minutes(x):
    if pd.isnull(x):
        return np.nan
    
    if isinstance(x, str):
        x = pd.to_datetime(x, errors="coerce").time()
    
    return x.hour * 60 + x.minute + x.second / 60

df["actual_duration_min"] = df["actual_duration"].apply(time_to_minutes)
df["estimated_duration_min"] = df["estimated_duration"].apply(time_to_minutes)

df["departure"] = pd.to_datetime(df["departure"].astype(str), errors="coerce")

departure_hour = df["departure"].dt.hour

df["rush_hour"] = departure_hour.apply(
    lambda x: "Yes" if (7 <= x <= 9) or (17 <= x <= 19) else "No"
)

df["delay_min"] = df["actual_duration_min"] - df["estimated_duration_min"]

df["distance"] = df["distance"].astype(str).str.replace("km", "", regex=False)
df["distance"] = df["distance"].str.replace(",", ".", regex=False)
df["distance"] = pd.to_numeric(df["distance"], errors="coerce")

df["trafic_level"] = df["trafic_level"].astype(str).str.strip()


print("==============================")
print("HYPOTHESIS TESTING RESULTS")
print("==============================")

# Rush Hour Effect - Independent t-test
rush = df[df["rush_hour"] == "Yes"]["actual_duration_min"].dropna()
non_rush = df[df["rush_hour"] == "No"]["actual_duration_min"].dropna()

t_stat, p_val = stats.ttest_ind(rush, non_rush, equal_var=False)

print("\n1. Independent T-test: Rush Hour vs Non-Rush Hour")
print("H0: There is no significant difference in actual travel duration between rush hour and non-rush hour trips.")
print("H1: There is a significant difference in actual travel duration between rush hour and non-rush hour trips.")
print("Rush hour mean:", rush.mean())
print("Non-rush hour mean:", non_rush.mean())
print("t-statistic:", t_stat)
print("p-value:", p_val)

if p_val < 0.05:
    print(f"Result: Since p-value ({p_val}) < 0.05 reject H0. Rush hour has a statistically significant effect on travel duration.")
else:
    print(f"Result: Since p-value ({p_val}) > 0.05 fail to reject H0. Rush hour does not have a statistically significant effect on travel duration.")

# Traffic Level Effect - ANOVA
traffic_groups = [
    group["actual_duration_min"].dropna()
    for name, group in df.groupby("trafic_level")
]

f_stat, p_val = stats.f_oneway(*traffic_groups)

print("\n2. ANOVA Test: Traffic Level and Actual Duration")
print("H0: Mean actual travel duration is the same across traffic levels.")
print("H1: At least one traffic level has a different mean actual travel duration.")
print("F-statistic:", f_stat)
print("p-value:", p_val)

if p_val < 0.05:
    print(f"Result: Since p-value ({p_val}) < 0.05 reject H0. Traffic level has a statistically significant effect on travel duration.")
else:
    print(f"Result: Since p-value ({p_val}) > 0.05 fail to reject H0. Traffic level does not have a statistically significant effect on travel duration.")

# Google Maps Accuracy - Paired t-test
paired_data = df[["actual_duration_min", "estimated_duration_min"]].dropna()

t_stat, p_val = stats.ttest_rel(
    paired_data["actual_duration_min"],
    paired_data["estimated_duration_min"]
)

print("\n3. Paired T-test: Actual Duration vs Estimated Duration")
print("H0: There is no significant difference between actual and estimated travel durations.")
print("H1: There is a significant difference between actual and estimated travel durations.")
print("Actual mean:", paired_data["actual_duration_min"].mean())
print("Estimated mean:", paired_data["estimated_duration_min"].mean())
print("t-statistic:", t_stat)
print("p-value:", p_val)

if p_val < 0.05:
    print(f"Result: Since p-value ({p_val}) < 0.05 reject H0. Google Maps estimates are significantly different from actual travel durations.")
else:
    print(f"Result: Since p-value ({p_val}) > 0.05 fail to reject H0. Google Maps estimates are not significantly different from actual travel durations.")

# Distance and Duration Relationship - Pearson correlation test
corr_data = df[["distance", "actual_duration_min"]].dropna()

corr, p_val = stats.pearsonr(
    corr_data["distance"],
    corr_data["actual_duration_min"]
)

print("\n4. Pearson Correlation Test: Distance vs Actual Duration")
print("H0: There is no linear relationship between distance and actual travel duration.")
print("H1: There is a significant linear relationship between distance and actual travel duration.")
print("Correlation coefficient:", corr)
print("p-value:", p_val)

if p_val < 0.05:
    print(f"Result: Since p-value ({p_val}) < 0.05 reject H0. Distance and actual travel duration have a statistically significant relationship.")
else:
    print(f"Result: Since p-value ({p_val}) > 0.05 fail to reject H0. Distance and actual travel duration do not have a statistically significant relationship.")

# Number of Traffic Lights and Duration - Pearson correlation test
corr_data = df[["num_lights", "actual_duration_min"]].dropna()

corr, p_val = stats.pearsonr(
    corr_data["num_lights"],
    corr_data["actual_duration_min"]
)

print("\n5. Pearson Correlation Test: Number of Traffic Lights vs Actual Duration")
print("H0: There is no linear relationship between number of traffic lights and actual travel duration.")
print("H1: There is a significant linear relationship between number of traffic lights and actual travel duration.")
print("Correlation coefficient:", corr)
print("p-value:", p_val)

if p_val < 0.05:
    print(f"Result: Since p-value ({p_val}) < 0.05 reject H0. Number of traffic lights and actual travel duration have a statistically significant relationship.")
else:
    print(f"Result: Since p-value ({p_val}) > 0.05 fail to reject H0. Number of traffic lights and actual travel duration do not have a statistically significant relationship.")

# Delay Test - One-sample t-test
delay_data = df["delay_min"].dropna()

t_stat, p_val = stats.ttest_1samp(delay_data, 0)

print("\n6. One-sample T-test: Delay")
print("H0: The average delay is equal to 0.")
print("H1: The average delay is significantly different from 0.")
print("Average delay:", delay_data.mean())
print("t-statistic:", t_stat)
print("p-value:", p_val)

if p_val < 0.05:
    print(f"Result: Since p-value ({p_val}) < 0.05 reject H0. The average delay is statistically significantly different from 0.")
else:
    print(f"Result: Since p-value ({p_val}) > 0.05 fail to reject H0. The average delay is not statistically significantly different from 0.")
