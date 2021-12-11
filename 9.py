from aoc import get_input
import functools
from collections import defaultdict

DATE = 9
data = get_input(DATE)

grid = [[int(c) for c in row] for row in data]

M = len(grid)
N = len(grid[0])


def p1():
    risk_sum = 0

    for x in range(M):
        for y in range(N):
            lower_neighbor = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (
                    0 <= x + dx < M
                    and 0 <= y + dy < N
                    and grid[x + dx][y + dy] <= grid[x][y]
                ):
                    lower_neighbor += 1
            if lower_neighbor == 0:
                risk_sum += 1 + grid[x][y]

    return risk_sum


def p2():
    low_points = []
    for x in range(M):
        for y in range(N):
            lower_neighbor = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (
                    0 <= x + dx < M
                    and 0 <= y + dy < N
                    and grid[x + dx][y + dy] <= grid[x][y]
                ):
                    lower_neighbor += 1
            if lower_neighbor == 0:
                low_points.append((x, y))

    visited = [[set() for _ in range(N)] for _ in range(M)]

    def dfs_basin(x, y, key):
        print(x,y,key)
        visited[x][y].add(key)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (
                0 <= x + dx < M
                and 0 <= y + dy < N
                and grid[x + dx][y + dy] > grid[x][y]
                and key not in visited[x + dx][y + dy]
            ):
                dfs_basin(x + dx, y + dy, key)

    for point in low_points:
        dfs_basin(point[0], point[1], point)

    basins = defaultdict(int)
    for x in range(M):
        for y in range(N):
            if len(visited[x][y]) == 1 and grid[x][y] != 9:
                basins[visited[x][y].pop()] += 1
    
    return sorted(basins.values())[-3:]


print(p1())
print(p2())
