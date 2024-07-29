# constraints.py

from definitions import max_availability_fat, max_availability_dry, price_elasticity, cross_elasticity, demand_limitation

class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def add_constraints(self, new_price, new_demand):
        max_availability_fat(self.model, self.data, new_demand)
        max_availability_dry(self.model, self.data, new_demand)
        price_elasticity(self.model, self.data, new_price, new_demand)
        cross_elasticity(self.model, self.data, new_price, new_demand)
        demand_limitation(self.model, self.data, new_price)
