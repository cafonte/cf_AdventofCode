

# A for Rock, B for Paper, C for Scissors
# X for Rock, Y for Paper, Z for Scissors
# Paper Covers Rock, Rock Breaks Scissors, Scissors Cuts Paper

Elve_Score = 0
My_Score = 0

with open('/Users/fonteca/Documents/AdventofCode/2022/Day2.txt') as f:
    content = f.readlines()

for line in content:
    elve = line[0].strip()
    player = line[2].strip()
    #print('Elve: '+elve)
    #print('Player: ' + player)

    if elve == 'A': # Rock
        if player == 'X': # Rock
            Elve_Score += 4
            My_Score += 4
        elif player == 'Y': # Paper
            Elve_Score += 1
            My_Score += 8
        elif player == 'Z': # Scissors
            Elve_Score += 7
            My_Score += 3
    elif elve == 'B': # Paper
        if player == 'X':
            Elve_Score += 8
            My_Score += 1
        elif player == 'Y':
            Elve_Score += 5
            My_Score += 5
        elif player == 'Z':
            Elve_Score += 2
            My_Score += 9
    elif elve == 'C': # Scissors
        if player == 'X':
            Elve_Score += 3
            My_Score += 7
        elif player == 'Y':
            Elve_Score += 9
            My_Score += 2
        elif player == 'Z':
            Elve_Score += 6
            My_Score += 6
print('\nPart 1\n'+'Elve Score: '+str(Elve_Score)+' | '+'My Score: '+str(My_Score)+'\n')

Elve_Score = 0
My_Score = 0

for line in content:
    elve = line[0].strip()
    player = line[2].strip()

    if player == 'Z': #Win
        if elve == 'A':
            Elve_Score += 1
            My_Score += 8
        elif elve == 'B':
            Elve_Score += 2
            My_Score += 9
        elif elve == 'C':
            Elve_Score += 3
            My_Score += 7
    elif player == 'Y': #Draw
        if elve == 'A':
            Elve_Score += 4
            My_Score += 4
        elif elve == 'B':
            Elve_Score += 5
            My_Score += 5
        elif elve == 'C':
            Elve_Score += 6
            My_Score += 6
    elif player == 'X': #Lose
        if elve == 'A':
            Elve_Score += 7
            My_Score += 3
        elif elve == 'B':
            Elve_Score += 8
            My_Score += 1
        elif elve == 'C':
            Elve_Score += 9
            My_Score += 2

print('Part 2\n'+'Elve Score: '+str(Elve_Score)+' | '+'My Score: '+str(My_Score))

