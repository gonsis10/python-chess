from unit import Unit
from pieces import *

class board:
    def __init__(self):
        self.board = Unit[8][8]
        self.board[0] = [Pawn]