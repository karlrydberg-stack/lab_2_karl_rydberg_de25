import matplotlib.pyplot as plt

class BaseClassShapes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
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
    def translate(self, new_x, new_y):
        if not isinstance(new_x, (int, float)) or not isinstance(new_y, (int, float)):
            raise TypeError(f"Coordinates must be int or float")
        else:
            if 10 < new_x < -10 or 10 < new_y < -10:
                raise ValueError("Acceptable range for coordinates is between 10 and -10")
        plt.arrow(self.x, self.y, new_x, new_y, width=0.05)
        self.x = new_x
        self.y = new_y

    