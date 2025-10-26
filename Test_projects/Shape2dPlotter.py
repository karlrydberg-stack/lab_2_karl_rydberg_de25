import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from circle import CircleObject
from rectangle import RectangleObject


class Shape2dPlotter(CircleObject):
    def __init__(self, *graph):
        self.graph = graph
    def show_graph(self):
        fig, graph = plt.subplots()
        for iterator in self.graph:
            iterator.draw_shape(self.graph)
        graph.set_xlim(-10, 10)
        graph.set_ylim(-10, 10)
        plt.grid(True)
        plt.show()

circle1 = CircleObject(1, -5, -5)

plotter = Shape2dPlotter(circle1)
plotter.show_graph()