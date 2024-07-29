# definitions.py
import os
from gurobipy import Model, GRB
import logging


def create_new_price_vars(model):
    """"
    new_price[i]
    creates a new price variable which denotes the new_price of the item[i] at present
    type:
    continous

    """
    logging.debug("new_price variable is declared")
    return [model.addVar(lb=0, name=f"prices{i}") for i in range(4)]

def create_new_demand_vars(model):
    """"
    new_demand[i]
    creates a new demand variable which denotes the new_demand of the item[i] at present
    type:
    continous

    """
    logging.debug("new_demand variable is declared")
    return [model.addVar(lb=0, name=f"demand{i}") for i in range(4)]

def max_availability_fat(model, data, new_demand):
    """"
    this constarint denotes the maximum availability of fat that is used to make the items 
    """
    logging.debug("add_constarint_1 is used ")
    model.addConstr(0.04 * new_demand[0] + 0.8 * new_demand[1] + 0.35 * new_demand[2] + 0.25 * new_demand[3] <= 600000)

def max_availability_dry(model, data, new_demand):
    """"
    this constarint denotes the maximum availability of dry matter that is used to make the items 
    """
    logging.debug("add_constarint_2 is used ")
    model.addConstr(0.09 * new_demand[0] + 0.02 * new_demand[1] + 0.3 * new_demand[2] + 0.4 * new_demand[3] <= 750000)

def price_elasticity(model, data, new_price, new_demand):
    """
    this constraint denotes the price elasticity of the item 
    E = Percentage decrease in demand/Percentage increase in price .

    """
    logging.debug("add_constarint_3 is used ")
    for i in range(4):
        model.addConstr(1 - (new_demand[i] / data.demand[i]) == data.e[i] * ((new_price[i] / data.prices[i]) - 1))

def cross_elasticity(model, data, new_price, new_demand):
    """

    this constraint denotes the cross-price elasticity between two items A and B
    E_AB = Percentage increase in demand for A/Percentage increase in price of B .

    """
    logging.debug("add_constarint_4 is used ")
    model.addConstr(1 - (new_demand[2] / data.demand[2]) == data.e[4] * (1 - (new_price[3] / data.prices[3])))
    model.addConstr(1 - (new_demand[3] / data.demand[3]) == data.e[5] * (1 - (new_price[2] / data.prices[2])))

def demand_limitation(model, data, new_price):
    """
    limitation simply demands
that the new prices must be such that the total cost of last year’s consumption
would not be increased.
    """
    logging.debug("add_constarint_5 is used ")
    temp1 = sum(data.demand[i] * new_price[i] for i in range(4))
    temp2 = sum(data.demand[i] * data.prices[i] for i in range(4))
    model.addConstr(temp1 <= temp2)

def set_objective_function(model, data, new_price):
    """
    The objective is to determine what prices and resultant demand will maximise
the total revenue
    """
    logging.debug("constraint is used ")
    model.setObjective(sum(data.demand[i] * (1 - data.e[i] * (-1 + (new_price[i] / data.prices[i]))) * new_price[i] for i in range(4)), GRB.MAXIMIZE)

def save_output(filename, content):
    """
    saves the output in aiims/output folder 
    
    """
    os.makedirs("AIIMS_CASE_STUDIES/agriculture/outputs", exist_ok=True)
    with open(f"AIIMS_CASE_STUDIES/agriculture/outputs/{filename}", "w") as file:
        file.write(content)

def print_table(model, new_price, new_demand):
    model.optimize()
    if model.status == GRB.OPTIMAL:
        output = 'Solution:\n'
        output += f'Objective value = {model.objVal}\n\n'
        #output += f'Best bound = {model.ObjBound}\n\n'
        output += '{:<15} {:<15} {:<15}\n'.format('Item', 'New Demand', 'New Price')
        Food=['Milk','Butter','cheese 1','Cheese 2']
        for i, item in enumerate(Food):
            output += '{:<15} {:<15.2f} {:<15.2f}\n'.format(item, new_demand[i].x, new_price[i].x)
        return output
    else:
        return "No optimal solution found."
