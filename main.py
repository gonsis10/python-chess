from player import Player
from pieces import Piece

first_player = Player()
second_player = Player()
players = [first_player, second_player]
board = [[3, 2, 1, 4, 5, 1, 2, 3], 
    [-1, -1, -1, -1, -1, -1, -1, -1], 
    [-1, -1, -1, -1, -1, -1, -1, -1], 
    [-1, -1, -1, -1, -1, -1, -1, -1], 
    [-1, -1, -1, -1, -1, -1, -1, -1], 
    [-1, -1, -1, -1, -1, -1, -1, -1], 
    [-1, -1, -1, -1, -1, -1, -1, -1], 
    [3, 2, 1, 4, 5, 1, 2, 3]

def display():
    for column in range(len(board)):
        for row in range(len(board[c])):
            print(board[column][row], end =" ")
        print()

def move(p):
    piece = player.select()
    move = p.move()
    if (piece.move(board, move)):
        board[piece.x][[piece.y]] = piece
        board[move[0]][move[1]] = piece

def game():
    for player in players:
        finished = False
        while (finished):
            piece = player.select()
            move(player)
            
            


def main():
    display()
    game()

if __name__ == "__main__":
    main()