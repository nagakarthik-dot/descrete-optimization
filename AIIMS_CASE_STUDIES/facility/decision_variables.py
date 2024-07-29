## deciison_variables.py

from definitions import *

class DecisionVariables:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        
        self.x=None
        self.v=None
        self.y=None

    def create_variables(self):
        self.x = create_quantity_vars(self.model,self.data)
        self.v=create_distribution_center_vars(self.model,self.data)
        self.y=create_customer_pref_vars(self.model,self.data)

        
    def get_variables(self):
        return {
            'x': self.x,
            'y': self.y ,
            'v': self.v
        }
