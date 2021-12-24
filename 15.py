from aoc import get_input

from utils import *
from heapq import *

DATE = 15
data = get_input(DATE)

grid = [[int(c) for c in row] for row in data]

def heuristic(x, y):
    return len(grid) - 1 - x + len(grid[0]) - 1 - y

def total_risk(grid):
    visited = set()
    heap = [(0, 0, 0)]
    while heap:
        curr_cost, x, y = heappop(heap)
        # print(min_cost, curr_cost, x, y)
        if (x, y) not in visited:
            visited.add((x, y))
        else:
            continue
        if x + 1 == len(grid) and y + 1 == len(grid[0]):
            return curr_cost
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and (x+dx, y+dy) not in visited:
                c = curr_cost+grid[x+dx][y+dy]
                mc = heuristic(x+dx, y+dy) + c
                heappush(heap, (c, x+dx, y+dy))

print(total_risk(grid))

def conv(n):
    if n >= 10:
        return n-9
    return n

def hcopy(arr, offset):
    return [conv((n+offset)) for n in arr]

def vcopy(grid, offset):
    return [[conv((n+offset)) for n in arr] for arr in grid]

grid_hcopy = [list(flatten([hcopy(arr, i) for i in range(5)])) for arr in grid]
grid = list(flatten([vcopy(grid_hcopy, i) for i in range(5)]))

print(total_risk(grid))