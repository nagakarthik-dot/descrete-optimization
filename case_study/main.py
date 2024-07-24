# main.py (need to run this)

from gurobipy import Model, GRB
from ortools.linear_solver import pywraplp
from input_data import InputData
from constraints import Constraints
from objective import Objective
from results import FinalTable
from decision_variable import DecisionVariables

def solve_problem(problem):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print('Solver not created.')
        return

    data = InputData(problem)
    decision_variables = DecisionVariables(solver, problem)
    decision_variables.create_variables()
    variables = decision_variables.get_variables()
    constraints = Constraints(solver, data, problem)
    constraints.add_constraints(**variables)

    objective = Objective(solver, data, problem)
    objective.set_objective(**variables)

    solution = FinalTable(solver, **variables, problem=problem)
    solution.print_table()



### remianing 12,24,25,26

if __name__ == '__main__':
    print('Done: ')
    problem_choice = input("Enter Problem num: ")
    
    solve_problem(int(problem_choice))
  
