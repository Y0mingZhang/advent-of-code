#!/opt/homebrew/bin/python3

import functools
import ast
import operator as op
from collections import deque

operators = {ast.Add: op.add, ast.Mult: op.mul}


class Monkey:
    def __init__(self, spec: str):
        spec = spec.split("\n")
        self.items = deque(
            int(item.strip()) for item in spec[1].split(":")[1].split(", ")
        )
        self.expr = ast.parse(spec[2].split("=")[1].strip(), mode="eval").body
        self.div = int(spec[3].split()[-1])
        self.true = int(spec[4].split()[-1])
        self.false = int(spec[5].split()[-1])
        self.throw_count = 0

    def eval(self, node: ast.Expression, old: int) -> int:
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](
                self.eval(node.left, old), self.eval(node.right, old)
            )
        elif isinstance(node, ast.Name):
            return old
        else:
            raise Exception

    def throw(self, val: int) -> int:
        self.throw_count += 1
        return self.true if val % self.div == 0 else self.false


def part_1(data: list[str]) -> None:
    monkeys = [Monkey(spec) for spec in data]
    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                old_level = monkey.items.popleft()
                new_level = monkey.eval(monkey.expr, old_level) // 3
                monkeys[monkey.throw(new_level)].items.append(new_level)

    activity = sorted(map(lambda m: m.throw_count, monkeys), reverse=True)
    print("part 1:", activity[0] * activity[1])


def part_2(data: list[str]) -> None:
    monkeys = [Monkey(spec) for spec in data]
    common_multiplier = functools.reduce(lambda i, m: i * m.div, monkeys, 1)

    for _ in range(10000):
        for monkey in monkeys:
            while monkey.items:
                old_level = monkey.items.popleft()
                new_level = monkey.eval(monkey.expr, old_level) % common_multiplier
                monkeys[monkey.throw(new_level)].items.append(new_level)

    activity = sorted(map(lambda m: m.throw_count, monkeys), reverse=True)
    print("part 2:", activity[0] * activity[1])


if __name__ == "__main__":
    with open("data/11.in") as f:
        data = f.read().split("\n\n")
    part_1(data)
    part_2(data)
