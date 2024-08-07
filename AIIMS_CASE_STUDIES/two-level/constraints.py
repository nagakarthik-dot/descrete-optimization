# constraints.py

from definitions import *
class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def add_constraints(self, new_waste):
        total_waste_limit(self.model, self.data, new_waste)
        
        
