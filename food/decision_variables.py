# decision_variables.py
from definitions import *

class DecisionVariables:
    def __init__(self, model,data):
        self.model = model
        self.data=data
        self.prepare=None
        self.waste=None
        self.unfull=None
        self.used=None

    def create_variables(self):
        self.prepare = create_prepared_food_vars(self.model,self.data)
        self.used=create_used_vars(self.model,self.data)
        self.waste=create_wastage_of_food_vars(self.model,self.data)
        self.unfull=create_unfullfilleded_demand_vars(self.model,self.data)

    def get_variables(self):
        return {
            'prepare':self.prepare,
            'used':self.used,
            'unfull':self.unfull,
            'waste':self.waste
        }
