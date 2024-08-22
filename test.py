import gurobipy as gp
from gurobipy import GRB
import random

# Parameters
locations = 20  # Number of delivery locations
days = ['M', 'T', 'W', 'R', 'F']  # Days of the week
twice_pairs = [('M', 'R'), ('T', 'F')]  # Pairs of days for twice-a-week deliveries
thrice_pairs = ['M', 'W', 'F']  # Days for thrice-a-week deliveries
five_times_pair = ['M', 'T', 'W', 'R', 'F']  # Days for five-times-a-week deliveries

# Truck capacities and costs
truck_capacity = {15: 15, 10: 10}  # Truck capacities (tons)
truck_cost = {15: 180, 10: 120}  # Cost for each truck type

# Example weight requirements for each location (randomly generated)
random.seed(1)
W = {i: random.randint(1, 50) for i in range(locations)}
print("Weight requirements for each location:", W)

# Model initialization
model = gp.Model("Truck_Delivery_Optimization")

# Decision Variables

# 1. `Select[i, t]`: Binary variable indicating if location `i` follows delivery routine `t`
#    `t` can be 1 (once a week), 2 (twice a week), 3 (thrice a week), or 5 (five times a week).
Select = model.addVars(locations, [1, 2, 3, 5], vtype=GRB.BINARY, name="Select")

# 2. `A[i, day, t]`: Binary variable indicating if location `i` receives a delivery on `day`
#    according to routine `t`.
A = model.addVars(locations, days, [1, 2, 3, 5], vtype=GRB.BINARY, name="A")

# 3. `N_15[day]`: Integer variable representing the number of 15-ton trucks used on `day`.
N_15 = model.addVars(days, vtype=GRB.INTEGER, name="N_15")

# 4. `N_10[day]`: Integer variable representing the number of 10-ton trucks used on `day`.
N_10 = model.addVars(days, vtype=GRB.INTEGER, name="N_10")

# 5. `min_trucks_10`: Auxiliary integer variable representing the minimum number of 10-ton trucks used across all days.
min_trucks_10 = model.addVar(vtype=GRB.INTEGER, lb=0, name="min_trucks_10")

# 6. `min_trucks_15`: Auxiliary integer variable representing the minimum number of 15-ton trucks used across all days.
min_trucks_15 = model.addVar(vtype=GRB.INTEGER, lb=0, name="min_trucks_15")

# Constraints

# 1. Ensure that the minimum number of trucks required (across all days) is correctly recorded.
for d in days:
    model.addConstr(min_trucks_15 >= N_15[d], f"MinTrucks15_{d}")
    model.addConstr(min_trucks_10 >= N_10[d], f"MinTrucks10_{d}")

# 2. Ensure that each location selects exactly one delivery routine.
for i in range(locations):
    model.addConstr(Select.sum(i, '*') == 1, f"SelectSum_{i}")

# 3. Ensure the correct routine is selected for each location, based on the delivery days.
for i in range(locations):
    for t in [1, 2, 3, 5]:
        model.addConstr(
            Select[i, t] == gp.quicksum(A[i, day, t] / t for day in days),
            f"Select_{i}_{t}"
        )

# 4. Ensure that the daily truck capacity meets the demand for all locations.
for day in days:
    model.addConstr(
        N_15[day] * truck_capacity[15] + N_10[day] * truck_capacity[10] >=
        gp.quicksum(A[i, day, t] * W[i] / t for i in range(locations) for t in [1, 2, 3, 5]),
        f"Capacity_{day}"
    )

# 5. Routine-specific constraints for twice-a-week deliveries.
for i in range(locations):
    for j in twice_pairs:
        model.addConstr(A[i, j[0], 2] == A[i, j[1], 2], f"TwicePair_{i}_{j}")

# 6. Routine-specific constraints for thrice-a-week deliveries.
    model.addConstr(A[i, thrice_pairs[0], 3] == A[i, thrice_pairs[1], 3], f"ThricePair_{i}_1")
    model.addConstr(A[i, thrice_pairs[1], 3] == A[i, thrice_pairs[2], 3], f"ThricePair_{i}_2")

# 7. Routine-specific constraints for five-times-a-week deliveries.
    for k in range(len(five_times_pair) - 1):
        model.addConstr(A[i, five_times_pair[k], 5] == A[i, five_times_pair[k + 1], 5], f"FiveTimesPair_{i}_{k}")

# Objective Function: Multi-objective optimization

# 1. Objective 1: Minimize the total cost of trucks used
model.setObjectiveN(
    gp.quicksum(N_15[day] * truck_cost[15] + N_10[day] * truck_cost[10] for day in days),
    priority=2, index=0, weight=1
)

# Set a time limit for the first objective
env_0 = model.getMultiobjEnv(0)
env_0.setParam("TimeLimit", 3)

# 2. Objective 2: Minimize the total number of trucks used across all days
model.setObjectiveN(
    expr=min_trucks_10 + min_trucks_15,
    priority=1, index=1, weight=1
)

# Optimize the model
model.optimize()

# Check the solution status and print the results
if model.status not in [GRB.UNBOUNDED, GRB.INFEASIBLE, GRB.INF_OR_UNBD]:
    if model.status == GRB.OPTIMAL:
        print(f"Optimal cost: {model.objVal}")
    else:
        print(f"Feasible cost: {model.objVal}")

    # Output truck usage per day
    for day in days:
        print(f"{day}: 15-ton trucks = {N_15[day].X}, 10-ton trucks = {N_10[day].X}")

    # Output selected decision variables
    for var in model.getVars():
        if var.X > 0.1:
            print(f"{var.VarName} = {var.X}")
else:
    print("No optimal solution found.")
