import matplotlib.pyplot as plt
from definitions import save_output, print_table
import numpy as np
from gurobipy import GRB

import matplotlib.pyplot as plt

class FinalTable:
    def __init__(self, model, variables, data):
        self.model = model
        self.new_waste = variables['new_waste']
        self.data = data

    def print_table(self):
        return print_table(self.model, self.new_waste, self.data)

    def save_output(self, filename, content):
        save_output(filename, content)

    def plot_results(self):
        # Example data for plotting
        tax_rates = [0.1, 0.5, 0.01]  # Replace with your actual tax rates
        objective_values = []
        for tax in tax_rates:
            self.data.tax = tax
            self.model.optimize()
            if self.model.status == GRB.OPTIMAL:
                objective_values.append(self.model.objVal)
            else:
                objective_values.append(float('inf'))


        plt.figure(figsize=(10, 6))
        plt.plot(tax_rates, objective_values, marker='o', linestyle='-', color='b')
        plt.xlabel('Tax Rate')
        plt.ylabel('Objective Value')
        plt.title('Objective Value vs. Tax Rate')
        
        # Add buffer to y-axis limits to avoid identical limits
      
        
        plt.grid(True)
        plt.show()
