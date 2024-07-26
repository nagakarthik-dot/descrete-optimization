# definitions.py
import os
from gurobipy import Model, GRB
import logging


def create_new_proportions_vars(model,data):
    """"
    new_price[i]
    creates a new proportions variable which denotes the weightage of inputs and outputs for each dmu 
    type:
    continous
    """
    e=10**-6
    return [model.addVar(lb=0,vtype=GRB.CONTINUOUS, name=f"PROPORTIONS{i}") for i in range(6)]
    logging.debug("new_servings variable is declared")


def efficiency(model, data, new_proportions,num):
    """"
    this constarint denotes that efficiency is less than 1
    """
    ##model.addConstr(sum(new_proportions[i]*int(data.weightage[num][i]) for i in range(4,6))<=sum(new_proportions[i]*int(data.weightage[num][i]) for i in range(4)))
    model.addConstr(sum(new_proportions[i]*int(data.weightage[num][i]) for i in range(4,6))<=1)
    #model.addConstr(sum(new_servings[i]*data.calories[i] for i in range(len(data.items)))<=117)
    logging.debug("efficiency is used ")

def weightage_proportion_input(model, data, new_proportions,num):
    """"
    this constarint denotes that efficiency weighatge of inputs sums to 1
    """
    model.addConstr(sum(new_proportions[i]*int(data.weightage[num][i]) for i in range(4))==1)
    #model.addConstr(sum(new_servings[i]*data.calories[i] for i in range(len(data.items)))<=117)
    logging.debug("efficiency  input is used ")



def set_objective_function(model, data, new_proportions,num):
    """
    the objective is Maximize: relative efficiency measure for a particular DMU,
    """
    logging.debug("constraint is used ")
    model.setObjective(sum(new_proportions[i]*int(data.weightage[num][i]) for i in range(4,6)), GRB.MAXIMIZE)

def save_output(filename, content):
    """
    saves the output in aiims/output folder 
    
    """
    os.makedirs("performance/outputs", exist_ok=True)
    with open(f"performance/outputs/{filename}", "w") as file:
        file.write(content)

def print_table(model, data, new_proportions, num):
    """Print table with results"""
    model.optimize()
    if model.status == GRB.OPTIMAL:
        output = 'Solution:\n'
        output += f'Objective value for dmu_{num+1} = {model.objVal}\n\n'
        output += 'Proportions:\n'
        for v in model.getVars():
            output += f'{v.varName}: {v.x}\n'
        return output
    else:
        return f"No optimal solution found. Status: {model.status}"