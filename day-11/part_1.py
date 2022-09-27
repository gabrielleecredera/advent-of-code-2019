from intcode_runner import intcode_runner
from collections import defaultdict
import re

program = [int(i) for i in re.findall(r'-?\d+', open('input.txt').read())]

surface = defaultdict(lambda: 0)
current_pos = (0, 0)
direction = 0  # 0 - 3: up, right, bottom, left
directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

pointer = 0
relative_base = 0
while True:
    end, outputs, *rest = \
        intcode_runner(program, [surface[current_pos]], pointer, 2, relative_base)
    if end:
        print(len(surface))
        break
    program, pointer, relative_base = rest
    paint, turn = outputs
    surface[current_pos] = paint
    direction = (direction + (turn or -1)) % 4
    current_pos = (current_pos[0] + directions[direction][0], current_pos[1] + directions[direction][1])
