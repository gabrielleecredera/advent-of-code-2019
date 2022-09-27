from intcode_runner import intcode_runner
import re

program = [int(i) for i in re.findall(r'-?\d+', open('input.txt').read())]
print(intcode_runner(program, [1])[1][0])
print(intcode_runner(program, [2])[1][0])
