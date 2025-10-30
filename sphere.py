from base_class import BaseClassShapes
class SphereObject(BaseClassShapes):
    def __init__(self, radius: int|float, x: int|float=0, y: int|float=0):
        """This is a class which enable the creation of spherical objects. It provides several related methods which give additional
         data, like the volume and perimeter of the sphere. """
        super().__init__(x, y)
        self.radius = radius
    
    @property
    def area_(self): # This method would generally not be called by the user, rather used by the parent class to compare areas of different objects
        return self.radius * self.radius * 3.14 * 4
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
    def area_sphere(self):
        return f"Surface area of sphere = {self.radius * self.radius * 3.14 * 4}"
    @property
    def perimeter_sphere(self):
        return f"Circumference of sphere = {self.radius * 2 * 3.14}"
    @property
    def volume_sphere(self):
        return f"Volume of sphere = {4/3 * 3.14 * self.radius**3}"
    def __repr__(self):
        return f"Sphere({self.radius}, {self.x}, {self.y})"
    def __str__(self):
        return f"Sphere object with coordinates ({self.x}, {self.y}) and radius {self.radius}"
    def unit_sphere(self): # Note: the definition of a unit sphere is not as clear to me in comparison to a unit circle
        if self.radius == 1:
            return True
        else:
            return False