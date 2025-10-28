import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from circle import CircleObject
from rectangle import RectangleObject
from base_class import BaseClassShapes
class Shape2DPlotter:
    def __init__(self, shape_list=[], arrow_list=[]):
        self.shape_list = shape_list
        self.arrow_list = arrow_list
    def show_plot(self):
        fig, self.graph= plt.subplots()
        for iterator in self.shape_list: 
            iterator.draw_shape(self.graph)
        for iterator in self.arrow_list:
            iterator.add_patch(self.graph)
        self.graph.set_xlim(-10, 10)
        self.graph.set_ylim(-10, 10)
        plt.grid(True)
        plt.show()

arrow1 = plt.arrow(1, 1, 1, 1, width=0.05)
rect1 = RectangleObject(1, 1, 2, 2)
lista_shape = [rect1]
arrow_lista = [arrow1]
a = Shape2DPlotter(lista_shape, arrow_lista)
a.show_plot()