import itertools

def accumulate(s):
    total = 0
    for i in puzzle :
        if i == "(" :
            total += 1
        else :
            total -= 1
    return list[total]

def num_etage(s):
    etage = accumulate(s)
    return etage[-1],etage.index(-1) +1


with open('Puzzle_1','r') as file :
    puzzle = file.read()

total = 0
etage = 0
for i in puzzle:
    if i == "(":
        total += 1
    else:
        total -= 1

print(f'total de laccumulation : {total}' )


print(len(puzzle))
print(puzzle)



etage , num_down_step = num_etage(puzzle)
print(f'Etage : {etage}')
print(f'num down step : {num_down_step}')

