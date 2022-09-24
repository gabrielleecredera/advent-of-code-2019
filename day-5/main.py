from intcode_runner import intcode_runner
import re

input = [int(i) for i in re.findall('-?\d+', open('input.txt').read())]
intcode_runner(input)