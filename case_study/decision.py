# decision.py
class DecisionVariables:
    def __init__(self, solver, problem):
        self.solver = solver
        self.problem = problem
        self.variables = {}

    def create_variables(self):
        if self.problem == 10:
            self._create_variables_for_problem_10()
        

    def _create_variables_for_problem_10(self):
        self.variables['open'] = [[self.solver.BoolVar(f'city_{i}_has_dept_{j}') for j in range(5)] for i in range(3)]
        self.variables['path'] = [[[[self.solver.BoolVar(f'city_{i}_has_dept_{j}_and_city_{k}_has_dept_{l}') for l in range(5)] for k in range(3)] for j in range(5)] for i in range(3)]

    

    def get_variables(self):
        return self.variables
