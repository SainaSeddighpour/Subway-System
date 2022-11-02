from MetricExtractor import *
from Itinerary import *
from SP_Algorithms import *
from degree_grapher import degree_grapher


class data_runner():
    def run(self):
        factory = ExtractorMaker()
        format = factory.make('formatB')
        output = format.extract()
        connections = output[0]

        graph = buildGraph()
        # grapher = degree_grapher()

        for item in connections:
            edge = Edge(item[0], item[1], item[2])
            graph.add_edge(edge)


class data_runner_formatC():
    def run(self):
        factory = ExtractorMaker()
        format = factory.make('formatC')
        output = format.extract(['id', 'latitude', 'longitude'], [
                                "station1", "station2", "time", "line"])
        connections = output[0]

        graph = buildGraph()
        for item in connections:
            edge = Edge(item[0], item[1], item[2], item[3])
            graph.add_edge(edge)

        # grapher = degree_grapher()
        # max_xaxis = grapher.max_degree(graph)
        # grapher.make_graph(graph, max_xaxis)

        #       TESTS
        # print(graph)
        sp = djikstra_alg(graph, 1)

        sp.print_result(1, 35)
        djikstra_alg.print_result

        #  #       ITINERARY TEST
        nodesWithLocation = output[1]
        myHeuristic = heuristicType()
        sd = aStar(graph, 1, nodesWithLocation, myHeuristic)
        sd.print_result(1, 35)
        # path = sd.print_result(11,193)
        # pathLength = sd.returnTime(193)
        # Itensd = Itinerary(path, pathLength,graph)

        # sg = djikstra_alg(graph,11)
        # path = sg.print_result(11,193)
        # Itensg = Itinerary(path, pathLength,graph)
        # # print(Itensd.compareConnections(Itensg))

        # # print(Itensd.getConnections())
        # # print(Itensd._connectionCount)

        # # print(Itensg.getConnections())
        # # print(Itensg._connectionCount)


dataRunner = data_runner_formatC()

dataRunner.run()
