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
        if problem==21:
            self.prices = [297, 720, 1050, 815]
            self.demand = [4820000, 320000, 210000, 70000]
            self.e = [0.4, 2.7, 1.1, 0.4, 0.1, 0.4]
