from aoc import get_input
import functools
from copy import deepcopy
DATE = 18
data = get_input(DATE)

class Node:
    
    def __init__(self, data, parent=None):
        self.parent = parent
        self.left = self.right = None

        if isinstance(data, list):
            assert(len(data) == 2)
            self.data = None
            self.left = Node(data[0], parent=self)
            self.right = Node(data[1], parent=self)
        elif isinstance(data, Node):
            self.data = data.data
            self.left = data.left
            self.left.parent = self
            self.right = data.right
            self.right.parent = self
        else:
            self.data = data
    
    @property
    def is_pair(self):
        return self.data == None
    
    @property
    def is_number(self):
        return not self.is_pair

    @property
    def is_simple_pair(self):
        return self.is_pair and self.left.is_number and self.right.is_number

    @property
    def depth(self):
        if self.parent == None:
            return 0
        return self.parent.depth + 1
    
    def __repr__(self):
        if self.is_pair:
            return f"[{self.left}, {self.right}]"
        return f"{self.data}"

    def __iter__(self):
        yield self
        if self.left != None:
            yield from self.left
        if self.right != None:
            yield from self.right

    def magnitude(self):
        if self.is_number:
            return self.data
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    

    

nodes = []
for row in data:
    nodes.append(Node(eval(row), parent=None))

def explode(n):
    nodes = list(n)
    for i, node in enumerate(nodes):
        if node.depth >= 4 and node.is_simple_pair:
            break
    else:
        return False
    
    l, r = node.left, node.right

    j = i
    while j >= 0:
        if nodes[j].is_number:
            nodes[j].data += l.data
            break
        j -= 1
    
    j = i + 3
    while j < len(nodes):
        if nodes[j].is_number:
            nodes[j].data += r.data
            break
        j += 1
    
    node.data = 0
    node.left = node.right = None

    return True

def split(n):
    for node in n:
        if node.is_number and node.data >= 10:
            down = node.data // 2
            up = down if node.data % 2 == 0 else down + 1
            node.left = Node(down, parent=node)
            node.right = Node(up, parent=node)
            node.data = None
            return True
    return False


def add(n1, n2):
    return reduce(Node([deepcopy(n1), deepcopy(n2)]))

def reduce(number):
    while explode(number) or split(number):
        pass
    return number

def p1():
    res = functools.reduce(add, nodes)
    return res.magnitude()

def p2():
    max_magnitude = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            sum_0 = add(nodes[i], nodes[j])
            sum_1 = add(nodes[j], nodes[i])
            max_magnitude = max(max_magnitude, sum_0.magnitude(), sum_1.magnitude())
    return max_magnitude

print(p1())
print(p2())