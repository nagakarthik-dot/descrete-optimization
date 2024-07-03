### prints the final table with all the results 

import os
from ortools.linear_solver import pywraplp

class FinalTable:
    def __init__(self, solver, **kwargs):
        self.solver = solver
        self.variables = kwargs
        self.months = ["January", "February", "March", "April", "May", "June"]
        self.products1 = ["veg 1", "veg 2", "oil 1", "oil 2", "oil 3"]
        self.products2 = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5", "Product 6", "Product 7"]

    def save_output(self, filename, content):
        os.makedirs("case_study/outputs", exist_ok=True)
        with open(f"case_study/outputs/{filename}", "w") as file:
            file.write(content)

    def print_table(self):
        
        if self.solver.Solve() == pywraplp.Solver.OPTIMAL  :
            output = 'Solution:\n'
            output += f'Objective value = {self.solver.Objective().Value()}\n\n'
            problem = self.variables['problem']
            
            if problem == 1 or problem == 2:
                header = "Month       " + "  ".join([f"{prod:<10}" for prod in self.products1]) + '\n'
                output += header
                
                for i in range(6):
                    item_row = f"{self.months[i]:<12}" + "  ".join([f"{self.variables['buy'][i][j].solution_value():<10.2f}" for j in range(5)]) + '\n'
                    sell_row = f"{'':<12}" + "  ".join([f"{self.variables['used'][i][j].solution_value():<10.2f}" for j in range(5)]) + '\n'
                    store_row = f"{'':<12}" + "  ".join([f"{self.variables['store'][i][j].solution_value():<10.2f}" for j in range(5)]) + '\n'
                    
                    output += item_row
                    output += sell_row
                    output += store_row
                    output += "-" * len(header) + '\n'
            
            elif problem == 3:
                header = "Month       " + "  ".join([f"{prod:<10}" for prod in self.products2]) + '\n'
                output += header

                for i in range(6):
                    item_row = f"{self.months[i]:<12}" + "  ".join([f"{self.variables['items'][i][j].solution_value():<10.2f}" for j in range(7)]) + '\n'
                    sell_row = f"{'':<12}" + "  ".join([f"{self.variables['sell'][i][j].solution_value():<10.2f}" for j in range(7)]) + '\n'
                    store_row = f"{'':<12}" + "  ".join([f"{self.variables['store'][i][j].solution_value():<10.2f}" for j in range(7)]) + '\n'
                    
                    output += item_row
                    output += sell_row
                    output += store_row
                    output += "-" * len(header) + '\n'
            
            elif problem == 4:
                header = "Month       " + "  ".join([f"{prod:<10}" for prod in self.products2]) + '\n'
                output += header

                for i in range(6):
                    item_row = f"{self.months[i]:<12}" + "  ".join([f"{self.variables['items'][i][j].solution_value():<10.2f}" for j in range(7)]) + '\n'
                    sell_row = f"{'':<12}" + "  ".join([f"{self.variables['sell'][i][j].solution_value():<10.2f}" for j in range(7)]) + '\n'
                    store_row = f"{'':<12}" + "  ".join([f"{self.variables['store'][i][j].solution_value():<10.2f}" for j in range(7)]) + '\n'
                    
                    output += item_row
                    output += sell_row
                    output += store_row
                    output += "-" * len(header) + '\n'
                
                header = "month      " + "grinding     " + "Vertical drilling     " + "hori            " + "boner    " + "planer    " + '\n'
                output += header
                for i in range(6):
                    row = item_row = f"{self.months[i]:<12}" + "  ".join([f"{self.variables['maintaince'][i][j].solution_value():<10.2f}" for j in range(7)]) + '\n'
                    output += row
                    output += "-" * len(header) + '\n'

            elif problem == 5 or problem == 51:
                months = ["Year 1", "Year 2", "Year 3"]
                variables = ["tSK", "tSS", "tUS", "uSK", "uSS", "uUS", "vUSSS", "vSSSK", "vSKSS", "uSKUS", "vSSUS", "wSK", "wSS", "wUS", "xSK", "xSS", "xUS", "ySK", "ySS", "yUS"]
                # Print header
                header = "Variable".ljust(10) + " ".join([f"{month:<10}" for month in months]) + '\n'
                output += header
                # Print variable values
                for var in variables:
                    var_name = var.ljust(10)
                    var_values = " ".join([f"{self.variables[var][i].solution_value():<10.2f}" for i in range(3)]) + '\n'
                    output += var_name + var_values

            elif problem == 7:
                output += "| {:<10} | {:<10} | {:<10} | {:<15} | {:<15}|\n".format("Index", "Year", "Operate","Open", "Output (millions)")
                for j in range(len(self.variables["operate"])):
                    for i in range(len(self.variables["operate"][j])):
                        operate_value = self.variables["operate"][j][i].solution_value()
                        ope_value = self.variables["ope"][j][i].solution_value()
                        output_value = self.variables["output"][j][i].solution_value() / (10**6)
                        output += "| {:<10} | {:<10} | {:<10} | {:<15.2f} |  {:<15.2f}|\n".format(i+1, j+1, operate_value,ope_value, output_value)

            elif problem == 10:
                for i in range(3):
                    output += f'City {i}:\n'
                    for j in range(5):
                        if self.variables['open'][i][j].solution_value() == 1:
                            output += f'- Department {j}\n'

            elif problem == 11 or problem == 111:
                output += f'a = {self.variables["a"].solution_value()}\n'
                output += f'b = {self.variables["b"].solution_value()}\n'

            elif problem == 13:
                for i in range(23):
                    output += f'M{i+1} belongs to D1: {self.variables["open"][i].solution_value()}\n'

            elif problem == 15:
                for i in range(5):
                    for j in range(3):
                        output += f'Period {i + 1}, Ty {j + 1}:  Num = {self.variables["num"][j][i].solution_value()}\n'
            
            elif problem == 19:
                for i in range(2):
                    for j in range(4):
                        output += f'factory{i} to depot{j} = {self.variables["facttodepot"][i][j].solution_value()}\n'
                output += '\n'
                for i in range(2):
                    for j in range(6):
                        output += f'factory{i} to cust{j} = {self.variables["facttocust"][i][j].solution_value()}\n'
                output += '\n'
                for i in range(4):
                    for j in range(6):
                        output += f'depot{i} to cust{j} = {self.variables["depottocust"][i][j].solution_value()}\n'
            elif problem ==17:
                output+="balck: "
                for i in range(27):
                    if self.variables["cell"][i].solution_value()>=0.5:
                        output+=f'    {i} ---->'

            elif problem == 27:
                for i in range(6):
                    if self.variables['used'][i].solution_value()>=1:
                        output+='\n'+f'path for day {i}'+'\n'
                        for j in range(15):
                            for k in range(15):
                                if self.variables['path'][i][j][k].solution_value()>=1:
                                    output+=f'{j} to {k}        '

    
            elif problem==14:
                output+='\n'
                output+="extracted blocks"
                output+='\n'
                for i in range(30):
                    if self.variables['remove'][i].solution_value()>0.5:
                        output+= f'{i}'
                        output+='   ->   '
            elif problem ==18:
                for i in range(8):
                    output+=f'a[{i}] = {self.variables['a'][i].solution_value()}\n'
                output+= f'arhs = {self.variables['arhs'].solution_value()}\n'
            
            elif problem ==23:
                for k in range(2):
                    
                    start = 0
                    path = []
                    while True:
                        path.append(start+1)
                        next_found = False
                        for j in range(21):
                            if self.variables['x'][start][j][k].solution_value() >= 0.5:
                                start = j
                                next_found = True
                                break
                        if not next_found or start == 0:
                            break
                    path.append(1)
                    output+=f'path for day {k} \n'
                    for i in path :
                        output+= str(i)
                        output+= "-> "
                    output+="\n"
            


        



            self.save_output(f'problem_{problem}.txt', output)
            

