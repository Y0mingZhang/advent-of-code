from aoc import get_input
import itertools
from utils import flatten

DATE = 8
data = get_input(DATE)


digit_map = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

code_set = set(digit_map.keys())


def crack(arr):
    alphabet = "abcdefg"
    for perm in itertools.permutations(alphabet):
        char_map = {c_i: c_o for c_i, c_o in zip(alphabet, perm)}

        for code in arr:
            if "".join(sorted(map(char_map.get, code))) not in code_set:
                break

        else:
            return char_map


def decode(arr, char_map):
    return [digit_map["".join(sorted(map(char_map.get, code)))] for code in arr]


decoded = []
for line in data:
    arr0, arr1 = map(str.strip, line.split("|"))
    char_map = crack(arr0.split())
    decoded.append(decode(arr1.split(), char_map))


def q1():
    return sum(1 if i in [1, 4, 7, 8] else 0 for i in flatten(decoded))


def q2():
    return sum(map(lambda a: a[0] * 1000 + a[1] * 100 + a[2] * 10 + a[3] * 1, decoded))


print(q1())
print(q2())
