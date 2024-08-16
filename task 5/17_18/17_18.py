import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:/Users/chint/Downloads/datasets_of_enrolment_by_age_and_class_udise_plus_6910916/data/enrolment_age_2017_18.csv")
print(data)
print(data.info())
print(data.describe())
print(data.drop_duplicates(inplace = True))
print(data.columns)

# 1. Total Enrolment by State
data['total_boys'] = data[[f'class_{i}_boys' for i in range(1, 13)]].sum(axis=1)
data['total_girls'] = data[[f'class_{i}_girls' for i in range(1, 13)]].sum(axis=1)
data['total_enrolment'] = data['total_boys'] + data['total_girls']

state_enrolment = data.groupby('state_name')['total_enrolment'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
state_enrolment.plot(kind='bar', color='skyblue')
plt.xlabel('State')
plt.ylabel('Total Enrolment')
plt.title('Total Enrolment by State')
plt.xticks(rotation=90)
plt.show()

# 2. Enrolment by Class for Boys and Girls
class_boys = data[[f'class_{i}_boys' for i in range(1, 13)]].sum()
class_girls = data[[f'class_{i}_girls' for i in range(1, 13)]].sum()

plt.figure(figsize=(12, 8))
plt.plot(range(1, 13), class_boys, marker='o', label='Boys')
plt.plot(range(1, 13), class_girls, marker='o', label='Girls')
plt.xlabel('Class')
plt.ylabel('Total Enrolment')
plt.title('Enrolment by Class for Boys and Girls')
plt.legend()
plt.xticks(range(1, 13))
plt.show()

# 3. Comparison of Enrolment between Boys and Girls for Each Class
total_class_enrolment = pd.DataFrame({
    'Class': range(1, 13),
    'Boys': class_boys.values,
    'Girls': class_girls.values
})

total_class_enrolment.plot(x='Class', kind='bar', stacked=False, figsize=(12, 8))
plt.xlabel('Class')
plt.ylabel('Total Enrolment')
plt.title('Comparison of Enrolment between Boys and Girls for Each Class')
plt.xticks(rotation=0)
plt.show()

# 4. Overall Distribution of Enrolment by Gender
total_boys = class_boys.sum()
total_girls = class_girls.sum()

labels = ['Boys', 'Girls']
sizes = [total_boys, total_girls]
colors = ['skyblue', 'lightcoral']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Overall Enrolment Distribution by Gender')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()