from input_data import InputData
import gurobipy as gp
from gurobipy import GRB

class DecisionVariables:
    def __init__(self, model, problem):
        self.model = model
        self.problem = problem
        self.variables = {}





    def create_variables(self):
        data = InputData(self.problem)
        if self.problem == 1:
            self.variables['buy'] = [[self.model.addVar(lb=0.0, ub=1000.0, vtype=GRB.CONTINUOUS, name=f'buy[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['used'] = [[self.model.addVar(lb=0.0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name=f'used[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['store'] = [[self.model.addVar(lb=0.0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name=f'store[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
        if self.problem ==21:
            self.variables['new_price'] = [self.model.addVar(lb=0, name=f"prices{i}") for i in range(4)]
            self.variables['new_demand'] = [self.model.addVar(lb=0, name=f"demand{i}") for i in range(4)]

        
        self.model.update()  

    def get_variables(self):
        return self.variables