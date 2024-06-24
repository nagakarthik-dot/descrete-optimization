from input_data import InputData


class DecisionVariables:
    def __init__(self, solver, problem):
        self.solver = solver
        self.problem = problem
        self.variables = {}

    def create_variables(self):
        data = InputData(self.problem)
        if self.problem == 1:
            self.variables['buy'] = [[self.solver.NumVar(0, 1000, f'buy[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['used'] = [[self.solver.NumVar(0, self.solver.infinity(), f'used[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['store'] = [[self.solver.NumVar(0, self.solver.infinity(), f'store[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
        if self.problem == 2:
            self.variables['buy'] = [[self.solver.NumVar(0, 1000, f'buy[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['used'] = [[self.solver.NumVar(0, self.solver.infinity(), f'used[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['store'] = [[self.solver.NumVar(0, self.solver.infinity(), f'store[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['usedby'] = [[self.solver.BoolVar(f'oil {j} used in month {i}') for j in range(5)] for i in range(6)]
        if self.problem == 3:
            self.variables['items'] = [[self.solver.NumVar(0, self.solver.infinity(), f'items[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            # Assuming these were intended to be added to self.variables:
            self.variables['sell'] = [[self.solver.NumVar(0, self.solver.infinity(), f'sell[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['store'] = [[self.solver.NumVar(0, 100, f'store[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
        if self.problem==4:
            self.variables['items'] = [[self.solver.NumVar(0, self.solver.infinity(), f'items[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            # Assuming these were intended to be added to self.variables:
            self.variables['sell'] = [[self.solver.NumVar(0, self.solver.infinity(), f'sell[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['store'] = [[self.solver.NumVar(0, 100, f'store[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
            self.variables['maintaince']=[[self.solver.BoolVar(f'maintain[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]

        if self.problem == 5 or self.problem == 51:
            self.variables['tSK'] = [self.solver.NumVar(0, self.solver.infinity(), f'tSK[{i}]') for i in range(4)]
            self.variables['tSS'] = [self.solver.NumVar(0, self.solver.infinity(), f'tSS[{i}]') for i in range(4)]
            self.variables['tUS'] = [self.solver.NumVar(0, self.solver.infinity(), f'tUS[{i}]') for i in range(4)]
        # Recruitment variables
            self.variables['uSK'] = [self.solver.NumVar(0, 500, f'uSK[{i}]') for i in range(data.num_years)]
            self.variables['uSS'] = [self.solver.NumVar(0, 800, f'uSS[{i}]') for i in range(data.num_years)]
            self.variables['uUS'] = [self.solver.NumVar(0, 500, f'uUS[{i}]') for i in range(data.num_years)]
        # Retraining variables
            self.variables['vUSSS'] = [self.solver.NumVar(0, 200, f'vUSSS[{i}]') for i in range(data.num_years)]  # unskill to semi skill
            self.variables['vSSSK'] = [self.solver.NumVar(0, self.solver.infinity(), f'vSSSK[{i}]') for i in range(data.num_years)]  # semi to skill
        # Downsizing variables
            self.variables['vSKSS'] = [self.solver.NumVar(0, self.solver.infinity(), f'vSKSS[{i}]') for i in range(data.num_years)]  # skill to semi
            self.variables['uSKUS'] = [self.solver.NumVar(0, self.solver.infinity(), f'uSKUS[{i}]') for i in range(data.num_years)]  # skill to unskill
            self.variables['vSSUS'] = [self.solver.NumVar(0, self.solver.infinity(), f'vSSUS[{i}]') for i in range(data.num_years)]  # semi to unskill
        # Redundancy variables
            self.variables['wSK'] = [self.solver.NumVar(0, self.solver.infinity(), f'wSK[{i}]') for i in range(data.num_years)]
            self.variables['wSS'] = [self.solver.NumVar(0, self.solver.infinity(), f'wSS[{i}]') for i in range(data.num_years)]
            self.variables['wUS'] = [self.solver.NumVar(0, self.solver.infinity(), f'wUS[{i}]') for i in range(data.num_years)]
        # Short-time variables
            self.variables['xSK'] = [self.solver.NumVar(0, 50, f'xSK[{i}]') for i in range(data.num_years)]
            self.variables['xSS'] = [self.solver.NumVar(0, 50, f'xSS[{i}]') for i in range(data.num_years)]
            self.variables['xUS'] = [self.solver.NumVar(0, 50, f'xUS[{i}]') for i in range(data.num_years)]
        # Over-man variables
            self.variables['ySK'] = [self.solver.NumVar(0, self.solver.infinity(), f'ySK[{i}]') for i in range(data.num_years)]
            self.variables['ySS'] = [self.solver.NumVar(0, self.solver.infinity(), f'ySS[{i}]') for i in range(data.num_years)]
            self.variables['yUS'] = [self.solver.NumVar(0, self.solver.infinity(), f'yUS[{i}]') for i in range(data.num_years)]
        if self.problem == 7:
            self.variables['operate'] = [[self.solver.BoolVar(f'mine{i} is operated in year{j}') for i in range(4)] for j in range(5)]
            self.variables['ope'] = [[self.solver.BoolVar(f'mine{i} is open in year{j}') for i in range(4)] for j in range(5)]
            self.variables['output'] = [[self.solver.NumVar(0, self.solver.infinity(), 'output') for i in range(4)] for j in range(5)]

        if self.problem == 10:
            self.variables['open'] = [[self.solver.BoolVar(f'city_{i}_has_dept_{j}') for j in range(5)] for i in range(3)]
            self.variables['path'] = [[[[self.solver.BoolVar(f'city_{i}_has_dept_{j}_and_city_{k}_has_dept_{l}') for l in range(5)] for k in range(3)] for j in range(5)] for i in range(3)]

    def get_variables(self):
        return self.variables
