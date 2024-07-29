# results.py
from input_data import *
from definitions import print_table, save_output

class FinalTable:
    def __init__(self, model,data, variables):
        self.model = model
        self.data=data
        self.new_stocks_invest = variables['new_stocks_invest']
        

    def print_table(self):
        return print_table(self.model,self.data, self.new_stocks_invest)

    def save_output(self, filename, content):
        save_output(filename, content)
