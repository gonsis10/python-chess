from pieces import *


class Player:
    def __init__(self, color):
        self.color = color

    def add_pieces(self, pieces):
        if pieces != None:
            self.pieces = pieces
        else:
            self.pieces.extend(pieces)
