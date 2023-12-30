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

# def pos_char(file):
#     pos = [compteur_etage(file)]
#     return pos[-1], pos.index(-1) + 1



def floors_pos(file):
    floors = []

    for o in test:
        if o == "(":
            floors.append(1)
        else:
            floors.append(-1)
    return floors

floors = []

for s in puzzle:
    if  s == "(":
        floors.append(1)
    else:
        floors.append(-1)

print(floors)
#
# print(f'Etage avant itertool : {floors}')
# test = list(itertools.accumulate(floors))
# print(f'Etage apres itertool : {test}')
# print(f'Etage : {test[-1]}')
# print(f"Etage Final: {test[-1]}")
# print(f"la première position où le personnage atteint le sous-sol: {test.index(-1) + 1}")
#



print("---------------------reponse 1 ----------------------------------------")

print(puzzle)
print(f'Longeur du puzzle : {len(puzzle)}')
etage = compteur_etage(puzzle)
print(f'Etage monté \nResponse 1 : {etage}' )
# print(f'posi={pos}')

print("---------------------reponse 2----------------------------------------")
print(f"Longueur de Puzzle : {len(puzzle)}")
print(f'Etage avant itertool : {floors}')
position = list(itertools.accumulate(floors))
print(f'Etage apres itertool : {position}')
print(f'Etage : {position[-1]}')
print(f"Etage Final: {position[-1]}")
print(f"la première position où le personnage atteint le sous-sol: {position.index(-1) + 1}")
print(f'Reponse 2 : {position.index(-1) + 1 }')


#
# floors = floors_pos(puzzle)
# print(puzzle)
# print(f'Puzzle Avant Iteration : {floors}')
# floors = list(itertools.accumulate(floors))
# print(f'Puzzle Apres Iteration : {floors[]}')
# print(f'Etage final : {floors}')
# print(f'Premier fois a atteindre  le Sous Sol : {floors.index(-1) +1 }')
# print(f'reponse : {floors.index(-1) +1}')
# #


print()


# etage , num_down_step = num_etage(puzzle)
# print(f'Etage : {etage}')
# print(f'num down step : {num_down_step}')

