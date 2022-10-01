# THIS DOESN'T WORK, NEED TO SEPARATE THE X, Y, Z PANES TO MAKE IT GO ZOOM ZOOM




import re
from itertools import combinations, count

original_pos = re.findall(r'x=(-?\d+), y=(-?\d+), z=(-?\d+)', open('input.txt').read())
moons = [[list([int(i) for i in pos]), [0, 0, 0]] for pos in original_pos]
states = []

for j in count():
    state = str(moons)
    if state in states:
        print(j)
        break

    for moon_a, moon_b in combinations(enumerate(moons), 2):
        for i in range(3):
            if moon_a[1][0][i] > moon_b[1][0][i]:
                moon_a[1][1][i] -= 1
                moon_b[1][1][i] += 1
            elif moon_a[1][0][i] < moon_b[1][0][i]:
                moon_a[1][1][i] += 1
                moon_b[1][1][i] -= 1

    for moon in moons:
        for i in range(3):
            moon[0][i] += moon[1][i]

    states.append(state)
