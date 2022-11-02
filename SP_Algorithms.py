import math
from Graph import *
from Interfaces.SP_AlgorithInterface import SP_AlgorithmInterface


class djikstra_alg(SP_AlgorithmInterface):
    def __init__(self, graph: buildGraph, start):
        self.graph = graph
        self.start = start
        self.unvisited_stations = list(graph._adj.keys())
        self.shortest_path = {}
        self.previous_nodes = {}
        INFINITY = float('inf')
        for station in self.unvisited_stations:
            self.shortest_path[station] = INFINITY
        self.shortest_path[start] = 0
        self.run()

    def run(self):
        while self.unvisited_stations:
            # finds the nodes with the lowest value
            current_min_node = None
            # current_min_node = start
            for station in self.unvisited_stations:
                if current_min_node is None:
                    current_min_node = station
                elif self.shortest_path[station] < self.shortest_path[current_min_node]:
                    current_min_node = station

            for edge in self.graph.adjacent_edges(current_min_node):
                temp = self.shortest_path[current_min_node] + edge.weight
                if temp < self.shortest_path[edge.other(current_min_node)]:
                    self.shortest_path[edge.other(current_min_node)] = temp
                    self.previous_nodes[edge.other(
                        current_min_node)] = current_min_node

            self.unvisited_stations.remove(current_min_node)
        self.previous_nodes = self.previous_nodes
        self.shortest_path = self.shortest_path

    def returnNodesAndPath(self):
        return self.previous_nodes, self.shortest_path

    def print_result(self, start_node, target_node):
        path = []
        node = target_node
        while node != start_node:
            path.append(node)
            node = self.previous_nodes[node]
        # Add the start node manually
        path.append(start_node)

        # print("We found the following best path with a value of {}.".format(self.shortest_path[target_node]))
        path.reverse()
        # print(path)
        return path

    def returnTime(self, target_node):
        return self.shortest_path[target_node]


class heuristicType:
    def __init__(self) -> None:
        pass

    def heuristic(self, nodesDict, start, sinkVert: int):
        def findLatitude(vertex):
            return nodesDict[vertex][0]

        def findLongitude(vertex):
            return nodesDict[vertex][1]
        x = abs(findLongitude(start) - findLongitude(sinkVert))
        y = abs(findLatitude(start) - findLatitude(sinkVert))
        dist = math.sqrt(x * x + y * y)
        return dist


class aStar(djikstra_alg):

    def __init__(
            self,
            graph: buildGraph,
            start,
            nodesWithLocation,
            heuristic: heuristicType):
        self.heuristicType = heuristic
        nodesDict = {}
        for row in nodesWithLocation:
            nodesDict[row[0]] = [row[1], row[2]]
        self.nodesDict = nodesDict
        super().__init__(graph, start)
        self.run()

    def run(self):
        while self.unvisited_stations:
            # finds the nodes with the lowest value
            current_min_node = None
            # current_min_node = start
            for station in self.unvisited_stations:
                if current_min_node is None:
                    current_min_node = station
                elif self.shortest_path[station] < self.shortest_path[current_min_node]:
                    current_min_node = station

            for edge in self.graph.adjacent_edges(current_min_node):
                temp = self.shortest_path[current_min_node] + edge.weight
                # heuristic applied here
                if temp + self.heuristicType.heuristic(self.nodesDict, self.start, edge.either()) < self.shortest_path[edge.other(
                        current_min_node)] + self.heuristicType.heuristic(self.nodesDict, self.start, edge.other(edge.either())):
                    self.shortest_path[edge.other(current_min_node)] = temp
                    self.previous_nodes[edge.other(
                        current_min_node)] = current_min_node

            self.unvisited_stations.remove(current_min_node)
        self.previous_nodes = self.previous_nodes
        self.shortest_path = self.shortest_path
