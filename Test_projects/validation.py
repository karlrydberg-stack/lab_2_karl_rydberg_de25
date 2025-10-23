class Validation:
    def __init__(self, x_coordinate, y_coordinate, height, width, radius):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.height = height
        self.width = width
        self.radius = radius
    
    @property
    def x_coordinate(self):
        return self._x_coordinate
    @x_coordinate.setter
    def x_coordinate(self, new_x):
        if not isinstance(new_x, (float, int)):
            raise ValueError(f"X-coordinate must be an integer or float, not '{new_x}'")
        self._x_coordinate = new_x
    
    @property
    def y_coordinate(self):
        return self._y_coordinate
    @y_coordinate.setter
    def y_coordinate(self, new_y):
        if not isinstance(new_y, (float, int)):
            raise ValueError(f"Y-coordinate must be an integer or float, not '{new_y}'")
        self._y_coordinate = new_y

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, (float, int)):
            raise ValueError(f"Height must be an integer or float, not '{new_height}'")
        self._height = new_height
    
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, new_width):
        if not isinstance(new_width, (float, int)):
            raise ValueError(f"Width must be an integer or float, not '{new_width}'")
        self._width = new_width
    
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, new_radius):
        if not isinstance(new_radius, (float, int)):
            raise ValueError(f"Radius must be an integer or float, not '{new_radius}'")
        self._radius = new_radius