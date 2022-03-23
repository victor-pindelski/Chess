class Board:
    def __init__(self, size_x=8, size_y=8):
        self.size_x = size_x
        self.size_y = size_y
        self.board = self.init_board(size_x, size_y)

    def init_board(self, size_x, size_y):
        board = []
        for _ in range(size_y):
            row = [' '] * size_x
            board.append(row)
        return board

    def print_board(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                if (x == 0):
                    print('|', end='')
                print(self.board[y][x] + '|', end='')
            print('')

def main():
    board = Board()
    board.print_board()

main()
