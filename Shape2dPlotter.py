import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from circle import CircleObject
from rectangle import RectangleObject
from base_class import BaseClassShapes

class Shape2DPlotter(BaseClassShapes):
    """The primary purpose of this class is to plot shapes created from the CircleObject class and/or the RectangleObject class.
    Thusly, this class only works in tandem with the aforementioned classes which will need to be imported."""
    def __init__(self, shape_list: list=[]):
        super().__init__()
        self.shape_list = shape_list
    def show_plot(self):
        fig, self.graph= plt.subplots()
        if self.shape_list: # Checks if the list is falsy, in essence empty
            for iterator in self.shape_list: 
                iterator.draw_shape(self.graph) # For each object in self.shape_list, this will call the draw shape function from the objects class 
        if self.arrow_list:
            for x, y, dx, dy in self.arrow_list:
                plt.arrow(x, y, dx, dy, width=0.05) # Iterates through the tuples from the arrow list inherited from base class, and plots arrows from the assorted data 
        self.graph.set_xlim(-10, 10) # Sets the graph dimensions, hence why the x and y setters have value limits
        self.graph.set_ylim(-10, 10)
        plt.grid(True)
        plt.show()