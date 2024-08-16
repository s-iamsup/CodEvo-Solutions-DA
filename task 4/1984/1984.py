import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path ="C:/Users/chint/Downloads/FARS1985NationalCSV/ACCIDENT.CSV"
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Display the first few rows of the dataset
print(data.head())

# Display basic information about the dataset
print(data.info())

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values:\n", missing_values)
# Drop columns that are completely empty
data_cleaned = data.dropna(axis=1, how='all')

# Display the cleaned dataset's columns
print("Columns after cleaning:")
print(data_cleaned.columns)
# Adjust the YEAR column to add '19' for years that seem to be in the '75' format
data_cleaned['YEAR'] = data_cleaned['YEAR'].apply(lambda x: 1900 + x if x < 100 else x)

# Now create the DATE column again
data_cleaned['DATE'] = pd.to_datetime(data_cleaned[['YEAR', 'MONTH', 'DAY']], errors='coerce')

# Group the data by date to analyze trends over time
accidents_over_time = data_cleaned.groupby('DATE').size()

# Plot the trend of accidents over time
plt.figure(figsize=(12, 6))
plt.plot(accidents_over_time.index, accidents_over_time.values, color='blue')
plt.title('Trend of Traffic Accidents Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.show()

# Group the data by weather conditions and count the number of accidents
weather_accidents = data_cleaned.groupby('WEATHER').size()

# Plot the correlation between weather conditions and accidents
plt.figure(figsize=(10, 6))
weather_accidents.plot(kind='bar', color='skyblue')
plt.title('Correlation Between Weather Conditions and Traffic Accidents')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.show()

# Group the data by STATE and COUNTY (or CITY) to identify hotspots
hotspots = data_cleaned.groupby(['STATE', 'COUNTY']).size().reset_index(name='Accidents')

# Sort to find the top hotspots
top_hotspots = hotspots.sort_values(by='Accidents', ascending=False).head(10)

# Display the top hotspots
print(top_hotspots)

# Aggregate the data by STATE and COUNTY
hotspots = data_cleaned.groupby(['STATE', 'COUNTY']).size().unstack(fill_value=0)

# Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(hotspots, cmap='Reds', linewidths=.5)

plt.title('Heatmap of Traffic Accident Hotspots by State and County')
plt.xlabel('County')
plt.ylabel('State')
plt.show()

# Save the cleaned dataset to a CSV file
data_cleaned.to_csv('ACCIDENT_CLEANED.csv', index=False)


