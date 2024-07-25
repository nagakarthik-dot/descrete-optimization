# decision_variables.py
from definitions import create_variables

class DecisionVariables:
    def __init__(self, model):
        self.model = model
        self.variables = {}

    def create_variables(self):
        self.variables = create_variables(self.model)

    def get_variables(self):
        return self.variables

