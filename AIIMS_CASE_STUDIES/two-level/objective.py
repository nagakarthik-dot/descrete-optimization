from definitions import set_objective_function

class Objective:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def set_objective(self, new_waste):
        set_objective_function(self.model, self.data, new_waste)

        