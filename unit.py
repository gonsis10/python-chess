from abc import ABC, abstractmethod

class Unit(ABC):    
    def __str__(self):
        return str(-1)

    # @abstractmethod
    # def move(self, board, move, opponent):
    #     pass