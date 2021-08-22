from abc import ABC, abstractmethod

class Unit(ABC):
    @abstractmethod
    def __init__(self, player):
        pass

    def __str__(self):
        return str(-1)