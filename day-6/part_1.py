import re

orbits = re.findall(r'(.+)\)(.+)', open('input.txt').read())

orbit_counts = {}
for orbit in orbits:
    orbit_counts[orbit[1]] = (orbit[0], 1)

for val in orbit_counts.values():
    active_planet = val[0]
    while True:
        if active_planet not in orbit_counts:
            break
        parent = orbit_counts[active_planet]
        orbit_counts[active_planet] = (parent[0], parent[1] + 1)
        active_planet = parent[0]

print(sum([x[1] for x in orbit_counts.values()]))
