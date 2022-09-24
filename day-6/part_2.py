import re

input = re.findall(r'(.+)\)(.+)', open('input.txt').read())

orbits = {}
for orbit in input:
    orbits[orbit[1]] = orbit[0]

dist_from_you = {}
active_planet = orbits['YOU']
dist = 0
while True:
    if active_planet not in orbits:
        break
    parent = orbits[active_planet]
    dist_from_you[active_planet] = dist
    active_planet = parent
    dist += 1

dist_from_san = {}
active_planet = orbits['SAN']
dist = 0
while True:
    if active_planet not in orbits:
        break
    parent = orbits[active_planet]
    dist_from_san[active_planet] = dist
    active_planet = parent
    dist += 1

min_transfer = 99999
for planet in dist_from_you:
    if planet in dist_from_san and dist_from_you[planet] + dist_from_san[planet] < min_transfer:
        min_transfer = dist_from_you[planet] + dist_from_san[planet]
print(min_transfer)

# print(sum([x[1] for x in orbit_counts.values()]))
