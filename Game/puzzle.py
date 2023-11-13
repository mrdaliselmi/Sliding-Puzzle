import random
import itertools

class Puzzle:
    def __init__(self, board):
        self.width = len(board[0])
        self.board = board

    @property
    def solved(self):
        N = self.width * self.width
        return str(self) == ''.join(map(str, range(1,N))) + '0'

    @property 
    def actions(self):
        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width),
                                      range(self.width)):
            direcs = {'R':(i, j-1),
                      'L':(i, j+1),
                      'D':(i-1, j),
                      'U':(i+1, j)}

            for action, (r, c) in direcs.items():
                if r >= 0 and c >= 0 and r < self.width and c < self.width and \
                   self.board[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves

    @property
    def manhattan(self):
        distance = 0
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j]-1, self.width)
                    distance += abs(x - i) + abs(y - j)
        return distance
    
    @property
    def hamming(self):
        distance = 0
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] != 0:
                    if self.board[i][j] != i*self.width + j + 1:
                        distance += 1
        return distance

    def shuffle(self, moves=1000):
        puzzle = self
        for _ in range(moves):
            puzzle = random.choice(puzzle.actions)[0]()
        return puzzle

    def copy(self):
        board = []
        for row in self.board:
            board.append([x for x in row])
        return Puzzle(board)

    def _move(self, at, to):
        copy = self.copy()
        i, j = at
        r, c = to
        copy.board[i][j], copy.board[r][c] = copy.board[r][c], copy.board[i][j]
        return copy

    def display(self):
        for row in self.board:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row
