from base_class import BaseClassShapes

class CubeObject(BaseClassShapes):
    def __init__(self, side, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    @property
    def area_(self):
        return self.side * self.side * 6
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self, new_side):
        if not isinstance(new_side, (int, float)):
            raise TypeError("Height must be an integer or float")
        elif new_side <= 0:
            raise ValueError("Height must be greater than 0")
        self._side = new_side
    @property
    def area(self):
        return f"Surface area of cube = {self.side * self.side * 6}"
    @property
    def perimeter(self):
        return f"Perimeter of cube = {self.side * 4}"
    @property
    def volume(self):
        return f"Volume of cube = {self.side**3}"
    def __repr__(self):
        return f"Cube({self.side}, {self.x}, {self.y})"
    def __str__(self):
        return f"Cube object with coordinates ({self.x}, {self.y}) and side {self.side}"
    def unit_cube(self):
        if self.x == 0 and self.y == 0 and self.side == 1:
            return True
        else:
            return False