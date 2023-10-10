import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class DataFramePractice:
    """Data frame practice"""

    def __init__(self):
        general = pd.read_csv("general.csv")
        prenatal = pd.read_csv("prenatal.csv")
        sports = pd.read_csv("sports.csv")

        pd.set_option('display.max_columns', 8)
        print(f"{general.head(20)}\n{prenatal.head(20)}\n{sports.head(20)}")

        prenatal.rename(columns={"HOSPITAL": "hospital", "Sex": "gender"}, inplace=True)
        sports.rename(columns={"Hospital": "hospital", "Male/female": "gender"}, inplace=True)
        print(f"{general.head(20)}\n{prenatal.head(20)}\n{sports.head(20)}")

        mono_df = pd.concat([general, prenatal, sports], ignore_index=True)
        mono_df.drop(["Unnamed: 0"], axis=1, inplace=True)
        print(mono_df)

        random_string = mono_df.sample(n=20, random_state=30)
        print(random_string)

        mono_df.dropna(axis=0, how="all", inplace=True)
        mono_df.replace({"man": "m", "woman": "f", "male": "m", "female": "f"}, inplace=True)
        mono_df["gender"].fillna("f", inplace=True)
        columns_of_df = ["bmi", "diagnosis", "blood_test", "ecg", "ultrasound", "mri", "xray", "children", "months"]
        for i in columns_of_df:
            mono_df[i].fillna(0, inplace=True)
        print(mono_df.shape)
        print(mono_df.sample(n=20, random_state=30))

        hospital_counts = mono_df.groupby("hospital")["gender"].count()
        max_hospital = hospital_counts.idxmax()
        print(f"The hospital with the largest number of patients: {max_hospital}")

        stomach_count = mono_df[mono_df["hospital"] == "general"]["diagnosis"].value_counts()
        print(f"Patients with stomach disease: {stomach_count['stomach']}")

        general_age = mono_df[mono_df["hospital"] == "general"]["age"]
        sports_age = mono_df[mono_df["hospital"] == "sports"]["age"]
        median_general_age = general_age.median()
        median_sports_age = sports_age.median()
        age_difference = median_general_age - median_sports_age

        print(f"The difference in median between drug and sports medicine: {age_difference}")

        age_range_35_55 = mono_df[(mono_df["age"] >= 35) & (mono_df["age"] < 55)]

        plt.figure(figsize=(8, 6))
        plt.hist(age_range_35_55["age"], bins=20, edgecolor='k', alpha=0.7)
        plt.xlabel('Age')
        plt.ylabel('Number of patients')
        plt.title('Age distribution of patients from 35 to 55 years')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()


if __name__ == "__main__":
    start = DataFramePractice()
