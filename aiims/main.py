# main.py

from gurobipy import Model
from definitions import InputData
from decision_variables import DecisionVariables
from constraints import Constraints
from objective import Objective
from results import FinalTable

def solve_problem():
    model = Model('Optimization Model')

    data = InputData()
    decision_variables = DecisionVariables(model)
    decision_variables.create_variables()
    variables = decision_variables.get_variables()
    
    constraints = Constraints(model, data)
    constraints.add_constraints(variables['new_price'], variables['new_demand'])
    
    objective = Objective(model, data)
    objective.set_objective(variables['new_price'])

    final_table = FinalTable(model, variables)
    table_output = final_table.print_table()
    
    print(table_output)
    final_table.save_output('problem_21.txt', table_output)

if __name__ == '__main__':
    solve_problem()
