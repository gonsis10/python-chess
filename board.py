import numpy as np
from unit import Unit
from pieces import *


class Board:
    COLUMN = 8
    ROW = 8

    def __init__(self, players):
        self.board = np.array(self.__setup(players))

    def display(self, board=None):
        if board == None:
            board = self.board
        string = ""
        for row in range(len(board)):
            string += f"{row + 1} "
            for column in range(len(board[row])):
                string += "_ " if str(board[row][column]
                                      ) == "-1" else f"{board[row][column]} "
            string += "\n"
        string += "  a b c d e f g h"
        return string

    def __setup(self, players):
        frame = [[Unit() for column in range(self.COLUMN)]
                 for row in range(self.ROW)]
        piece_orders = {"white": [0, 1], "black": [7, 6]}
        for player in players:
            order = piece_orders.get(player.color)
            for row in order:
                pieces = []
                if row == order[0]:
                    pieces.extend([Rook(player), Knight(player), Bishop(player), Queen(
                        player), King(player), Bishop(player), Knight(player), Rook(player)])
                else:
                    pieces.extend([Pawn(player)] * 8)

                player.add_pieces(pieces)
                frame[row] = pieces

        return frame

    def get_piece(self, x, y):
        x_order = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
        y_order = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}

        try:
            column = x_order.get(x)
            row = y_order.get(y)
            return True, self.board[row][column]
        except:
            return False

    def select_piece(self, piece):
        copy = self.board
        [row, column] = np.where(self.board == piece)
        row = int(row)
        column = int(column)

        def pawn():
            column = 0

        paths = {Pawn: pawn, Rook: rook, Knight: knight,
                 Bishop: bishop, Queen: queen, King: king}

        return paths.get(piece)()

    def move_piece(self, piece):
        self.board.remove(piece)
