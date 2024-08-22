# constraints.py

from definitions import *

class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def add_constraints(self,prepare,used,waste,unfull):
        prepared_food_multiple_of_10(self.model, self.data, prepare, used,unfull,waste)
        quantity_sold(self.model, self.data, used,prepare)
        unfull_filled_demand(self.model, self.data, used,unfull)
        wastage_of_food(self.model, self.data, waste, used)
       

     
