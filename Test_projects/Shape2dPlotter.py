import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from circle import CircleObject
from rectangle import RectangleObject

class Shape2DPlotter:
    def __init__(self, shape_list):
        self.shape_list = shape_list
    def show_plot(self):
        fig, graph= plt.subplots()
        for iterator in self.shape_list: 
            iterator.draw_shape(graph)
        graph.set_xlim(-10, 10)
        graph.set_ylim(-10, 10)
        plt.grid(True)
        plt.show()

circle1 = CircleObject(1, 2, 2)
circle1.translate(4, 4)
circle2 = CircleObject(1, 4, 4)
rectangle1 = RectangleObject(1, 1, 7, 7)
rectangle2 = RectangleObject(1, 1, -10, -6)
rectangle3 = RectangleObject(2, 1, 2, 2)
shape_list= [circle1, circle2]


d = Shape2DPlotter(shape_list)
d.show_plot()