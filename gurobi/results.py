# results.py

import os
from gurobipy import GRB

class FinalTable:
    def __init__(self, model, variables, problem):
        self.model = model
        self.variables = variables
        self.problem = problem
        self.months = ["January", "February", "March", "April", "May", "June"]
        self.products1 = ["veg 1", "veg 2", "oil 1", "oil 2", "oil 3"]
        self.products2 = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5", "Product 6", "Product 7"]

    def save_output(self, filename, content):
        os.makedirs("gurobi/outputs", exist_ok=True)
        with open(f"gurobi/outputs/{filename}", "w") as file:
            file.write(content)

    def print_table(self):
        self.model.optimize()
        if self.model.status == GRB.OPTIMAL:
            output = 'Solution:\n'
            output += f'Objective value = {self.model.objVal}\n\n'
            #problem = self.variables['problem']
            
            if self.problem == 1 or self.problem == 2:
                header = "Month       " + "  ".join([f"{prod:<10}" for prod in self.products1]) + '\n'
                output += header
                
                for i, month in enumerate(self.months):
                    item_row = f"{month:<12}" + "  ".join([f"{self.variables['buy'][i][j].x:<10.2f}" for j in range(5)]) + '\n'
                    sell_row = f"{'':<12}" + "  ".join([f"{self.variables['used'][i][j].x:<10.2f}" for j in range(5)]) + '\n'
                    store_row = f"{'':<12}" + "  ".join([f"{self.variables['store'][i][j].x:<10.2f}" for j in range(5)]) + '\n'
                    
                    output += item_row
                    output += sell_row
                    output += store_row
                    output += "-" * len(header) + '\n'
                ##return output
            
                    
                self.save_output(f'problem_{self.problem}.txt', output)
            if self.problem==21:
                for i in  range(4):
                    output+=f'new_demand: {self.variables['new_demand'][i].x}'+'\n'
                    output+=f'new_prices: {self.variables['new_price'][i].x}'+'\n'
                self.save_output(f'problem_{self.problem}.txt', output)
