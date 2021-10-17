from board import Board
from player import Player
from pieces import *


class Game:
    players = [Player("white"), Player("black")]
    board = Board(players)

    def start(self):
        round = 1
        while True:
            for player in self.players:
                if self.check_game_over():
                    break
                self.piece_selection(player)
                # self.check_win(player)
            round += 1

    def piece_selection(self, player):
        print(f"{self.board.display()}\nSelect piece.")
        valid, piece = self.board.unit(input(), player)
        if valid:
            self.position_selection(piece, player)
        else:
            self.piece_selection(player)

    def position_selection(self, piece, player):
        piece_paths = piece.paths(self.board) if type(
            piece) != King else piece.paths(self.board, True)
        # print(piece_paths)
        print(f"{self.board.display(piece_paths)}\nSelect position.")
        response = input()
        if response.lower() == "b":
            self.piece_selection(player)
            return
        valid, position = self.board.unit(response)
        if valid and list(self.board.location(position)) in piece_paths:
            self.board.move(piece, position)
        else:
            self.position_selection(piece, player)

    def check_game_over(self):
        status, winner = self.board.status(self.players)
        if status == "checkmate":
            print(
                f"{self.board.display()}\n{status.capitalize()}! {winner.capitalize()} wins.")
            return True
        elif status == "stalemate":
            print(
                f"{self.board.display()}\n{status.capitalize()}! Draw.")
            return True

        return False


if __name__ == "__main__":
    game = Game()
    game.start()
