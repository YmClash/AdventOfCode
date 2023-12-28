import itertools


with open('Puzzle_1','r') as enigme :
    puzzle = enigme.read()

def compteur_etage(file):
    etage= 0
    for i in puzzle:
        if i == "(":
            etage += 1
        else:
            etage -= 1
    return etage

def pos_char(file):
    pos = [compteur_etage(file)]
    return pos[-1], pos.index(-1) + 1


test = "()())"
floors = []
for o in test:
    if o == "(":
        floors.append(1)
    else:
        floors.append(-1)

print(floors)
floors = list(itertools.accumulate(floors))
print(floors)
print(f'Floors : {floors[-1]}')
print(f"Final floor: {floors[-1]}")
print(f"First position reaching basement: {floors.index(-1) + 1}")


pos = compteur_etage(test)




etage = compteur_etage(puzzle)
posi = etage
print(f'Reponse 1 : etage monté : {etage}' )
# print(f'posi={pos}')

print(len(puzzle))
print(puzzle)



# etage , num_down_step = num_etage(puzzle)
# print(f'Etage : {etage}')
# print(f'num down step : {num_down_step}')

