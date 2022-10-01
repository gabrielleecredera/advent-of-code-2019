##### DAY 2 ALSO NOT DONE ;(









from intcode_runner import intcode_runner
from itertools import count
import re


def get_val(pos):
    if surface[pos] == 0:
        return '\033[1;31m█\033[0;0m'  # red
    elif surface[pos] == 1:
        return '\033[1;34m█\033[0;0m'  # blue
    elif surface[pos] == 2:
        return '\033[1;36m█\033[0;0m'  # cyan
    elif surface[pos] == 3:
        return '\033[0;32m█\033[0;0m'  # green
    elif surface[pos] == 4:
        return '\033[95m█\033[0;0m'  # purple


program = [2, *[int(i) for i in re.findall(r'-?\d+', open('input.txt').read())][1:]]

pointer = 0
relative_base = 0
surface = {}
while True:
    state, *rest = intcode_runner(program, pointer=pointer, relative_base=relative_base, return_on_input=True)
    if state:
        break
    outputs, program, pointer, relative_base = rest
    for i in count():
        if (i + 3) * 3 >= len(outputs):
            break
        tile_ins = outputs[i * 3:(i + 3) * 3]
        surface[(tile_ins[0], tile_ins[1])] = tile_ins[2]

    print(surface)
    all_x = [i for i, _ in surface.keys()]
    all_y = [i for _, i in surface.keys()]
    for y in range(min(all_y), max(all_y)):
        for x in range(min(all_x), max(all_x)):
            print(get_val((x, y)), end='')
            print(get_val((x, y)), end='')
        print()