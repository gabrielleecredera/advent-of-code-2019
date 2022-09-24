input = '206938-679128'

count = 0
for number in range(int(input.split('-')[0]), int(input.split('-')[1]) + 1):
    adj_found = False
    wrong_dir = False
    for i, char in enumerate(str(number)):
        if i > 0:
            if char == str(number)[i - 1] and (i == 1 or char != str(number)[i - 2]) and (i >= len(str(number)) - 1 or char != str(number)[i + 1]):
                adj_found = True
            if int(char) < int(str(number)[i - 1]):
                wrong_dir = True
        prev_num = int(char)
    if adj_found and not wrong_dir:
        count += 1

print(count)