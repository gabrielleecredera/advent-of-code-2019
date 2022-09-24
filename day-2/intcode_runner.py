# writen as days go by, solutions for earlier days might be broken as this method changes
def intcode_runner(program):
    program = program[:]
    index = 0
    while True:
        if program[index] == 99:
            return program

        val1 = program[program[index + 1]]
        val2 = program[program[index + 2]]
        targetPos = program[index + 3]

        if program[index] == 1:
            program[targetPos] = val1 + val2
        elif program[index] == 2:
            program[targetPos] = val1 * val2

        index += 4
        if index >= len(program):
            print('unexpected end')
            raise
