# objective.py

from definitions import set_objective_function

class Objective:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def set_objective(self, trucks,min_trucks):
        set_objective_function(self.model, self.data, trucks,min_trucks)
        
