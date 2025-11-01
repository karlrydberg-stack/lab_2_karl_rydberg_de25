from base_class import BaseClassShapes
from matplotlib.patches import Rectangle 
import matplotlib.pyplot as plt
class RectangleObject(BaseClassShapes):
    """This is a class which provide several primary and supporting features. Primarily it is used to generate representations
    of a rectangle and provide related data - like its area and perimeter."""
    def __init__(self, width: int|float, height: int|float, x: int|float=0, y: int|float=0):
        super().__init__(x, y)
        self.height = height
        self.width = width

    @property
    def area_(self): # This method would generally not be called by the user, rather used by the parent class to compare areas of different objects
        return self.height * self.width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, new_height: int|float):
        if not isinstance(new_height, (int, float)):
            raise TypeError("Height must be an integer or float")
        if isinstance(new_height, bool):
            raise TypeError("Height can not be a boolean value")
        elif new_height <= 0:
            raise ValueError("Height must be greater than 0")
        self._height = new_height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, new_width: int|float):
        if not isinstance(new_width, (int, float)):
            raise TypeError("Width must be an integer or float")
        elif isinstance(new_width, bool):
            raise TypeError("Width can not be a boolean value")
        elif new_width <= 0:
            raise ValueError("Width must be greater than 0")
        self._width = new_width
    @property
    def area_rectangle(self):
        return f"Area of rectangle = {self.height * self.width}"
    @property
    def perimeter_rectangle(self):
        return f"Perimeter of rectangle = {self.height * 2 + self.width * 2}"
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height}, {self.x}, {self.y})"
    def __str__(self):
        return f"Rectangle object with coordinates ({self.x}, {self.y}) with width {self.width} and height {self.height}"
    def check_square(self):
        if self.height == self.width:
            return True
        else:
            return False
    def draw_shape(self, graph): # This method would not be called directly by the user, but provide data to the plotting class
        rectangle_object = Rectangle((self.x - self.width/2, self.y - self.height/2), self.width, self.height, fill=False)
        graph.add_patch(rectangle_object)