from intcode_runner import intcode_runner

input = open('input.txt').read().replace('\n', '').split(',')
program = list(map(lambda x: int(x), input))

print(intcode_runner(program)[0])
