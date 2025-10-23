from validation import Validation

class Rectangle(Validation):
    def __init__(self, x_coordinate: float | int, y_coordinate: float | int, width, height):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.width = width
        self.height = height
    
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
        area1 = self.width * self.height
        area2 = other.width * other.height
        if area1 < area2:
            return True
        else:
            return False
    def __eq__(self, other):
        area1 = self.width * self.height
        area2 = other.width * other.height
        if area1 == area2:
            return True
        else:
            return False
    
    

    def __str__(self):
        return f"X-coordinate = {self.x_coordinate}\nY-coordinate = {self.y_coordinate}\nWidth = {self.width}\nHeight = {self.height}"


rect1 = Rectangle(1, 2, -1, 4)

rect2 = Rectangle(2, 3, 4, 5)

print(rect1 == rect2)