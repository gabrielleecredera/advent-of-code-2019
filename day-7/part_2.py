from intcode_runner import intcode_runner
import re
from itertools import permutations, cycle

program = [int(i) for i in re.findall(r'-?\d+', open('input.txt').read())]

max_signal = 0
for combinations in permutations(range(5, 10)):
    output = 0
    states = {}
    for i in cycle(range(5)):
        if i in states:
            result = intcode_runner(states[i][0], [output], states[i][1], True)
        else:
            result = intcode_runner(program, [combinations[i], output], return_on_output=True)

        if result[0]:
            break
        else:
            output = result[1]
            states[i] = result[2:]
    if output > max_signal:
        max_signal = output

print(max_signal)
