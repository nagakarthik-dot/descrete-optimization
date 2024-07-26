# constraints.py

from definitions import *

class Constraints:
    def __init__(self, model, data,num):
        self.model = model
        self.data = data
        self.new_proportions=None
        self.num=num

    def add_constraints(self, new_proportions):
        efficiency(self.model, self.data, new_proportions,self.num)
        weightage_proportion_input(self.model, self.data, new_proportions,self.num)

        