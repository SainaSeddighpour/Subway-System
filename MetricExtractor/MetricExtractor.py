from abc import ABCMeta
from Graph import *
import csv


class ExtractorFactory(metaclass=ABCMeta):
    def factory(self):
        """ Interface Method"""


class Extractors(metaclass=ABCMeta):
    def extract(self):
        """ Interface Method"""


class ExtractorMaker(ExtractorFactory):
    # if need be more types can be added
    def make(self, t):
        if t == "formatA":
            return FormatA()
        if t == "formatB":
            return FormatB()
        if t == "formatC":
            return FormatC()
        else:
            return None


class FormatA(Extractors):
    def extract(self):
        nodes = []
        connections = []
        with open('_dataset/london.stations.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            for row in reader:
                nodes.append(int(row[0]))

        with open('_dataset/london.connections.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            stn1Index = 0
            stn2Index = 1
            timeIndex = 3
            for row in reader:
                tuple_input = (int(row[stn1Index]), int(
                    row[stn2Index]), int(row[timeIndex]))
                connections.append(tuple(tuple_input))

        return connections


class FormatB(
        Extractors):  # OUTPUT: [connections, nodes], Stations w/Location, and connections
    def extract(self):
        nodesWithLocation = []
        connections = []
        with open('_dataset/london.stations.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            for row in reader:
                tuple_input = (int(row[0]), float(row[1]), float(
                    row[2]))  # (ID, Longitude, Latitude)
                nodesWithLocation.append(tuple(tuple_input))

        with open('_dataset/london.connections.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            stn1Index = 0
            stn2Index = 1
            timeIndex = 3
            for row in reader:
                tuple_input = (int(row[stn1Index]), int(
                    row[stn2Index]), int(row[timeIndex]))
                connections.append(tuple(tuple_input))

        return [connections, nodesWithLocation]


class FormatC(
        Extractors):      # #OUTPUT: [connections, nodes]  input for what info you want from header
    def extract(self, nodesInfo: list, connectionsInfo: list):
        nodes = []
        connections = []

        with open('_dataset/london.stations.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader, None)

            nodesInfoIndices = []
            for i in nodesInfo:
                try:  # Error handling if one of the options does not exist
                    # get index of all required columns from header
                    nodesInfoIndices.append(header.index(str(i)))
                except BaseException:
                    pass

            for row in reader:
                tempList = [float(row[i]) for i in nodesInfoIndices]
                nodes.append(tuple(tempList))

        with open('_dataset/london.connections.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader, None)

            connectionsInfoIndices = []
            for i in connectionsInfo:
                try:  # Error handling if one of the options does not exist
                    # get indx of all required columns from header
                    connectionsInfoIndices.append(header.index(str(i)))
                except BaseException:
                    pass

            for row in reader:
                tempList = [int(row[i]) for i in connectionsInfoIndices]
                connections.append(tuple(tempList))

        return [connections, nodes]


# TEST
def MetricExtractorTester():
    factory = ExtractorMaker()
    format = factory.make('formatC')
    output = format.extract(['id', 'latitude', 'longitude'], [
                            "station1", "station2", "time", "line"])
    connections = output[0]
    nodes = output[1]
    print(connections[0])
