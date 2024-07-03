# main.py

import os
from gurobipy import Model, GRB
from input_data import InputData
from decision_variables import DecisionVariables
from constraints import Constraints
from objective import Objective
from results import FinalTable

def solve_problem(problem):
    # Create a Gurobi model
    model = Model('Optimization Model')

    data = InputData(problem)
    decision_variables = DecisionVariables(model, problem)
    decision_variables.create_variables()
    variables = decision_variables.get_variables()
    
    constraints = Constraints(model, data, problem)
    constraints.add_constraints(**variables)
    
    objective = Objective(model, data, problem)
    objective.set_objective(**variables)

    final_table = FinalTable(model, variables, problem)
    table_output = final_table.print_table()
    

    print(table_output)
    final_table.save_output(f'output_problem_{problem}.txt', table_output)

if __name__ == '__main__':
    print('Done:  [1,2,3,4,5,7,10,11,13,14,15,17,18,19,23,27]')
    problem_choice = input("Enter Problem num: ")
    
    solve_problem(int(problem_choice))
