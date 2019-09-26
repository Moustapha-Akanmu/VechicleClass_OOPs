from vehicle_class import *
class Car(Vehicle):
    def __init__(self, wheels, capacity, color, year, brand, model,license_plane,air_bag):
        super().__init__(wheels, capacity, color, year)
        self.brand = brand
        self.license_plane = brand
        self.air_bag



    def play_music(self):
        return 'slownnnnn jammmmmm'

    def model(self):
        return 'Toyota'

    def lock_it(self):
        return 'click'

    def seat_belt(self):
        return '<-------------->'