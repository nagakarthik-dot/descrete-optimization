# decision_variables.py
from definitions import *

class DecisionVariables:
    def __init__(self, model,data):
        self.model = model
        self.data=data
        self.prepare=None
        self.waste=None
        self.sold=None
        self.unfull=None
        self.inventory=None

    def create_variables(self):
        self.prepare = create_prepared_food_vars(self.model,self.data)
        self.inventory=create_inventory_vars(self.model,self.data)
        self.waste=create_wastage_of_food_vars(self.model,self.data)
        self.unfull=create_unfullfilleded_demand_vars(self.model,self.data)
        self.sold=create_sold_vars(self.model,self.data)
        

    def get_variables(self):
        return {
            'prepare':self.prepare,
            'inventory':self.inventory,
            'sold':self.sold,
            'unfull':self.unfull,
            'waste':self.waste
        }
