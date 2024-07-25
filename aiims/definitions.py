# definitions.py
import os
from gurobipy import Model, GRB

class InputData:
    def __init__(self):
        self.prices = [297, 720, 1050, 815]
        self.demand = [4820000, 320000, 210000, 70000]
        self.e = [0.4, 2.7, 1.1, 0.4, 0.1, 0.4]

def create_new_price_vars(model):
    return [model.addVar(lb=0, name=f"prices{i}") for i in range(4)]

def create_new_demand_vars(model):
    return [model.addVar(lb=0, name=f"demand{i}") for i in range(4)]

def add_constraints_1(model, data, new_demand):
    model.addConstr(0.04 * new_demand[0] + 0.8 * new_demand[1] + 0.35 * new_demand[2] + 0.25 * new_demand[3] <= 600000)

def add_constraints_2(model, data, new_demand):
    model.addConstr(0.09 * new_demand[0] + 0.02 * new_demand[1] + 0.3 * new_demand[2] + 0.4 * new_demand[3] <= 750000)

def add_constraints_3(model, data, new_price, new_demand):
    for i in range(4):
        model.addConstr(1 - (new_demand[i] / data.demand[i]) == data.e[i] * ((new_price[i] / data.prices[i]) - 1))

def add_constraints_4(model, data, new_price, new_demand):
    model.addConstr(1 - (new_demand[2] / data.demand[2]) == data.e[4] * (1 - (new_price[3] / data.prices[3])))
    model.addConstr(1 - (new_demand[3] / data.demand[3]) == data.e[5] * (1 - (new_price[2] / data.prices[2])))

def add_constraints_5(model, data, new_price):
    temp1 = sum(data.demand[i] * new_price[i] for i in range(4))
    temp2 = sum(data.demand[i] * data.prices[i] for i in range(4))
    model.addConstr(temp1 <= temp2)

def set_objective_function(model, data, new_price):
    model.setObjective(sum(data.demand[i] * (1 - data.e[i] * (-1 + (new_price[i] / data.prices[i]))) * new_price[i] for i in range(4)), GRB.MAXIMIZE)

def save_output(filename, content):
    os.makedirs("aiims/outputs", exist_ok=True)
    with open(f"aiims/outputs/{filename}", "w") as file:
        file.write(content)

def print_table(model, new_price, new_demand):
    model.optimize()
    if model.status == GRB.OPTIMAL:
        output = 'Solution:\n'
        output += f'Objective value = {model.objVal}\n\n'
        for i in range(4):
            output += f'new_demand: {new_demand[i].x}\n'
            output += f'new_prices: {new_price[i].x}\n'
        return output
    else:
        return "No optimal solution found."
