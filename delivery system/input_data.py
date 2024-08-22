# input_data.py
import pandas as pd
import numpy as np

class InputData:
    def __init__(self):
        self.load_data()

    def load_data(self):
        file_path = 'delivery system/truckdata.xlsx'
        df = pd.read_excel(file_path)
        self.num_locations=10
        df=df.head(self.num_locations)
        self.days = ['M', 'T', 'W', 'R', 'F']
        self.num_days = len(self.days)
        self.truck_types = [15, 10]   
        self.truck_costs = [150, 120] 
        self.W=df["Weekly_Weight_Requirement"]
        self.patterns={
    0: ['M', 'T', 'W', 'R', 'F'],  
    1: ['M'],                      
    2: ['M', 'R'],                 
    3: ['M', 'W', 'F']            
}
        

                        

