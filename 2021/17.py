
from aoc import get_input

min_x = 128
max_x = 160

min_y = -142
max_y = -88

min_dx = 1
max_dx = 160

min_dy = -142
max_dy = 142

def simulate(dx, dy):
    highest_reached = 0
    hit = False
    x = y = 0
    while y >= min_y:
        x += dx
        y += dy
        highest_reached = max(highest_reached, y)
        if min_x <= x <= max_x and min_y <= y <= max_y:
            hit = True
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1
    return highest_reached if hit else float('-inf')

def p1():
    reached = 0
    for dx in range(min_dx, max_dx+1, 1):
        for dy in range(min_dy, max_dy+1, 1):
            reached = max(reached, simulate(dx, dy))

    return reached

def p2():
    good = 0
    for dx in range(min_dx, max_dx+1, 1):
        for dy in range(min_dy, max_dy+1, 1):
            if simulate(dx, dy) > float('-inf'):
                good += 1
    return good

print(p1())
print(p2())