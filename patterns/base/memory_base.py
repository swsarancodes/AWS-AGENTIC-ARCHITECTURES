from abc import ABC, abstractmethod

class MemoryBase(ABC):
    """
    Abstract base class for memory modules (episodic, semantic, graph, etc).
    """
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def store(self, key, value):
        pass

    @abstractmethod
    def retrieve(self, key):
        pass

    @abstractmethod
    def clear(self):
        pass
