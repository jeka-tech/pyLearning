from kivy.garden.graph import Graph, MeshLinePlot
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from math import sin


class ChartApp(App):
    def build(self):
        # Create box layout
        layout = BoxLayout()

        # Create graph
        graph = Graph(xlabel='X', ylabel='Ygrek', x_ticks_minor=5,
                      x_ticks_major=25, y_ticks_major=.1,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)

        # Create plot
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)

        # Add graph to the layout
        layout.add_widget(graph)

        return layout

if __name__ == '__main__':
    ChartApp().run()