from validation import Validation
from matplotlib.patches import Circle


class CircleObject(Validation):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius
        
    @property
    def area_(self):
        return self.radius * self.radius * 3.14
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
    def __repr__(self):
        return f"Circle({self.x}, {self.y})"
    def __str__(self):
        return f"Circle object with coordinates ({self.x}, {self.y})"
    def unit_circle(self):
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False
    def draw_shape(self, graph):
        circle_object = Circle((self.x, self.y), self.radius)
        graph.add_patch(circle_object)