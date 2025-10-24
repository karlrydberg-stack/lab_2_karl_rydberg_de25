from validation import Validation

class Rectangle(Validation):
    def __init__(self, x_coordinate: float | int, y_coordinate: float | int, width, height):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.width = width
        self.height = height
        self.arealo = self.width * self.height
    
    @property
    def area(self):
        return f"Area of rectangle is {self.width * self.height} units of area"
    
    @property
    def perimeter(self):
        return f"Perimeter of rectangle is {(self.width * 2) + (self.height * 2)} units of length"
    
    def move_rectangle(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y
    
    def __lt__(self, other):
        return self.arealo < other.arealo
    
    def __eq__(self, other):
        return self.arealo == other.arealo
    
    def __str__(self):
        return f"X-coordinate = {self.x_coordinate}\nY-coordinate = {self.y_coordinate}\nWidth = {self.width}\nHeight = {self.height}"


rect1 = Rectangle(1, 1, 1, 1)
rect2 = Rectangle(1, 1, 1, 1)

print(rect1 == rect2)