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
        board = ""
        for row in range(len(self.board)):
            board += f"{row + 1} "
            for column in range(len(self.board[row])):
                board += f"{self.board[row][column]} "
            board += "\n"
        board += "  a b c d e f g h"
        return board

    def __setup(self, board, players) -> list:
        def return_type_object(pieces, value) -> object:
            for piece in pieces:
                if isinstance(piece, value):
                    return piece
            return None

        def return_back_row(pieces) -> list:
            back_row = []
            order = {0: Rook, 1: Knight, 2: Bishop, 3: Queen,
                     4: King, 5: Bishop, 6: Knight, 7: Rook}
            for index in range(len(pieces)):
                supposed_value = order.get(index)
                if not isinstance(pieces[index], supposed_value):
                    piece = return_type_object(pieces, supposed_value)
                    pieces.remove(piece)
                    back_row.append(piece)
            return back_row

        board[0] = return_back_row(players[0].pieces)
        return board
