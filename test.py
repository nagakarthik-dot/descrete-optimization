import gurobipy as gp
from gurobipy import GRB
import numpy as np

min_value = 2
max_value = 7
hour = 15
work_hours = 9
employee_cost = 80

requirement = np.random.randint(min_value, max_value + 1, size=hour)

num_employees = 30

model = gp.Model('Shift Scheduling')

work = {}
overnight = {}

for i in range(num_employees):
    overnight[i] = model.addVar(vtype=GRB.BINARY, name=f'employee_{i}_works_overnight')
    for j in range(hour - work_hours + 1):
        for k in range(j, j + work_hours):
            work[(i, j, k)] = model.addVar(vtype=GRB.BINARY, name=f'employee_{i}_start_{j}_work_{k}')

# Constraints
for i in range(num_employees):
    for j in range(hour - work_hours + 1):
        model.addConstr(gp.quicksum(work[(i, j, k)] for k in range(j, j + work_hours)) == 8 * work[(i, j, j)])

for i in range(num_employees):
    model.addConstr(gp.quicksum(work[(i, j, j)] for j in range(hour - work_hours + 1)) <= 1)

for i in range(num_employees):
    for j in range(6):
        for k in range(j, 6):
            model.addConstr(overnight[i] >= work[(i, j, k)])

for i in range(num_employees):
    for j in range(hour - work_hours + 1):
        model.addConstr(gp.quicksum(work[(i, j, k)] for k in range(j + 3, j + 6)) == 2 * work[(i, j, j)])

for k in range(hour):
    model.addConstr(gp.quicksum(work[(i, j, k)] for i in range(num_employees)
                                for j in range(max(0, k - work_hours + 1), k + 1)
                                if (i, j, k) in work) >= requirement[k])

# Objective Function
model.setObjective(10 * (gp.quicksum(work[(i, j, k)] for i in range(num_employees)
                                     for j in range(hour - work_hours + 1)
                                     for k in range(j, j + work_hours)))
                   + 20 * (gp.quicksum(overnight[i] for i in range(num_employees))),
                   GRB.MINIMIZE)

# Optimize the model
model.optimize()

# Check if the solution is optimal
if model.status == GRB.OPTIMAL:
    print(f'Optimal objective value (total cost): {model.objVal}')

    for i in range(num_employees):
        for j in range(hour - work_hours + 1):
            if work[(i, j, j)].x > 0.5:
                for k in range(j, j + work_hours):
                    if work[(i, j, k)].x < 0.5:
                        print(f'Employee {i} starts at hour {j} and takes a break at hour {k}')

    arr = []
    for k in range(hour):
        sumi = 0
        for j in range(max(0, k - work_hours + 1), k + 1):
            for i in range(num_employees):
                if (i, j, k) in work:
                    sumi += int(work[(i, j, k)].x)
        arr.append(sumi)

    print("Employees working each hour:", arr)
    print("Hourly requirements:", requirement)
else:
    print('No optimal solution found.')