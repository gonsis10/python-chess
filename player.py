from pieces import Piece

class Player:
    def select():
        coord = input().split(", ")
        return Piece(coord[0], coord[1])
    def move():
        coord = input().split(", ")
        return Piece(coord[0], coord[1])