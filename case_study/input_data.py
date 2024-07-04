# input_data.py
# contains all the input data
class InputData:
    def __init__(self, problem):
        if problem == 1:
            self.hardmax = [2.8, 0.1, -4.0, -1.8, -1.0]
            self.hardmin = [5.8, 3.1, -1.0, 1.2, 2.0]
            self.prices = [
                [110, 120, 130, 110, 115],
                [130, 130, 110, 90, 115],
                [110, 140, 130, 100, 95],
                [120, 110, 120, 120, 125],
                [100, 120, 150, 110, 105],
                [90, 100, 140, 80, 135]
            ]
            self.num_months = 6
            self.num_products = 5
        if problem ==2:
            self.hardmax = [2.8, 0.1, -4.0, -1.8, -1.0]
            self.hardmin = [5.8, 3.1, -1.0, 1.2, 2.0]
            self.prices = [
                [110, 120, 130, 110, 115],
                [130, 130, 110, 90, 115],
                [110, 140, 130, 100, 95],
                [120, 110, 120, 120, 125],
                [100, 120, 150, 110, 105],
                [90, 100, 140, 80, 135]
            ]
            self.num_months = 6
            self.num_products = 5

        if problem == 3:
            self.machines = [[3,2,3,1,1],[4,2,1,1,1],[4,2,3,0,1],[4,1,3,1,1],[3,1,3,1,1],[4,2,2,1,0]]
            self.hours = [
                [0.5, 0.7, 0.0, 0.0, 0.3, 0.2, 0.5], 
                [0.1, 0.2, 0.0, 0.3, 0.0, 0.6, 0.0],  
                [0.2, 0.0, 0.8, 0.0, 0.0, 0.0, 0.6],  
                [0.05, 0.03, 0.0, 0.07, 0.1, 0.0, 0.08],  
                [0.0, 0.0, 0.01, 0.0, 0.05, 0.0, 0.05]   
            ]
            self.limit = [
                [500, 1000, 300, 300, 800, 200, 100],   
                [600, 500, 200, 0, 400, 300, 150],      
                [300, 600, 0, 0, 500, 400, 100],        
                [200, 300, 400, 500, 200, 0, 100],      
                [0, 100, 500, 100, 1000, 300, 0],       
                [500, 500, 100, 300, 1100, 500, 60]     
            ]
            self.cost = [10, 6, 8, 4, 11, 9, 3]
            self.num_months = 6
            self.num_products = 7
        if problem==4:
            self.machines = [4,2,3,1,1]
            self.hours = [
                [0.5, 0.7, 0.0, 0.0, 0.3, 0.2, 0.5], 
                [0.1, 0.2, 0.0, 0.3, 0.0, 0.6, 0.0],  
                [0.2, 0.0, 0.8, 0.0, 0.0, 0.0, 0.6],  
                [0.05, 0.03, 0.0, 0.07, 0.1, 0.0, 0.08],  
                [0.0, 0.0, 0.01, 0.0, 0.05, 0.0, 0.05]   
            ]
            self.limit = [
                [500, 1000, 300, 300, 800, 200, 100],   
                [600, 500, 200, 0, 400, 300, 150],      
                [300, 600, 0, 0, 500, 400, 100],        
                [200, 300, 400, 500, 200, 0, 100],      
                [0, 100, 500, 100, 1000, 300, 0],       
                [500, 500, 100, 300, 1100, 500, 60]     
            ]
            self.cost = [10, 6, 8, 4, 11, 9, 3]
            self.num_months = 6
            self.num_products = 7

        
        if problem ==5 or problem==51:
            self.num_years=3
            self.num_variables = 3 * self.num_years
            self.skill=[1000,1500,2000]
            self.semi=[1400,2000,2500]
            self.un=[1000,500,0]
        
        if problem ==7:
            self.capacity=[2000000,2500000,1300000,3000000]
            self.mine_quality=[1.0,0.7,1.5,0.5]
            self.year_quality=[0.9,0.8,1.2,0.6,1.0]
            self.royal=[5,4,4,5]
        
        if problem ==10:
            self.comm = [
    [0,   0,   1.0, 1.5, 0.0],
    [0,   0,   1.4, 1.2, 0.0],
    [1.0, 1.4, 0,   0,   2.0],
    [1.5, 1.2, 0,   0,   0.7],
    [0.0, 0,0, 2,   0.7,  0.0]
]
            self.city = [
    [5, 14, 13],
    [14, 5, 9],
    [13, 9, 10]
]

            self.dept =[ [10, 15, 10, 20, 5], [10, 20, 15, 15, 15],[0,0,0,0,0]]
        if problem ==11 or problem ==111:
            self.x = [0.0, 0.5, 1.0, 1.5, 1.9, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.6, 7.0, 7.6, 8.5, 9.0, 10.0]
            self.y = [1.0, 0.9, 0.7, 1.5, 2.0, 2.4, 3.2, 2.0, 2.7, 3.5, 1.0, 4.0, 3.6, 2.7, 5.7, 4.6, 6.0, 6.8, 7.3]
        
        if problem ==13:
            self.dict = [
    [1, 9, 11, 34, 'A'],
    [1, 13, 47, 411, 'A'],
    [1, 14, 44, 82, 'A'],
    [1, 17, 25, 157, 'B'],
    [1, 18, 10, 5, 'A'],
    [1, 19, 26, 183, 'A'],
    [1, 23, 26, 14, 'B'],
    [1, 21, 54, 215, 'B'],
    [2, 9, 18, 102, 'B'],
    [2, 11, 51, 21, 'A'],
    [2, 17, 20, 54, 'B'],
    [2, 18, 105, 0, 'B'],
    [2, 18, 7, 6, 'B'],
    [2, 17, 16, 96, 'B'],
    [2, 22, 34, 118, 'A'],
    [2, 24, 100, 112, 'B'],
    [2, 36, 50, 535, 'B'],
    [2, 43, 21, 8, 'B'],
    [3, 6, 11, 53, 'B'],
    [3, 15, 19, 28, 'A'],
    [3, 15, 14, 69, 'B'],
    [3, 25, 10, 65, 'B'],
    [3, 39, 11, 27, 'B']
]
        if problem ==15:
            self.minwatt = [850, 1250, 1500]
            self.minwatt = [850, 1250, 1500]
            self.maxwatt = [2000, 1750, 4000]
            self.demand = [15000, 30000, 25000, 40000, 27000]
            self.setup = [2000, 1000, 500]
            self.avail = [12, 10, 5]
            self.costmin = [1000, 2600, 3000]
            self.costex = [2, 1.3, 3]

        if problem == 19:
            self.f_c=[150000,200000]
            self.d_c=[70000,50000,100000,40000]
            self.demand=[50000,10000,40000,35000,60000,20000]
            self.dat1=[
    [0.5, 0.0],  
    [0.5, 0.3],  
    [1.0, 0.5],  
    [0.2, 0.2]   
]
            self.dat2=[[1,0,1.5,2,0,1],[2,0,0,0,0,0]]
            self.dat3=[[0,1.5,0.5,1.5,0,1],[1,0.5,0.5,1,0.5,0],[0,1.5,2,0,0.5,1.5],[0,0,0.2,1.5,0.5,1.5]]
        
        if problem ==17:
            self.cells_line = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [10, 11, 12], [13, 14, 15], [16, 17, 18],
    [19, 20, 21], [22, 23, 24], [25, 26, 27],
    [1, 4, 7], [2, 5, 8], [3,6, 9],
    [10, 13, 16], [11, 14, 17], [12, 15, 18],
    [19, 22, 25], [20, 23, 26], [21, 24, 27],
    [1, 5, 9], [3, 5, 7], [10, 14, 18], [16, 14, 12], [19, 23, 27], [21, 23, 25],
    [1, 10, 19], [2, 11, 20], [3, 12, 21], [1, 11, 21], [3, 11, 19],
    [4, 13, 22], [5, 14, 23], [6, 15, 24], [4, 14, 24], [6, 14, 22],
    [7, 16, 25], [8, 17, 26], [9, 18, 27], [7, 17, 27], [9, 17, 25],
    [1, 13, 25], [7, 13, 19], [3, 15, 27], [21, 15, 9],
    [1, 14, 27], [3, 14, 25], [7, 14, 21], [9, 14, 19], [2, 14, 26], [8, 14, 20]
]
        if problem==27:
            self.distance_matrix = [
    [0, 20, 25, 35, 65, 90, 85, 80, 86, 25, 35, 20, 44, 35, 82],  # Heathrow
    [20, 0, 15, 35, 60, 55, 57, 85, 90, 25, 35, 30, 37, 20, 40],  # Harrow
    [25, 15, 0, 30, 50, 70, 55, 50, 65, 10, 25, 15, 24, 20, 90],  # Ealing
    [35, 35, 30, 0, 45, 60, 53, 55, 47, 12, 22, 20, 12, 10, 21],  # Holborn
    [65, 60, 50, 45, 0, 46, 15, 45, 75, 25, 11, 19, 15, 25, 25],  # Sutton
    [90, 55, 70, 60, 46, 0, 15, 25, 45, 65, 53, 43, 63, 70, 27],  # Dartford
    [85, 57, 55, 53, 15, 15, 0, 17, 25, 41, 25, 33, 27, 45, 30],  # Bromley
    [80, 85, 50, 55, 45, 25, 17, 0, 25, 40, 34, 32, 20, 30, 10],  # Greenwich
    [86, 90, 65, 47, 75, 45, 25, 25, 0, 65, 70, 72, 61, 45, 13],  # Barking
    [25, 25, 10, 12, 25, 65, 41, 40, 65, 0, 20, 8, 7, 15, 25],    # Hammersmith
    [35, 35, 25, 22, 11, 53, 25, 34, 70, 20, 0, 5, 12, 45, 65],   # Kingston
    [20, 30, 15, 20, 19, 43, 33, 32, 72, 8, 5, 0, 14, 34, 56],    # Richmond
    [44, 37, 24, 12, 15, 63, 27, 20, 61, 7, 12, 14, 0, 30, 40],   # Battersea
    [35, 20, 20, 10, 25, 70, 45, 30, 45, 15, 45, 34, 30, 0, 27],  # Islington
    [82, 40, 90, 21, 25, 27, 30, 10, 13, 25, 65, 56, 40, 27, 0]   # Woolwich
]
            self.num_cities = 15
            self.num_vehicles = 6
        if problem ==14:
            self.blocks = [[0], [1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]]
            self.value=[6,5,4,12,6,2,2,0.5,3,3,1,4,4,2,0.75,0.75,0.5,0.25,1,1,0.75,0.5,1.5,2,1.5,0.75,1.5,1.5,1.5,0.75]
            self.above={0: [1, 2, 3, 4], 1: [5, 6, 8, 9], 2: [6, 7, 9, 10], 3: [8, 9, 11, 12], 4: [12, 13, 9, 10], 5: [14, 15, 18, 19], 6: [15, 16, 20, 19], 7: [16, 17, 20, 21], 8: [18, 19, 22, 23], 9: [19, 20, 23, 24], 10: [20, 21, 24, 25], 11: [22, 23, 26, 27], 12: [23, 24, 27, 28], 13: [24, 25, 28, 29]} 
        if problem ==18:
            self.coff=[23, 21, 19, 17, 14, 13, 13, 9]
            self.rhs=70
        
        if problem ==23:
            self.num_farms = 21
            self.num_days = 2
            self.farms_data = {
    0: {"Position": (0, 0), "Collection Frequency": None, "Requirement": 0},
    1: {"Position": (-3, 3), "Collection Frequency": "Every day", "Requirement": 5},
    2: {"Position": (1, 11), "Collection Frequency": "Every day", "Requirement": 4},
    3: {"Position": (4, 7), "Collection Frequency": "Every day", "Requirement": 3},
    4: {"Position": (-5, 9), "Collection Frequency": "Every day", "Requirement": 6},
    5: {"Position": (-5, -2), "Collection Frequency": "Every day", "Requirement": 7},
    6: {"Position": (-4, -7), "Collection Frequency": "Every day", "Requirement": 3},
    7: {"Position": (6, 0), "Collection Frequency": "Every day", "Requirement": 4},
    8: {"Position": (3, -6), "Collection Frequency": "Every day", "Requirement": 6},
    9: {"Position": (-1, -3), "Collection Frequency": "Every day", "Requirement": 5},
    10: {"Position": (0, -6), "Collection Frequency": "Every other day", "Requirement": 4},
    11: {"Position": (6, 4), "Collection Frequency": "Every other day", "Requirement": 7},
    12: {"Position": (2, 5), "Collection Frequency": "Every other day", "Requirement": 3},
    13: {"Position": (-2, 8), "Collection Frequency": "Every other day", "Requirement": 4},
    14: {"Position": (6, 10), "Collection Frequency": "Every other day", "Requirement": 5},
    15: {"Position": (1, 8), "Collection Frequency": "Every other day", "Requirement": 6},
    16: {"Position": (-3, 1), "Collection Frequency": "Every other day", "Requirement": 8},
    17: {"Position": (-6, 5), "Collection Frequency": "Every other day", "Requirement": 5},
    18: {"Position": (2, 9), "Collection Frequency": "Every other day", "Requirement": 7},
    19: {"Position": (-6, -5), "Collection Frequency": "Every other day", "Requirement": 6},
    20: {"Position": (5, -4), "Collection Frequency": "Every other day", "Requirement": 6},
}
