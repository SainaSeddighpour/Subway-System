import copy
import math
from collections import defaultdict
from Interfaces.edgeInterface import edgeInterface
from Interfaces.graphInterface import graphInterface


class Edge(edgeInterface):
    
    def __init__(self, station1, station2, weight, line=0):
        self.station1 = station1
        self.station2 = station2
        self._weight = weight
        self._line = line


    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def line(self):
        return self._line
    @line.setter
    def line(self, line):
        self._line = line

    def either(self):
        return self.station1

    def other(self, vertex):
        if vertex not in (self.station1, self.station2):
            return None

        return self.station1 if vertex == self.station2 else self.station2

    # def comapreEdges(self, other):
    #     if self._weight < other._weight: return -1
    #     if self._weight == other._weight: return 0
    #     if self._weight > other._weight: return 1

    def __repr__(self):
        return "{}-{} {} line:{}".format(self.station1, self.station2, self.weight,self.line)

    def __eq__(self, other):
        return self._weight == other._weight and self._line == other._line 

    def __lt__(self, other):
        return self._weight < other._weight

    def __le__(self, other):
        return self._weight <= other._weight

    def __hash__(self):
        return hash('{} {} {}'.format(self.station1, self.station2, self._weight))

    def equalLine(self, other):
        if self._line == other.line: 
            return True
        return False


class buildGraph(graphInterface):
    def __init__(self, graph=None):
        self._adj = defaultdict(set)
        self._edges_size = 0
        self._vertices = set()

        
        if graph:
            self._vertices = set(v for v in graph.vertices())
            self._edges_size = graph.edges_size()
            self._adj = copy.deepcopy(graph._adj)

    def edges_size(self):
        return self._edges_size

    def vertices_size(self):
        return len(self._adj.keys())

    def add_edge(self, edge):
        station1 = edge.either()
        station2 = edge.other(station1)
        if edge not in self._adj[station1] and edge not in self._adj[station2]:
            self._adj[station1].add(edge)
            self._adj[station2].add(edge)
            self._vertices.add(edge.station1)
            self._vertices.add(edge.station2)
            self._edges_size +=1
        else:
            pass

    def adjacent_edges(self, vertex):
        return self._adj[vertex]

    def vertices (self):
        return self._adj.keys()
    
    def edges(self):
        result = set()
        for v in self.vertices():
            for edge in self.adjacent_edges(v):
                if edge.other(v) != v:
                    result.add(edge)
        return result

    def nodes_size(self):
        return len(self.vertices())

    def __repr__(self):
        print_string = '{} vertices, {} edges.\n'.format(
            self.vertices_size(), self.edges_size())
        for v in self.vertices():
            try:
                lst = ', '.join([vertex for vertex in self._adj[v]])
            except TypeError:
                lst = ', '.join([str(vertex) for vertex in self._adj[v]])
            print_string += '{}: {}\n'.format(v, lst)
        return print_string
    
    def averageDegree(self):
        sum = 0 
        for v in self.vertices:
            sum = sum + len(self.adjacent_edges(v))
        return sum/self.num_of_nodes()



# #         #  TESTS 1 FOR GRAPH
# a = Edge(1,2,4)
# b= Edge(1, 3, 1)
# c = Edge(2, 6, 2)
# d = Edge(1, 5, 6)

# graph = buildGraph


# print(type(d.weight))
# print(d > c)

# mine = buildGraph()

# mine.add_edge(a)
# mine.add_edge(b)
# mine.add_edge(c)
# mine.add_edge(d)

# print(mine.nodes_size())



# test_data = ((4, 5, 0.35), (4, 7, 0.37), (5, 7, 0.28), (0, 7, 0.16), (1, 5, 0.32),
# (0, 4, 0.38), (2, 3, 0.17), (1, 7, 0.19), (0, 2, 0.26), (1, 2, 0.36),
# (1, 3, 0.29), (2, 7, 0.34), (6, 2, 0.4), (3, 6, 0.52), (6, 0, 0.58),
# (6, 4, 0.93))

# ewg = buildGraph()
# for a, b, weight in test_data:
#     edge = Edge(a, b, weight)
#     ewg.add_edge(edge)

# print(ewg.edges_size())
# print(ewg.vertices_size())

# print([e for e in ewg.adjacent_edges(5)])

# print(ewg)
