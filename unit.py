from abc import abstractmethod


class Unit():
    def __init__(self, player=None):
        self.player = player

    def __str__(self):
        return str(-1)

    @abstractmethod
    def path(self, board):
        pass

    @property
    @abstractmethod
    def moved(self):
        pass
