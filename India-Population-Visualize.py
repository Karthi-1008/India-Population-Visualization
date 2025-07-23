import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = "C:\\Users\\karth\\Downloads\\API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
data = pd.read_csv(file_path, skiprows=4)  # Skip metadata rows

# Filter only India
india_data = data[data['Country Name'] == 'India']

# Step 3: Extract year columns (from 1960 to 2022)
years = [str(year) for year in range(1960, 2023)]
population = india_data[years].values.flatten()  # Get population values
population = [int(x) if pd.notnull(x) else 0 for x in population]  # Clean data

# Plot a Bar Chart (Population by Year)
plt.figure(figsize=(12, 6))
plt.bar(years, population, color='skyblue')
plt.title("India's Population Over Years (Bar Chart)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot a Histogram (Distribution of Population Values)
plt.figure(figsize=(8, 5))
plt.hist(population, bins=10, color='orange', edgecolor='black')
plt.title("Distribution of India's Population Values (Histogram)")
plt.xlabel("Population Range")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
