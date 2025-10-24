class Circle:
    def __init__(self, x, y, radius):
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
        if not isinstance(new_x, (int, float)):
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

circle1 = Circle(0, 0, 1)
circle2 = Circle(1, 3, 4)

circle1.translate(1, "2")

print(circle1)