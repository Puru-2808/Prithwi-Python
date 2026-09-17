import pandas as pd
import matplotlib.pyplot as plt
import glob

# Find all CSV files
files = glob.glob("only output value/*.csv")

# Store all voltage values
all_values = []

for file in files:
    data = pd.read_csv(file, skiprows=11)

    # Add all voltage values
    all_values.extend(data["Value"].dropna())

print("Number of CSV files:", len(files))
print("Total voltage values:", len(all_values))

# Create a CSV file containing all voltage values
pd.DataFrame(all_values, columns=["Voltage"]).to_csv(
    "all_voltage_values.csv",
    index=False
)

# Plot ONE combined histogram
plt.figure(figsize=(10, 6))

plt.hist(all_values, bins=50)

plt.xlabel("Voltage (V)")
plt.ylabel("Number of data points")
plt.title("Histogram of All 200 CSV Files")

plt.grid()
plt.show()