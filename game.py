from board import Board
from player import Player
from pieces import *


class Game:
    players = [Player("white"), Player("black")]
    board = Board(players)

    def start(self):
        round = 1
        game_over = False
        while not game_over:
            for player in self.players:
                self.piece_selection(player)
            round += 1

    def piece_selection(self, player):
        print(f"{self.board.display()}\nSelect piece.")
        [valid, piece] = self.board.unit(input(), player)
        if valid:
            self.position_selection(piece, player)
        else:
            self.piece_selection(player)

    def position_selection(self, piece, player):
        piece_paths = piece.paths(self.board)
        print(piece_paths)
        print(f"{self.board.display(piece_paths)}\nSelect position.")
        response = input()
        if response.lower() == "b":
            self.piece_selection(player)
            return
        [valid, position] = self.board.unit(response)
        if valid and list(self.board.location(position)) in piece_paths:
            self.board.move(piece, position)
        else:
            self.position_selection(piece, player)


if __name__ == "__main__":
    game = Game()
    game.start()
