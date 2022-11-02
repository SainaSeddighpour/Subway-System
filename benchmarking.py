from datasetGen import *
from SP_Algorithms import *
from GraphBuilder import *
import time
from matplotlib import pyplot as plt
from Itinerary import Itinerary


class benchmark_Setup():
    def __init__(self, algo):
        self.algo = algo

    def getdataset(self):
        gen = datasetGen()
        dataset = gen.randomNodes()

        return dataset

    def benchmarking(self):
        dt = datasetGen()
        graph = dt.build()
        heuristic = heuristicType()
        station = self.getdataset()[0]
        if self.algo == "dijkstra":
            st = time.time()
            algo = djikstra_alg(graph, station)
            end = time.time()
            result = end - st
            return result

        if self.algo == 'aStar':
            st = time.time()
            algo = aStar(graph, station, dt.getNodes(), heuristic)
            end = time.time()
            result = end - st
            return result


def cycle(numOfCycles):
    bench_dij = benchmark_Setup('dijkstra')
    bench_aStar = benchmark_Setup('aStar')
    time1 = 0
    time2 = 0
    for i in range(numOfCycles):
        time1 += bench_dij.benchmarking()
        time2 += bench_aStar.benchmarking()
    return [time1, time2]


def benchmark(valuesToTest):

    timeResultsDij = []
    timeResultsAstar = []

    for n in valuesToTest:
        times = cycle(n)
        print("Dijkstra: ", times[0])
        print("A*: ", times[1])
        timeResultsDij.append(times[0])
        timeResultsAstar.append(times[1])
    return [valuesToTest, timeResultsDij, timeResultsAstar]


def GraphResults(valuesToTest, timeResultsDij, timeResultsAstar):
    x_axis = valuesToTest
    y_axis1 = timeResultsDij
    y_axis2 = timeResultsAstar

    plt.xlabel('Number of Stations Tested')
    plt.ylabel('Runtime ms')
    plt.scatter(x_axis, y_axis1, color='red', label='Dijkstra')
    plt.scatter(x_axis, y_axis2, color='blue', label='A*')
    plt.legend()
    plt.title('Runtime of Dijkstra and A*')
    plt.show()


benchmarkResults = benchmark([1, 10, 50, 100, 200, 300])
GraphResults(benchmarkResults[0], benchmarkResults[1], benchmarkResults[2])


class benchmark_Setup_Itinerary(benchmark_Setup):

    def benchmarking(self):
        dt = datasetGen()
        graph = dt.build()
        heuristic = heuristicType()
        station = self.getdataset()[0]
        station2 = self.getdataset()[1]

        if self.algo == "dijkstra":
            algo = djikstra_alg(graph, station)
            path = algo.print_result(station, station2)
            time = algo.returnTime(station2)
            Itin = Itinerary(path, time, graph)

        if self.algo == "aStar":
            algo2 = aStar(graph, station, dt.getNodes(), heuristic)
            path2 = algo2.print_result(station, station2)
            time2 = algo2.returnTime(station2)
            Itin = Itinerary(path2, time2, graph)

        return Itin.countConnections()

# returns the average number of connections for each algorithm
    def cycle(self, numOfCycles):
        bench_dij = benchmark_Setup_Itinerary('dijkstra')
        bench_aStar = benchmark_Setup_Itinerary('aStar')
        ItineraryDij = 0
        ItineraryAstar = 0
        for i in range(numOfCycles):
            ItineraryDij += bench_dij.benchmarking()
            ItineraryAstar += bench_aStar.benchmarking()
        return [ItineraryDij, ItineraryAstar]

    def benchmark2(self, valuesToTest):
        ItinResultsDij = []
        ItinResultsAstar = []
        for n in valuesToTest:
            NumOfConnections = self.cycle(n)
            print("Dijkstra: ", NumOfConnections[0])
            print("A*: ", NumOfConnections[1])
            ItinResultsDij.append(NumOfConnections[0])
            ItinResultsAstar.append(NumOfConnections[1])
        return [valuesToTest, ItinResultsDij, ItinResultsAstar]

    def GraphResults2(self, valuesToTest, ItinResultsDij, ItinResultsAstar):
        x_axis = valuesToTest
        y_axis1 = ItinResultsDij
        y_axis2 = ItinResultsAstar
        plt.xlabel('Number of Paths Tested')
        plt.ylabel('Number of Connections')
        plt.scatter(x_axis, y_axis1, color='red', label='Dijkstra')
        plt.scatter(x_axis, y_axis2, color='blue', label='A*')
        plt.legend()
        plt.title('Number of Line Changes for Each Algorithm')
        plt.show()


# test = benchmark_Setup_Itinerary('dijkstra')
# benchmarkResults = test.benchmark2([5, 10, 50, 100, 200, 300])
# test.GraphResults2(benchmarkResults[0], benchmarkResults[1], benchmarkResults[2])
