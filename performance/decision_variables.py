## deciison_variables.py

from definitions import *

class DecisionVariables:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.new_proportions = None

    def create_variables(self):
        self.new_proportions = create_new_proportions_vars(self.model, self.data)
        
    def get_variables(self):
        return {
            'new_proportions': self.new_proportions
        }
