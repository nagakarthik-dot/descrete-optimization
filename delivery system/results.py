# results.py

from definitions import *

class FinalTable:
    def __init__(self, model, variables,data):
        self.model = model
        self.data=data
        self.trucks=variables['trucks']
        self.select=variables['select']
        
        self.min_trucks=variables['min_trucks']

        

    def print_table(self):
        return print_table(self.model,self.data, self.trucks, self.select)
    

    def save_output(self, filename, content):
        save_output(filename, content)
