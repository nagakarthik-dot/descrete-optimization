# results.py

from definitions import print_table, save_output

class FinalTable:
    def __init__(self, model, variables):
        self.model = model
        self.new_price = variables['new_price']
        self.new_demand = variables['new_demand']

    def print_table(self):
        return print_table(self.model, self.new_price, self.new_demand)

    def save_output(self, filename, content):
        save_output(filename, content)
