# main.py

from ortools.linear_solver import pywraplp
from input_data import InputData
from constraints import Constraints
from objective import Objective
from final_table import FinalTable

def solve_problem(problem):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print('Solver not created.')
        return

    data = InputData(problem)

    if problem == 1:
        buy = [[solver.NumVar(0, 1000, f'buy[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
        used = [[solver.NumVar(0, solver.infinity(), f'used[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
        store = [[solver.NumVar(0, solver.infinity(), f'store[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]

        constraints = Constraints(solver, data, problem)
        constraints.add_constraints(buy=buy, used=used, store=store)

        objective = Objective(solver, data, problem)
        objective.set_objective(buy=buy, used=used, store=store)

        final_table = FinalTable(solver, buy=buy, used=used, store=store, problem=problem)
        final_table.print_table()
    if problem==2:
        buy = [[solver.NumVar(0, solver.infinity(), f'buy[{i}][{j}]') for j in range(5)] for i in range(6)]
        used = [[solver.NumVar(0, solver.infinity(), f'used[{i}][{j}]') for j in range(5)] for i in range(6)]
        store = [[solver.NumVar(0, solver.infinity(), f'store[{i}][{j}]') for j in range(5)] for i in range(6)]
        usedby =[[solver.BoolVar(f'oil {j} used in month {i}') for j in range(5)] for i in range(6)]
        constraints = Constraints(solver, data, problem)
        constraints.add_constraints(buy=buy, used=used, store=store,usedby=usedby)

        objective = Objective(solver, data, problem)
        objective.set_objective(buy=buy, used=used, store=store,usedby=usedby)

        final_table = FinalTable(solver, buy=buy, used=used, store=store,usedby=usedby, problem=problem)
        final_table.print_table()
    if problem == 3:
        items = [[solver.NumVar(0, solver.infinity(), f'items[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
        sell = [[solver.NumVar(0, solver.infinity(), f'sell[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]
        store = [[solver.NumVar(0, 100, f'store[{i}][{j}]') for j in range(data.num_products)] for i in range(data.num_months)]

        constraints = Constraints(solver, data, problem)
        constraints.add_constraints(items=items, sell=sell, store=store)

        objective = Objective(solver, data, problem)
        objective.set_objective(items=items, sell=sell, store=store)

        final_table = FinalTable(solver, items=items, sell=sell, store=store, problem=problem)
        final_table.print_table()
    
    if problem ==5 or problem==51:
        tSK = [solver.NumVar(0, solver.infinity(), f'tSK[{i}]') for i in range(4)] 
        tSS = [solver.NumVar(0, solver.infinity(), f'tSS[{i}]') for i in range(4)]
        tUS = [solver.NumVar(0, solver.infinity(), f'tUS[{i}]') for i in range(4)]
        ## recuited
        uSK = [solver.NumVar(0, 500, f'uSK[{i}]') for i in range(data.num_years)]
        uSS = [solver.NumVar(0, 800, f'uSS[{i}]') for i in range(data.num_years)]
        uUS = [solver.NumVar(0, 500, f'uUS[{i}]') for i in range(data.num_years)]
## retrained
        vUSSS = [solver.NumVar(0, 200, f'vUSSS[{i}]') for i in range(data.num_years)]  ## unskill to semi skill
        vSSSK = [solver.NumVar(0, solver.infinity(), f'vSSSK[{i}]') for i in range(data.num_years)]  ## semi to skill
## down
        vSKSS = [solver.NumVar(0, solver.infinity(), f'vSKSS[{i}]') for i in range(data.num_years)]  ## skill to semi
        uSKUS = [solver.NumVar(0, solver.infinity(), f'uSKUS[{i}]') for i in range(data.num_years)]   ## skill to unskill
        vSSUS = [solver.NumVar(0, solver.infinity(), f'vSSUS[{i}]') for i in range(data.num_years)]   ## semi to uns kill 
## redundacy
        wSK = [solver.NumVar(0, solver.infinity(), f'wSK[{i}]') for i in range(data.num_years)]
        wSS = [solver.NumVar(0, solver.infinity(), f'wSS[{i}]') for i in range(data.num_years)]
        wUS = [solver.NumVar(0, solver.infinity(), f'wUS[{i}]') for i in range(data.num_years)]
## short time
        xSK = [solver.NumVar(0,50, f'xSK[{i}]') for i in range(data.num_years)]
        xSS = [solver.NumVar(0, 50, f'xSS[{i}]') for i in range(data.num_years)]
        xUS = [solver.NumVar(0, 50, f'xUS[{i}]') for i in range(data.num_years)]
        #3 over man 
        ySK = [solver.NumVar(0, solver.infinity(), f'ySK[{i}]') for i in range(data.num_years)]
        ySS = [solver.NumVar(0, solver.infinity(), f'ySS[{i}]') for i in range(data.num_years)]
        yUS = [solver.NumVar(0, solver.infinity(), f'yUS[{i}]') for i in range(data.num_years)]
        constraints = Constraints(solver, data, problem)
        constraints.add_constraints(tSK=tSK,tSS=tSS,tUS=tUS,uSK=uSK,uSS=uSS,uUS=uUS,vUSSS=vUSSS,vSSSK=vSSSK,vSKSS=vSKSS,uSKUS=uSKUS,vSSUS=vSSUS,wSK=wSK,wSS=wSS,wUS=wUS,xSK=xSK,xSS=xSS,xUS=xUS,ySK=ySK,ySS=ySS,yUS=yUS)

        objective = Objective(solver, data, problem)
        objective.set_objective(tSK=tSK,tSS=tSS,tUS=tUS,uSK=uSK,uSS=uSS,uUS=uUS,vUSSS=vUSSS,vSSSK=vSSSK,vSKSS=vSKSS,uSKUS=uSKUS,vSSUS=vSSUS,wSK=wSK,wSS=wSS,wUS=wUS,xSK=xSK,xSS=xSS,xUS=xUS,ySK=ySK,ySS=ySS,yUS=yUS)

        final_table = FinalTable(solver, tSK=tSK, tSS=tSS, tUS=tUS, uSK=uSK, uSS=uSS, uUS=uUS, vUSSS=vUSSS, vSSSK=vSSSK, vSKSS=vSKSS,
                             uSKUS=uSKUS, vSSUS=vSSUS, wSK=wSK, wSS=wSS, wUS=wUS, xSK=xSK, xSS=xSS, xUS=xUS, ySK=ySK, ySS=ySS, yUS=yUS, problem=problem)
        final_table.print_table()

    if problem ==7:
        operate = [[solver.BoolVar(f'mine{i} is operated in year{j}') for i in range(4)]for j in range(5)]
        ope = [[solver.BoolVar(f'mine{i} is open in year{j}') for i in range(4)]for j in range(5)]
        output=[[solver.NumVar(0,solver.infinity(),'output') for i in range(4)]for j in range(5)]
        constraints = Constraints(solver, data, problem)
        constraints.add_constraints(operate=operate,ope=ope,output=output)

        objective = Objective(solver, data, problem)
        objective.set_objective(operate=operate,ope=ope,output=output)

        final_table = FinalTable(solver, operate=operate,ope=ope,output=output, problem=problem)
        final_table.print_table()
    
    
    if problem ==10:
        open = [[solver.BoolVar(f'city_{i}_has_dept_{j}') for j in range(5)] for i in range(3)]
        path= [[[[solver.BoolVar(f'city_{i}_has_dept_{j}_and_city_{k}_has_dept_{l}')for l in range(5)]for k in range(3)]for j in range(5)]for i in range(3)]
        constraints = Constraints(solver, data, problem)
        constraints.add_constraints(open=open,path=path)

        objective = Objective(solver, data, problem)
        objective.set_objective(open=open,path=path)

        final_table = FinalTable(solver, open=open,path=path, problem=problem)
        final_table.print_table()





if __name__ == '__main__':
    problem_choice = input("Enter Problem num: ")
    
    solve_problem(int(problem_choice))
  
