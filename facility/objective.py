# objective.py

from definitions import set_objective_function

class Objective:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def set_objective(self, x,y,v):
        set_objective_function(self.model, self.data, x,y,v)
