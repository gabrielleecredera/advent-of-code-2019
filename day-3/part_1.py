import re

instructions = [re.findall(r'(.)(\d+)', line) for line in open('input.txt').read().splitlines()]
directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

pts = {(0, 0)}

x = 0
y = 0
for line in instructions[0]:
    for i in range(int(line[1])):
        x += directions[line[0]][0]
        y += directions[line[0]][1]
        pts.add((x, y))

closest_dist = 999999

x = 0
y = 0
for line in instructions[1]:
    for i in range(int(line[1])):
        x += directions[line[0]][0]
        y += directions[line[0]][1]
        if (x, y) in pts and abs(x) + abs(y) < closest_dist:
            closest_dist = abs(x) + abs(y)

print(closest_dist)
