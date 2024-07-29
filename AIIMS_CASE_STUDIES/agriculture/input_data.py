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
        demand_prices_df = pd.read_excel('AIIMS_CASE_STUDIES/agriculture/demand_price.xlsx')
        self.prices = demand_prices_df['Price (£/ton)']
        self.demand = demand_prices_df['Domestic consumption (1000 tons)']
        # Read transfer coefficients
        transfer_df = pd.read_excel('AIIMS_CASE_STUDIES/agriculture/elasticity.xlsx')
        #self.transfer_coefficients = transfer_df.set_index('Item').to_dict(orient='index')
        self.e = transfer_df['Conversion factor']

