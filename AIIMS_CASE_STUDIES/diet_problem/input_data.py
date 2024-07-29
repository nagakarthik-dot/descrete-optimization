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
        nutritions_df = pd.read_excel('AIIMS_CASE_STUDIES/diet_problem/nutrition_data.xlsx')
        nutrition_df=nutritions_df.head(9)
        self.items=nutrition_df['Item']
        self.calories=nutrition_df['Calories (kcal)']
        self.protein=nutrition_df['Protein (gram)']
        self.Fat=nutrition_df['Fat (gram)']
        self.carbohydrates=nutrition_df['Carbohydrates (gram)']
        self.servings=nutrition_df['Max Servings']
        self.price=nutrition_df['Price (Hfl)']
        self.max_allowance=117
        self.min_req={"calories":3000, "protein":65,"carbohydrates":375}
        
