import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:/Users/chint/Downloads/datasets_of_enrolment_by_age_and_class_udise_plus_6910916/data/enrolment_age_2014_15.csv")
print(data)

print(data.info())
print(data.describe())
print(data.columns)

#visualizations
#barplot
age_data = data.groupby('age').sum().reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x='age', y='value', hue='variable', data=pd.melt(age_data, ['age'], value_vars=['class_1_boys', 'class_1_girls']))
plt.title('Enrollment by Age')
plt.xlabel('Age')
plt.ylabel('Number of Students')
plt.legend(title='Gender/Class', loc='upper right')
plt.show()

# Aggregate data by state
state_data = data.groupby('state_name').sum().reset_index()

# Plot
plt.figure(figsize=(15, 8))
state_data_melted = pd.melt(state_data, ['state_name'], value_vars=['class_1_boys', 'class_1_girls'])
sns.barplot(x='value', y='state_name', hue='variable', data=state_data_melted)
plt.title('Total Enrollment by State')
plt.xlabel('Number of Students')
plt.ylabel('State')
plt.legend(title='Gender/Class', loc='upper right')
plt.show()

# Aggregate data by class
class_data = data[['class_1_boys', 'class_2_boys', 'class_3_boys', 'class_4_boys', 'class_5_boys',
                   'class_6_boys', 'class_7_boys', 'class_8_boys', 'class_9_boys', 'class_10_boys',
                   'class_11_boys', 'class_12_boys', 'class_1_girls', 'class_2_girls', 'class_3_girls',
                   'class_4_girls', 'class_5_girls', 'class_6_girls', 'class_7_girls', 'class_8_girls',
                   'class_9_girls', 'class_10_girls', 'class_11_girls', 'class_12_girls']].sum().reset_index()
class_data.columns = ['class_gender', 'total']
class_data['class'] = class_data['class_gender'].apply(lambda x: x.split('_')[1])
class_data['gender'] = class_data['class_gender'].apply(lambda x: x.split('_')[2])

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x='class', y='total', hue='gender', data=class_data)
plt.title('Class-Wise Enrollment')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.legend(title='Gender')
plt.show()

# Aggregate gender data
total_boys = class_data[class_data['gender'] == 'boys']['total'].sum()
total_girls = class_data[class_data['gender'] == 'girls']['total'].sum()

# Plot
plt.figure(figsize=(8, 8))
plt.pie([total_boys, total_girls], labels=['Boys', 'Girls'], autopct='%1.1f%%', startangle=140)
plt.title('Overall Gender Distribution')
plt.show()

# Scatter Plot: Age vs. Class Enrollment

# Aggregating data for boys and girls separately
age_class_boys = data[['age', 'class_1_boys', 'class_2_boys', 'class_3_boys', 'class_4_boys', 'class_5_boys',
                       'class_6_boys', 'class_7_boys', 'class_8_boys', 'class_9_boys', 'class_10_boys',
                       'class_11_boys', 'class_12_boys']].groupby('age').sum().reset_index()
age_class_girls = data[['age', 'class_1_girls', 'class_2_girls', 'class_3_girls', 'class_4_girls', 'class_5_girls',
                        'class_6_girls', 'class_7_girls', 'class_8_girls', 'class_9_girls', 'class_10_girls',
                        'class_11_girls', 'class_12_girls']].groupby('age').sum().reset_index()

plt.figure(figsize=(14, 7))
for class_num in range(1, 13):
    plt.scatter(age_class_boys['age'], age_class_boys[f'class_{class_num}_boys'], label=f'Class {class_num} Boys')
    plt.scatter(age_class_girls['age'], age_class_girls[f'class_{class_num}_girls'], label=f'Class {class_num} Girls')

plt.title('Age vs. Class Enrollment')
plt.xlabel('Age')
plt.ylabel('Number of Students')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Line Plot: Enrollment trends over age

# Aggregating data for boys and girls separately
age_class_boys = data[['age', 'class_1_boys', 'class_2_boys', 'class_3_boys', 'class_4_boys', 'class_5_boys',
                       'class_6_boys', 'class_7_boys', 'class_8_boys', 'class_9_boys', 'class_10_boys',
                       'class_11_boys', 'class_12_boys']].groupby('age').sum().reset_index()
age_class_girls = data[['age', 'class_1_girls', 'class_2_girls', 'class_3_girls', 'class_4_girls', 'class_5_girls',
                        'class_6_girls', 'class_7_girls', 'class_8_girls', 'class_9_girls', 'class_10_girls',
                        'class_11_girls', 'class_12_girls']].groupby('age').sum().reset_index()

plt.figure(figsize=(14, 7))
for class_num in range(1, 13):
    plt.plot(age_class_boys['age'], age_class_boys[f'class_{class_num}_boys'], marker='o', label=f'Class {class_num} Boys')
    plt.plot(age_class_girls['age'], age_class_girls[f'class_{class_num}_girls'], marker='o', label=f'Class {class_num} Girls')

plt.title('Enrollment Trends Over Age')
plt.xlabel('Age')
plt.ylabel('Number of Students')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()