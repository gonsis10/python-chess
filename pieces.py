from unit import Unit

class Pawn(Unit):
    def __init__(self):
        super().__init__(None, None)

    def __repr__(self):
        return -1

    def move(self, board, move, opponent):
        x = move[0]

# class Bishop(Piece):
#     def __init__(self):


# class Knight(Piece):
#     def __init__(self):

# class Rook(Piece):
#     def __init__(self):

# class Queen(Piece):
#     def __init__(self):

# class King(Piece):
#     def __init__(self):