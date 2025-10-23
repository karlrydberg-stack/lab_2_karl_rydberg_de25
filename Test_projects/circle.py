from validation import Validation

class Circle(Validation):
    def __init__(self, x_coordinate, y_coordinate, radius):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.radius = radius