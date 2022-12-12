from aoc import get_input

DATE = 6
data = get_input(DATE)

state = [0] * 9
for val in map(int, data[0].split(',')):
    state[val] += 1

def q2():
    curr_state = state

    for iter in range(256):
        next_state = curr_state[1:] + [curr_state[0]]
        next_state[6] += curr_state[0]
        curr_state = next_state
    return sum(curr_state)

print(q2())

    
    