# main.py
# main.py
from gurobipy import Model
from input_data import InputData
from decision_variables import DecisionVariables
from constraints import Constraints
from objective import Objective
from results import FinalTable

def solve_problem():
    data = InputData()
    results = []

    for i in range(30):
        model = Model('Optimization Model')

        decision_variables = DecisionVariables(model, data)
        decision_variables.create_variables()
        variables = decision_variables.get_variables()
        
        constraints = Constraints(model, data, i)
        constraints.add_constraints(variables['new_proportions'])
        
        objective = Objective(model, data, i)
        objective.set_objective(variables['new_proportions'])

        final_table = FinalTable(model, data, variables, i)
        table_output = final_table.print_table()

        results.append({
            'DMU': f'dmu_{i + 1}',
            'Objective Value': model.objVal,
            'Proportions': {v.varName: v.x for v in model.getVars()}
        })
        model.update()

        ##final_table.save_output(f'dmu_{i + 1}.txt', table_output)

    # Save all results to a single file
    with open('performance/outputs/all_results.txt', 'w') as f:
        for result in results:
            f.write(f"DMU: {result['DMU']}\n")
            f.write(f"Objective Value: {result['Objective Value']}\n")
            f.write("Proportions:\n")
            for name, value in result['Proportions'].items():
                f.write(f"  {name}: {value}\n")
            f.write("\n")
    

if __name__ == '__main__':
    solve_problem()
