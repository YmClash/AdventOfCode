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


test = "((()))()())))"
floors = []
print(f'text step leng  : {len(test)}')
for o in test:
    if o == "(":
        floors.append(1)
        print(floors)
    else:
        floors.append(-1)
        print()

print(f'Etage avant itertool : {floors}')
floors = list(itertools.accumulate(floors))
print(f'Etage avant itertool : {floors}')
print(f'Etage : {floors[-1]}')
print(f"Etage Final: {floors[-1]}")
print(f"la première position où le personnage atteint le sous-sol: {floors.index(-1) + 1}")

#
# pos = compteur_etage(test)

print("---------------------reponse 1 ----------------------------------------")


etage = compteur_etage(puzzle)
posi = etage
print(f'Reponse 1 : etage monté : {etage}' )
# print(f'posi={pos}')

print(len(puzzle))
print(puzzle)



# etage , num_down_step = num_etage(puzzle)
# print(f'Etage : {etage}')
# print(f'num down step : {num_down_step}')

