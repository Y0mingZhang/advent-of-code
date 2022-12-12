from aoc import get_input
from collections import defaultdict, Counter
DATE = 12
data = get_input(DATE)

graph = defaultdict(list)

for line in data:
    u, v = line.split('-')
    graph[u].append(v)
    graph[v].append(u)

def small(s):
    return s[0].islower()


def count_paths(curr, visited):
    if curr == 'end':
        return 1
    
    if small(curr):
        visited.add(curr)
    
    ways = 0
    for nei in graph[curr]:
        if small(nei) and nei in visited:
            continue
        ways += count_paths(nei, visited)
    
    if small(curr):
        visited.remove(curr)
    return ways


def count_paths_v2(curr, visited, twice):
    if curr == 'end':
        return 1
    
    if small(curr):
        visited.add(curr)
    
    ways = 0
    for nei in graph[curr]:
        if small(nei) and nei in visited:
            if not twice and nei != 'start':
                ways += count_paths_v2(nei, visited, True)
                visited.add(nei)
            continue
        ways += count_paths_v2(nei, visited, twice)
    
    if small(curr):
        visited.remove(curr)
    return ways

print(count_paths('start', set()))
print(count_paths_v2('start',set(), False))
