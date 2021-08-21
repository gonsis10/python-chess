from board import Board
from player import Player
from pieces import *

class Game:
    def __init__(self):
        self.board = Board()
        self.first_player = Player()
        self.second_player = Player()
        self.players = [self.first_player, self.second_player]

    def start(self):
        print(self.board)