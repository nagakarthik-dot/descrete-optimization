# constraints.py

from gurobipy import GRB

class Constraints:
    def __init__(self, model, data, problem):
        self.model = model
        self.data = data
        self.problem = problem

    def add_constraints(self, **kwargs):
        if self.problem == 1:
            for i in range(self.data.num_months):
                self.model.addConstr(kwargs['used'][i][0] + kwargs['used'][i][1] <= 200, f'constraint1_{i}')
                self.model.addConstr(kwargs['used'][i][2] + kwargs['used'][i][3] + kwargs['used'][i][4] <= 250, f'constraint2_{i}')

                for j in range(self.data.num_products):
                    if i == 0:
                        self.model.addConstr(kwargs['buy'][i][j] - kwargs['used'][i][j] - kwargs['store'][i][j] == -500, f'constraint3_{i}_{j}')
                    elif i == self.data.num_months - 1:
                        self.model.addConstr(kwargs['buy'][i][j] - kwargs['used'][i][j] - kwargs['store'][i][j] + kwargs['store'][i-1][j] == 500, f'constraint4_{i}_{j}')
                    else:
                        self.model.addConstr(kwargs['buy'][i][j] - kwargs['used'][i][j] - kwargs['store'][i][j] + kwargs['store'][i-1][j] == 0, f'constraint5_{i}_{j}')

            for i in range(self.data.num_months):
                temp1 = sum(self.data.hardmax[j] * kwargs['used'][i][j] for j in range(self.data.num_products))
                temp2 = sum(self.data.hardmin[j] * kwargs['used'][i][j] for j in range(self.data.num_products))
                self.model.addConstr(temp1 <= 0.0, f'constraint6_{i}')
                self.model.addConstr(temp2 >= 0.0, f'constraint7_{i}')
        if self.problem ==21:
            self.model.addConstr(0.04*kwargs['new_demand'][0]+0.8*kwargs['new_demand'][1]+0.35*kwargs['new_demand'][2]+0.25*kwargs['new_demand'][3]<=600000)
            self.model.addConstr(0.09*kwargs['new_demand'][0]+0.02*kwargs['new_demand'][1]+0.3*kwargs['new_demand'][2]+0.4*kwargs['new_demand'][3]<=750000)
            for i in range(4):
                self.model.addConstr(1 - (kwargs['new_demand'][i] / self.data.demand[i]) == self.data.e[i] * ((kwargs['new_price'][i] / self.data.prices[i]) - 1))

            self.model.addConstr(1 - (kwargs['new_demand'][2] /  self.data.demand[2]) == self.data.e[4] * (1 - (kwargs['new_price'][3] / self.data.prices[3])))
            self.model.addConstr(1 - (kwargs['new_demand'][3] /  self.data.demand[3]) == self.data.e[5] * (1 - (kwargs['new_price'][2] / self.data.prices[2])))

            temp1 = 0
            temp2 = 0
            for i in range(4):
                temp1 +=  self.data.demand[i] * kwargs['new_price'][i]
                temp2 +=  self.data.demand[i] * self.data.prices[i]
            self.model.addConstr(temp1 <= temp2)


