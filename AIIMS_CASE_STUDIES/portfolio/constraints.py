# constraints.py

from definitions import *

class Constraints:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.new_stocks_invest=None

    def add_constraints(self, new_stocks_invest):
        total_fraction_of_stocks(self.model, self.data, new_stocks_invest)
        desired_returns(self.model, self.data, new_stocks_invest)


        