import re

with open('../AdventofCode/2023/Day1.txt') as f:
    content = f.readlines()
sum_ofall = 0

for line in content:
    line = line.strip('\n')
    num_integers = sum(line.isdigit() for line in line)
    if num_integers == 1:
        match = re.search(r'\d', line)
        first_int = match.group()
        last_int = match.group()
    else:
        match = re.search(r'\d', line)
        first_int = match.group()
        chars = list(line)
        chars.reverse()
        for char in chars:
            if char.isdigit():
                last_int = char
                break
    def concat_ints(first_int, last_int):
        return int(str(first_int) + str(last_int))
    calibration = concat_ints(first_int, last_int)
    sum_ofall = sum_ofall + calibration
    print('Num of Int: '+str(num_integers))
    print('First Int: '+str(first_int))
    print('Last Int: '+str(last_int))
    print('Line: '+str(line))
    print('Calibration: '+str(calibration))
    print('Sum of all: '+str(sum_ofall))
    print('\n')
