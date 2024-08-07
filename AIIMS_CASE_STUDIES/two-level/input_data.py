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
        self.waste=[2000000,2500000,1500000,3000000]
        self.concentration=[1.5,1,2.5,2]
        self.eff=[1,0.8,1.3,1]
        self.moni=1000000
        self.target=11000000
        self.subsidy=0.1

