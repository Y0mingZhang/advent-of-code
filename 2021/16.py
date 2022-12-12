from aoc import get_input
from operator import add, mul, gt, lt, eq
import functools
DATE = 16
data = get_input(DATE)

def binary(data):
    b = bin(int(data, 16))[2:]
    while len(b) % 4 != 0:
        b = '0' + b
    return b

class Packet:
    def __init__(self, ver, type, data=None, subpackets=[]):
        self.ver = ver
        self.type = type
        self.data = data
        self.subpackets = subpackets

    def __repr__(self):
        if self.data == None:
            return str(self.subpackets)
        return str(self.data)

    @property
    def is_literal(self):
        return self.data != None
    
    @property
    def is_operator(self):
        return not self.is_literal
    
    @classmethod
    def as_literal(cls, ver, type, data):
        return cls(ver, type, data=data)
    
    @classmethod
    def as_operator(cls, ver, type, subpackets):
        return cls(ver, type, subpackets=subpackets)


def read_packet(data, offset):
    ver = int(data[offset:offset+3], 2)
    type = int(data[offset+3:offset+6], 2)
    if type == 4:
        literal = ''
        for pos in range(offset+6, len(data), 5):
            literal += data[pos+1:pos+5]
            if data[pos] == '0':
                break
        literal = int(literal, 2)
        return Packet.as_literal(ver, type, literal), pos+5
    
    else:
        bit = data[offset+6]
        if bit == '0':
            length = int(data[offset+7:offset+22], 2)
            subpackets = []
            subpacket_offset = offset+22
            while subpacket_offset < offset + 22 + length:
                subpacket, subpacket_offset = read_packet(data, subpacket_offset)
                subpackets.append(subpacket)
        else:
            count = int(data[offset+7:offset+18], 2)
            subpackets = []
            subpacket_offset = offset+18
            for _ in range(count):
                subpacket, subpacket_offset = read_packet(data, subpacket_offset)
                subpackets.append(subpacket)
        
        return Packet.as_operator(ver, type, subpackets), subpacket_offset
            


packet, _ = read_packet(binary(data[0]), 0)


def ver_sum(packet):
    if packet.is_literal:
        return packet.ver
    return packet.ver + sum(map(ver_sum, packet.subpackets))

reduce_ops = {
    0: add,
    1: mul,
    2: min,
    3: max
}

binary_ops = {
    5: gt,
    6: lt,
    7: eq
}

def eval(packet):
    if packet.is_literal:
        return packet.data
    
    elif packet.type in reduce_ops:
        op = reduce_ops[packet.type]
        return functools.reduce(op, map(eval, packet.subpackets))
    
    else:
        op = binary_ops[packet.type]
        return 1 if op(eval(packet.subpackets[0]), eval(packet.subpackets[1])) else 0

    
print(ver_sum(packet))
print(eval(packet))

