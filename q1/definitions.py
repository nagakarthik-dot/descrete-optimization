# definitions.py
import os
from gurobipy import Model, GRB
import logging,io,csv
import pandas as pd 


def create_prepared_food_vars(model,data):
    """"
    prepare[i,h]
    creates a new variable prepare which denotes the amount of dish[i] prepared at hour h 
    type:
    integer

    """
    return model.addVars(data.num_dishes, data.num_hours, vtype=GRB.INTEGER, lb=0, name=f"amounnt of particular dish prepared at particular hour")

def create_used_vars(model,data):
    """"
    used[i,h,k]
    creates a new variable inventory  which denotes the amount of dish[i] sold   at hour k that is prepared at hour h 
    type:
    integer

    """
    return model.addVars(data.num_dishes, data.num_hours,data.num_hours, vtype=GRB.INTEGER, lb=0, name=f"amounnt of particular dish already available at particular hour")

def create_wastage_of_food_vars(model,data):
    """"
    waste[i,h]
    creates a new variable waste which denotes the amount of dish[i] wasted at hour h 
    type:
    integer

    """
    return model.addVars(data.num_dishes, data.num_hours, vtype=GRB.INTEGER, lb=0, name=f"amounnt of particular dish wasted at particular hour")

def create_unfullfilleded_demand_vars(model,data):
    """"
    unfull[i,h]
    creates a new variable unfull which denotes the amount of dish[i] un full filled  at hour h 
    type:
    integer

    """
    return model.addVars(data.num_dishes, data.num_hours, vtype=GRB.INTEGER, lb=0, name=f"amounnt of particular dish unfull filled at particular hour")
    logging.debug("new_price variable is declared")


def prepared_food_multiple_of_10(model, data, prepare, used,unfull,waste):
    """
    This constraint denotes that the quantity of dish[i] prepared at hour[h] is a multiple of 10
    and matches the used quantity over the shelf life period.
    """
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            dummy = model.addVar(lb=0, vtype=GRB.INTEGER, name=f'dish{i}_hour{h}')
            model.addConstr(prepare[i, h] == 10 * dummy)
            
    logging.debug("prepared_food_multiple_of_10 is used ")


def quantity_sold(model, data, used,prepare):
    """"
    this constarint denotes that the quantity of dish[i] sold at hour[h] is less than or equal to requiremnent at that particulat hour and also the total available amount at that time
    """
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            inventory_avail=0
            for j in range(h):
                for k in range(h,data.num_hours):
                    inventory_avail+=used[i,j,k]

            inventory_future=0
            sold=0
            for k in range(data.num_hours):
                ## before fifth hour there is no requirement 
                if h<5 and k<5:
                    model.addConstr(used[i,h,k]==0)
                ## if a dish is 
                ##if k not in range(h,h+data.shelf_life[i]+1):
                if not (k>=h and k<=h+(data.shelf_life[i])):
                    model.addConstr(used[i,h,k]==0)
                if k<=h+(data.shelf_life[i]) and k>h :
                    inventory_future+=used[i,h,k]
                if k<=h and k>=h-(data.shelf_life[i]-1) :
                    sold+=used[i,k,h]
            
            
            
            model.addConstr(sold<=data.requirement[i,h])
            model.addConstr(sold<=prepare[i,h]+inventory_avail)
            model.addConstr(prepare[i,h]==used[i,h,h]+inventory_future)

def unfull_filled_demand(model, data, used,unfull):
    """"
    this constarint denotes that the quantity of dish[i] unfull filled  at hour[h] is the abs of required amount -  sold amount
    """
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            sold=0
            for k in range(data.num_hours):
                if k<=h and k>=h-(data.shelf_life[i]-1):
                    sold+=used[i,k,h]
            model.addConstr(unfull[i,h]>=data.requirement[i,h]-sold)
          
    logging.debug("unfull_filled_demand is used ")

def wastage_of_food(model, data, waste, used):
    """
    This constraint denotes that the quantity of dish[i] wasted at hour[h] 
    is the food prepared before h - shelf_life[i] for dish i that remains.
    """
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            if h<data.shelf_life[i]:
                model.addConstr(waste[i,h]==0)
            if h >= data.shelf_life[i]:
                model.addConstr(waste[i,h]==used[i,h-(data.shelf_life[i]),h])

def set_objective_function(model, data, used, waste, unfull):
    """
    The objective is to determine the quantity prepared, sold, wasted in order to get maximum profits
    while also minimizing the total wastage.
    """
    profit_bysell = 0
    losswaste = 0
    losteunfill = 0
    
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            for k in range(h - (data.shelf_life[i] - 1), h + 1):
                if k >= 0:
                    profit_bysell += data.profit[i] * used[i, k, h]
            losswaste += data.loss_of_wastage[i] * waste[i,h]
            losteunfill += data.loss_of_demand[i] * unfull[i, h]
          

    model.setObjective(
        (profit_bysell - losswaste - losteunfill) ,
        GRB.MAXIMIZE
    )
    logging.debug("set_objective_function is used")


def save_output(filename, content):
    """
    saves the output in aiims/output folder 
    
    """
    os.makedirs("q1/outputs", exist_ok=True)
    with open(f"q1/outputs/{filename}", "w") as file:
        file.write(content)

import io
import csv

def print_table(model, data, prepare, used, waste, unfull):
    model.optimize()
    if model.status == GRB.OPTIMAL:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Dish', 'Hour', 'Requirement', 'Prepare','inventory available', 'Waste', 'Unfilled', 'used'])
        writer.writerow(["Optimal Profit", model.objVal])
        for i in range(data.num_dishes):
            for h in range(data.num_hours):
                sold=0 
                inventory=0 
                for k in range(data.num_hours):
                    if k<=h and k>=h-(data.shelf_life[i]-1) and k>=0:
                        sold+=used[i,k,h].X
                for j in range(h):
                    for k in range(h,data.num_hours):
                        inventory+=used[i,j,k].X
                writer.writerow([
                    data.dishes[i],
                    h,
                    data.requirement[i, h],
                    prepare[i, h].X,
                    inventory,
                    waste[i,h].X,
                    unfull[i, h].X,
                    sold
                ])
        
        return output.getvalue()
    else:
        return "No optimal solution found."


# def print_table1(model,data, prepare,sold,waste,unfull,inventory):
#   model.optimize()
#   if model.status == GRB.OPTIMAL:
#       output = 'Solution:\n'
#       output += f'Objective value = {model.objVal}\n\n'
#       #output += f'Best bound = {model.ObjBound}\n\n'
#       output += '{:<15} {:<15} {:<15}{:<15} {:<15} {:<15} {:<15} {:<15} \n'.format('Dish','Hour','Requirement','Prepare','Inventory','Waste','Unfilled','Sold')
#       for i in range(data.num_dishes):
#           for h in range(data.num_hours):
#               output += '{:<15} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} \n'.format(data.dishes[i],h,data.requirement[i,h],prepare[i, h].X,inventory[i, h].X,waste[i, h].X, unfull[i, h].X,sold[i, h].X)
#       return output
#   else:
#       return "No optimal solution found."
