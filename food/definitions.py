# definitions.py
import os
from gurobipy import Model, GRB
import logging,io,csv


def create_prepared_food_vars(model,data):
    """"
    prepare[i,h]
    creates a new variable prepare which denotes the amount of dish[i] prepared at hour h 
    type:
    integer

    """
    return model.addVars(data.num_dishes, data.num_hours, vtype=GRB.INTEGER, lb=0, name=f"amounnt of particular dish prepared at particular hour")

def create_inventory_vars(model,data):
    """"
    inventory[i,h]
    creates a new variable inventory  which denotes the amount of dish[i] already available  at hour h 
    type:
    integer

    """
    return model.addVars(data.num_dishes, data.num_hours, vtype=GRB.INTEGER, lb=0, name=f"amounnt of particular dish already available at particular hour")

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

def create_sold_vars(model,data):
    """"
    sold[i,h]
    creates a new variable prepare which denotes the amount of dish[i] sold at hour h 
    type:
    integer

    """
    return model.addVars(data.num_dishes, data.num_hours, vtype=GRB.INTEGER, lb=0, name=f"amounnt of particular dish sold at particular hour")
    logging.debug("new_price variable is declared")


def prepared_food_multiple_of_10(model, data, prepare):
    """"
    this constarint denotes that the quantity of dish[i] prepared at hour[h] is a multiple of 10
    """
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            dummy = model.addVar(lb=0, vtype=GRB.INTEGER, name=f'dish{i} hour{h}')
            model.addConstr(prepare[i, h] == 10 * dummy)
    logging.debug("prepared_food_multiple_of_10 is used ")

def wastage_before_span_life(model, data, waste):
    """"
    this constarint denotes that the quantity of dish[i] wasted at hour[h] before spanlife is 0
    """
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            if h<data.shelf_life[i]:
                model.addConstr(waste[i, h] == 0)
    logging.debug("wastage_before_span_life is used ")

def quantity_sold(model, data, sold,prepare,inventory):
    """"
    this constarint denotes that the quantity of dish[i] sold at hour[h] is less than or equal to requiremnent at that particulat hour and also the total available amount at that time
    """
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            if h<5:
                model.addConstr(sold[i,h]==0)
            else:
                model.addConstr(sold[i, h] <= data.requirement[i, h] )
                model.addConstr(sold[i, h] <= prepare[i, h] + inventory[i, h])
    logging.debug("quantity_sold is used ")

def unfull_filled_demand(model, data, sold,unfull,prepare):
    """"
    this constarint denotes that the quantity of dish[i] unfull filled  at hour[h] is the abs of required amount -  sold amount
    """
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            if h<5 :
                model.addConstr(unfull[i,h]==0)
            else:
                model.addConstr(unfull[i,h]>=data.requirement[i,h]-sold[i,h])
                #model.addConstr(unfull[i,h]>=-data.requirement[i,h]+sold[i,h])
    logging.debug("unfull_filled_demand is used ")

def inventory_available(model, data, sold,inventory,prepare,waste,unfull):
    """"
    this constarint denotes that the quantity of dish[i] already available  at the start of  hour[h] is the difference between the total prepared and (total sold,wasted)
    """
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            if h==0:
                model.addConstr(inventory[i,h]==0)
            elif h<=5:
                model.addConstr(inventory[i,h]==prepare[i,h-1]+inventory[i,h-1]-waste[i,h-1])
            else:
                #model.addConstr(inventory[i, h] == sum(prepare[i, t] - sold[i, t] - waste[i, t] for t in range(h)))
                model.addConstr(inventory[i,h]==prepare[i,h-1]+inventory[i,h-1]-sold[i,h-1]-waste[i,h-1])
    logging.debug("inventory_available is used ")

# def wastage_of_food(model, data,inventory,waste,sold,prepare):
#     """"
#     this constarint denotes that the quantity of dish[i] wasted  at hour[h] 
#     """
#     for i in range(data.num_dishes):
#         for h in range(data.num_hours):
#             if h >= data.shelf_life[i] and h<data.num_hours-1:
#                 #model.addConstr(waste[i, h] + waste[i, h - 1] == sum(inventory[i, t] for t in range(h - data.shelf_life[i]+1)))
#                 model.addConstr(waste[i, h]+waste[i,h-1]==  sum(prepare[i,t]-sold[i,t] for t in range(h - data.shelf_life[i]+1)) )
                
#             if h==data.num_hours-1:
#                 model.addConstr(waste[i,h]==prepare[i,h]-sold[i,h]+inventory[i,h])

            
            
            
#     logging.debug("wastage_of_food is used ")
def wastage_of_food(model, data, inventory, waste, sold, prepare):
    """
    This constraint denotes that the quantity of dish[i] wasted at hour[h] 
    is the food prepared before h - shelf_life[i] for dish i that remains.
    """
    shelflife=3
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            if h >= data.shelf_life[i]:
                # Total food prepared before hour h - shelf_life[i]
                expirehour = h - data.shelf_life[i] 
                
                
                
                # Total food carried forward (including from previous hour)
                total_prepare_forward = sum(prepare[i, t] for t in range(h - data.shelf_life[i] + 1,h))
                total_sold_forward = sum(sold[i, t] for t in range(h - data.shelf_life[i] + 1,h))
                
               
                
                # Waste calculation for the current hour h
                model.addConstr(inventory[i,expirehour]+waste[i,h]+total_prepare_forward-total_sold_forward==inventory[i,h])
            
            if h == data.num_hours - 1:
                # Ensure waste at the last hour accounts for any remaining food not sold
                model.addConstr(waste[i, h] == prepare[i, h] - sold[i, h] + inventory[i, h])




def set_objective_function(model, data, sold,waste,unfull ):
    """
    The objective is to determine the quantity prepared,sold,wasted in order to get maximum profits
    """
    profit_bysell = 0
    losswaste = 0
    losteunfill = 0
    for i in range(data.num_dishes):
        for h in range(data.num_hours):
            profit_bysell += data.profit[i] * sold[i, h]
            losswaste += data.loss_of_wastage[i] * waste[i, h]
            losteunfill += data.loss_of_demand[i] * unfull[i, h]
    model.setObjective(profit_bysell-losswaste-losteunfill, GRB.MAXIMIZE)
    logging.debug("set_objective_functio is used ")

def save_output(filename, content):
    """
    saves the output in aiims/output folder 
    
    """
    os.makedirs("food/outputs", exist_ok=True)
    with open(f"food/outputs/{filename}", "w") as file:
        file.write(content)

import io
import csv

def print_table(model, data, prepare, sold, waste, unfull, inventory):
    model.optimize()
    if model.status == GRB.OPTIMAL:
        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow(['Dish', 'Hour', 'Requirement', 'Prepare', 'Inventory', 'Waste', 'Unfilled', 'Sold'])

        for i in range(data.num_dishes):
            for h in range( data.num_hours):
                writer.writerow([
                    data.dishes[i],
                    h,
                    data.requirement[i, h],
                    prepare[i, h].X,
                    inventory[i, h].X,
                    waste[i, h].X,
                    unfull[i, h].X,
                    sold[i, h].X
                ])
        return output.getvalue()
    else:
        return "No optimal solution found."


def print_table1(model,data, prepare,sold,waste,unfull,inventory):
  model.optimize()
  if model.status == GRB.OPTIMAL:
      output = 'Solution:\n'
      output += f'Objective value = {model.objVal}\n\n'
      #output += f'Best bound = {model.ObjBound}\n\n'
      output += '{:<15} {:<15} {:<15}{:<15} {:<15} {:<15} {:<15} {:<15} \n'.format('Dish','Hour','Requirement','Prepare','Inventory','Waste','Unfilled','Sold')
      for i in range(data.num_dishes):
          for h in range(data.num_hours):
              output += '{:<15} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} \n'.format(data.dishes[i],h,data.requirement[i,h],prepare[i, h].X,inventory[i, h].X,waste[i, h].X, unfull[i, h].X,sold[i, h].X)
      return output
  else:
      return "No optimal solution found."
