# definitions.py
import os
from gurobipy import Model, GRB
import logging,io,csv
import pandas as pd 


def create_trucks_vars(model,data):
    """"
    trucks[i,h,k]
    creates a new variable trucks which denotes number of trucks of type k delivered to location i on day h
    type:
    integer

    """
    return model.addVars(data.num_locations, data.num_days,len(data.truck_types), vtype=GRB.INTEGER, lb=0, name=f"number of trucks delivered to location i on day h by truck type k")

def create_select_vars(model,data):
    """"
    select[i,h]
    creates a new variable select  which denotes the whether location i selects pattern h or not 
    type:
    Binary

    """
    return model.addVars(data.num_locations, len(data.patterns), vtype=GRB.BINARY, name=f"whether location i selects pattern h or not ")

def create_min_trucks_vars(model,data):
    """"
    min_trucks
    creates a new variable min_10 denotes the min number of 15 trucks - 10 type trucks needed for satisfying all day requiremnets 
    type:
    Integer

    """
    return model.addVar(vtype=GRB.INTEGER, name=f"min trucks needed ")

# def create_min_15_trucks_vars(model,data):
#     """"
#     min_10
#     creates a new variable min_15 denotes the min number of 15 type trucks needed for satisfying all day requiremnets 
#     type:
#     Integer

#     """
#     return model.addVar(vtype=GRB.INTEGER, name=f"min 15 ton trucks")



def weekly_weight_requirement(model, data, trucks,select):
    """
    This constraint denotes that total weight delivered by both the trucks in a week is exactly equal to W[i]
    """
    for i in range(data.num_locations):
        weight=(data.W[i]//150)*150
        model.addConstr(sum(data.truck_types[t] * trucks[i, d, t] 
                                for d in range(data.num_days) 
                                for t in range(len(data.truck_types))) == weight, 
                    name=f"weekly_weight_{i}")
        
    logging.debug("weekly_weight_requirement")


def pattern_selcted(model, data, select):
    """"
    this constarint denotes which pattern is selected by location i
    """
    for i in range(data.num_locations):
        model.addConstr(sum(select[i, s] for s in range(4)) == 1, name=f"schedule_selection_{i}")
    logging.debug("pattern_selcted")


def pattern_requiremnets(model, data,trucks, select):
    """"
    this constarint denotes the weight requiremnts according to the pattern selected 
    """
    day_indices = {day: i for i, day in enumerate(data.days)}

    for i in range(data.num_locations):
        total_weight = (data.W[i]//150)*150
        for d in data.patterns[1]:
            #model.addConstr(sum(data.truck_types[t] * trucks[i, day_indices[d], t]  for t in range(len(data.truck_types))) >= total_weight * select[i, 1], name=f"once_a_week_{i}")
            model.addGenConstrIndicator(select[i, 1], True,
            sum(data.truck_types[t] * trucks[i, day_indices[d], t] for t in range(len(data.truck_types))) == total_weight, name=f"once_a_week_{i}")

        for d in data.patterns[2]:
            model.addGenConstrIndicator(select[i, 2], True,
            sum(data.truck_types[t] * trucks[i, day_indices[d], t] for t in range(len(data.truck_types))) == total_weight / 2, name=f"twice_a_week_{i}")

        for d in data.patterns[3]:
            model.addGenConstrIndicator(select[i, 3], True,
            sum(data.truck_types[t] * trucks[i, day_indices[d], t] for t in range(len(data.truck_types))) == total_weight / 3, name=f"thrice_a_week_{i}")

        for d in data.patterns[0]:
            model.addGenConstrIndicator(select[i, 0], True,
            sum(data.truck_types[t] * trucks[i, day_indices[d], t] for t in range(len(data.truck_types))) == total_weight / 5, name=f"five_a_week_{i}")
        
        logging.debug("pattern_requiremnets")
    
def min_requiremnets(model, data,trucks, min_trucks):
    """"
    this constarint denotes the min number of trucks requirement to satisfy the requiremnts over all days 
    """ 
    for j in range(data.num_days):
        #model.addConstr(min_10>=sum(trucks[i,j,1] for i in range(data.num_locations)))
        model.addConstr(min_trucks>=sum(trucks[i,j,0]-trucks[i,j,1] for i in range(data.num_locations)))
        model.addConstr(min_trucks>=-sum(trucks[i,j,0]-trucks[i,j,1] for i in range(data.num_locations)))
    

def set_objective_function(model, data, trucks,min_trucks):
    """
    The objective is to minimize the truck costs and also minimizing the total number of trucks 
    """
    model.setObjectiveN(sum(data.truck_costs[t] * trucks[i, d, t] 
                               for i in range(data.num_locations) 
                               for d in range(data.num_days) 
                               for t in range(len(data.truck_types))), priority=1, index=0, weight=1) 
    model.setObjectiveN(min_trucks,priority=2, index=0, weight=1)

    logging.debug("set_objective_function is used")


def save_output(filename, content):
    """
    saves the output in aiims/output folder 
    
    """
    os.makedirs("delivery system/outputs", exist_ok=True)
    with open(f"delivery system/outputs/{filename}", "w") as file:
        file.write(content)

import io
import csv

def print_table(model, data,trucks,select):
    model.optimize()
    if model.status == GRB.OPTIMAL:
        output = io.StringIO()
        writer = csv.writer(output)
        schedule_type = ["Five times a week", "Once a week", "Twice a week", "Thrice a week"]
        writer.writerow(['Location', 'Day', 'number of 15 trucks','number of 10 trucks', 'Pattern selected'])
        writer.writerow(["Optimal Profit",sum(data.truck_costs[t] * trucks[i, d, t].x 
                               for i in range(data.num_locations) 
                               for d in range(data.num_days) 
                               for t in range(len(data.truck_types)))])
        for i in range(data.num_locations):
            for d in range(data.num_days):
                if trucks[i,d,0].x + trucks[i,d,1].x >0:
                    row=[i,data.days[d],trucks[i,d,0].x,trucks[i,d,1].x]
                    for s in range(4):
                        if select[i,s].x>0:
                            row.append(schedule_type[s])
                    writer.writerow(row)
        
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
