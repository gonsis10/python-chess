from unit import Unit


class Pawn(Unit):
    moved = False

    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return str(0)

    def paths(self, board):
        [row, column] = board.location(self)
        direction = f"{row} - " if self.player.color == "white" else f"{row} + "
        FORWARD_1 = eval(f"{direction} 1")
        FORWARD_2 = eval(f"{direction} 2")
        positions = []
        try:
            position = board.board[FORWARD_1][column]
            if type(position) is Unit:
                positions.append([FORWARD_1, column])
                if not self.moved:
                    try:
                        position = board.board[FORWARD_2][column]
                        if type(position) is Unit:
                            positions.append([FORWARD_2, column])
                    except:
                        pass
        finally:
            try:
                position = board.board[FORWARD_1][column - 1]
                if not type(position) is Unit:
                    positions.append([FORWARD_1, column - 1])
            except:
                pass

            try:
                position = board.board[FORWARD_1][column + 1]
                if not type(position) is Unit:
                    positions.append([FORWARD_1, column + 1])
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
