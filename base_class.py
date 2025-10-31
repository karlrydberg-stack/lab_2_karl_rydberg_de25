import matplotlib.pyplot as plt

class BaseClassShapes:
    def __init__(self, x=0, y=0, arrow_list=[]):
        self.x = x
        self.y = y
        self.arrow_list = arrow_list
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
    def translate(self, new_x: int|float, new_y: int|float):
        if not isinstance(new_x, (int, float)) or not isinstance(new_y, (int, float)):
            raise TypeError(f"Coordinates must be int or float")
        else:
            if 10 < new_x < -10 or 10 < new_y < -10:
                raise ValueError("Acceptable range for coordinates is between 10 and -10")
        self.arrow_list.append((self.x, self.y, new_x - self.x, new_y - self.y))
        self.x = new_x
        self.y = new_y