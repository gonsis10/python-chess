from unit import Unit


class Pawn(Unit):
    moved = False

    def __init__(self, player):
        super().__init__(player)

    def paths(self, board):
        row, column = board.location(self)
        DIRECTION = f"{row} - " if self.player.color == "white" else f"{row} + "
        FORWARD_1 = eval(f"{DIRECTION} 1")
        FORWARD_2 = eval(f"{DIRECTION} 2")
        positions = []
        # Forward
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
            # Attack
            try:
                position = board.board[FORWARD_1][column - 1]
                if position.player.color != self.player.color:
                    positions.append([FORWARD_1, column - 1])
            except:
                pass

            try:
                position = board.board[FORWARD_1][column + 1]
                if position.player.color != self.player.color:
                    positions.append([FORWARD_1, column + 1])
            except:
                pass

        return positions


class Bishop(Unit):
    def __init__(self, player):
        super().__init__(player)

    def paths(self, board):
        row, column = board.location(self)
        positions = []
        # Top left
        try:
            amount = 1
            while True:
                position = board.board[row + amount][column - amount]
                if type(position) is Unit:
                    positions.append([row + amount, column - amount])
                elif position.player.color != self.player.color:
                    positions.append([row + amount, column - amount])
                    break
                else:
                    break
                amount += 1
        except:
            pass
        # Top right
        try:
            amount = 1
            while True:
                position = board.board[row + amount][column + amount]
                if type(position) is Unit:
                    positions.append([row + amount, column + amount])
                elif position.player.color != self.player.color:
                    positions.append([row + amount, column + amount])
                    break
                else:
                    break
                amount += 1
        except:
            pass
        # Bottom reft
        try:
            amount = 1
            while True:
                position = board.board[row - amount][column - amount]
                if type(position) is Unit:
                    positions.append([row - amount, column - amount])
                elif position.player.color != self.player.color:
                    positions.append([row - amount, column - amount])
                    break
                else:
                    break
                amount += 1
        except:
            pass
        # Bottom right
        try:
            amount = 1
            while True:
                position = board.board[row - amount][column + amount]
                if type(position) is Unit:
                    positions.append([row - amount, column + amount])
                elif position.player.color != self.player.color:
                    positions.append([row - amount, column + amount])
                    break
                else:
                    break
                amount += 1
        except:
            pass

        return positions


class Knight(Unit):
    def __init__(self, player):
        super().__init__(player)

    def paths(self, board):
        row, column = board.location(self)
        positions = []
        try:
            position = board.board[row + 2][column - 1]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row + 2, column - 1])
        except:
            pass

        try:
            position = board.board[row + 2][column + 1]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row + 2, column + 1])
        except:
            pass

        try:
            position = board.board[row + 1][column + 2]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row + 1, column + 2])
        except:
            pass

        try:
            position = board.board[row - 1][column + 2]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row - 1, column + 2])
        except:
            pass

        try:
            position = board.board[row - 2][column - 1]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row - 2, column - 1])
        except:
            pass

        try:
            position = board.board[row - 2][column + 1]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row - 2, column + 1])
        except:
            pass

        try:
            position = board.board[row - 1][column - 2]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row - 1, column - 2])
        except:
            pass

        try:
            position = board.board[row + 1][column - 2]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row + 1, column - 2])
        except:
            pass

        return positions


class Rook(Unit):
    moved = False

    def __init__(self, player):
        super().__init__(player)

    def paths(self, board):
        row, column = board.location(self)
        positions = []
        # Up
        try:
            amount = 1
            while True:
                position = board.board[row + amount][column]
                if type(position) is Unit:
                    positions.append([row + amount, column])
                elif position.player.color != self.player.color:
                    positions.append([row + amount, column])
                    break
                else:
                    break
                amount += 1
        except:
            pass
        # Right
        try:
            amount = 1
            while True:
                position = board.board[row][column + amount]
                if type(position) is Unit:
                    positions.append([row, column + amount])
                elif position.player.color != self.player.color:
                    positions.append([row, column + amount])
                    break
                else:
                    break
                amount += 1
        except:
            pass
        # Down
        try:
            amount = 1
            while True:
                position = board.board[row - amount][column]
                if type(position) is Unit:
                    positions.append([row - amount, column])
                elif position.player.color != self.player.color:
                    positions.append([row - amount, column])
                    break
                else:
                    break
                amount += 1
        except:
            pass
        # Left
        try:
            amount = 1
            while True:
                position = board.board[row][column - amount]
                if type(position) is Unit:
                    positions.append([row, column - amount])
                elif position.player.color != self.player.color:
                    positions.append([row, column - amount])
                    break
                else:
                    break
                amount += 1
        except:
            pass

        return positions


class Queen(Unit):
    def __init__(self, player):
        super().__init__(player)

    def paths(self, board):
        positions = []
        positions.extend(Rook.paths(self, board))
        positions.extend(Bishop.paths(self, board))

        return positions


class King(Unit):
    moved = False

    def __init__(self, player):
        super().__init__(player)

    def paths(self, board, check_once=False):
        row, column = board.location(self)
        positions = []
        if not self.moved:
            try:
                for rook in filter(lambda piece: type(piece) is Rook, board.player_pieces[self.player.color]):
                    if not rook.moved:
                        _, rook_column = board.location(rook)
                        step = 1 if column > rook_column else -1
                        if all(type(board.board[row][space]) is Unit for space in range(rook_column + step, column, step)):
                            positions.append(
                                [row, column + (2 if step < 0 else - 2)])
            except:
                pass

        for direction in ["top", "bottom"]:
            DIRECTION = row + 1 if direction == "top" else row - 1
            for amount in range(-1, 2):
                try:
                    position = board.board[DIRECTION][column + amount]
                    if type(position) is Unit or position.player.color != self.player.color:
                        positions.append([DIRECTION, column + amount])
                except:
                    pass

        try:
            position = board.board[row][column - 1]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row, column - 1])
        except:
            pass

        try:
            position = board.board[row][column + 1]
            if type(position) is Unit or position.player.color != self.player.color:
                positions.append([row, column + 1])
        except:
            pass

        if check_once:
            enemy_pieces = board.player_pieces["black" if self.player.color ==
                                               "white" else "white"]
            for enemy_piece in enemy_pieces:
                positions = [
                    position for position in positions if position not in enemy_piece.paths(board)]

        return positions

    def checked(self, board):
        enemy_pieces = board.player_pieces["black" if self.player.color ==
                                           "white" else "white"]
        for enemy_piece in enemy_pieces:
            location = list(board.location(self))
            paths = enemy_piece.paths(board)
            if location in paths:
                return True

        return False
