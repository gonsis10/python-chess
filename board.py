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
        def return_type_object(pieces) -> object:
            for piece in pieces:
                if
            return

        def return_back_row(pieces) -> list:
            back_row = []
            order = {0: Rook, 1: Knight, 2: Bishop, 3: Queen,
                     4: King, 5: Bishop, 6: Knight, 7: Rook}
            for index in range(len(pieces)):
                if not isinstance(pieces[index], order.get(index)):
                    piece = return_type_object(pieces)
                    pieces.remove(return)
                    back_row.append()
            return pieces

        board[0] = return_back_row(players[0].pieces)
        return board
