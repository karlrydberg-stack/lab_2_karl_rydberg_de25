from circle import CircleObject
from rectangle import RectangleObject
from matplotlib.patches import Rectangle, Circle
import matplotlib.pyplot as plt



fig, graph= plt.subplots()
circle1 = CircleObject(1, 1, 1)
rectangle1 = RectangleObject(1, 1, 1, 1)
circle1.draw_shape(graph)
plt.grid(True)
plt.show()