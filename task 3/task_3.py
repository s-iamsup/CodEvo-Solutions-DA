import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"C:/Users/chint/Desktop/codevo/task 3/day.csv")

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Visualize the distribution of total users ('cnt')
plt.figure(figsize=(10, 6))
sns.histplot(data['cnt'], bins=30, kde=True)
plt.title('Distribution of Total Users')
plt.xlabel('Total Users')
plt.ylabel('Frequency')
plt.show()

# Visualize the trend of total users over time
plt.figure(figsize=(14, 7))
plt.plot(data['dteday'], data['cnt'], label='Total Users')
plt.title('Total Users Over Time')
plt.xlabel('Date')
plt.ylabel('Total Users')
plt.legend()
plt.show()

# Boxplot 
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=data)
plt.title('Total Users by Season')
plt.xlabel('Season')
plt.ylabel('Total Users')
plt.show()


# Scatter plot of temperature vs. total users
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=data)
plt.title('Temperature vs. Total Users')
plt.xlabel('Normalized Temperature')
plt.ylabel('Total Users')
plt.show()

# Visualize the effect of weekdays on total users
plt.figure(figsize=(10, 6))
sns.boxplot(x='weekday', y='cnt', data=data)
plt.title('Total Users by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Total Users')
plt.show()

plt.figure(figsize=(12, 8))

# Select only numeric columns for the correlation matrix
plt.figure(figsize=(14, 10))
numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
corr_matrix = data[numeric_cols].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
plt.figure(figsize=(14, 10))
sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm', fmt='.2f',
            linewidths=.5, cbar_kws={"shrink": .8}, center=0)
plt.title('Correlation Heatmap of Numeric Features', fontsize=18)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.show()