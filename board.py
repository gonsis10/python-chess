from unit import Unit
from pieces import *

class positiveIndexList(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError()
        return list.__getitem__(self, n)


class Board:
    COLUMN = 8
    ROW = 8

    def __init__(self, players):
        self.player_pieces = {"white": [], "black": []}
        self.board = positiveIndexList(self.s1(players))

    def display(self, piece_paths=None):
        string = ""
        for row in range(len(self.board)):
            string += f"{8 - row} "
            for column in range(len(self.board[row])):
                unit = self.board[row][column]
                if piece_paths != None and [row, column] in piece_paths:
                    if not type(unit) is Unit:
                        string += "✖ "
                    else:
                        string += "☐ "
                else:
                    piece_strings = {Pawn: {"white": "♟", "black": "♙"}, Bishop: {"white": "♝", "black": "♗"}, Knight: {
                        "white": "♞", "black": "♘"}, Rook: {"white": "♜", "black": "♖"}, Queen: {"white": "♛", "black": "♕"}, King: {"white": "♚", "black": "♔"}}
                    try:
                        string += f"{piece_strings[type(unit)][unit.player.color]} "
                    except:
                        string += "_ "
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

                self.player_pieces[player.color].extend(pieces)
                frame[row] = pieces
        return frame

    def s1(self, players):
        white, black = players
        frame = [[Unit() for column in range(self.COLUMN)]
                 for row in range(self.ROW)]
        pieces = []
        pieces.extend([Rook(black), Knight(black), Bishop(black), Queen(
            black), King(black), Bishop(black), Knight(black), Rook(black)])
        a, b = [Pawn(black), Pawn(black)]
        frame[1][3] = a
        frame[1][5] = b
        frame[0] = pieces
        self.player_pieces[black.color].extend(pieces)
        self.player_pieces[black.color].append(a)
        self.player_pieces[black.color].append(b)
        attack = Queen(white)
        frame[4][3] = attack
        self.player_pieces[white.color].extend([attack])
        king = King(white)
        frame[7][4] = king
        self.player_pieces[white.color].extend([king])
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
            x, y = list(response)
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
        try:
            piece.moved = True
        except:
            pass
        piece_row, piece_column = self.location(piece)
        position_row, position_column = self.location(position)
        try:
            self.player_pieces[position.player.color].remove(position)
        except:
            pass
        self.board[position_row][position_column] = piece
        self.board[piece_row][piece_column] = Unit()

    def status(self, players):
        for player in players:
            for row in self.board:
                for unit in row:
                    if type(unit) is King and unit.player.color == player.color:
                        checked = unit.checked(self)
                        paths = unit.paths(self, True)
                        if checked and not paths:
                            for piece in self.player_pieces[player.color]:
                                    if type(piece) != King and all(coordinate in unit.paths(self) for coordinate in piece.paths(self)):
                                        return "checkmate", "white" if player.color == "black" else "black"

                        remaining_pieces = sum(
                            [value for value in self.player_pieces.values()], [])
                        if len(remaining_pieces) == 3:
                            for option in [Bishop, Knight]:
                                if all(type(piece) in [King, option] for piece in remaining_pieces):
                                    return "stalemate", None
                        elif len(remaining_pieces) == 2:
                            if all(type(piece) in [King] for piece in remaining_pieces):
                                return "stalemate", None

                        # if not unit.paths(self, True):
                        #     return "stalemate", None

        return None, None
