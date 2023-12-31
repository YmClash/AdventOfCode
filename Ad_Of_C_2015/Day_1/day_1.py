import itertools

with open('Puzzle_1', 'r') as enigme:
    puzzle = enigme.read()


def compteur_etage(file):
    etage = 0
    for i in file :
        if i == "(" :
            etage += 1
        else :
            etage -= 1
    return etage


# def pos_char(file):
#     pos = [compteur_etage(file)]
#     return pos[-1], pos.index(-1) + 1

def position_etage(file):
    floors = []

    for o in file:
        if o == "(":
            floors.append(1)
        else :
            floors.append(-1)
    return floors

# test
pos_etage = []

for s in puzzle:
    if s == "(":
        pos_etage.append(1)
    else :
        pos_etage.append(-1)

print(pos_etage)
#
# print(f'Etage avant itertool : {floors}')
# test = list(itertools.accumulate(floors))
# print(f'Etage apres itertool : {test}')
# print(f'Etage : {test[-1]}')
# print(f"Etage Final: {test[-1]}")
# print(f"la première position où le personnage atteint le sous-sol: {test.index(-1) + 1}")
#
print("---------------------Advent of code 2015--Day 1--------------------------------------")
print()
print(puzzle)
print()
print("---------------------reponse 1 ----------------------------------------")

etage = compteur_etage(puzzle)

print(f'Longeur du puzzle : {len(puzzle)}')
print(f'Etage monté \nResponse 1 : {etage}')
# print(f'posi={pos}')

print("---------------------reponse 2----------------------------------------")

floors = position_etage(puzzle)
print(floors)
print(f'Puzzle Avant Iteration : {floors}')
floors = list(itertools.accumulate(floors))
print(f'Puzzle Apres Iteration : {floors}')
print(f'Etage final : {floors[-1]}')
print(f'Premier fois a atteindre  le Sous Sol : {floors.index(-1) + 1}')
print(f'reponse 2 : {floors.index(-1) + 1}')

print("---------------------Test Zone--------------------------------------")

#

# #

print(f"Longueur de Puzzle : {len(puzzle)}")
print(f'Etage avant itertool : {pos_etage}')
position = list(itertools.accumulate(pos_etage))
print(f'Etage apres itertool : {position}')
print(f'Etage : {position[-1]}')
print(f"Etage Final: {position[-1]}")
print(f"la première position où le personnage atteint le sous-sol: {position.index(-1) + 1}")
print(f'Reponse 2 : {position.index(-1) + 1}')
print()

# etage , num_down_step = num_etage(puzzle)
# print(f'Etage : {etage}')
# print(f'num down step : {num_down_step}')
