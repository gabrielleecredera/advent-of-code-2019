input = '206938-679128'

count = 0
for number in range(int(input.split('-')[0]), int(input.split('-')[1]) + 1):
    prev_num = 0
    adj_found = False
    wrong_dir = False
    for char in str(number):
        if int(char) == prev_num:
            adj_found = True
        if int(char) < prev_num:
            wrong_dir = True
        prev_num = int(char)
    if adj_found and not wrong_dir:
        count += 1

print(count)