import random

class Puzzle15:
    def __init__(self):
        self.tiles = [str(i) for i in range(1, 16)]
        self.tiles.append(' ')
        self.board = []
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.empty_pos = (3, 3)
        self.generate_board()

    def generate_board(self):
        random.shuffle(self.tiles)
        for i in range(0, 16, 4):
            self.board.append(self.tiles[i:i + 4])

    def move_tile(self, direction):
        dx, dy = self.moves[direction]
        new_x = self.empty_pos[0] + dx
        new_y = self.empty_pos[1] + dy

        if 0 <= new_x < 4 and 0 <= new_y < 4:
            self.board[self.empty_pos[0]][self.empty_pos[1]], self.board[new_x][new_y] = (
                self.board[new_x][new_y],
                self.board[self.empty_pos[0]][self.empty_pos[1]],
            )
            self.empty_pos = (new_x, new_y)
        else:
            print("Invalid move!")

    def is_solved(self):
        return self.tiles == sum(self.board, [])

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print('\n')

game = Puzzle15()
game.print_board()