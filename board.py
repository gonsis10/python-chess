import numpy as np

from unit import Unit
from pieces import *

class Board:
    def __init__(self):
        self.setup()
    
    def setup(self):
        self.board = []
        for n in range(8):
            if (n == 0 or n == 7):
                self.board[n].append([Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()])
            elif (n == 1 or n == 6):
                self.board[n].append([Pawn] * 8)
            else:
                self.board[n].append([Unit] * 8)
        self.board = np.array(self.board)

    def __str__(self):
        string = ""
        for c in self.board:
            string += (c + 1) + " "
            for r in self.board[c]:
                string += r + " "
            string += "\n"
        string += "  a b c d e f g h"

        return string

