from pieces import *

class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = [self.setup()]

    def setup(self):
        pieces = []
        pieces.append(Pawn(self) * 8, Rook(self) * 2, Knight(self) * 2, Bishop(self) * 2, Queen(self), King(self))
        return pieces