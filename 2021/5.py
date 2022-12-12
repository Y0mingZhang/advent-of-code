from aoc import get_input
from utils import *

DATE = 5
data = get_input(DATE)



def p1():
    grid = [[0] * 1000 for _ in range(1000)]
    for line in data:
        l, r = line.split(' -> ')
        x0, y0 = map(int, l.split(','))
        x1, y1 = map(int, r.split(','))

        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                grid[x0][y] += 1
        
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                grid[x][y0] += 1
        
    return sum(1 if n >= 2 else 0 for n in flatten(grid))

def p2():
    grid = [[0] * 1000 for _ in range(1000)]
    for line in data:
        l, r = line.split(' -> ')
        x0, y0 = map(int, l.split(','))
        x1, y1 = map(int, r.split(','))

        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                grid[x0][y] += 1
        
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                grid[x][y0] += 1

        elif abs(x1-x0)==abs(y1-y0):
            dx = 1 if x1 > x0 else -1
            dy = 1 if y1 > y0 else -1

            x, y = x0, y0
            while x != x1:
                grid[x][y] += 1
                x += dx
                y += dy
            assert(y == y1)
            grid[x1][y1] += 1

    return sum(1 if n >= 2 else 0 for n in flatten(grid))

print(p1())
print(p2())