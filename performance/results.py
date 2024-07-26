# results.py
from input_data import *
from definitions import print_table, save_output
from gurobipy import GRB
class FinalTable:
    def __init__(self, model,data, variables,num):
        self.model = model
        self.data=data
        self.new_proportions = variables['new_proportions']
        self.num=num

       

    def print_table(self):
        return print_table(self.model,self.data, self.new_proportions,self.num)

    def save_output(self, filename, content):
        save_output(filename, content)
