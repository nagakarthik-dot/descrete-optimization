# definitions.py
import os
from gurobipy import Model, GRB
import logging


def create_stocks_invest_vars(model,data):
    """"
    new_price[i]
    creates a new variable that denotes the fraction of stock i that is invested 
    type:
    continous
    """
    return [model.addVar(lb=0,ub=1,vtype=GRB.CONTINUOUS, name=f"fraction of stock{i} invested ") for i in range(len(data.items))]


def total_fraction_of_stocks(model, data, new_stocks_invest):
    """"
    this constarint denotes that total fraction of stocks that are being invested is equal to one 
    """
    model.addConstr(sum(new_stocks_invest[i] for i in range(len(data.items)))==1)
    #model.addConstr(sum(new_servings[i]*data.calories[i] for i in range(len(data.items)))<=117)
    logging.debug("total fraction of stocks  is used ")

def desired_returns(model, data, new_stocks_invest):
    """"
    this constarint denotes that total expeted returns on all stocks is gretaer than the desired 
    """
    model.addConstr(sum(new_stocks_invest[i]*data.expected[i] for i in range(len(data.items)))>=data.desired)
    #model.addConstr(sum(new_servings[i]*data.protein[i] for i in range(len(data.items)))<=117)
    logging.debug("desired_returns is used ")



def set_objective_function(model, data, new_stocks_invest):
    """
    Minimize: the total risk of the portfolio
    """
    total=0
    for i in range(len(data.items)):
        for j in range(len(data.items)):
            total+=new_stocks_invest[i]*data.cov[i][j]*new_stocks_invest[j]

    model.setObjective(total, GRB.MINIMIZE)

def save_output(filename, content):
    """
    saves the output in aiims/output folder 
    
    """
    os.makedirs("AIIMS_CASE_STUDIES/portfolio/outputs", exist_ok=True)
    with open(f"AIIMS_CASE_STUDIES/portfolio/outputs/{filename}", "w") as file:
        file.write(content)

def print_table(model, data,new_stocks_invest):
    model.optimize()
    if model.status == GRB.OPTIMAL:
        output = 'Solution:\n'
        output += f'Objective value = {model.objVal}\n\n'
        #output += f'Best bound = {model.ObjBound}\n\n'
        output += '{:<15} {:<15}\n'.format('Item', 'stock fraction ' )
        Food=data.items
        for i, item in enumerate(Food):
            output += '{:<15} {:<15.2f} \n'.format(item, new_stocks_invest[i].x)
        return output
    else:
        return "No optimal solution found."
