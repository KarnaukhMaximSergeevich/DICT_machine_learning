import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class PandasPractice:
    """Pandas practice"""

    def __init__(self):
        self.df_data = pd.read_csv("players_20.csv")
        print(self.df_data.head(5))
        print(self.df_data.shape)
        df_columns = self.df_data.columns.to_list()
        print(df_columns)
        useless_columns = ['dob', 'sofifa_id', 'player_url', 'long_name', 'body_type', 'real_face', 'loaned_from',
                           'nation_position', 'nation_jersey_number']
        df_dropped = self.df_data.drop(useless_columns, axis=1)
        print(df_dropped)
        print(self.df_data['weight_kg'].tail(5))
        print(self.df_data[['short_name', 'weight_kg']].head(5))
        df_dropped['BMI'] = df_dropped['weight_kg'] / (df_dropped['height_cm'] / 100) ** 2
        print(df_dropped[['short_name', 'BMI']].head(5))

    def show_hist(self):
        """show hist"""

        plt.hist(self.df_data["age"], label="age")
        plt.xlabel("age of player")
        plt.ylabel("number")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    start = PandasPractice()
    start.show_hist()
