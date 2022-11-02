from MetricExtractor import *
import matplotlib.pyplot as plt


class degree_grapher():
    def max_degree(self, graph):
        degrees = []
        for node in graph.vertices():
            degrees.append(len(graph.adjacent_edges(node)))
        return max(degrees)

    def make_graph(self, graph, maximum_xaxis):
        count = 0
        nodes = graph.vertices()
        x_axis = []
        y_axis = []
        for i in range(1, (maximum_xaxis + 1)):
            x_axis.append(i)
            count = 0
            for node in nodes:
                if len(graph.adjacent_edges(node)) == i:
                    count = count + 1
            y_axis.append(count)

        plt.xlabel('degrees')
        plt.ylabel('number of nodes')
        plt.bar(x_axis, y_axis)
        plt.show()

# class data_ruuner():
#     reader = input_reader()
#     reader.read_input_nodes('../_dataset/london.stations.csv')
#     reader.read_input_edges('../_dataset/london.connections.csv')
#     #degrees = reader.read_input_lines('london.stations.csv')
#     graph = buildGraph()
#     grapher = degree_grapher()

#     for node in nodes:
#         for item in connections:
#             if node == item[0]:
#                 edge = Edge(item[0], item[1], item[2])
#                 graph.add_edge(edge)
#     max_xaxis = grapher.max_degree(graph)
#     grapher.make_graph(graph, max_xaxis)
#     print(graph)
