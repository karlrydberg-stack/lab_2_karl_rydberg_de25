import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from circle import CircleObject
from rectangle import RectangleObject
from base_class import BaseClassShapes
class Shape2DPlotter(BaseClassShapes):
    def __init__(self, shape_list):
        self.shape_list = shape_list

    def show_plot(self):
        fig, self.graph= plt.subplots()
        for iterator in self.shape_list: 
            iterator.draw_shape(self.graph)
        self.graph.set_xlim(-10, 10)
        self.graph.set_ylim(-10, 10)
        plt.grid(True)
        plt.show()
    def draw_arrow(self, new_x, new_y):
        arrow_object = plt.arrow(self.x, self.y, new_x - self.x, new_y - self.y)
        self.graph.add_patch(arrow_object)

rect1 = RectangleObject(10, 2)
lista = [rect1]
a = Shape2DPlotter(lista)
a.show_plot()
