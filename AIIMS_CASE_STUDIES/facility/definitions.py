# definitions.py
import os
from gurobipy import Model, GRB
import logging
import math

def k_pdz(point1,point2,point3):
    return (math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)+math.sqrt((point3[0]-point2[0])**2+(point3[1]-point2[1])**2))/100

def create_quantity_vars(model,data):
    """"
    x c|p|d|z represents the nonnegative amount of commodity c shipped from plant
p via distribution center d to customer zone z
type:
integer
    """
    return [[[[model.addVar(lb=0,vtype=GRB.INTEGER,name=f'quantity of {i} from {j} through {k} to {l}') for l in range(data.z) ] for k in range(data.d)] for j in range(data.p)] for i in range(data.c)]

def create_distribution_center_vars(model,data):
    """
    v d depresents the binary variables describing whether the location d if distribution centre is there or not 
    type: Binary
    """

    return [model.addVar(vtype=GRB.BINARY,name=f'distribution {i} is open ') for i in range(data.d)]

def create_customer_pref_vars(model,data):
    """
    y d|z denotes the binary to indicate that customer zone z is served by distribution center d
    type: Binary
    """

    return [[model.addVar(vtype=GRB.BINARY, name=f'customer {i} got through distribution {j}') for i in range(data.z)] for j in range(data.d)]


def supply(model, data, x):
    """"
    this constarint denotes that amount of commodity c shipped from plant
p via distribution center d to customer zone z satisfies the supply  from plant 
    """
    for i in range(data.c):
        for j in range(data.p):
            quantity=0
            for k in range(data.d):
                for l in range(data.z):
                    quantity+=x[i][j][k][l]
            model.addConstr(quantity<=data.s_cp[i][j])

def demand(model,data,x,y):
    """"
    this constarint denotes that amount of commodity c shipped from plant
p via distribution center d to customer zone z satisfies the demand  from customerzone 
    """
    for i in range(data.c):
        for l in range(data.z):
            quantity=0
            for j in range(data.p):
                for k in range(data.d):
                    quantity+= x[i][j][k][l]
            model.addConstr(quantity>=data.d_cz[i][l])

def supply_zone_count(model,data,y):
    """
    this constarints ansures that each customer gets form exactly one distribution 
    """
    for i in range(data.z):
        model.addConstr(sum(y[j][i] for j in range(data.d))==1)

def distribution_supply(model, data, x, v):
    """
    This constraint ensures that for each distribution location, the total amount
    of supply to customers is between the maximum and minimum demand.
    """
    for i in range(data.d):
        quantity = 0
        for j in range(data.c):
            for k in range(data.p):
                for l in range(data.z):
                    quantity += x[j][k][i][l]
        # Access individual max_d[i] and min_d[i] instead of the whole list
        model.addConstr(quantity <= data.max_d[i] * v[i])
        model.addConstr(quantity >= data.min_d[i] * v[i])


def distribution_customer(model,data,y,v):
    """
    this shows that a distribution can serve the customer only if the center of distributionid open 
    """
    for i in range(data.d):
        for j in range(data.z):
            model.addConstr(y[i][j]<=v[i])

def distribution(model,data,x,y):
    """
    this ensures that for a particular commodity,distribution center and zone the total quantity must meet the demand * whether it ois served by the distribution center 
    """
    for i in range(data.c):
        for k in range(data.d):
            for l in range(data.z):
                quantity=0
                for j in range(data.p):
                    quantity+=x[i][j][k][l]*y[k][l]
                model.addConstr(quantity>=data.d_cz[i][l]*y[k][l])


def set_objective_function(model, data, x,y,v):
    """
    The objective function that is to be minimized is essentially the addition of
production and transportation costs augmented with the fixed and variable
charges for distribution centers and the throughput of commodities through
these centers.
    """
    logging.debug("constraint is used ")
    result=0
    for i in range(data.c):
        for j,point1 in enumerate(data.lp):
            for k,point2 in enumerate(data.ld):
                for l,point3 in enumerate(data.lc):
                    result+=k_pdz(point1,point2,point3)*x[i][j][k][l]
                    result+=data.f_d[k]*v[k]
    for i in range(data.d):
        temp=0
        for j in range(data.c):
            for k in range(data.z):
                temp+=data.d_cz[j][k]*y[i][k]
        result+=temp*data.r_d[i]
    model.setObjective(result, GRB.MINIMIZE)


def save_output(filename, content):
    """
    saves the output in aiims/output folder 
    
    """
    os.makedirs("AIIMS_CASE_STUDIES/facility/outputs", exist_ok=True)
    with open(f"AIIMS_CASE_STUDIES/facility/outputs/{filename}", "w") as file:
        file.write(content)

def print_table(model, data,x,y,v):
    model.optimize()
    if model.status == GRB.OPTIMAL:
        output = 'Solution:\n'
        output += f'Objective value = {model.objVal}\n\n'
        #output += f'Best bound = {model.ObjBound}\n\n'
        output += '{:<15} {:<15} {:<15} {:<15} {:<15}\n'.format('Commodities', 'Production Plant' ,"Distribution Center","Customer ","Quantity" )
        pro=["Arnhem","Rotterdam"]
        com=[" Product a","Product b"]
        distri=["Amsterdam","The Hague","Utrecht ","Gouda","Amersfoort","Zwolle ","Nijmegen"]
        cus=["Maastricht","Haarlem","Groningen"]
        for i in range(2):
            for j in range(2):
                for k in range(7):
                    for l in range(3):
                        if x[i][j][k][l].x>0.5:
                            #print(x[i][j][k][l].x)
                            output += '{:<15} {:<15} {:<15} {:<15} {:<15.2f} \n'.format(com[i], pro[j],distri[k],cus[l],x[i][j][k][l].x)
        return output
        
    else:
        return "No optimal solution found."
