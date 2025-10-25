import matplotlib as plt
from matplotlib.patches import Rectangle, Circle

class Circle:
    def __init__(self, radius, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = radius
    
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, (int, float)):
            raise TypeError("Coordinate must be an integer or float")
        else:
            if new_x > 10 or new_x < -10:
                raise ValueError("Acceptable range is between 10 and -10")
        self._x = new_x
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, (int, float)):
            raise TypeError("Coordinate must be an integer or float")
        else:
            if new_y > 10 or new_y < -10:
                raise ValueError("Acceptable range is between 10 and -10")
        self._y = new_y
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, new_radius):
        if not isinstance(new_radius, (int, float)):
            raise TypeError("Radius must be an integer or float")
        elif new_radius <= 0:
            raise ValueError("Radius must be greater than 0")
        self._radius = new_radius
    @property
    def area(self):
        return f"Area of circle = {self.radius * self.radius * 3.14}"
    @property
    def perimeter(self):
        return f"Perimeter of circle = {self.radius * 2 * 3.14}"
    def __eq__(self, other):
        return self.radius == other.radius
    def __lt__(self, other):
        return self.radius < other.radius
    def __gt__(self, other):
        return self.radius > other.radius
    def __le__(self, other):
        return self.radius <= other.radius
    def __ge__(self, other):
        return self.radius >= other.radius
    def __repr__(self):
        return f"Circle({self.x}, {self.y})"
    def __str__(self):
        return f"Circle object with coordinates ({self.x}, {self.y})"
    def translate(self, new_x, new_y):
        if not isinstance(new_x, (int, float)) or not isinstance(new_y, (int, float)):
            raise TypeError(f"Coordinates must be int or float")
        else:
            if 10 < new_x < -10 or 10 < new_y < -10:
                raise ValueError("Acceptable range for coordinates is between 10 and -10")
        self.x = new_x
        self.y = new_y
    def unit_circle(self):
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False




class Rectangle:
    def __init__(self, height, width, x=0, y=0):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.area_ = self.height * self.width
    
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, (int, float)):
            raise TypeError("Coordinate must be an integer or float")
        else:
            if new_x > 10 or new_x < -10:
                raise ValueError("Acceptable range is between 10 and -10")
        self._x = new_x
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, (int, float)):
            raise TypeError("Coordinate must be an integer or float")
        else:
            if new_y > 10 or new_y < -10:
                raise ValueError("Acceptable range is between 10 and -10")
        self._y = new_y
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
    def __eq__(self, other):
        return self.area_ == other.area_
    def __lt__(self, other):
        return self.area_ < other.area_
    def __gt__(self, other):
        return self.area_ > other.area_
    def __le__(self, other):
        return self.area_ <= other.area_
    def __ge__(self, other):
        return self.area_ >= other.area_
    def __repr__(self):
        return f"Rectangle({self.x}, {self.y})"
    def __str__(self):
        return f"Rectangle object with coordinates ({self.x}, {self.y})"
    def translate(self, new_x, new_y):
        if not isinstance(new_x, (int, float)) or not isinstance(new_y, (int, float)):
            raise TypeError(f"Coordinates must be int or float")
        else:
            if 10 < new_x < -10 or 10 < new_y < -10:
                raise ValueError("Acceptable range for coordinates is between 10 and -10")
        self.x = new_x
        self.y = new_y
    def check_square(self):
        if self.height == self.width:
            return True
        else:
            return False