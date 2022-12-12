from aoc import get_input
import functools
from utils import flatten

DATE = 20
data = get_input(DATE)


def convert_row(row):
    return [1 if pixel == "#" else 0 for pixel in row]


array = convert_row(data[0])
grid = [convert_row(row) for row in data[2:]]


def pad(arr, n):
    w = len(arr[0]) + 2 * n
    padded = []
    for i in range(len(arr)):
        padded.append([0] * n + arr[i] + [0] * n)

    padded = [[0] * w for _ in range(n)] + padded + [[0] * w for _ in range(n)]
    return padded

def print_grid(grid):
    for row in grid:
        print(''.join(map(lambda x: '.' if x == 0 else '#', row)))

def binary_to_pixel(binary):
    k = functools.reduce(
                lambda x, y: x * 2 + y, binary, 0
            )
    return array[k]

def enhance(n):
    gridp = pad(grid, n)
    H, W = len(gridp), len(gridp[0])

    def conv(i, j):
        binary = [
            gridp[x][y] if 0 <= x < len(gridp) and 0 <= y < len(gridp[0]) else bg
            for x in range(i - 1, i + 2)
            for y in range(j - 1, j + 2)
        ]
        return binary_to_pixel(binary)

    bg = 0
    for _ in range(n):
        grid_copy = [[0] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                grid_copy[i][j] = conv(i, j)
        bg = binary_to_pixel([bg] * 9)
        gridp = grid_copy
    
    print('pixels on:', sum(flatten(gridp)))
    return gridp

enhance(2)
enhance(50)