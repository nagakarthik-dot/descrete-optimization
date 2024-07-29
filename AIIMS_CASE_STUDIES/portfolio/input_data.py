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
        stocks_df = pd.read_excel('AIIMS_CASE_STUDIES/portfolio/stocks.xlsx')
        self.items=stocks_df['i']
        self.expected=stocks_df['m_i']
        self.cov1=stocks_df['cov_1']
        self.cov2=stocks_df['cov_2']
        self.cov3=stocks_df['cov_3']
        self.cov=[]
        self.cov.append(self.cov1)
        self.cov.append(self.cov2)
        self.cov.append(self.cov3)
        self.desired=9.0

        