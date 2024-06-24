# objective.py

class Objective:
    def __init__(self, solver, data, problem):
        self.solver = solver
        self.data = data
        self.problem = problem

    def set_objective(self, **kwargs):
        result = 0
        if self.problem == 1 or self.problem == 2:
            for i in range(self.data.num_months):
                for j in range(self.data.num_products):
                    result += -self.data.prices[i][j] * kwargs['buy'][i][j] + 150 * kwargs['used'][i][j] - 5 * kwargs['store'][i][j]
            self.solver.Maximize(result)

        elif self.problem == 3 or self.problem==4:
            for i in range(6):
                for j in range(7):
                    result += self.data.cost[j] * kwargs['sell'][i][j] - 0.5 * kwargs['store'][i][j]
            self.solver.Maximize(result)

        elif self.problem == 5:
            result = 0
            for i in range(3):
                result += kwargs['wSK'][i] + kwargs['wSS'][i] + kwargs['wUS'][i]
            self.solver.Minimize(result)
        elif self.problem==51:
            result=0
            for i in range(3):
                result += 400 * kwargs['vUSSS'][i] + 500 * kwargs['vSSSK'][i] + 200 * kwargs['wUS'][i] + 500 * (kwargs['wSS'][i] + kwargs['wSK'][i]) + 400 * kwargs['xSK'][i] + 400 * kwargs['xSS'][i] + 500 * kwargs['xUS'][i] + 3000 * kwargs['ySK'][i] + 2000 * kwargs['ySS'][i] + 1500 * kwargs['yUS'][i]
            
            self.solver.Minimize(result)
        elif self.problem==7:
            for j in range(5):
                for i in range(4):
                    result+=(10*kwargs['output'][j][i]-self.data.royal[i]*kwargs['ope'][j][i])
            self.solver.Maximize(result)
        
        elif self.problem ==10:
            for i in range(3):
                for j in range(5):
                    for k in range(3):
                        for l in range(5):
                            if  l > j and  k>=i:
                                result+=(kwargs['path'][i][j][k][l]*self.data.city[i][k]*self.data.comm[j][l])
            for i in range(5):
                for j in range(3):
                    result-=(self.data.dept[j][i]*kwargs['open'][j][i])
            self.solver.Minimize(result)