# objective.py

from definitions import set_objective

class Objective:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def set_objective(self, variables):
        set_objective(self.model, self.data, variables)
