from base_class import BaseClassShapes
class SphereObject(BaseClassShapes):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius
    
    @property
    def area_(self):
        return self.radius * self.radius * 3.14 * 4
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
        return f"Surface area of sphere = {self.radius * self.radius * 3.14 * 4}"
    @property
    def perimeter(self):
        return f"Circumference of sphere = {self.radius * 2 * 3.14}"
    @property
    def volume(self):
        return f"Volume of sphere = {4/3 * 3.14 * self.radius**3}"
    def __repr__(self):
        return f"Sphere({self.radius}, {self.x}, {self.y})"
    def __str__(self):
        return f"Sphere object with coordinates ({self.x}, {self.y}) and radius {self.radius}"
    def unit_sphere(self):
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False