from aoc import get_input
from copy import deepcopy

DATE = 25
data = get_input(DATE)

grid = [list(row) for row in data]

def transform(grid):
    grid_t = deepcopy(grid)
    H, W = len(grid), len(grid[0])

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '>' and grid[i][(j + 1) % W] == '.':
                grid_t[i][j] = '.'
                grid_t[i][(j + 1) % W] = '>'
    
    grid, grid_t = grid_t, deepcopy(grid_t)
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'v' and grid[(i + 1) % H][j] == '.':
                grid_t[i][j] = '.'
                grid_t[(i + 1) % H][j] = 'v'

    return grid_t
    
def print_grid(grid):
    for row in grid:
        print(''.join(row))

def solve():
    
    curr = grid
    next = transform(curr)
    i = 1

    while curr != next:
        curr = next
        next = transform(curr)
        i += 1

    print(i)
    return i
    
solve()