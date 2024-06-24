# constraints.py

from ortools.linear_solver import pywraplp

class Constraints:
    def __init__(self, solver, data, problem):
        self.solver = solver
        self.data = data
        self.problem = problem

    def add_constraints(self, **kwargs):
        if self.problem == 1:
            for i in range(self.data.num_months):
                self.solver.Add(kwargs['used'][i][0] + kwargs['used'][i][1] <= 200)
                self.solver.Add(kwargs['used'][i][2] + kwargs['used'][i][3] + kwargs['used'][i][4] <= 250)

                for j in range(self.data.num_products):
                    if i == 0:
                        self.solver.Add(kwargs['buy'][i][j] - kwargs['used'][i][j] - kwargs['store'][i][j] == -500)
                    elif i == self.data.num_months - 1:
                        self.solver.Add(kwargs['buy'][i][j] - kwargs['used'][i][j] - kwargs['store'][i][j] + kwargs['store'][i-1][j] == 500)
                    else:
                        self.solver.Add(kwargs['buy'][i][j] - kwargs['used'][i][j] - kwargs['store'][i][j] + kwargs['store'][i-1][j] == 0)

            for i in range(self.data.num_months):
                temp1 = sum(self.data.hardmax[j] * kwargs['used'][i][j] for j in range(self.data.num_products))
                temp2 = sum(self.data.hardmin[j] * kwargs['used'][i][j] for j in range(self.data.num_products))
                self.solver.Add(temp1 <= 0.0)
                self.solver.Add(temp2 >= 0.0)

        if self.problem == 2:
            for i in range(self.data.num_months):
                self.solver.Add(sum(kwargs['usedby'][i][j] for j in range(5)) <= 3)
                self.solver.Add(kwargs['usedby'][i][0] + kwargs['usedby'][i][1] <= 2 * kwargs['usedby'][i][4])
                for j in range(self.data.num_products):
                    ##  if oil used min 20 is used
                    self.solver.Add(kwargs['used'][i][j] >= 20 * kwargs['usedby'][i][j])
                    if j == 0 or j == 1:
                        self.solver.Add(kwargs['used'][i][j] <= 200 * kwargs['usedby'][i][j])
                    else:
                        self.solver.Add(kwargs['used'][i][j] <= 250 * kwargs['usedby'][i][j])
                self.solver.Add(kwargs['used'][i][0] + kwargs['used'][i][1] <= 200)
                self.solver.Add(kwargs['used'][i][3] + kwargs['used'][i][2] + kwargs['used'][i][4] <= 250)
                for j in range(5):
                    if i == 0:
                        self.solver.Add(kwargs['buy'][i][j] - kwargs['used'][i][j] - kwargs['store'][i][j] == -500)
                    elif i == 5:
                        self.solver.Add(kwargs['buy'][i][j] - kwargs['used'][i][j] + kwargs['store'][i-1][j] == 500)
                    else:
                        self.solver.Add(kwargs['buy'][i][j] - kwargs['used'][i][j] - kwargs['store'][i][j] + kwargs['store'][i-1][j] == 0)
            for i in range(self.data.num_months):
                temp1 = sum(self.data.hardmax[j] * kwargs['used'][i][j] for j in range(self.data.num_products))
                temp2 = sum(self.data.hardmin[j] * kwargs['used'][i][j] for j in range(self.data.num_products))
                self.solver.Add(temp1 <= 0.0)
                self.solver.Add(temp2 >= 0.0)
            for i in range(self.data.num_months):
                for j in range(self.data.num_products):
                    if i == 5:
                        self.solver.Add(kwargs['store'][i][j] == 500)

        if self.problem == 3:
            for i in range(6):
                for j in range(7):
                    self.solver.Add(kwargs['items'][i][j] <= self.data.limit[i][j])
                for j in range(5):
                    self.solver.Add(sum(self.data.hours[j][k] * kwargs['items'][i][k] for k in range(7)) <= self.data.machines[i][j] * 24 * 16)
            for i in range(6):
                for j in range(7):
                    if i == 0:
                        self.solver.Add(kwargs['items'][i][j] == kwargs['sell'][i][j] + kwargs['store'][i][j])
                    else:
                        self.solver.Add(kwargs['items'][i][j] + kwargs['store'][i-1][j] == kwargs['sell'][i][j] + kwargs['store'][i][j])
            for j in range(7):
                self.solver.Add(kwargs['store'][5][j] == 50)
        if self.problem==4:
            for i in range(6):
                for j in range(7):
                    self.solver.Add(kwargs['items'][i][j] <= self.data.limit[i][j])
                for j in range(5):
                    self.solver.Add(sum(self.data.hours[j][k] * kwargs['items'][i][k] for k in range(7)) <= (self.data.machines[j] * 24 * 16)-(kwargs['maintaince'][i][j]*24*16))
            for i in range(6):
                for j in range(7):
                    if i == 0:
                        self.solver.Add(kwargs['items'][i][j] == kwargs['sell'][i][j] + kwargs['store'][i][j])
                    else:
                        self.solver.Add(kwargs['items'][i][j] + kwargs['store'][i-1][j] == kwargs['sell'][i][j] + kwargs['store'][i][j])
            for j in range(7):
                self.solver.Add(kwargs['store'][5][j] == 50)
            self.solver.Add(sum(kwargs['maintaince'][i][0] for i in range(6))==2)
            self.solver.Add(sum(kwargs['maintaince'][i][1] for i in range(6))==2)
            self.solver.Add(sum(kwargs['maintaince'][i][2] for i in range(6))==3)
            self.solver.Add(sum(kwargs['maintaince'][i][3] for i in range(6))==1)
            self.solver.Add(sum(kwargs['maintaince'][i][4] for i in range(6))==1)

        if self.problem == 5 or self.problem ==51:
            self.solver.Add(kwargs['tSK'][0] == 1000)
            self.solver.Add(kwargs['tSS'][0] == 1500)
            self.solver.Add(kwargs['tUS'][0] == 2000)
            for i in range(1, 4):
                self.solver.Add(kwargs['tSK'][i] - kwargs['ySK'][i-1] - 0.5 * kwargs['xSK'][i-1] == self.data.skill[i-1])
                self.solver.Add(kwargs['tSS'][i] - kwargs['ySS'][i-1] - 0.5 * kwargs['xSS'][i-1] == self.data.semi[i-1])
                self.solver.Add(kwargs['tUS'][i] - kwargs['yUS'][i-1] - 0.5 * kwargs['xUS'][i-1] == self.data.un[i-1])
            for i in range(3):
                self.solver.Add(kwargs['vSSSK'][i] - 0.25 * kwargs['tSK'][i+1] <= 0)
                self.solver.Add(kwargs['ySK'][i] + kwargs['ySS'][i] + kwargs['yUS'][i] <= 150)
                self.solver.Add(kwargs['tSK'][i+1] == 0.95 * kwargs['tSK'][i] + 0.9 * kwargs['uSK'][i] + kwargs['vSSSK'][i] - kwargs['vSKSS'][i] - kwargs['uSKUS'][i] - kwargs['wSK'][i])
                self.solver.Add(kwargs['tSS'][i+1] == 0.95 * kwargs['tSS'][i] + 0.8 * kwargs['uSS'][i] + kwargs['vUSSS'][i] - kwargs['vSSSK'][i] + 0.5 * kwargs['vSKSS'][i] - kwargs['wSS'][i] - kwargs['vSSUS'][i])
                self.solver.Add(kwargs['tUS'][i+1] == 0.9 * kwargs['tUS'][i] + 0.75 * kwargs['uUS'][i] - kwargs['vUSSS'][i] + 0.5 * kwargs['vSKSS'][i] + 0.5 * kwargs['vSSUS'][i] - kwargs['wUS'][i])
        
        if self.problem ==7:
            ## atmost 3 mine sin a year
            for j in range(5):
                self.solver.Add(sum(kwargs['operate'][j][i] for i in range(4)) <= 3)
## if it is closed one year then it is closed further also 
            for i in range(4):
                for j in range(4):
                    self.solver.Add(kwargs['ope'][j+1][i]-kwargs['ope'][j][i]<=0)
            ## upper limit of capacities 
            for j in range(5):
                for i in range(4):
                    self.solver.Add(kwargs['output'][j][i]<=self.data.capacity[i]*kwargs['operate'][j][i])
                    self.solver.Add(kwargs['operate'][j][i]-kwargs['ope'][j][i]<=0)
            for j in range(5):
                tot=0
                for i in range(4):
                    tot+=(self.data.year_quality[j]*kwargs['output'][j][i]-self.data.mine_quality[i]*kwargs['output'][j][i])
                self.solver.Add(tot==0)

        if self.problem ==10:
            for i in range(3):
                self.solver.Add(self.solver.Sum(kwargs['open'][i][j] for j in range(5)) <= 3)
            for j in range(5):
                self.solver.Add(self.solver.Sum(kwargs['open'][i][j] for i in range(3)) == 1)

            for i in range(3):
                for j in range(5):
                    for k in range(3):
                        for l in range(5):
                            self.solver.Add(kwargs['path'][i][j][k][l] <= kwargs['open'][i][j])
                            self.solver.Add(kwargs['path'][i][j][k][l] <= kwargs['open'][k][l])
                            self.solver.Add(kwargs['path'][i][j][k][l] >= kwargs['open'][i][j] + kwargs['open'][k][l]-1 )
