from aoc import get_input
DATE = 3
data = get_input(DATE)

numbers = data[:]

def ox_crit(arr, bit):
    zeros = [i for i in arr if i[bit] == '0']
    ones = [i for i in arr if i[bit] == '1']
    if len(ones) >= len(zeros):
        return ones
    return zeros

def co2_crit(arr, bit):
    zeros = [i for i in arr if i[bit] == '0']
    ones = [i for i in arr if i[bit] == '1']
    if len(zeros) <= len(ones):
        return zeros
    return ones

def find_value(arr, filter_crit):
    bit = 0
    while len(arr) > 1:
        arr = filter_crit(arr, bit)
        bit += 1
    return int(arr[0], 2)


ox = find_value(numbers, ox_crit)
co2 = find_value(numbers, co2_crit)

print(ox * co2)