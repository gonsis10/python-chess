from abc import ABC, abstractmethod

class Unit(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return -1

    @abstractmethod
    def move(self, board, move, opponent):
        pass