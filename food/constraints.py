# constraints.py

from definitions import *

class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def add_constraints(self,prepare,used,waste,unfull):
        prepared_food_multiple_of_10(self.model, self.data, prepare,used,unfull,waste)
       


