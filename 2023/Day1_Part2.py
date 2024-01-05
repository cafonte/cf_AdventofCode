import re

with open('.../AdventofCode/2023/Day1.txt') as f:
    content = f.readlines()
sum_ofall = 0
replacements = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
pattern = '|'.join(map(re.escape, replacements.keys()))

for line in content:
    line = line.strip('\n')
    print('Input Line: ' + str(line))
    line2 = re.sub(pattern, lambda match: replacements[match.group(0)], line) #Initial Pass
    line = re.sub(pattern, lambda match: replacements[match.group(0)], line2) #Overlap Correction
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
    print('Corrected Line: '+str(line))
    print('Calibration: '+str(calibration))
    print('Sum of all: '+str(sum_ofall))
    print('\n')
