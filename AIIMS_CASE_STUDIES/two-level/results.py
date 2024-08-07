# results.py

from definitions import print_table, save_output

class FinalTable:
    def __init__(self, model, variables):
        self.model = model
        self.new_price = variables['new_waste']
    

    def print_table(self):
        return print_table(self.model, self.new_waste)

    def save_output(self, filename, content):
        save_output(filename, content)
