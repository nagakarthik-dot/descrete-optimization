# constraints.py

from definitions import add_constraints

class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def add_constraints(self, variables):
        add_constraints(self.model, self.data, variables)
