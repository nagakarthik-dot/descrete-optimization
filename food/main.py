# main.py

from gurobipy import Model
from input_data import InputData
from decision_variables import DecisionVariables
from constraints import Constraints
from objective import Objective
from results import FinalTable

def solve_problem():
    model = Model('Optimization Model')

    data = InputData()
    print(data.requirement)
    decision_variables = DecisionVariables(model,data)
    decision_variables.create_variables()
    variables = decision_variables.get_variables()
    
    constraints = Constraints(model, data)
    constraints.add_constraints(variables['prepare'],variables['inventory'],variables['sold'],variables['waste'],variables['unfull'] )
    
    objective = Objective(model, data)
    objective.set_objective(variables['sold'],variables['waste'],variables['unfull'])

    final_table = FinalTable(model, variables,data)
    table_output = final_table.print_table()
    
    print(table_output)
    final_table.save_output('quantity.csv', table_output)

if __name__ == '__main__':
    solve_problem()