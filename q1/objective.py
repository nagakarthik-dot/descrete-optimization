# objective.py

from definitions import set_objective_function

class Objective:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def set_objective(self, used,waste,unfull):
        set_objective_function(self.model, self.data, used,waste,unfull)
        
