def calcule_surface(longeur:int, largeur:int, hauteur:int) :
    surface = 2 * longeur * largeur + 2 * largeur * hauteur + 2 * hauteur * longeur
    return surface

def calcule_ruban(longeur,largeur):
    ruban = longeur + longeur + largeur +largeur
    return ruban

def calcule_noeud(longeur,largeur,hauteur):
    noeud = longeur * largeur * hauteur
    return noeud


def petit_cote(longeur:int,largeur:int,hauteur:int):
    return min(longeur*largeur,largeur*hauteur,hauteur*longeur)


# def tri(longeur:int,largeur:int,hauteur:int):
#     return sorted(longeur,largeur,hauteur)
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
total_ruban = 0
with open('test.txt', 'r') as file :
    test_puzzle = file

    for line in test_puzzle:
        splited_dimension = line.strip().split('x')
        splited_dimension = [int(n) for n in splited_dimension]
        sorted_diimension = sorted(splited_dimension)
        surface = calcule_surface(splited_dimension[0],splited_dimension[1],splited_dimension[2])
        ptit_extra = petit_cote(splited_dimension[0],splited_dimension[1],splited_dimension[2])
        ruban = calcule_ruban(sorted_diimension[0], sorted_diimension[1])
        noeud = calcule_noeud(splited_dimension[0],splited_dimension[1],splited_dimension[2])
        print(splited_dimension)
        print(ptit_extra)
        resultat =  surface + ptit_extra
        resultat_ruban_extra = ruban + noeud
        total += resultat
        total_ruban += resultat_ruban_extra
        print(f'surface : {surface} + {ptit_extra} = {surface + ptit_extra} ')
        print(f'surface ruban : {ruban} + {noeud} = {ruban + noeud} ')
        boxes.append(splited_dimension)
        extra.append(ptit_extra)

        # print(splited_dimension)

# print(boxes[0])
# print(extra)
