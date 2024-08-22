# main.py

from gurobipy import Model
from input_data import InputData
from decision_variables import DecisionVariables
from constraints import Constraints
from objective import Objective
from results import FinalTable

def solve_problem():
    model = Model('Optimization Model')
    #model.Params.MIPGap = 0.0012
    data = InputData()
    decision_variables = DecisionVariables(model,data)
    decision_variables.create_variables()
    variables = decision_variables.get_variables()
    
    constraints = Constraints(model, data)
    constraints.add_constraints(variables['trucks'],variables['select'],variables['min_trucks'] )
    
    objective = Objective(model, data)
    objective.set_objective(variables['trucks'],variables['min_trucks'])

    final_table = FinalTable(model, variables,data)
    table_output = final_table.print_table()
    
    print(table_output)
    final_table.save_output('results.csv', table_output)

if __name__ == '__main__':
    solve_problem()
