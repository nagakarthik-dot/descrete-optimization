# constraints.py

from definitions import *

class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data
    def add_constraints(self,trucks,select,min_10,min_15):
        weekly_weight_requirement(self.model, self.data, trucks,select)
        pattern_selcted(self.model, self.data, select)
        pattern_requiremnets(self.model, self.data,trucks, select)
        min_requiremnets(self.model, self.data,trucks, min_10,min_15)


        

     
