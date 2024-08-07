import os
from gurobipy import Model, GRB
import logging
import matplotlib.pyplot as plt
import numpy as np

def create_new_waste_vars(model):
    """
    Creates new waste variables for the model.
    Type: Continuous
    """
    logging.debug("new_waste variable is declared")
    return [model.addVar(name=f"waste{i}", vtype=GRB.CONTINUOUS) for i in range(4)]

def total_waste_limit(model, data, new_waste):
    """
    The total waste limitation constraint requires that the annual amount of waste 
    dumped into the river is less than or equal to the target level.
    """
    logging.debug("total_waste_limit constraint is added")
    model.addConstr(sum(data.waste[i] * (data.concentration[i] - new_waste[i]) for i in range(4)) <= data.target)

def set_objective_function(model, data, new_waste):
    """
    Sets the objective function for minimizing the cost.
    """
    tax = (data.target + data.subsidy * sum(data.waste[i] * new_waste[i] for i in range(4))) / \
          sum(data.waste[i] * (data.concentration[i] - new_waste[i]) for i in range(4))

    objective = GRB.INFINITY
    for i in range(4):
        temp = data.waste[i] * ((data.eff[i] / (data.concentration[i] - new_waste[i])) - 
                                (data.eff[i] / data.concentration[i]) + tax * (data.concentration[i] - new_waste[i]) - 
                                data.subsidy * new_waste[i])
        objective = min(objective, temp)
    model.setObjective(objective, GRB.MINIMIZE)

def save_output(filename, content):
    """
    Saves the output in the specified folder.
    """
    os.makedirs("AIIMS_CASE_STUDIES/two-level/outputs", exist_ok=True)
    with open(f"AIIMS_CASE_STUDIES/two-level/outputs/{filename}", "w") as file:
        file.write(content)

def print_table(model, new_waste, data):
    """
    Iterates through different subsidy rates, prints results, and plots a graph.
    """
    model.optimize()
    if model.status == GRB.OPTIMAL:
        subsidy_rates = np.arange(0.05, 0.30, 0.05)  # Iterate through subsidy rates from 0.05 to 0.30
        results = []
        
        # Specify the company index you want to focus on, for example, 0 for the first company
        company_index = 0

        for subsidy in subsidy_rates:
            data.subsidy = subsidy
            # Re-calculate the objective function with the new subsidy rate
            set_objective_function(model, data, new_waste)
            model.optimize()
            
            if model.status == GRB.OPTIMAL:
                output = f'Subsidy rate = {subsidy:.2f}\n'
                output += f'Objective value = {model.objVal:.2f}\n\n'
                output += '{:<15} {:<15} {:<15}\n'.format('Item', 'New Demand', 'New Price')
                
                # Update Food list to reflect actual items
                Food = ['Milk', 'Butter', 'Cheese 1', 'Cheese 2']
                
                for i, item in enumerate(Food):
                    output += '{:<15} {:<15.2f} {:<15.2f}\n'.format(item, new_waste[i].x, new_waste[i].x)  # Assuming 'new_waste[i].x' represents new price
                
                results.append((subsidy, model.objVal))
                print(output)  # Print results to console
            else:
                print(f"No optimal solution found for subsidy rate {subsidy:.2f}")
        
        # Plot results for the specified company
        plt.figure(figsize=(10, 6))
        subsidies, objectives = zip(*results)
        plt.plot(subsidies, objectives, marker='o', linestyle='-', color='b')
        plt.xlabel('Subsidy Rate')
        plt.ylabel('Objective Value')
        plt.title(f'Objective Value vs. Subsidy Rate for Company {company_index + 1}')
        plt.grid(True)
        plt.savefig('AIIMS_CASE_STUDIES/two-level/outputs/objective_vs_subsidy.png')
        plt.show()
        
    else:
        print("No optimal solution found.")
