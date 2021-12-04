from aoc import get_input

DATE = 2
data = get_input(DATE)

aim = pos = depth = 0

for line in data:
    a, b = line.split()
    b = int(b)

    if a == 'forward':
        pos += b
        depth += b * aim
    elif a == 'down':
        aim += b
    else:
        aim -= b


print(pos*depth)
