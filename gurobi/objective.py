# objective.py

from gurobipy import GRB

class Objective:
    def __init__(self, model, data, problem):
        self.model = model
        self.data = data
        self.problem = problem

    def set_objective(self, **kwargs):
        objective_expr = 0
        if self.problem == 1 or self.problem == 2:
            for i in range(self.data.num_months):
                for j in range(self.data.num_products):
                    objective_expr += -self.data.prices[i][j] * kwargs['buy'][i][j] + 150 * kwargs['used'][i][j] - 5 * kwargs['store'][i][j]
            self.model.setObjective(objective_expr, sense=GRB.MAXIMIZE)
        if self.problem ==21:
            
            for i in range(4):
                objective_expr += kwargs['new_price'][i] * ((1 - self.data.e[i] * ((kwargs['new_price'][i] / self.data.prices[i]) - 1)) * self.data.demand[i])

            self.model.setObjective(objective_expr, sense=GRB.MAXIMIZE)
