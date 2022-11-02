import random
from MetricExtractor import *

# This class is used to pick random stations from the dataset


class datasetGen():
    def __init__(self):
        pass

    def getMetrics(self):
        factory = ExtractorMaker()
        format = factory.make('formatC')
        output = format.extract(['id', 'latitude', 'longitude'], [
                                "station1", "station2", "time", "line"])
        return output

    def getNodes(self):
        output = self.getMetrics()
        return output[1]

    def getConnections(self):
        output = self.getMetrics()
        return output[0]

    def randomNodes(self):
        nodes = self.getNodes()
        randomNodes = []
        index1 = random.choice(nodes)
        index2 = random.choice(nodes)
        randomNodes = [index1[0], index2[0]]

        return randomNodes

    def build(self):
        graph = buildGraph()
        for item in self.getConnections():
            edge = Edge(item[0], item[1], item[2], item[3])
            graph.add_edge(edge)

        return graph

# setgen = datasetGen()
# printing = setgen.getMetrics()
# print (printing)
# print(setgen.getNodes())


'''
    # num of stations we want
    for i in range(10):
        self.stationList.append(i)

    # num of connections we want
    for i in range(5):
        index1 = random.randrange(len(stationList))
        index2 = random.randrange(len(stationList))
        a = Edge(index1, index2, random.randint(1,100))
        edgesList.append(a)

    graph = buildGraph()

    for i in edgesList:
        graph.add_edge(i)

'''
