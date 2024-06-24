# main.py

from ortools.linear_solver import pywraplp
from input_data import InputData
from constraints import Constraints
from objective import Objective
from final_table import FinalTable
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

    final_table = FinalTable(solver, **variables, problem=problem)
    final_table.print_table()





if __name__ == '__main__':
    problem_choice = input("Enter Problem num: ")
    
    solve_problem(int(problem_choice))
  
