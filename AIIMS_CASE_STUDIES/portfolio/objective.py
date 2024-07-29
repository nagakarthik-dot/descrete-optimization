# objective.py

from definitions import set_objective_function

class Objective:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def set_objective(self, new_stocks_invest):
        set_objective_function(self.model, self.data, new_stocks_invest)
