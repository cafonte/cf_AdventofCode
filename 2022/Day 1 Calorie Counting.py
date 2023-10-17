
import pandas as pd

elves = []

with open('/Users//Documents/AdventofCode/2022/Q1.txt') as f:
    content = f.readlines()
elve_count = 0
elve_name = ('Elve' + str(elve_count))

for line in content:
    line = line.strip()
    if line == '':
        elve_count += 1
        #elve_name = ('Elve' + str(elve_count))
        #elves[elve_name] = ''
    else:
        elve_name = ('Elve'+str(elve_count))
        elves.append({elve_name:int(line)})

df = pd.DataFrame(elves)
df = df.fillna(0)
print(str(elve_count))
print(elves)
print(df)
totals = df.sum()
sorted_totals = totals.sort_values(ascending=False)
print(sorted_totals)
