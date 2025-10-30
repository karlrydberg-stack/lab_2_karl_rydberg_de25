from base_class import BaseClassShapes
from matplotlib.patches import Circle


class CircleObject(BaseClassShapes):
    """This is a class which provide several primary and supporting features. Primarily it is used to generate representations
    of a circle and provide related data - like its area and perimeter. """
    def __init__(self, radius: int|float, x: int|float=0, y: int|float=0):
        super().__init__(x, y)
        self.radius = radius
        
    @property
    def area_(self): # This method would generally not be called by user, rather used by the parent class to compare areas of different objects 
        return self.radius * self.radius * 3.14
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, new_radius: int|float):
        if not isinstance(new_radius, (int, float)):
            raise TypeError("Radius must be an integer or float")
        if isinstance(new_radius, bool):
            raise TypeError("Radius can not be a boolean value")
        elif new_radius <= 0:
            raise ValueError("Radius must be greater than 0")
        self._radius = new_radius
    @property
    def area_circle(self):
        return f"Area of circle = {self.radius * self.radius * 3.14}"
    @property
    def perimeter_circle(self):
        return f"Perimeter of circle = {self.radius * 2 * 3.14}"
    def __repr__(self):
        return f"Circle({self.radius}, {self.x}, {self.y})"
    def __str__(self):
        return f"Circle object with coordinates ({self.x}, {self.y}) and radius {self.radius}"
    def unit_circle(self):
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False
    def draw_shape(self, graph): # This method would not be called by the user, but provide data to the plotting class 
        circle_object = Circle((self.x, self.y), self.radius, fill=False)
        graph.add_patch(circle_object)