# results.py
from input_data import *
from definitions import print_table, save_output

class FinalTable:
    def __init__(self, model,data, variables):
        self.model = model
        self.data=data
        self.x=variables['x']
        self.y=variables['y']
        self.v=variables['v']
        

    def print_table(self):
        return print_table(self.model,self.data, self.x,self.y,self.v)

    def save_output(self, filename, content):
        save_output(filename, content)
