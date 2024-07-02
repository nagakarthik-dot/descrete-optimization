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

        elif self.problem==11:
            self.solver.Minimize(self.solver.Sum(kwargs['abs_diff']))
        elif self.problem==111:
            self.solver.Minimize(kwargs['res'])
        elif self.problem==13:
            intermediate_values = kwargs.get('intermediate_values', {})
            temp2 = intermediate_values.get('temp2', 1)
            temp4 = intermediate_values.get('temp4', 1)
            temp7 = intermediate_values.get('temp7', 1)
            t7 = intermediate_values.get('t7', 1)
            temp9 = intermediate_values.get('temp9', 1)
            t2 = intermediate_values.get('t2', 1)
            t4 = intermediate_values.get('t4', 1)

            self.solver.Minimize(
                kwargs['deviations'][0] / (0.4 * temp2) +
                kwargs['deviations'][1] / (0.4 * temp4) +
                kwargs['deviations'][2] / (0.4 * temp7) +
                kwargs['deviations'][3] / (0.4 * t7) +
                kwargs['deviations'][4] / (0.4 * temp9) +
                kwargs['deviations'][5] / (0.4 * t2) +
                kwargs['deviations'][6] / (0.4 * t4)
            )
        
        elif self.problem ==15:
            total_cost = 0
            for i in range(5):
                for j in range(3):
                    total_cost += self.data.setup[j] * kwargs['start'][j][i]
                    total_cost += kwargs['num'][j][i] * self.data.costmin[j]
                    total_cost +=   (kwargs['ty'][j][i] - self.data.minwatt[j]*kwargs['num'][j][i]) * self.data.costex[j]

            self.solver.Minimize(total_cost)
        
        elif self.problem==19:
            result=0
            for i in range(2):
                for j in range(4):
                    result+=kwargs['facttodepot'][i][j]*self.data.dat1[j][i]
                    result+=0
            for i in range(2):
                for j in range(6):
                    result+=kwargs['facttocust'][i][j]*self.data.dat2[i][j]
            for i in range(4):
                for j in range(6):
                    result+=kwargs['depottocust'][i][j]*self.data.dat3[i][j]

            self.solver.Minimize(result)
        elif self.problem ==17:
            self.solver.Minimize(sum(kwargs['lines'][i] for i in range(49)))
        elif self.problem==27:
            self.solver.Minimize(sum(kwargs['used'][k] for k in range(self.data.num_vehicles)))
        elif self.problem==14:
            result=0
            for i in range(4):
                if i==0:
                    for j in range(14,30):
                        result+=kwargs['remove'][j]*(self.data.value[j]*2000-3000)
                if i==1:
                    for j in range(5,14):
                        result+=kwargs['remove'][j]*(self.data.value[j]*2000-6000)
                if i==2:
                    for j in range(1,5):
                        result+=kwargs['remove'][j]*(self.data.value[j]*2000-8000)
                if i==3:
                    for j in range(1):
                        result+=kwargs['remove'][j]*(self.data.value[j]*2000-10000)
            self.solver.Maximize(result)
        elif self.problem ==18:
            ##result = kwargs['arhs'] - kwargs['a'][2] - kwargs['a'][5]
            result=sum(kwargs['a'][i] for i in range(8))
            self.solver.Minimize(result)




