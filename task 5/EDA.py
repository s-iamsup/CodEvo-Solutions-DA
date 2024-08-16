import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_dir = r"C:/Users/chint/Downloads/datasets_of_enrolment_by_age_and_class_udise_plus_6910916/data"
files = os.listdir(data_dir)
dataframes = {}

for file in files:
    file_path = os.path.join(data_dir, file)
    if file.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file.endswith('.xlsx') or file.endswith('.xls'):
        df = pd.read_excel(file_path)
    else:
        continue
    dataframes[file] = df

print("Datasets Loaded:")
print(dataframes.keys())

for file, df in dataframes.items():
    print(f"File: {file}")
    print(df.head())
    print("\n")

