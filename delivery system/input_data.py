# input_data.py
import pandas as pd
import numpy as np

class InputData:
    def __init__(self):
        self.load_data()

    def load_data(self):
        file_path = 'delivery system/truckdata.xlsx'
        df = pd.read_excel(file_path)
        self.num_locations=100
        df=df.head(self.num_locations)
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.num_days = len(self.days)
        self.truck_types = [15, 10]   
        self.truck_costs = [150, 120] 
        self.W=df["Weekly_Weight_Requirement"]
        self.patterns={
    0: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],  
    1: ['Monday'],                      
    2: ['Monday', 'Thursday'],                 
    3: ['Monday', 'Wednesday', 'Friday']            
}
        

                        

