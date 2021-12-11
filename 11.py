from aoc import get_input
from copy import deepcopy


DATE = 11
data = get_input(DATE)

grid = [list(map(int, row)) for row in data]
M = len(grid)
N = len(grid[0])
print(grid)


def find_flash(state, has_flashed):
    for x in range(M):
        for y in range(N):
            if not has_flashed[x][y] and state[x][y] > 9:
                return x, y

    return -1, -1


def p1():
    state = deepcopy(grid)
    flashes = 0

    for _ in range(100):
        has_flashed = [[False] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                state[x][y] += 1
        while True:
            x, y = find_flash(state, has_flashed)
            if x < 0:
                break
            flashes += 1
            has_flashed[x][y] = True
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == dy == 0:
                        continue
                    if 0 <= x + dx < M and 0 <= y + dy < N:
                        state[x + dx][y + dy] += 1
        for x in range(M):
            for y in range(N):
                if has_flashed[x][y]:
                    state[x][y] = 0

    return flashes


def p2():
    state = deepcopy(grid)

    for step in range(1, 99999):
        flashes = 0
        has_flashed = [[False] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                state[x][y] += 1
        while True:
            x, y = find_flash(state, has_flashed)
            if x < 0:
                break
            flashes += 1
            has_flashed[x][y] = True
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == dy == 0:
                        continue
                    if 0 <= x + dx < M and 0 <= y + dy < N:
                        state[x + dx][y + dy] += 1
        for x in range(M):
            for y in range(N):
                if has_flashed[x][y]:
                    state[x][y] = 0

        if flashes == M * N:
            return step


print(p1())
print(p2())
