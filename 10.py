from aoc import get_input

DATE = 10
data = get_input(DATE)

cost = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

L = '([{<'
R = ')]}>'
match = {}
for l, r in zip(L, R):
    match[l] = r
    match[r] = l

def check(s):
    stk = []
    for c in s:
        if c in L:
            stk.append(c)
        else:
            if match[stk[-1]] != c:
                return cost[c]
            stk.pop()
    return 0

cost = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}
def complete(s):
    stk = []
    for c in s:
        if c in L:
            stk.append(c)
        else:
            stk.pop()
    
    score = 0
    while stk:
        score = score * 5 + cost[match[stk.pop()]]
    return score

def median(m):
    scores = sorted(m)
    return scores[len(scores)//2]
    
def p1():
    return sum(map(check, data))

def p2():
    return median(map(complete, filter(lambda d: check(d)==0, data)))

print(p2())