# input_data.py
import pandas as pd
import numpy as np

class InputData:
    def __init__(self):
        self.load_data()

    def load_data(self):
        file_path = 'C:/Users/olw09/karthikcase/descrete-optimization/food/foodconsumption.xlsx'
        df = pd.read_excel(file_path)

        self.dishes = df['Dishes']
        self.profit = pd.to_numeric(df['Profit(₹)'], errors='coerce').fillna(0).values
        self.loss_of_demand = pd.to_numeric(df['Loss_on_demand(₹)'], errors='coerce').fillna(0).values
        self.loss_of_wastage = pd.to_numeric(df['Loss_on_wastage₹'], errors='coerce').fillna(0).values
        self.shelf_life = pd.to_numeric(df['shelf_life(hr)'], errors='coerce').fillna(0).values
        self.num_dishes = 20
        self.num_hours = 14
        file='C:/Users/olw09/karthikcase/descrete-optimization/food/requirement.xlsx'
        df1=pd.read_excel(file)
        np.random.seed(0)  
        self.requirement = np.zeros((self.num_dishes, self.num_hours), dtype=int)
        #self.requirement = np.zeros((self.num_dishes, self.num_hours), dtype=int)
        #self.requirement[:, 5:] = np.random.randint(0, 11, size=(self.num_dishes, self.num_hours-5))
        self.requirement[:, 5:]=df1.iloc[:, 1:self.num_hours-4].values.astype(int)
        

                        

