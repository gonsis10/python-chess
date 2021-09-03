import numpy as numpy
from unit import Unit


class Pawn(Unit):
    moved = False

    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return str(0)

    def path(self, board):
        [row, column] = super().location(self, board)

        positions = []
        for _ in range(2):
            try:
                amount = 2 if not self.moved else 1
                position = board[row - amount if self.player.color == "white" else row + amount][column]
                
                if isinstance(position, Unit):
                    positions.append(position)
                    if not self.moved:
                        self.moved = True
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
