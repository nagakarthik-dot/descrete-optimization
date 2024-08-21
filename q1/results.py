# results.py

from definitions import *

class FinalTable:
    def __init__(self, model, variables,data):
        self.model = model
        self.data=data
        self.prepare=variables['prepare']
        self.used=variables['used']
        
        self.waste=variables['waste']
        self.unfull=variables['unfull']

        

    def print_table(self):
        return print_table(self.model,self.data, self.prepare, self.used,self.waste,self.unfull)
    def print_table1(self):
        return 

    def save_output(self, filename, content):
        save_output(filename, content)
