# results.py

from definitions import print_table, save_output

class FinalTable:
    def __init__(self, model, variables,data):
        self.model = model
        self.data=data
        self.prepare=variables['prepare']
        self.sold=variables['sold']
        self.inventory=variables['inventory']
        self.waste=variables['waste']
        self.unfull=variables['unfull']

        

    def print_table(self):
        return print_table(self.model,self.data, self.prepare, self.sold,self.waste,self.unfull,self.inventory)

    def save_output(self, filename, content):
        save_output(filename, content)
