from player import Player
import numpy as np

from unit import Unit
from pieces import *

class Board:
    def __init__(self, players):
        self.players = players
        self.setup(players)
    
    def setup(self):
        self.board = []
        for n in range(8):
            if (n == 0 or n == 7):
                for p in self.players:
                    if (n == 0 and p.color == "white"):
                        for pp in p.pieces:
                            
                    else:
                
                self.board.append()
            elif (n == 1 or n == 6):
                self.board.append([Pawn()] * 8)
            else:
                self.board.append([Unit()] * 8)
        self.board = np.array(self.board)

    def __str__(self):
        string = ""
        row = 0
        for c in range(len(self.board)):
            string += f"{c + 1} "
            for r in range(len(self.board[c])):
                string += f"{self.board[c][r]} "
            string += "\n"
        string += "  a b c d e f g h"

        return string

