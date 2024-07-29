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
        df = pd.read_excel('AIIMS_CASE_STUDIES/performance/DMU.xlsx')
        # Perform the required transformations
        ##df['Total Cost [103$/yr]'] = df['Total Cost [103$/yr]'] / 1000
        #df['Staff Cost [103$/yr]'] = df['Staff Cost [103$/yr]'] / 1000
        #df['Non-staff Cost [103$/yr]'] = df['Non-staff Cost [103$/yr]'] / 1000
        #df['Age of Competition [month]'] = df['Age of Competition [month]'] / 12
        #df['Revenue [103$/yr]'] = df['Revenue [103$/yr]'] / 1000
        self.num_dmu=df["DMU"]
        self.weightage={}
        for i in range(30):
            self.weightage[i]=df.iloc[i][1:]

        