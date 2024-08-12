# constraints.py

from definitions import *

class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def add_constraints(self,prepare,inventory,sold,waste,unfull):
        prepared_food_multiple_of_10(self.model, self.data, prepare)
        wastage_before_span_life(self.model, self.data, waste)
        quantity_sold(self.model, self.data, sold,prepare,inventory)
        unfull_filled_demand(self.model, self.data, sold,unfull,prepare)
        inventory_available(self.model, self.data, sold,inventory,prepare,waste,unfull)
        wastage_of_food(self.model, self.data,inventory,waste)


