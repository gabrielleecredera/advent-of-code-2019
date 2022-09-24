import re
import math

inputs = re.findall('(\d+)\n', open('input.txt').read())
print(sum([math.floor(int(input) / 3) - 2 for input in inputs]))

total_fuel = 0
for input in inputs:
    sum_fuel = 0
    new_mass = int(input)
    while True:
        new_fuel = math.floor(new_mass / 3) - 2
        if new_fuel <= 0:
            break
        new_mass = new_fuel
        sum_fuel += new_fuel
    total_fuel += sum_fuel
print(total_fuel)
