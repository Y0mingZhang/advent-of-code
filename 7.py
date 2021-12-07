from aoc import get_input

DATE = 7
data = get_input(DATE)
arr = list(map(int, data[0].split(',')))
def median(arr):
    return sorted(arr)[len(arr)//2]

def p1():
    mid = median(arr)
    return sum(abs(v-mid) for v in arr)

def p2():
    def sum_to(n):
        return (n+1)*n//2

    def cost(pos):
        return sum(sum_to(abs(v-pos)) for v in arr)
    return min(map(cost, range(1500)))

print(p1())
print(p2())