
#  On  cree le fonction neccesaire  a l'operation
def calcule_surface(longeur :int, largeur :int, hauteur :int) :
    surface = 2 * longeur * largeur + 2 * largeur * hauteur + 2 * hauteur * longeur
    return surface

def petit_cote(longeur :int ,largeur :int ,hauteur :int ):
    return min(longeur *largeur ,largeur *hauteur ,hauteur *longeur)

def calcule_ruban(longeur ,largeur ):
    ruban = 2 * (longeur + largeur)
    return ruban


def calcule_noeud(longeur, largeur, hauteur) :
    noeud = longeur * largeur * hauteur
    return noeud


boxes = []
extra = []
total = 0
total_ruban = 0




with open('Puzzle_2', 'r') as enigme :
        for i ,line in  enumerate(enigme) :
            # Supprime les espaces et les sauts de ligne avant de diviser
            splited_dimension = line.strip().split('x')
            # on convertit les dimension en entier int dans  une  liste comprehension
            splited_dimension = [int(n) for n in splited_dimension]
            # on  calcule les  surface  et les  ruban  neccessaire  avec la fonction
            sorted_dimension = sorted(splited_dimension)

            surface = calcule_surface(splited_dimension[0], splited_dimension[1], splited_dimension[2])
            small_extra = petit_cote(splited_dimension[0], splited_dimension[1], splited_dimension[2])
            # ruban_extra = calcule_ruban(splited_dimension[0], splited_dimension[1])
            ruban_extra = calcule_ruban(sorted_dimension[0], sorted_dimension[1])

            noeud_extra = calcule_noeud(splited_dimension[0], splited_dimension[1], splited_dimension[2])
            print(f'Dimension {i} : {splited_dimension}')
            print(f'smallest side : {small_extra}')
            resultat = surface + small_extra
            resultat_ruban = ruban_extra + noeud_extra
            total += resultat
            total_ruban += resultat_ruban

            print(f'Surface: {surface} + {small_extra} = {resultat} ')
            print(f'Surface Ruban: {ruban_extra} + {noeud_extra} = {resultat_ruban} ')
            print()

            boxes.append(splited_dimension)
            extra.append(small_extra)

print("Boxe lenght :",len(boxes))
print()
print()
print("Reponse part 1 ")
print(f'surface total : {total}')
print()
print()
print("Reponse Part 2 ")
print(f'Surface ruban : {total_ruban}')
