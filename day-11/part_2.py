from intcode_runner import intcode_runner
from collections import defaultdict
import re

program = [int(i) for i in re.findall(r'-?\d+', open('input.txt').read())]

surface = defaultdict(lambda: 0, {(0, 0): 1})
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
        break
    program, pointer, relative_base = rest
    paint, turn = outputs
    surface[current_pos] = paint
    direction = (direction + (turn or -1)) % 4
    current_pos = (current_pos[0] + directions[direction][0], current_pos[1] + directions[direction][1])

all_x = [i for i, _ in surface.keys()]
all_y = [i for i, _ in surface.keys()]
for y in range(min(all_y), max(all_y) - min(all_y)):
    for x in range(min(all_x), max(all_x) - min(all_x)):
        print('#' if surface[(x, y)] else ' ', end='')
    print()