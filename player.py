from pieces import *


class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = [self.setup()]

    def setup(self) -> list:
        pieces = []
        pieces.extend([Pawn(self)] * 8)
        pieces.extend([Rook(self)] * 2)
        pieces.extend([Knight(self)] * 2)
        pieces.extend([Bishop(self)] * 2)
        pieces.append(Queen(self))
        pieces.append(King(self))
        return pieces
