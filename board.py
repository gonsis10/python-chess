from unit import Unit
from pieces import *


class Board:
    COLUMN = 8
    ROW = 8

    def __init__(self, players):
        self.players = players
        frame = [[Unit() for row in range(self.ROW)]
                 for column in range(self.COLUMN)]
        self.board = self.__setup(frame, players)

    def __str__(self) -> str:
        board = [[f"{unit} " for unit in row] and "\n" for row in self.board]
        return board

    def __setup(self, board, players) -> list:
        def return_back_row(pieces) -> list:
            back_row = []
            order = {0: Rook, 1: Knight, 2: Bishop, 3: Queen,
                     4: King, 5: Bishop, 6: Knight, 7: Rook}
            for index in range(len(pieces)):
                if pieces[index] != order.get(index):
                    back_row.append(pieces.pop(order.get(index)))
            return pieces

        board[0] = return_back_row(players[0].pieces)
        return board
