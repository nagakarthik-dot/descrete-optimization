# constraints.py

from definitions import *

class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.x=None
        self.v=None
        self.y=None

    def add_constraints(self, x,y,v):
        supply(self.model,self.data,x)
        demand(self.model,self.data,x,y)
        supply_zone_count(self.model,self.data,y)
        distribution_supply(self.model,self.data,x,v)
        distribution_customer(self.model,self.data,y,v)
        distribution(self.model,self.data,x,y)
        

        

        
        