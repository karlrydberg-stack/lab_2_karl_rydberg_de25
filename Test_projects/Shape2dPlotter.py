import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from circle import CircleObject
from rectangle import RectangleObject
from base_class import BaseClassShapes
class Shape2DPlotter(BaseClassShapes):
    def __init__(self, shape_list=[]):
        super().__init__()
        self.shape_list = shape_list
    def show_plot(self):
        fig, self.graph= plt.subplots()
        if self.shape_list:
            for iterator in self.shape_list: 
                iterator.draw_shape(self.graph)
        if self.arrow_list:
            for x, y, dx, dy in self.arrow_list:
                plt.arrow(x, y, dx, dy, width=0.05)
        self.graph.set_xlim(-10, 10)
        self.graph.set_ylim(-10, 10)
        plt.grid(True)
        plt.show()

rect1 = RectangleObject(1, 1, 2, 2)
rect1.translate(3, 3)
rect2 = RectangleObject(4, 4, -2, -2)
circle1 = CircleObject(1, 9, 9)
circle1.translate(7, 7)
lista_shape = [rect1, rect2, circle1]
a = Shape2DPlotter(lista_shape)
a.show_plot()