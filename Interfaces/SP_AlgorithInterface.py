from abc import ABC, abstractmethod


class SP_AlgorithmInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def returnNodesAndPath(self):
        pass

    @abstractmethod
    def print_result(self):
        pass
