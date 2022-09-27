import math

asteroid_map = open('input.txt').read().splitlines()

max_detected = 0
max_pos = None
max_asteroids = {}
for x in range(len(asteroid_map[0])):
    for y in range(len(asteroid_map)):
        asteroids = {}
        if asteroid_map[y][x] == '.':
            continue

        for alt_x in range(len(asteroid_map[0])):
            for alt_y in range(len(asteroid_map)):
                if alt_x == x and alt_y == y:
                    continue
                if asteroid_map[alt_y][alt_x] == '.':
                    continue
                asteroids[(alt_x, alt_y)] = ((math.degrees(math.atan2((alt_y - y), (alt_x - x))) + 90) % 360, abs(alt_y - y) + abs(alt_x - x))

        unique_angles = len(set([i for i, _ in asteroids.values()]))
        if unique_angles > max_detected:
            max_pos = (x, y)
            max_detected = unique_angles
            max_asteroids = asteroids

print(max_detected)
sorted_asteroids = sorted(max_asteroids.items(), key=lambda x: x[1][0] * 1000 + x[1][1])

last_angle = -1
for i in range(200):
    for asteroid in sorted_asteroids:
        angle = asteroid[1][0]
        if asteroid[1][0] > last_angle:
            if i == 199:
                print(asteroid[0][0] * 100 + asteroid[0][1])
            last_angle = asteroid[1][0]
            sorted_asteroids.pop(0)
            break
