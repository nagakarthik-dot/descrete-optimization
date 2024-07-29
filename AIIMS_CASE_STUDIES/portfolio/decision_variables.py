## deciison_variables.py

from definitions import *

class DecisionVariables:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.new_stocks_invest = None

    def create_variables(self):
        self.new_stocks_invest = create_stocks_invest_vars(self.model, self.data)
        
    def get_variables(self):
        return {
            'new_stocks_invest': self.new_stocks_invest
        }
