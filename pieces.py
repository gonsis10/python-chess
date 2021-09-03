import numpy as numpy
from unit import Unit


class Pawn(Unit):
    moved = False

    def __init__(self, player):
        super.__init__(player)

    def __str__(self):
        return str(0)

    def path(self, board):
        [row, column] = numpy.where(board == self)
        row = int(row)
        column = int(column)

        positions = []
        try:
            position = None
            if not self.moved:
                position = board[row - 2 if self.player.color ==
                                 "white" else row + 2][column]
            else:
                position = board[row - 1 if self.player.color ==
                                 "white" else row + 1][column]

            if isinstance(position, Unit):
                positions.append(position)
        except:
            pass

        return positions


class Bishop(Unit):
    def __init__(self, player):
        super.__init__(player)

    def __str__(self):
        return str(1)


class Knight(Unit):
    def __init__(self, player):
        super.__init__(player)

    def __str__(self):
        return str(2)


class Rook(Unit):
    def __init__(self, player):
        super.__init__(player)

    def __str__(self):
        return str(3)


class Queen(Unit):
    def __init__(self, player):
        super.__init__(player)

    def __str__(self):
        return str(4)


class King(Unit):
    def __init__(self, player):
        super.__init__(player)

    def __str__(self):
        return str(5)
