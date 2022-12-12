from aoc import get_input

DATE = 13
data = get_input(DATE)

points = []
folds = []
for line in data:
    try:
        x, y = map(int, line.split(','))
        points.append((x, y))
    except:
        if line.startswith('fold'):
            xy, n = line.split()[-1].split('=')
            n = int(n)
            folds.append((xy, n))

print(points, folds)

def transform(x, y, xy, n):
    if xy == 'x' and x > n:
        return 2 * n - x, y
    if xy == 'y' and y > n:
        return x, 2 * n - y
    return x, y

def p2():
    pts = points
    max_x = float('inf')
    max_y = float('inf')
    for xy, n in folds:
        pts = set(map(lambda p: transform(p[0], p[1], xy, n), pts))
        if xy == 'x':
            max_x = min(max_x, n)
        elif xy == 'y':
            max_y = min(max_y, n)
    
    grid = [[' '] * max_x for _ in range(max_y)]
    for x, y in pts:
        grid[y][x] = '*'

    for row in grid:
        print(''.join(row))
p2()