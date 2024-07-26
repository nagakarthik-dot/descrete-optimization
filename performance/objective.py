# objective.py

from definitions import set_objective_function

class Objective:
    def __init__(self, model, data,num):
        self.model = model
        self.data = data
        self.num=num

    def set_objective(self, new_proportions):
        set_objective_function(self.model, self.data, new_proportions,self.num)
