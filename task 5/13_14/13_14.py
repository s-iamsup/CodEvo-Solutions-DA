import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\chint\Downloads\datasets_of_enrolment_by_age_and_class_udise_plus_6910916\data\enrolment_age_2013_14.csv")
print(data)

# Bar plot
data['total_enrollment'] = data.iloc[:, 6:].sum(axis=1)
state_enrollment = data.groupby('state_name')['total_enrollment'].sum().sort_values()

plt.figure(figsize=(12, 8))
state_enrollment.plot(kind='bar', color='Green')
plt.title('Total Enrollment by State (2013-14)')
plt.xlabel('Total Enrollment')
plt.ylabel('State')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
data['age'].hist(bins=range(3, 18), color='SkyBlue', edgecolor='black')
plt.title('Enrollment Distribution by Age (2013-14)')
plt.xlabel('Age')
plt.ylabel('Number of Enrollments')
plt.show()

# Calculate total enrollment for each class and gender
class_cols = [col for col in data.columns if 'class' in col]
class_enrollment = data[class_cols].sum()

boys_cols = [col for col in class_cols if 'boys' in col]
girls_cols = [col for col in class_cols if 'girls' in col]

boys_enrollment = class_enrollment[boys_cols]
girls_enrollment = class_enrollment[girls_cols]

# Stacked Bar
ind = range(len(boys_cols))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(ind, boys_enrollment, width, label='Boys')
ax.bar(ind, girls_enrollment, width, bottom=boys_enrollment, label='Girls')

ax.set_ylabel('Enrollment')
ax.set_title('Enrollment by Class and Gender (2013-14)')
ax.set_xticks(ind)
ax.set_xticklabels([col.replace('class_', '').replace('_boys', '').replace('_girls', '') for col in boys_cols])
ax.legend()
plt.show()

# Sample a few districts for visibility
sample_districts = data['district_name'].unique()[:5]
sample_data = data[data['district_name'].isin(sample_districts)]

# Line plot
plt.figure(figsize=(14, 8))
for district in sample_districts:
    district_data = sample_data[sample_data['district_name'] == district]
    plt.plot(district_data['age'], label=district)

plt.title('Enrollment Trend by District (2013-14)')
plt.xlabel('Age')
plt.ylabel('Total Enrollment')
plt.legend()
plt.show()

# Define the columns for classes
class_cols = [col for col in data.columns if 'class' in col]
boys_cols = [col for col in class_cols if 'boys' in col]
girls_cols = [col for col in class_cols if 'girls' in col]

# Total enrollment by gender and state
boys_enrollment_state = data.groupby('state_name')[boys_cols].sum().sum(axis=1)
girls_enrollment_state = data.groupby('state_name')[girls_cols].sum().sum(axis=1)

# Stacked bar
ind = range(len(boys_enrollment_state))
width = 0.35

fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(ind, boys_enrollment_state, width, label='Boys')
ax.bar(ind, girls_enrollment_state, width, bottom=boys_enrollment_state, label='Girls')

ax.set_ylabel('Enrollment')
ax.set_title('Comparison of Boys vs. Girls Enrollment by State (2013-14)')
ax.set_xticks(ind)
ax.set_xticklabels(boys_enrollment_state.index)
ax.legend()

plt.xticks(rotation=90)
plt.show()

class_cols = [col for col in data.columns if 'class' in col]
corr_matrix = data[class_cols].corr()

# Heatmap
plt.figure(figsize=(14, 12))  # Increase figure size for better spacing
heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, horizontalalignment='right')
heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation=0)

plt.title('Correlation Heatmap of Enrollments in Different Classes (2013-14)')
plt.show()




