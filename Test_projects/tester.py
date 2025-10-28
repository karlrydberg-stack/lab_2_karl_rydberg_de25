from circle import CircleObject
from rectangle import RectangleObject
from matplotlib.patches import Rectangle, Circle
import matplotlib.pyplot as plt
from cube import CubeObject
from sphere import SphereObject

cube1 = CubeObject(1, 1, 1)
sphere1 = SphereObject(1, 1, 1)
cube1.translate(2, 2)
print(cube1)