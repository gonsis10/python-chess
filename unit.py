from abc import ABC, abstractmethod
import numpy as numpy


class Unit:
    def __init__(self, player=None):
        self.player = player

    def __str__(self):
        return str(-1)

    @abstractmethod
    def path(self, board):
        pass

    @property
    def moved(self):
        pass
