# input_data.py
import pandas as pd

class InputData:
    def __init__(self):
        self.load_data()

    def load_data(self):

        data=pd.read_excel("AIIMS_CASE_STUDIES/facility/city_data.xlsx")
        type_of_centers=set(data["Type"])
        type_counts = data["Type"].value_counts()
        # Read demand and prices
        self.c=2   ###commodities
        self.p=type_counts.get("Production plant", 0)
        #self.p=2   ### production plants
        self.d=type_counts.get("Distribution center", 0)
        #self.d= 7   ###distribution centers
        self.z=type_counts.get("Customer zone", 0)
        #self.z= 3  ### customer zones
        ## supply for c at p

        self.s_cp=[[18,15],[18,40]]
        ## demand for c in z
        self.d_cz=[[8,9,7],[9,10,11]]
        ### max demand at d
        self.max_d=[20,20,14,20,21,17,16]
        ### min demand at d
        self.min_d=[2,0,0,0,0,0,0]
        ### per unit charge at d
        self.r_d=[5,7,3,5.5,6,7,3.5]
        ### fixed cost for d 
        self.f_d=[180,130,60,150,140,150,100]
        ### cost prodution and shipping for c from p via d to z
        production_plants = data[data['Type'] == 'Production plant']
        self.lp=production_plants[['X-coord.', 'Y-coord.']].values

        Distribution = data[data['Type'] == 'Distribution center']
        self.ld=Distribution[['X-coord.', 'Y-coord.']].values

        Customer = data[data['Type'] == 'Customer zone']
        self.lc=Customer[['X-coord.', 'Y-coord.']].values

        #self.lp=[[191,444],[92,436]]
        #self.ld=[[121,488],[79,454],[136,455],[108,447],[155,464],[203,503],[187,427]]
        #self.lc=[[175,318],[103,489],[233,582]]


