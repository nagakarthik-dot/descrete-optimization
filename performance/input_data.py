# input_data.py
import pandas as pd

class InputData:
    def __init__(self):
        self.load_data()

    def load_data(self):
        # Read nutritional data
        #nutritional_df = pd.read_excel('nutritional_data.xlsx')
        #self.fat = nutritional_df.set_index('Item')['Fat'].to_dict()
        #self.dry_matter = nutritional_df.set_index('Item')['Dry matter'].to_dict()
        #self.water = nutritional_df.set_index('Item')['Water'].to_dict()

        # Read demand and prices
        DMU_df = pd.read_excel('performance\DMU.xlsx')
        self.num_dmu=DMU_df["DMU"]
        self.weightage={}
        for i in range(30):
            self.weightage[i]=DMU_df.iloc[i][1:]

        