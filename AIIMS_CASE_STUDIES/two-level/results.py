import matplotlib.pyplot as plt
from definitions import save_output, print_table
from gurobipy import GRB

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
        tax = 0.1
        tax_rates = []
        objective_values = []
        
        while tax < 0.5:
            self.data.tax = tax
            tax_rates.append(tax)
            self.model.optimize()
            
            if self.model.status == GRB.OPTIMAL:
                objective_values.append((self.model.objVal)*10000)
            else:
                objective_values.append(float('inf'))
                
            tax += 0.05
        
        plt.figure(figsize=(10, 6))
        plt.plot(tax_rates, objective_values, marker='o', linestyle='-', color='b')
        plt.xlabel('Tax Rate')
        plt.ylabel('Objective Value')
        plt.title('Objective Value vs. Tax Rate')

        if objective_values:
            y_min = min(objective_values)
            y_max = max(objective_values)
            plt.ylim(bottom=y_min, top=y_max)

        plt.grid(True)
        plt.show()
