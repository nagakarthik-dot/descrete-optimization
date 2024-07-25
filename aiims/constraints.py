# constraints.py

from definitions import add_constraints_1, add_constraints_2, add_constraints_3, add_constraints_4, add_constraints_5

class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def add_constraints(self, new_price, new_demand):
        add_constraints_1(self.model, self.data, new_demand)
        add_constraints_2(self.model, self.data, new_demand)
        add_constraints_3(self.model, self.data, new_price, new_demand)
        add_constraints_4(self.model, self.data, new_price, new_demand)
        add_constraints_5(self.model, self.data, new_price)
