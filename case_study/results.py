# final_table.py

from ortools.linear_solver import pywraplp

class FinalTable:
    def __init__(self, solver, **kwargs):
        self.solver = solver
        self.variables = kwargs
        self.months = ["January", "February", "March", "April", "May", "June"]
        self.products1 = ["veg 1", "veg 2", "oil 1", "oil 2", "oil 3"]
        self.products2 = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5", "Product 6", "Product 7"]

    def print_table(self):
        if self.solver.Solve() == pywraplp.Solver.OPTIMAL:
            print('Solution:')
            print(f'Objective value = {self.solver.Objective().Value()}')

            if self.variables['problem'] == 1 or self.variables['problem'] == 2:
                header = "Month       " + "  ".join([f"{prod:<10}" for prod in self.products1])
                print(header)

                for i in range(6):
                    item_row = f"{self.months[i]:<12}" + "  ".join([f"{self.variables['buy'][i][j].solution_value():<10.2f}" for j in range(5)])
                    sell_row = f"{'':<12}" + "  ".join([f"{self.variables['used'][i][j].solution_value():<10.2f}" for j in range(5)])
                    store_row = f"{'':<12}" + "  ".join([f"{self.variables['store'][i][j].solution_value():<10.2f}" for j in range(5)])
                    
                    print(item_row)
                    print(sell_row)
                    print(store_row)
                    print("-" * len(header))

            elif self.variables['problem'] == 3 :
                header = "Month       " + "  ".join([f"{prod:<10}" for prod in self.products2])
                print(header)

                for i in range(6):
                    item_row = f"{self.months[i]:<12}" + "  ".join([f"{self.variables['items'][i][j].solution_value():<10.2f}" for j in range(7)])
                    sell_row = f"{'':<12}" + "  ".join([f"{self.variables['sell'][i][j].solution_value():<10.2f}" for j in range(7)])
                    store_row = f"{'':<12}" + "  ".join([f"{self.variables['store'][i][j].solution_value():<10.2f}" for j in range(7)])
                    
                    print(item_row)
                    print(sell_row)
                    print(store_row)
                    print("-" * len(header))
                
                
            elif self.variables['problem']==4:
                header = "Month       " + "  ".join([f"{prod:<10}" for prod in self.products2])
                print(header)

                for i in range(6):
                    item_row = f"{self.months[i]:<12}" + "  ".join([f"{self.variables['items'][i][j].solution_value():<10.2f}" for j in range(7)])
                    sell_row = f"{'':<12}" + "  ".join([f"{self.variables['sell'][i][j].solution_value():<10.2f}" for j in range(7)])
                    store_row = f"{'':<12}" + "  ".join([f"{self.variables['store'][i][j].solution_value():<10.2f}" for j in range(7)])
                    
                    print(item_row)
                    print(sell_row)
                    print(store_row)
                    print("-" * len(header))
                
                header="month      "+ "grinding     "+"Vertical drilling     "+"hori            "+"boner    "+"planer    "
                print(header)
                for i in range(6):
                    row=item_row = f"{self.months[i]:<12}" + "  ".join([f"{self.variables['maintaince'][i][j].solution_value():<10.2f}" for j in range(7)])
                    print(row)
                    print("-"*len(header))

            elif self.variables['problem'] == 5 or self.variables['problem'] == 51:
                months = ["Year 1", "Year 2", "Year 3"]
                variables = ["tSK", "tSS", "tUS", "uSK", "uSS", "uUS", "vUSSS", "vSSSK", "vSKSS", "uSKUS", "vSSUS", "wSK", "wSS", "wUS", "xSK", "xSS", "xUS", "ySK", "ySS", "yUS"]
                # Print header
                header = "Variable".ljust(10) + " ".join([f"{month:<10}" for month in months])
                print(header)
                # Print variable values
                for var in variables:
                    var_name = var.ljust(10)
                    var_values = " ".join([f"{self.variables[var][i].solution_value():<10.2f}" for i in range(3)])
                    print(var_name + var_values)
            
            elif self.variables['problem']==7:
                print("| {:<10} | {:<10} | {:<10} | {:<15} | {:<15}|".format("Index", "Year", "Operate","Open", "Output (millions)"))
                for j in range(len(self.variables["operate"])):
                    for i in range(len(self.variables["operate"][j])):
                        operate_value = self.variables["operate"][j][i].solution_value()
                        ope_value = self.variables["ope"][j][i].solution_value()
                        output_value = self.variables["output"][j][i].solution_value() / (10**6)
                        print("| {:<10} | {:<10} | {:<10} | {:<15.2f} |  {:<15.2f}|".format(i+1, j+1, operate_value,ope_value, output_value))

            elif self.variables['problem']==10:
                for i in range(3):
                    print(f'City {i}:')
                    for j in range(5):
                        if self.variables['open'][i][j].solution_value() == 1:
                            print(f'- Department {j}')
            
            elif self.variables['problem']==11 or self.variables['problem']==111:
                print(f'a = {self.variables['a'].solution_value()}')
                print(f'b = {self.variables['b'].solution_value()}')
            
            elif self.variables['problem']==13:
                for i in range(23):
                    print(f'M{i+1} belongs to D1: {self.variables['open'][i].solution_value()}')
            
            elif self.variables['problem']==15:
                for i in range(5):
                    for j in range(3):
                        print(f'Period {i + 1}, Ty {j + 1}:  Num = {self.variables['num'][j][i].solution_value()}')
                        #print(f'  Ty = {ty[j][i].solution_value()}')
                    
                        ##print(f'  Num = {self.variables['num'][j][i].solution_value()}')
                        #print(f'  Start = {start[j][i].solution_value()}')
                           
