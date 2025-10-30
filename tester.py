from circle import CircleObject
from rectangle import RectangleObject
from matplotlib.patches import Rectangle, Circle
import matplotlib.pyplot as plt
from cube import CubeObject
from sphere import SphereObject

cube1 = RectangleObject(2, 1, 1)
sphere1 = SphereObject(1, 1, 1)
print(cube1.area_)
print(sphere1.area_)
print(cube1.area_ <= sphere1.area_)