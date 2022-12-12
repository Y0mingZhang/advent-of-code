from aoc import get_input

DATE = 1
data = get_input(DATE)

numbers = list(map(int, data))


def window(numbers, k):
    return [sum(numbers[i : i + k]) for i in range(len(numbers) - k + 1)]


def increase_count(arr):
    return sum(bool(a < b) for a, b in zip(arr, arr[1:]))


print("p1", increase_count(window(numbers, 1)))
print("p2", increase_count(window(numbers, 3)))
