from gurobipy import Model,GRB
from input_data import InputData
from decision_variables import DecisionVariables
from constraints import Constraints
from objective import Objective
from results import FinalTable

def solve_problem():
    model = Model('Optimization Model')
    data = InputData()

    # Initial tax rate
    initial_tax = 0.1
    tolerance = 0.05  # Tolerance level to determine how close we are to the target

    # Iterate to find optimal tax rate
    tax_rate = initial_tax
    while True:
        # Set tax rate
        data.tax = tax_rate

        # Create decision variables
        decision_variables = DecisionVariables(model)
        decision_variables.create_variables()
        variables = decision_variables.get_variables()
        
        # Add constraints
        constraints = Constraints(model, data)
        constraints.add_constraints(variables['new_waste'])
        
        # Set objective function
        objective = Objective(model, data)
        objective.set_objective(variables['new_waste'])

        # Solve the model
        model.optimize()
        if model.status == GRB.OPTIMAL:
            total_waste_removed = sum(data.waste[i] * (data.concentration[i] - variables['new_waste'][i].x) for i in range(4))
            
            # Compute subsidy after optimization
            if total_waste_removed == 0:
                subsidy = 0
            else:
                subsidy = (data.tax * total_waste_removed - data.moni) / total_waste_removed

            # Check if total waste is approximately equal to the target
            if abs(total_waste_removed - data.target) <= tolerance:
                break
            elif total_waste_removed < data.target:
                tax_rate -= 0.05  # Decrease tax rate
            else:
                tax_rate += 0.05  # Increase tax rate
        else:
            print("No optimal solution found.")
            return

    # Output results
    final_table = FinalTable(model, variables, data)
    table_output = final_table.print_table()
    
    print(table_output)
    final_table.save_output('two-level.txt', table_output)
    final_table.plot_results()  # Plot results with tax

if __name__ == '__main__':
    solve_problem()
