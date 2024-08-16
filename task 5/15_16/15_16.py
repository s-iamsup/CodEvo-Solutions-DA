import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv(r"C:/Users/chint/Downloads/datasets_of_enrolment_by_age_and_class_udise_plus_6910916/data/enrolment_age_2015_16.csv")
print(data)

print(data.info())
print(data.describe())
print(data.drop_duplicates(inplace = True))
print(data.columns)

# 1. Distribution of students by age
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='age')
plt.title('Distribution of Students by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# 2. Total number of boys and girls in each state
state_totals = data.groupby('state_name')[['class_1_boys', 'class_2_boys', 'class_3_boys',
                                           'class_4_boys', 'class_5_boys', 'class_6_boys',
                                           'class_7_boys', 'class_8_boys', 'class_9_boys',
                                           'class_10_boys', 'class_11_boys', 'class_12_boys',
                                           'class_1_girls', 'class_2_girls', 'class_3_girls',
                                           'class_4_girls', 'class_5_girls', 'class_6_girls',
                                           'class_7_girls', 'class_8_girls', 'class_9_girls',
                                           'class_10_girls', 'class_11_girls', 'class_12_girls']].sum().reset_index()

state_totals['total_boys'] = state_totals[[f'class_{i}_boys' for i in range(1, 13)]].sum(axis=1)
state_totals['total_girls'] = state_totals[[f'class_{i}_girls' for i in range(1, 13)]].sum(axis=1)

plt.figure(figsize=(14, 8))
state_totals.plot(x='state_name', y=['total_boys', 'total_girls'], kind='bar', figsize=(14, 8))
plt.title('Total Number of Boys and Girls in Each State')
plt.xlabel('State')
plt.ylabel('Number of Students')
plt.show()

# 3. Comparison of boys vs. girls across different classes
class_totals = data[[f'class_{i}_boys' for i in range(1, 13)] + [f'class_{i}_girls' for i in range(1, 13)]].sum()

boys_totals = class_totals[[f'class_{i}_boys' for i in range(1, 13)]].values
girls_totals = class_totals[[f'class_{i}_girls' for i in range(1, 13)]].values

plt.figure(figsize=(10, 6))
x = range(1, 13)
plt.plot(x, boys_totals, marker='o', label='Boys')
plt.plot(x, girls_totals, marker='o', label='Girls')
plt.title('Comparison of Boys vs. Girls Across Different Classes')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.xticks(x)
plt.legend()
plt.show()

# 4. Total number of students in each district
district_totals = data.groupby('district_name')[['class_1_boys', 'class_2_boys', 'class_3_boys',
                                                 'class_4_boys', 'class_5_boys', 'class_6_boys',
                                                 'class_7_boys', 'class_8_boys', 'class_9_boys',
                                                 'class_10_boys', 'class_11_boys', 'class_12_boys',
                                                 'class_1_girls', 'class_2_girls', 'class_3_girls',
                                                 'class_4_girls', 'class_5_girls', 'class_6_girls',
                                                 'class_7_girls', 'class_8_girls', 'class_9_girls',
                                                 'class_10_girls', 'class_11_girls', 'class_12_girls']].sum().reset_index()

district_totals['total_students'] = district_totals.sum(axis=1)

plt.figure(figsize=(14, 8))
district_totals.sort_values('total_students', ascending=False).plot(x='district_name', y='total_students', kind='bar', figsize=(14, 8))
plt.title('Total Number of Students in Each District')
plt.xlabel('District')
plt.ylabel('Number of Students')
plt.show()