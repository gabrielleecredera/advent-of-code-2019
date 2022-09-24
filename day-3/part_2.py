import re

instructions = [re.findall(r'(.)(\d+)', line) for line in open('input.txt').read().splitlines()]
directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

pts = dict()

x = 0
y = 0
steps = 0
for line in instructions[0]:
    for i in range(int(line[1])):
        steps += 1
        x += directions[line[0]][0]
        y += directions[line[0]][1]
        if (x, y) not in pts:
            pts[(x, y)] = steps

common_pts = dict()

x = 0
y = 0
steps = 0
for line in instructions[1]:
    for i in range(int(line[1])):
        steps += 1
        x += directions[line[0]][0]
        y += directions[line[0]][1]
        if (x, y) in pts and (x, y) not in common_pts:
            common_pts[(x, y)] = (pts[(x, y)], steps)

fewest_steps = 99999999
for pt in common_pts.values():
    if pt[0] + pt[1] < fewest_steps:
        fewest_steps = pt[0] + pt[1]

print(fewest_steps)
