from abc import ABC, abstractmethod


class edgeInterface(ABC):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @abstractmethod
    def either(self):
        pass

    @abstractmethod
    def other(self, other):
        pass
