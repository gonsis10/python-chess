from board import Board
from player import Player
from pieces import *


class Game:
    players = [Player("white"), Player("black")]
    board = Board(players)

    def start(self):
        print(self.board.display())


if __name__ == "__main__":
    game = Game()
    game.start()
