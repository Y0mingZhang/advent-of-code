import itertools
import functools
from aoc import get_input
from utils import flatten
from tqdm import tqdm

DATE = 22
data = get_input(DATE)


def parse(line):
    mode = True if line.startswith("on") else False

    def parse_field(s):
        s = s.split("=")[1]
        return tuple(map(int, s.split("..")))

    x, y, z = map(parse_field, line.split(","))

    return mode, x, y, z


steps = [parse(row) for row in data]


class Cuboid:
    def __init__(self, x0, x1, y0, y1, z0, z1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1

    def __repr__(self):
        if self.proper:
            return f"({self.x0}, {self.x1}), ({self.y0}, {self.y1}), ({self.z0}, {self.z1}) Volume: {self.volume}"
        else:
            return "EMPTY"

    @functools.cached_property
    def volume(self):
        if not self.proper:
            return 0
        return (
            (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1)
        )

    @functools.cached_property
    def proper(self):
        return self.x1 >= self.x0 and self.y1 >= self.y0 and self.z1 >= self.z0

    def intersection(self, other):
        return Cuboid(
            max(self.x0, other.x0),
            min(self.x1, other.x1),
            max(self.y0, other.y0),
            min(self.y1, other.y1),
            max(self.z0, other.z0),
            min(self.z1, other.z1),
        )

    def minus(self, other):
        common = self.intersection(other)
        if not common.proper:
            return [self]

        left = Cuboid(
            self.x0,
            common.x0 - 1,
            self.y0,
            self.y1,
            self.z0,
            self.z1,
        )
        right = Cuboid(
            common.x1 + 1,
            self.x1,
            self.y0,
            self.y1,
            self.z0,
            self.z1,
        )
        up = Cuboid(common.x0, common.x1, self.y0, self.y1, common.z1 + 1, self.z1)
        down = Cuboid(common.x0, common.x1, self.y0, self.y1, self.z0, common.z0 - 1)
        front = Cuboid(
            common.x0, common.x1, self.y0, common.y0 - 1, common.z0, common.z1
        )
        back = Cuboid(
            common.x0, common.x1, common.y1 + 1, self.y1, common.z0, common.z1
        )

        rem = [left, right, up, down, front, back]
        return [c for c in rem if c.proper]


def p1():
    cubes = {
        (x, y, z): False
        for x, y, z in itertools.product(range(-50, 51), range(-50, 51), range(-50, 51))
    }

    for mode, xrange, yrange, zrange in steps:
        for x in range(max(xrange[0], -50), min(xrange[1] + 1, 51)):
            for y in range(max(yrange[0], -50), min(yrange[1] + 1, 51)):
                for z in range(max(zrange[0], -50), min(zrange[1] + 1, 51)):
                    cubes[(x, y, z)] = mode

    print(sum(cubes.values()))


def p2():
    cuboids = []
    for (mode, x, y, z) in tqdm(steps):
        if mode:
            curr_cuboids = [Cuboid(*x, *y, *z)]
            for cuboid in cuboids:
                curr_cuboids = list(
                    flatten(map(lambda c: c.minus(cuboid), curr_cuboids))
                )
            cuboids.extend(curr_cuboids)
        else:
            cuboids = list(flatten(map(lambda c: c.minus(Cuboid(*x, *y, *z)), cuboids)))

    total_volume = sum(c.volume for c in cuboids)
    print(total_volume)


p1()
p2()
