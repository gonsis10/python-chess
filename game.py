from board import Board
from player import Player
from pieces import *

class Game:
    players = [Player("white"), Player("black")]
    board = Board(players)

    def __init__(self):
        self.start()

    def start(self):
        print(self.board)