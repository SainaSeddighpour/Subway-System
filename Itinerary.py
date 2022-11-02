from Graph import *
from Interfaces.itineraryInterface import itineraryInterface


class Itinerary(itineraryInterface):
    def __init__(self, routeStations, time, graph: buildGraph):
        self._time = time
        self._NumOfStations = 0
        self._connectionCount = 0
        self._routeStations = routeStations
        self._graph = graph

        self._NumOfStations = self.countStations()
        self._connectionCount = self.countConnections()

    #Getters and setters

    @property
    def routeStations(self):
        return self._routeStations

    @property
    def time(self):
        return self._time

    @property
    def connectionCount(self):
        return self._connectionCount

    @connectionCount.setter
    def connectionCount(self, connectionCount):
        self._connectionCount = connectionCount

    def countStations(self):
        return len(self._routeStations)

    def returnEdges(self):
        return self._routeStations

        # Get the list of all lines travelled upon for this path
    def getConnections(self):
        linesUsed = []
        for station in range(1, len(self._routeStations)):
            station1 = self._routeStations[station]
            station2 = self._routeStations[station - 1]

            station1AdjList = self._graph.adjacent_edges(station1)

            for i in station1AdjList:
                if i.other(station1) == station2:
                    linesUsed.append(i._line)
        return linesUsed

    def switchLine(self, edgeLine1, edgeLine2):
        return edgeLine1 != edgeLine2
    # Count connections

    def countConnections(self):
        linesCount = 0
        linesUsed = self.getConnections()
        for station in range(len(linesUsed) - 1):
            if self.switchLine(linesUsed[station], linesUsed[station - 1]):
                linesCount += 1
        return linesCount

    def compareTime(self, other):
        if self._time < other._time:
            return -1    # Smaller
        if self._time == other._time:
            return 0    # Equal
        if self._time > other._time:
            return 1     # Larger

    def compareConnections(self, other):
        # if self._connectionCount < other._connectionCount: return -1
        # if self._connectionCount == other._connectionCount: return 0
        # if self._connectionCount > other._connectionCount: return 1
        return self._connectionCount - other._connectionCount


def ItineraryTest():

    a = Edge(1, 2, 4, 1)
    b = Edge(1, 6, 1, 1)
    c = Edge(2, 6, 2, 2)
    #1 - 2 - 6

    mine = buildGraph()

    mine.add_edge(a)
    mine.add_edge(b)
    mine.add_edge(c)

    mineIt = Itinerary([1, 2, 6], 6, mine)
    mineIt2 = Itinerary([1, 6], 1, mine)

    print(mineIt._connectionCount)

    print(mineIt2._connectionCount)

    print(mineIt.compareTime(mineIt2))
    print(mineIt2.compareTime(mineIt))
    print(mineIt.compareConnections(mineIt2))
