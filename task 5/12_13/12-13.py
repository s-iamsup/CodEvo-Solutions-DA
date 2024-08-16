import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:/Users/chint/Downloads/datasets_of_enrolment_by_age_and_class_udise_plus_6910916/data/enrolment_age_2012_13.csv")
print(data)

data['total_enrolment'] = data.filter(like='boys').sum(axis=1) + data.filter(like='girls').sum(axis=1)
state_enrolment = data.groupby('state_name')['total_enrolment'].sum().sort_values()

plt.figure(figsize=(12, 8))
sns.barplot(x=state_enrolment.values, y=state_enrolment.index, palette='viridis')
plt.title('Total Enrolment by State (2012-13)')
plt.xlabel('Total Enrolment')
plt.ylabel('State')
plt.show()


age_enrolment = data.groupby('age')['total_enrolment'].sum()

plt.figure(figsize=(10, 6))
sns.lineplot(x=age_enrolment.index, y=age_enrolment.values, marker='o')
plt.title('Enrolment by Age Group (2012-13)')
plt.xlabel('Age')
plt.ylabel('Total Enrolment')
plt.show()


state_data = data[data['state_name'] == 'Jammu & Kashmir']

district_enrolment = state_data.groupby('district_name')['total_enrolment'].sum().sort_values()

plt.figure(figsize=(12, 8))
sns.barplot(x=district_enrolment.values, y=district_enrolment.index, palette='viridis')
plt.title('Total Enrolment by District in Jammu & Kashmir (2012-13)')
plt.xlabel('Total Enrolment')
plt.ylabel('District')
plt.show()


plt.figure(figsize=(12, 8))
sns.boxplot(data=data.filter(like='class_'), palette='viridis')
plt.title('Distribution of Enrolment Numbers by Class (2012-13)')
plt.xlabel('Class')
plt.ylabel('Enrolment Numbers')
plt.xticks(rotation=45)
plt.show()


age_gender_enrolment = data.groupby(['age'])[['class_1_boys', 'class_1_girls']].sum().reset_index()

for i in range(1, 13):
    age_gender_enrolment[f'class_{i}_boys'] = data.groupby('age')[f'class_{i}_boys'].sum().values
    age_gender_enrolment[f'class_{i}_girls'] = data.groupby('age')[f'class_{i}_girls'].sum().values

age_gender_enrolment['total_boys'] = age_gender_enrolment.filter(like='boys').sum(axis=1)
age_gender_enrolment['total_girls'] = age_gender_enrolment.filter(like='girls').sum(axis=1)

plt.figure(figsize=(10, 6))
sns.lineplot(x=age_gender_enrolment['age'], y=age_gender_enrolment['total_boys'], label='Boys', marker='o')
sns.lineplot(x=age_gender_enrolment['age'], y=age_gender_enrolment['total_girls'], label='Girls', marker='o')
plt.title('Enrolment Trends Over Different Age Groups by Gender (2012-13)')
plt.xlabel('Age')
plt.ylabel('Total Enrolment')
plt.legend()
plt.show()


state_gender_enrolment = data.groupby('state_name')[['total_enrolment', 'class_1_boys', 'class_1_girls']].sum()

for i in range(1, 13):
    state_gender_enrolment[f'class_{i}_boys'] = data.groupby('state_name')[f'class_{i}_boys'].sum().values
    state_gender_enrolment[f'class_{i}_girls'] = data.groupby('state_name')[f'class_{i}_girls'].sum().values

state_gender_enrolment['total_boys'] = state_gender_enrolment.filter(like='boys').sum(axis=1)
state_gender_enrolment['total_girls'] = state_gender_enrolment.filter(like='girls').sum(axis=1)
state_gender_enrolment['gender_ratio'] = state_gender_enrolment['total_girls'] / state_gender_enrolment['total_boys']
plt.figure(figsize=(12, 8))
sns.barplot(x=state_gender_enrolment['gender_ratio'], y=state_gender_enrolment.index, palette='viridis')
plt.title('Gender Ratio by State (2012-13)')
plt.xlabel('Gender Ratio (Girls/Boys)')
plt.ylabel('State')
plt.show()


state_data = data[data['state_name'] == 'Jammu & Kashmir']
class_enrolment_state = state_data.filter(like='class_').sum()
plt.figure(figsize=(12, 8))
sns.barplot(x=class_enrolment_state.index, y=class_enrolment_state.values, palette='viridis')
plt.title('Distribution of Enrolment by Class in Jammu & Kashmir (2012-13)')
plt.xlabel('Class')
plt.ylabel('Total Enrolment')
plt.xticks(rotation=45)
plt.show()


district_enrolment = data.groupby('district_name')['total_enrolment'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x=district_enrolment.values, y=district_enrolment.index, palette='viridis')
plt.title('Top 10 Districts with Highest Enrolment (2012-13)')
plt.xlabel('Total Enrolment')
plt.ylabel('District')
plt.show()





