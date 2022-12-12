from aoc import get_input
import collections

DATE = 4
data = get_input(DATE)

numbers = map(int, data[0].split(','))

def flatten(iteriter):
    for iter in iteriter:
        yield from iter

class Board:
    def __init__(self, rows):
        assert(len(rows) == 5)
        self.matrix = [list(map(int, rows[i].split())) for i in range(5)]
        self.rows = [5] * 5
        self.cols = [5] * 5
        self.on = [[True] * 5 for _ in range(5)]
        self.has_won = False
    
    def mark(self, x, y):
        if self.on[x][y]:
            self.rows[x] -= 1
            self.cols[y] -= 1
            self.on[x][y] = False
        return self.rows[x] * self.cols[y] == 0
    
    def score(self):
        tot = 0
        for val, on in zip(flatten(self.matrix), flatten(self.on)):
            if on:
                tot += val
        return tot

def p1():
    val2boardxy = collections.defaultdict(list)
    boards = []

    for row in range(2, len(data), 6):
        boards.append(Board(data[row:row+5]))
        for i in range(5):
            for j in range(5):
                val2boardxy[boards[-1].matrix[i][j]].append((len(boards)-1, i, j))


    for n in numbers:
        for board_idx, x, y in val2boardxy[n]:
            board = boards[board_idx]
            if board.mark(x, y):
                # won
                print("score:", board.score() * n)
                return

def p2():
    val2boardxy = collections.defaultdict(list)
    boards = []

    for row in range(2, len(data), 6):
        boards.append(Board(data[row:row+5]))
        for i in range(5):
            for j in range(5):
                val2boardxy[boards[-1].matrix[i][j]].append((len(boards)-1, i, j))

    rem = len(boards)
    for n in numbers:
        for board_idx, x, y in val2boardxy[n]:
            board = boards[board_idx]
            if not board.has_won and board.mark(x, y):
                board.has_won = True
                rem -= 1
                if rem == 0:
                    print("score:", board.score() * n)
                
p1()
p2()

