# definitions.py
import os
from gurobipy import Model, GRB

class InputData:
    def __init__(self):
        self.prices = [297, 720, 1050, 815]
        self.demand = [4820000, 320000, 210000, 70000]
        self.e = [0.4, 2.7, 1.1, 0.4, 0.1, 0.4]

def create_variables(model):
    data = InputData()
    variables = {
        'new_price': [model.addVar(lb=0, name=f"prices{i}") for i in range(4)],
        'new_demand': [model.addVar(lb=0, name=f"demand{i}") for i in range(4)]
    }
    model.update()
    return variables

def add_constraints(model, data, variables):
    model.addConstr(0.04 * variables['new_demand'][0] + 0.8 * variables['new_demand'][1] + 0.35 * variables['new_demand'][2] + 0.25 * variables['new_demand'][3] <= 600000)
    model.addConstr(0.09 * variables['new_demand'][0] + 0.02 * variables['new_demand'][1] + 0.3 * variables['new_demand'][2] + 0.4 * variables['new_demand'][3] <= 750000)
    
    for i in range(4):
        model.addConstr(1 - (variables['new_demand'][i] / data.demand[i]) == data.e[i] * ((variables['new_price'][i] / data.prices[i]) - 1))

    model.addConstr(1 - (variables['new_demand'][2] / data.demand[2]) == data.e[4] * (1 - (variables['new_price'][3] / data.prices[3])))
    model.addConstr(1 - (variables['new_demand'][3] / data.demand[3]) == data.e[5] * (1 - (variables['new_price'][2] / data.prices[2])))

    temp1 = sum(data.demand[i] * variables['new_price'][i] for i in range(4))
    temp2 = sum(data.demand[i] * data.prices[i] for i in range(4))
    model.addConstr(temp1 <= temp2)

def save_output(filename, content):
    os.makedirs("aiims/outputs", exist_ok=True)
    with open(f"aiims/outputs/{filename}", "w") as file:
        file.write(content)

def print_table(model, variables):
    model.optimize()
    if model.status == GRB.OPTIMAL:
        output = 'Solution:\n'
        output += f'Objective value = {model.objVal}\n\n'
        for i in range(4):
            output += f'new_demand: {variables["new_demand"][i].x}\n'
            output += f'new_prices: {variables["new_price"][i].x}\n'
        return output
    else:
        return "No optimal solution found."

def set_objective(model, data, variables):
    model.setObjective(sum(data.demand[i] * (1 - data.e[i] * (-1 + (variables['new_price'][i] / data.prices[i]))) * variables['new_price'][i] for i in range(4)), GRB.MAXIMIZE)
