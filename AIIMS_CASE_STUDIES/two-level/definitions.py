import os
from gurobipy import GRB, QuadExpr

def create_new_waste_vars(model):
    """
    Creates new waste variables for the model which represents the removal of waste water by j (company j)
    Type: Continuous
    """
    return [model.addVar(name=f"waste{i}", vtype=GRB.CONTINUOUS) for i in range(4)]

def total_waste_limit(model, data, new_waste):
    """
    The total waste limitation constraint requires that the annual amount of waste 
    dumped into the river is less than or equal to the target level.
    """
    model.addConstr(sum(data.waste[i] * (data.concentration[i] - new_waste[i]) for i in range(4)) <= data.target)

def set_objective_function(model, data, new_waste):
    """
    Sets the objective function for minimizing the cost. The function handles quadratic objectives.
    """
    expr = QuadExpr()
    
    # Build the objective function
    for i in range(4):
        expr.add(data.waste[i] * (data.tax * (data.concentration[i] - new_waste[i]) - new_waste[i]) ** 2)
    
    model.setObjective(expr, GRB.MINIMIZE)

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
        output = f'Objective value = {model.objVal:.2f}\n'
        output += "Variables:\n"
        for var in new_waste:
            output += f"{var.varName} = {var.x:.2f}\n"
        return output
    else:
        return "No optimal solution found."
