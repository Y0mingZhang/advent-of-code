from collections import Counter
from aoc import get_input

DATE = 19
data = get_input(DATE)

scanners = []
points = []

for line in data:
    if not line:
        scanners.append(points)
        points = []
    try:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))
    except:
        continue

scanners.append(points)


def cross_product(u, v):
    return [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    ]


def transform(v1, v2):
    v3 = cross_product(v1, v2)

    v_arr = [v1, v2, v3]

    def func(v):
        res = [0, 0, 0]
        for i in range(3):
            for j in range(3):
                if v_arr[j][i] != 0:
                    res[i] = v[j] * v_arr[j][i]
        return tuple(res)

    return func


def all_transforms():
    Ts = []
    for a0 in range(3):
        for sign in (-1, 1):
            v0 = [0, 0, 0]
            v0[a0] = sign
            for a1 in range(3):
                if a0 == a1:
                    continue
                for sign in (-1, 1):
                    v1 = [0, 0, 0]
                    v1[a1] = sign
                    Ts.append(transform(v0, v1))

    return Ts


Ts = all_transforms()


def match_sets(s1, s2):
    for t in Ts:
        s2_T = [t(p) for p in s2]
        diffs = Counter()
        for a in s1:
            for b in s2_T:
                diffs[(a[0] - b[0], a[1] - b[1], a[2] - b[2])] += 1
        for k, v in diffs.items():
            if v >= 12:
                return t, k
    return None


def merge():
    merged = [True] + [False] * (len(scanners) - 1)
    diffs = [(0, 0, 0)] * len(scanners)
    merged_points = set(scanners[0])

    for _ in range(len(scanners) - 1):
        for i in range(len(scanners)):
            if not merged[i]:
                match = match_sets(merged_points, scanners[i])
                if match != None:
                    transform, diff = match
                    diffs[i] = diff
                    for point in scanners[i]:
                        x, y, z = transform(point)
                        dx, dy, dz = diff
                        merged_points.add((x + dx, y + dy, z + dz))
                    merged[i] = True
                    print("Merged", i)
                    break

    print("distinct points", len(merged_points))
    print(
        "max manhattan distance",
        max(
            abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
            for a in diffs
            for b in diffs
        ),
    )


merge()
