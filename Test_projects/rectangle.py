from validation import Validation
from matplotlib.patches import Rectangle 

class RectangleObject(Validation):
    def __init__(self, height, width, x=0, y=0):
        super().__init__(x, y)
        self.height = height
        self.width = width

    @property
    def area_(self):
        return self.height * self.width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, (int, float)):
            raise TypeError("Height must be an integer or float")
        elif new_height <= 0:
            raise ValueError("Height must be greater than 0")
        self._height = new_height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, new_width):
        if not isinstance(new_width, (int, float)):
            raise TypeError("Width must be an integer or float")
        elif new_width <= 0:
            raise ValueError("Width must be greater than 0")
        self._width = new_width
    @property
    def area(self):
        return f"Area of rectangle = {self.height * self.width}"
    @property
    def perimeter(self):
        return f"Perimeter of rectangle = {self.height * 2 + self.width * 2}"
    def __repr__(self):
        return f"Rectangle({self.x}, {self.y})"
    def __str__(self):
        return f"Rectangle object with coordinates ({self.x}, {self.y})"
    def check_square(self):
        if self.height == self.width:
            return True
        else:
            return False
    def draw_shape(self, graph):
        rectangle_object = Rectangle((self.x - self.width/2, self.y - self.height/2), self.width, self.height)
        graph.add_patch(rectangle_object)