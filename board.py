from unit import Unit
from pieces import *


class Board:
    COLUMN = 8
    ROW = 8

    def __init__(self, players):
        self.board = self.__setup(players)

    def display(self, piece_paths=None):
        string = ""
        for row in range(len(self.board)):
            string += f"{8 - row} "
            for column in range(len(self.board[row])):
                unit = self.board[row][column]
                if piece_paths != None and [row, column] in piece_paths:
                    if not type(unit) is Unit:
                        string += "X "
                    else:
                        string += "O "
                else:
                    string += "_ " if str(unit
                                          ) == "-1" else f"{unit} "
            string += "\n"
        string += "  a b c d e f g h"
        return string

    def __setup(self, players):
        frame = [[Unit() for column in range(self.COLUMN)]
                 for row in range(self.ROW)]
        piece_orders = {"black": [0, 1], "white": [7, 6]}
        for player in players:
            order = piece_orders[player.color]
            for row in order:
                pieces = []
                if row == order[0]:
                    pieces.extend([Rook(player), Knight(player), Bishop(player), Queen(
                        player), King(player), Bishop(player), Knight(player), Rook(player)])
                else:
                    pieces.extend([Pawn(player)
                                  for column in range(self.COLUMN)])

                player.add_pieces(pieces)
                frame[row] = pieces

        return frame

    def location(self, piece):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if piece is self.board[row][column]:
                    return row, column
        return None, None

    def unit(self, response, player=None):
        x_order = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
        y_order = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
        try:
            [x, y] = list(response)
            column = x_order[x]
            row = y_order[y]
            unit = self.board[row][column]
            if player != None:
                if unit.player.color == player.color:
                    return True, unit
            else:
                return True, unit
        except:
            pass
        return False, None

    def move(self, piece, position):
        if hasattr(piece, "moved"):
            if not piece.moved:
                piece.moved = True
        [piece_row, piece_column] = self.location(piece)
        [position_row, position_column] = self.location(position)
        self.board[position_row][position_column] = piece
        self.board[piece_row][piece_column] = Unit()
