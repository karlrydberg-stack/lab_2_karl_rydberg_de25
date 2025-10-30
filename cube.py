from base_class import BaseClassShapes

class CubeObject(BaseClassShapes):
    def __init__(self, side:int|float, x: int|float=0, y: int|float=0):
        super().__init__(x, y)
        self.side = side

    @property
    def area_(self): # This method would generally not be called by the user, rather used by the parent class to compare areas of different objects
        return self.side * self.side * 6
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self, new_side: int|float):
        if not isinstance(new_side, (int, float)):
            raise TypeError("Height must be an integer or float")
        if isinstance(new_side, bool):
            raise TypeError("Side length can not be a boolean value")
        elif new_side <= 0:
            raise ValueError("Height must be greater than 0")
        self._side = new_side
    @property
    def area_cube(self):
        return f"Surface area of cube = {self.side * self.side * 6}"
    @property
    def perimeter_cube(self):
        return f"Perimeter of cube = {self.side * 4}"
    @property
    def volume_cube(self):
        return f"Volume of cube = {self.side**3}"
    def __repr__(self):
        return f"Cube({self.side}, {self.x}, {self.y})"
    def __str__(self):
        return f"Cube object with coordinates ({self.x}, {self.y}) and side length {self.side}"
    def unit_cube(self): # Note: the definition of a unit sphere is not as clear to me in comparison to a unit circle
        if self.side == 1:
            return True
        else:
            return False