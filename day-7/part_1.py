from intcode_runner import intcode_runner
import re
from itertools import permutations

program = [int(i) for i in re.findall(r'-?\d+', open('input.txt').read())]

max_signal = 0
for combinations in permutations(range(5)):
    output = 0
    for i in range(5):
        output = intcode_runner(program, [combinations[i], output])[1][-1]
    if output > max_signal:
        max_signal = output

print(max_signal)
