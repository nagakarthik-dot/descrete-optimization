from definitions import create_new_waste_vars

class DecisionVariables:
    def __init__(self, model):
        self.model = model
        self.new_waste = None

    def create_variables(self):
        self.new_waste = create_new_waste_vars(self.model)

    def get_variables(self):
        return {'new_waste': self.new_waste}
