# decision_variables.py
from definitions import create_new_price_vars, create_new_demand_vars

class DecisionVariables:
    def __init__(self, model):
        self.model = model
        self.new_price = None
        self.new_demand = None

    def create_variables(self):
        self.new_price = create_new_price_vars(self.model)
        self.new_demand = create_new_demand_vars(self.model)

    def get_variables(self):
        return {
            'new_price': self.new_price,
            'new_demand': self.new_demand
        }
