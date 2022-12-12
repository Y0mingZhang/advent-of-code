from functools import cached_property
from heapq import *
from aoc import get_input
from copy import deepcopy
from utils import flatten


DATE = 23
data = get_input(DATE)

p1_rows = [list(row) + [" "] * (13 - len(row)) for row in data[1:-1]]
added_rows = ["  #D#C#B#A#", "  #D#B#A#C#"]
p2_rows = [
    list(row) + [" "] * (13 - len(row)) for row in data[1:3] + added_rows + data[3:-1]
]

AMPHIPOD_COLUMNS = {"A": 3, "B": 5, "C": 7, "D": 9}
AMPHIPOD_COST = {"A": 1, "B": 10, "C": 100, "D": 1000}
HALLWAY_COLUMNS = [1, 2, 4, 6, 8, 10, 11]


def manhattan(x0, x1, y0, y1):
    return abs(x0 - x1) + abs(y0 - y1)


class State:
    def __init__(self, grid):
        self.grid = grid

    def __eq__(self, other):
        return self.grid == other.grid

    def __lt__(self, other):
        return hash(self) < hash(other)

    @cached_property
    def _hash(self):
        return hash(tuple(flatten(self.grid)))

    def __repr__(self):
        return "\n".join(map(lambda row: "".join(row), self.grid))

    def __hash__(self):
        return self._hash

    def reachable(self, i, j):
        visited = set()
        stk = [(i, j)]
        while stk:
            x, y = stk.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x_next, y_next = x + dx, y + dy
                if (
                    0 <= x_next < len(self.grid)
                    and 0 <= y_next < len(self.grid[0])
                    and self.grid[x_next][y_next] == "."
                ):
                    stk.append((x_next, y_next))

        return list(visited)

    def validate(self, letter):
        row = len(self.grid) - 1
        col = AMPHIPOD_COLUMNS[letter]
        while row >= 1 and self.grid[row][col] == letter:
            row -= 1
        while row >= 1 and self.grid[row][col] == ".":
            row -= 1
        return row == 0

    def next_states(self):
        next_states = []
        for j in range(len(self.grid[0])):
            if self.grid[0][j] in AMPHIPOD_COLUMNS:
                amphipod = self.grid[0][j]
                room = AMPHIPOD_COLUMNS[amphipod]
                reachables = self.reachable(0, j)
                if self.validate(amphipod):
                    for row in range(len(self.grid) - 1, 0, -1):
                        if (row, room) in reachables:
                            grid = deepcopy(self.grid)
                            grid[0][j] = "."
                            grid[row][room] = amphipod
                            cost = manhattan(0, row, j, room) * AMPHIPOD_COST[amphipod]
                            next_states.append((cost, State(grid)))
                            break

            for i in range(1, len(self.grid)):
                if self.grid[i][j] in AMPHIPOD_COLUMNS:
                    amphipod = self.grid[i][j]
                    reachables = self.reachable(i, j)
                    for col in HALLWAY_COLUMNS:
                        if (0, col) in reachables:
                            grid = deepcopy(self.grid)
                            grid[0][col] = amphipod
                            grid[i][j] = "."
                            cost = manhattan(0, i, col, j) * AMPHIPOD_COST[amphipod]
                            next_states.append((cost, State(grid)))

        return next_states

    def is_terminal(self):
        for letter, column in AMPHIPOD_COLUMNS.items():
            if any(row[column] != letter for row in self.grid[1:]):
                return False
        return True


def solve(state):
    visited = set()
    heap = [(0, state)]
    while heap:
        cost, curr_state = heappop(heap)
        if curr_state.is_terminal():
            print("Minimum cost:", cost)
            return
        if curr_state in visited:
            continue
        visited.add(curr_state)
        for new_cost, new_state in curr_state.next_states():
            heappush(heap, (cost + new_cost, new_state))


p1 = State(p1_rows)
p2 = State(p2_rows)

solve(p1)
solve(p2)
