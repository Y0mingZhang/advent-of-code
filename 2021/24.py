import functools
from aoc import get_input

DATE = 24
data = get_input(DATE)

def parse_block(lines):
    mode = 'pop' if lines[4] == 'div z 26' else 'push'
    diff = int(lines[5].split()[-1])
    added = int(lines[15].split()[-1])

    return mode, diff, added

def generate_rules(blocks):
    stk = []
    rules = []
    for i, (mode, diff, added) in enumerate(blocks):
        if mode == 'push':
            stk.append((i, added))
        elif mode == 'pop':
            j, added = stk.pop()
            j + added == i + diff
            rules.append((j, i, added + diff))
    return rules

blocks = []
for i in range(0, len(data), 18):
    blocks.append(parse_block(data[i:i+18]))
rules = generate_rules(blocks)


def p1():
    sol = [-1] * 14
    for l, r, diff in rules:
        for i in range(9, 0, -1):
            if 1 <= i + diff <= 9:
                sol[l] = i
                sol[r] = i + diff
                break
    
    print('max answer', functools.reduce(lambda x, y: x*10 + y, sol))

def p2():
    sol = [-1] * 14
    for l, r, diff in rules:
        for i in range(1, 10):
            if 1 <= i + diff <= 9:
                sol[l] = i
                sol[r] = i + diff
                break
    
    print('min answer', functools.reduce(lambda x, y: x*10 + y, sol))

p1()
p2()
