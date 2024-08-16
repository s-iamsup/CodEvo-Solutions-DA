import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"C:/Users/chint/Downloads/datasets_of_enrolment_by_age_and_class_udise_plus_6910916/data/enrolment_age_2019_20.csv")
print(data)
print(data.head())
print(data.info())
print(data.describe())
print(data.columns)

#visualizations
# 1. Total Boys and Girls Enrollment by Class
classes = [f'class_{i}' for i in range(1, 13)]
boys = data[[f'class_{i}_boys' for i in range(1, 13)]].sum()
girls = data[[f'class_{i}_girls' for i in range(1, 13)]].sum()

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = range(len(classes))

bar1 = plt.bar(index, boys, bar_width, label='Boys')
bar2 = plt.bar([i + bar_width for i in index], girls, bar_width, label='Girls')

plt.xlabel('Class')
plt.ylabel('Total Enrollment')
plt.title('Total Boys and Girls Enrollment by Class')
plt.xticks([i + bar_width / 2 for i in index], classes)
plt.legend()
plt.show()

# 2. Total Enrollment by State
data['total_enrollment'] = data[[f'class_{i}_boys' for i in range(1, 13)] + [f'class_{i}_girls' for i in range(1, 13)]].sum(axis=1)
state_enrollment = data.groupby('state_name')['total_enrollment'].sum().reset_index()

plt.figure(figsize=(12, 8))
sns.barplot(x='total_enrollment', y='state_name', data=state_enrollment.sort_values('total_enrollment', ascending=False))
plt.xlabel('Total Enrollment')
plt.ylabel('State')
plt.title('Total Enrollment by State')
plt.show()

# 3. Age Distribution of Students
plt.figure(figsize=(10, 6))
sns.histplot(data['age'], bins=20, kde=True)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Students')
plt.show()

# 5. Class-wise Enrollment Trend
class_enrollment = data[[f'class_{i}_boys' for i in range(1, 13)] + [f'class_{i}_girls' for i in range(1, 13)]].sum().reset_index()
class_enrollment.columns = ['class', 'enrollment']
class_enrollment['class'] = class_enrollment['class'].apply(lambda x: x.replace('_boys', '').replace('_girls', ''))

plt.figure(figsize=(10, 6))
sns.lineplot(x='class', y='enrollment', data=class_enrollment, marker='o')
plt.xlabel('Class')
plt.ylabel('Total Enrollment')
plt.title('Class-wise Enrollment Trend')
plt.show()
