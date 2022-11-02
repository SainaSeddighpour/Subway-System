from abc import ABC, abstractmethod


class graphInterface(ABC):
    def __init__(self, graph=None):
        self._adj = []
        self._edges_size = 0

    def edges_size(self):
        return self._edges_size

    @abstractmethod
    def vertices_size(self):
        pass

    @abstractmethod
    def add_edge(self, edge):
        pass

    @abstractmethod
    def adjacent_edges(self, vertex):
        return self._adj[vertex]

    @abstractmethod
    def vertices(self):
        pass

    @abstractmethod
    def edges(self):
        pass

    def nodes_size(self):
        return len(self.vertices())
