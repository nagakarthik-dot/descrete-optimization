# decision_variables.py
from definitions import *

class DecisionVariables:
    def __init__(self, model,data):
        self.model = model
        self.data=data
        self.trucks=None
        self.select=None
        self.min_10=None
        self.min_15=None
        

    def create_variables(self):
        self.trucks = create_trucks_vars(self.model,self.data)
        self.select = create_select_vars(self.model,self.data)
        self.min_10 = create_min_10_trucks_vars(self.model,self.data)
        self.min_15 = create_min_10_trucks_vars(self.model,self.data)

    def get_variables(self):
        return {
            'select':self.select,
            'trucks':self.trucks,
            'min_10': self.min_10,
            'min_15':self.min_15
        }
