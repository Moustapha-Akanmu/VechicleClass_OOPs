from vehicle_class import *
class Bike(Vehicle):
    def __init__(self, wheels, capacity, color, year, paddle, wheely, chain_it):
        super().__init__(wheels, capacity, color, year)
        self.paddle = paddle
        self.wheely = wheely
        self.chain_it = chain_it


    def gears(self):
        return 'tic'

    def handle_bar_type(self):
        return 'smoooth'

    def bask_size(self):
        return 'plug'

    def make_noise(self):
        return'tac tac tac tac tac'