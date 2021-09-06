import numpy as numpy
from unit import Unit


class Pawn(Unit):
    moved = False

    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return str(0)

    def path(self, board):
        [row, column] = board.location(self)
        direction = f"{row} - " if self.player.color == "white" else f"{row} + "

        positions = []
        try:
            position = board[eval(direction + 1)][column]
            if isinstance(position, Unit):
                positions.append(position)
                if not self.moved:
                    try:
                        position = board[eval(direction + 2)][column]
                        if isinstance(position, Unit):
                            positions.append(position)
                    except:
                        pass
        finally:
            try:
                position = board[eval(direction + 1)][column - 1]
                if not isinstance(position, Unit):
                    positions.append(position)
            except:
                pass

            try:
                position = board[eval(direction + 1)][column + 1]
                if not isinstance(position, Unit):
                    positions.append(position)
            except:
                pass

        return positions


class Bishop(Unit):
    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return str(1)


class Knight(Unit):
    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return str(2)


class Rook(Unit):
    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return str(3)


class Queen(Unit):
    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return str(4)


class King(Unit):
    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return str(5)
