from validation import Validation

class Circle(Validation):
    def __init__(self, x_coordinate, y_coordinate, radius):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.radius = radius
        self.area = self.radius * self.radius * 3.14
    
    def __lt__(self, other):
        return self.area < other.area
    
    def __eq__(self, other):
        return self.area == other.area

c1 = Circle(1, 1, 1)
c2 = Circle(2, 2, 2)

print(c1 < c2)