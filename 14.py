from aoc import get_input
from collections import Counter

DATE = 14
data = get_input(DATE)

start = data[0]
rules = {}
for rule in data[2:]:
    a, b = rule.split(' -> ')
    rules[a] = b

def p1():
    old = start
    for i in range(10):
        new = []
        for ca, cb in zip(old, old[1:]):
            new.append(ca)
            if ca+cb in rules:
                new.append(rules[ca+cb])
        new.append(old[-1])
        old = ''.join(new)

    freqs = Counter(old)
    print(max(freqs.values()) - min(freqs.values()))

def p2():
    old = Counter()
    for a, b in zip(start, start[1:]):
        old[a+b] += 1

    for i in range(40):
        new = Counter()
        for pair, count in old.items():
            if pair in rules:
                new[pair[0] + rules[pair]] += count
                new[rules[pair] + pair[1]] += count
            else:
                new[pair] += count
        old = new
    
    char_counts = Counter()
    char_counts[start[0]] += 1
    char_counts[start[-1]] += 1
    for pair, count in old.items():
        char_counts[pair[0]] += count
        char_counts[pair[1]] += count
    
    for c in char_counts:
        char_counts[c] //= 2

    print(max(char_counts.values()) - min(char_counts.values()))

p2()