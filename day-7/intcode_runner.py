# writen as days go by, solutions for earlier days might be broken as this method changes
def get_val(program, param, mode):
    if mode == 0:
        return program[param]
    elif mode == 1:
        return param
    else:
        print('unexpected mode: {}'.format(mode))
        raise


def intcode_runner(program, inputs=None, pointer=0, return_on_output=False):
    if inputs is None:
        inputs = []
    program = program[:]
    outputs = []
    input_pointer = 0
    while True:
        if pointer >= len(program):
            print('unexpected end')
            raise

        operation = str(program[pointer])
        opcode = int(operation[-2:])
        # 0 for position, 1 for immediate
        mode_1 = int(operation[-3]) if len(operation) >= 3 else 0
        mode_2 = int(operation[-4]) if len(operation) >= 4 else 0
        mode_3 = int(operation[-5]) if len(operation) >= 5 else 0

        # print('opcode: {}, modes: {} {} {}'.format(opcode, mode_1, mode_2, mode_3))

        if opcode == 1:
            val1 = get_val(program, program[pointer + 1], mode_1)
            val2 = get_val(program, program[pointer + 2], mode_2)
            program[program[pointer + 3]] = val1 + val2
            pointer += 4
        elif opcode == 2:
            val1 = get_val(program, program[pointer + 1], mode_1)
            val2 = get_val(program, program[pointer + 2], mode_2)
            program[program[pointer + 3]] = val1 * val2
            pointer += 4
        elif opcode == 3:
            try:
                val = inputs[input_pointer]
            except IndexError:
                val = input('input: ')
            program[program[pointer + 1]] = int(val)
            pointer += 2
            input_pointer += 1
        elif opcode == 4:
            output = get_val(program, program[pointer + 1], mode_1)
            # print('output: {}'.format(output))
            outputs.append(output)
            pointer += 2
            if return_on_output:
                return [False, output, program, pointer, input_pointer]
        elif opcode == 5:
            if get_val(program, program[pointer + 1], mode_1) != 0:
                pointer = get_val(program, program[pointer + 2], mode_2)
            else:
                pointer += 3
        elif opcode == 6:
            if get_val(program, program[pointer + 1], mode_1) == 0:
                pointer = get_val(program, program[pointer + 2], mode_2)
            else:
                pointer += 3
        elif opcode == 7:
            program[program[pointer + 3]] = int(
                get_val(program, program[pointer + 1], mode_1) < get_val(program, program[pointer + 2], mode_2))
            pointer += 4
        elif opcode == 8:
            program[program[pointer + 3]] = int(
                get_val(program, program[pointer + 1], mode_1) == get_val(program, program[pointer + 2], mode_2))
            pointer += 4
        elif opcode == 99:
            # print('end')
            return [True, outputs]
        else:
            print('unexpected opcode: {}'.format(opcode))
            raise

        # print(program)
