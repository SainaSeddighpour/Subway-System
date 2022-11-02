from abc import ABC, abstractmethod


class itineraryInterface(ABC):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        stationsOnRoute = []

    def findRoute(self):
        pass

    def countStations(self):
        return len(self.stationOnRoute)

    def returnStations(self):
        return self.tationsOnRoute
