def calcule_surface(longeur:int, largeur:int, hauteur:int) :
    surface = 2 * longeur * largeur + 2 * largeur * hauteur + 2 * hauteur * longeur
    return surface

def petit_cote(longeur:int,largeur:int,hauteur:int):
    return min(longeur*largeur,largeur*hauteur,hauteur*longeur)

#
# resultat = calcule_surface(longeur=1, largeur=1, hauteur=10)
# ptit_cote = petit_cote(longeur=1,largeur=1,hauteur=10)
# print(resultat)
# print(ptit_cote)
#
# print(f'Resultat final : {resultat} + {ptit_cote} = {resultat+ptit_cote}')

print()

boxes = []
extra = []
total = 0
with open('test.txt', 'r') as file :
    test_puzzle = file

    for line in test_puzzle:
        splited_dimension = line.strip().split('x')
        splited_dimension = [int(n) for n in splited_dimension]
        surface = calcule_surface(splited_dimension[0],splited_dimension[1],splited_dimension[2])
        ptit_extra = petit_cote(splited_dimension[0],splited_dimension[1],splited_dimension[2])
        print(splited_dimension)
        print(ptit_extra)
        resultat =  surface + ptit_extra
        total += resultat
        print(f'surface : {surface} + {ptit_extra} = {surface + ptit_extra} ')
        boxes.append(splited_dimension)
        extra.append(ptit_extra)

        # print(splited_dimension)

# print(boxes)
# print(extra)