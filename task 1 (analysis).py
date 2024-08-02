import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
data = pd.read_csv("C:/Users/chint/Desktop/task_1.csv",encoding='ISO-8859-1')

# Display the first few rows of the dataset
print(data.columns)

# Basic statistics of the dataset
print(data.describe())

# Visualize the distribution of a specific column (replace 'column_name' with actual column name)
plt.figure(figsize=(10, 6))
sns.countplot(x='Sentiment', data=data, palette='viridis')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Rating distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['Rating'], bins=5, kde=True)
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Ratings by Location
plt.figure(figsize=(10, 8))
sns.boxplot(x='Location', y='Rating', data=data)
plt.xticks(rotation=90)
plt.title('Ratings by Location')
plt.xlabel('Location')
plt.ylabel('Rating')
plt.show()