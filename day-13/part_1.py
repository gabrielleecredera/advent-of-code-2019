from intcode_runner import intcode_runner
from itertools import count
import re

program = [int(i) for i in re.findall(r'-?\d+', open('input.txt').read())]

surface = {}
_, output = intcode_runner(program)
for i in count():
    if (i + 3) * 3 >= len(output):
        break
    tile_ins = output[i * 3:(i + 3) * 3]
    surface[(tile_ins[0], tile_ins[1])] = tile_ins[2]

print(list(surface.values()).count(2))
