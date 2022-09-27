from collections import defaultdict
# writen as days go by, solutions for earlier days might be broken as this method changes


def get_val_pos(param, mode, relative_base):
    if mode == 0:
        return param
    elif mode == 1:
        return False
    elif mode == 2:
        return param + relative_base
    else:
        print('unexpected mode: {}'.format(mode))
        raise


def get_val(program, param, mode, relative_base):
    pos = get_val_pos(param, mode, relative_base)
    if pos is False:
        return param
    else:
        return program[pos]


def intcode_runner(program, inputs=None, pointer=0, return_on_output=False, relative_base=0):
    if inputs is None:
        inputs = []
    program = defaultdict(lambda: 0, enumerate(program))
    outputs = []
    input_pointer = 0
    while True:
        if pointer >= len(program):
            print('unexpected end')
            raise

        operation = str(program[pointer])
        opcode = int(operation[-2:])
        # 0 for position, 1 for immediate, 2 for relative
        mode_1 = int(operation[-3]) if len(operation) >= 3 else 0
        mode_2 = int(operation[-4]) if len(operation) >= 4 else 0
        mode_3 = int(operation[-5]) if len(operation) >= 5 else 0

        # print('opcode: {}, modes: {} {} {}'.format(opcode, mode_1, mode_2, mode_3))

        if opcode == 1:
            val1 = get_val(program, program[pointer + 1], mode_1, relative_base)
            val2 = get_val(program, program[pointer + 2], mode_2, relative_base)
            program[get_val_pos(program[pointer + 3], mode_3, relative_base)] = val1 + val2
            pointer += 4
        elif opcode == 2:
            val1 = get_val(program, program[pointer + 1], mode_1, relative_base)
            val2 = get_val(program, program[pointer + 2], mode_2, relative_base)
            program[get_val_pos(program[pointer + 3], mode_3, relative_base)] = val1 * val2
            pointer += 4
        elif opcode == 3:
            try:
                val = inputs[input_pointer]
            except IndexError:
                val = input('input: ')
            program[get_val_pos(program[pointer + 1], mode_1, relative_base)] = int(val)
            pointer += 2
            input_pointer += 1
        elif opcode == 4:
            output = get_val(program, program[pointer + 1], mode_1, relative_base)
            print('output: {}'.format(output))
            outputs.append(output)
            pointer += 2
            if return_on_output:
                return [False, output, program, pointer, input_pointer]
        elif opcode == 5:
            if get_val(program, program[pointer + 1], mode_1, relative_base) != 0:
                pointer = get_val(program, program[pointer + 2], mode_2, relative_base)
            else:
                pointer += 3
        elif opcode == 6:
            if get_val(program, program[pointer + 1], mode_1, relative_base) == 0:
                pointer = get_val(program, program[pointer + 2], mode_2, relative_base)
            else:
                pointer += 3
        elif opcode == 7:
            program[get_val_pos(program[pointer + 3], mode_3, relative_base)] = int(
                get_val(program, program[pointer + 1], mode_1, relative_base)
                < get_val(program, program[pointer + 2], mode_2, relative_base))
            pointer += 4
        elif opcode == 8:
            program[get_val_pos(program[pointer + 3], mode_3, relative_base)] = int(
                get_val(program, program[pointer + 1], mode_1, relative_base)
                == get_val(program, program[pointer + 2], mode_2, relative_base))
            pointer += 4
        elif opcode == 9:
            relative_base += get_val(program, program[pointer + 1], mode_1, relative_base)
            pointer += 2
        elif opcode == 99:
            # print('end')
            return [True, outputs]
        else:
            print('unexpected opcode: {}'.format(opcode))
            raise

        # print(program.items())
