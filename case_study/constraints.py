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
        
        if self.problem==11:
            for i in range(len(self.data.x)):
                self.solver.Add(kwargs['abs_diff'][i] >= (kwargs['a'] * self.data.x[i] + kwargs['b'] - self.data.y[i]))
                self.solver.Add(kwargs['abs_diff'][i] >= -(kwargs['a'] * self.data.x[i] + kwargs['b'] - self.data.y[i]))
        
        if self.problem==111:
            for i in range(len(self.data.x)):
                self.solver.Add(kwargs['res'] >= (kwargs['a'] * self.data.x[i] + kwargs['b'] - self.data.y[i]))
                self.solver.Add(kwargs['res'] >= -(kwargs['a'] * self.data.x[i] + kwargs['b'] - self.data.y[i]))
        
        if self.problem==13:
            temp1=temp2=temp3=temp4=temp6=temp7=temp8=temp9=t1=t2=t3=t4=t6=t7=0
            for i in range(len(self.data.dict)):
                temp1+=self.data.dict[i][2]*kwargs['open'][i]
                temp2+=self.data.dict[i][2]
                temp3+=self.data.dict[i][3]*kwargs['open'][i]
                temp4+=self.data.dict[i][3]
                if self.data.dict[i][0]==1:
                    temp6+=self.data.dict[i][1]*kwargs['open'][i]
                    temp7+=self.data.dict[i][1]
                if self.data.dict[i][0]==2:
                    temp8+=self.data.dict[i][1]*kwargs['open'][i]
                    temp9+=self.data.dict[i][1]
                if self.data.dict[i][0]==3:
                    t6+=self.data.dict[i][1]*kwargs['open'][i]
                    t7+=self.data.dict[i][1]
                if self.data.dict[i][4]=='A':
                    t1+=kwargs['open'][i]
                    t2+=1
                if self.data.dict[i][4]=='B':
                    t3+=kwargs['open'][i]
                    t4+=1
            self.solver.Add(temp1<=0.45*temp2)
            self.solver.Add(temp1>=0.35*temp2)
            self.solver.Add(temp3<=0.45*temp4)
            self.solver.Add(temp3>=0.35*temp4)
            self.solver.Add(temp6<=0.45*temp7)
            self.solver.Add(temp6>=0.35*temp7)
            self.solver.Add(t6<=0.45*t7)
            self.solver.Add(t6>=0.35*t7)
            self.solver.Add(temp8<=0.45*temp9)
            self.solver.Add(temp8>=0.35*temp9)
            self.solver.Add(t1<=0.45*t2)
            self.solver.Add(t1>=0.35*t2)
            self.solver.Add(t3<=0.45*t4)
            self.solver.Add(t3>=0.35*t4)
            self.solver.Add(kwargs['deviations'][0]>=temp1-0.4*temp2)
            self.solver.Add(kwargs['deviations'][0]>=-temp1+0.4*temp2)
            self.solver.Add(kwargs['deviations'][1]>=temp3-0.4*temp4)
            self.solver.Add(kwargs['deviations'][1]>=-temp3+0.4*temp4)
            self.solver.Add(kwargs['deviations'][2]>=temp6-0.4*temp7)
            self.solver.Add(kwargs['deviations'][2]>=-temp6+0.4*temp7)
            self.solver.Add(kwargs['deviations'][3]>=t6-0.4*t7)
            self.solver.Add(kwargs['deviations'][3]>=-t6+0.4*t7)
            self.solver.Add(kwargs['deviations'][4]>=temp8-0.4*temp9)
            self.solver.Add(kwargs['deviations'][4]>=-temp8+0.4*temp9)
            self.solver.Add(kwargs['deviations'][5]>=t1-0.4*t2)
            self.solver.Add(kwargs['deviations'][5]>=-t1+0.4*t2)
            self.solver.Add(kwargs['deviations'][6]>=t3-0.4*t4)
            self.solver.Add(kwargs['deviations'][6]>=-t3+0.4*t4)
            kwargs['intermediate_values'] = {
                'temp2': temp2,
                'temp4': temp4,
                'temp7': temp7,
                't7': t7,
                'temp9': temp9,
                't2': t2,
                't4': t4
            }
        
        if self.problem ==15:
            for i in range(5):
                for j in range(3):
                    self.solver.Add(kwargs['ty'][j][i]>=self.data.minwatt[j]*kwargs['num'][j][i])
                    self.solver.Add(kwargs['ty'][j][i]<=self.data.maxwatt[j]*kwargs['num'][j][i])
                    self.solver.Add(kwargs['num'][j][i]<=self.data.avail[j])
                    if i == 0:
                        self.solver.Add(kwargs['start'][j][i] == kwargs['num'][j][i])
                    else:
                        self.solver.Add(kwargs['start'][j][i] == kwargs['num'][j][i] - kwargs['num'][j][i - 1])
                self.solver.Add(sum(kwargs['ty'][j][i] for j in range(3))>=self.data.demand[i])
                self.solver.Add(sum(kwargs['num'][j][i]*self.data.maxwatt[j] for j in range(3))>=1.15*self.data.demand[i])
        
        if self.problem ==19:
            ### have 0 possiblility 
            self.solver.Add(kwargs['facttodepot'][1][0]==0)
            self.solver.Add(kwargs['facttocust'][0][1]==0)
            self.solver.Add(kwargs['facttocust'][0][4]==0)
            for i in range(1,6):
                self.solver.Add(kwargs['facttocust'][1][i]==0)
            self.solver.Add(kwargs['depottocust'][0][0]==0)
            self.solver.Add(kwargs['depottocust'][0][4]==0)
            self.solver.Add(kwargs['depottocust'][1][5]==0)
            self.solver.Add(kwargs['depottocust'][2][0]==0)
            self.solver.Add(kwargs['depottocust'][2][3]==0)
            self.solver.Add(kwargs['depottocust'][3][0]==0)
            self.solver.Add(kwargs['depottocust'][3][1]==0)

            ###   capacity of fcatory check 
            for i in range(2):
                temp=0
                for j in range(4):
                    temp+=kwargs['facttodepot'][i][j]
                for j in range(6):
                    temp+=kwargs['facttocust'][i][j]
                self.solver.Add(temp<=self.data.f_c[i])

            ###  depot check 
            for i in range(4):
                self.solver.Add(sum(kwargs['facttodepot'][j][i] for j in range(2))>=sum(kwargs['depottocust'][i][j] for j in range(6)))
                self.solver.Add(sum(kwargs['facttodepot'][j][i] for j in range(2))<=self.data.d_c[i])

            ## customer check 
            for i in range(6):
                self.solver.Add(sum(kwargs['depottocust'][j][i] for j in range(4))+sum(kwargs['facttocust'][j][i] for j in range(2))>=self.data.demand[i])
                if i==0:
                    for j in range(2):
                        self.solver.Add(kwargs['facttocust'][0][0]>=kwargs['facttocust'][j][i])
                    for j in range(4):
                        self.solver.Add(kwargs['facttocust'][0][0]>=kwargs['depottocust'][j][i])
                if i==1:
                    for j in range(2):
                        self.solver.Add(kwargs['depottocust'][0][1]>=kwargs['facttocust'][j][i])
                    for j in range(4):
                        self.solver.Add(kwargs['depottocust'][0][1]>=kwargs['depottocust'][j][i])
                if i==4:
                    for j in range(2):
                        self.solver.Add(kwargs['depottocust'][1][4]>=kwargs['facttocust'][j][i])
                    for j in range(4):
                        self.solver.Add(kwargs['depottocust'][1][4]>=kwargs['depottocust'][j][i])
                if i==5:
                    for j in range(2):
                        self.solver.Add(kwargs['depottocust'][2][5]>=kwargs['facttocust'][j][i])
                        self.solver.Add(kwargs['depottocust'][3][i]>=kwargs['facttocust'][j][i])
                    for j in range(4):
                        self.solver.Add(kwargs['depottocust'][2][5]>=kwargs['depottocust'][j][i])
                        self.solver.Add(kwargs['depottocust'][3][i]>=kwargs['depottocust'][j][i])
        if self.problem ==17:
            self.solver.Add(sum(kwargs['cell'][i] for i in range(27))==14)
            for i in range(49):
                self.solver.Add(kwargs['cell'][self.data.cells_line[i][0]-1]+kwargs['cell'][self.data.cells_line[i][1]-1]+kwargs['cell'][self.data.cells_line[i][2]-1]-kwargs['lines'][i]<=2)
                self.solver.Add(kwargs['cell'][self.data.cells_line[i][0]-1]+kwargs['cell'][self.data.cells_line[i][1]-1]+kwargs['cell'][self.data.cells_line[i][2]-1]+kwargs['lines'][i]>=1)
        if self.problem==27:
            for k in range(self.data.num_vehicles):
                for i in range(self.data.num_cities):
                    for j in range(self.data.num_cities):
                        self.solver.Add(kwargs['path'][k][j][j] == 0)
                        self.solver.Add(kwargs['visit'][k][j] <= kwargs['used'][k])
                        #self.solver.Add(kwargs['path'][k][j][0] == 0)
                        self.solver.Add(sum(kwargs['path'][k][j][i] for i in range(self.data.num_cities)) == kwargs['visit'][k][j])
                        self.solver.Add(sum(kwargs['path'][k][i][j] for i in range(self.data.num_cities)) == kwargs['visit'][k][j])

                self.solver.Add(sum(self.data.distance_matrix[i][j] * kwargs['path'][k][i][j] for i in range(self.data.num_cities) for j in range(1,self.data.num_cities)) <= 120)

            for i in range(self.data.num_cities):
                if i == 0:
                    self.solver.Add(sum(kwargs['visit'][k][i]-kwargs['used'][k] for k in range(self.data.num_vehicles)) == 0)
                else:
                    self.solver.Add(sum(kwargs['visit'][k][i] for k in range(self.data.num_vehicles)) == 1)
            for k in range(self.data.num_vehicles):
                self.solver.Add(kwargs['visit'][k][0]==kwargs['used'][k])
        
        if self.problem==14:
            for i in self.data.above.keys():
                for j in self.data.above[i]:
                    self.solver.Add(kwargs['remove'][j]>=kwargs['remove'][i])