# -----------------------------
# 9. RESULTS
# -----------------------------

print("\n========== ANALYSIS RESULTS ==========")

# Seasonal production
highest_season = seasonal_production.idxmax()
lowest_season = seasonal_production.idxmin()

print("\n1. Seasonal Production Analysis")
print("Highest average production season:", highest_season)
print("Lowest average production season:", lowest_season)

# Crop analysis
crop_avg = df.groupby("Crop")["Production"].mean()
top_crop = crop_avg.idxmax()

print("\n2. Crop Performance")
print("Highest average producing crop:", top_crop)

# Environmental analysis
if "Rainfall" in df.columns:
    rainfall_production = df[["Rainfall", "Production"]].corr().iloc[0, 1]
    print("\n3. Rainfall vs Production Correlation:",
          round(rainfall_production, 2))

if "Temperature" in df.columns:
    temperature_production = df[["Temperature", "Production"]].corr().iloc[0, 1]
    print("Temperature vs Production Correlation:",
          round(temperature_production, 2))

# Resource analysis
if "Water_Usage" in df.columns:
    water_production = df[["Water_Usage", "Production"]].corr().iloc[0, 1]
    print("Water Usage vs Production Correlation:",
          round(water_production, 2))

print("\n4. Visualizations Generated")
print("- seasonal_production.png")
print("- crop_comparison.png")
print("- correlation_heatmap.png")

print("\nAnalysis completed successfully!")