import pandas as pd

class InputData:
    def __init__(self):
        self.load_data()

    def load_data(self):
        self.waste = [2000000, 2500000, 1500000, 3000000]
        self.concentration = [1.5, 1, 2.5, 2]
        self.eff = [1, 0.8, 1.3, 1]
        self.moni = 1000000
        self.target = 11000000
        self.tax = 0.1
