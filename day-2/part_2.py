from intcode_runner import intcode_runner

input = open('input.txt').read().replace('\n', '').split(',')
program_base = list(map(lambda x: int(x), input))

for noun in range(117):
    for verb in range(117):
        program = [program_base[0]] + [noun, verb] + program_base[3:]
        result = intcode_runner(program)

        if result[0] == 19690720:
            print(100 * noun + verb)
            exit()
