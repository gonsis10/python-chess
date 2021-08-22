from unit import Unit

class Pawn(Unit):
    def __init__(self, player):
        self.player = player

    def __str__(self):
        return str(0)

class Bishop(Unit):
    def __init__(self, player):
        self.player = player

    def __str__(self):
        return str(1)

class Knight(Unit):
    def __init__(self, player):
        self.player = player

    def __str__(self):
        return str(2)

class Rook(Unit):
    def __init__(self, player):
        self.player = player

    def __str__(self):
        return str(3)

class Queen(Unit):
    def __init__(self, player):
        self.player = player

    def __str__(self):
        return str(4)

class King(Unit):
    def __init__(self, player):
        self.player = player

    def __str__(self):
        return str(5)