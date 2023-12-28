import itertools


with open('Puzzle_1','r') as file :
    puzzle = file.read()

etage= 0
for i in puzzle:
    if i == "(":
        etage += 1
    else:
        etage -= 1

print(f'Reponse 1 : etage monté : {etage}' )


print(len(puzzle))
print(puzzle)



# etage , num_down_step = num_etage(puzzle)
# print(f'Etage : {etage}')
# print(f'num down step : {num_down_step}')

