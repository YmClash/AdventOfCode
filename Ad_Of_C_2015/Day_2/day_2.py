
def calcule_surface(longeur:int, largeur:int, hauteur:int) :
    surface = 2 * longeur * largeur + 2 * largeur * hauteur + 2 * hauteur * longeur
    return surface

def petit_cote(longeur:int,largeur:int,hauteur:int):
    return min(longeur*largeur,largeur*hauteur,hauteur*longeur)

boxes = []
extra = []
total = 0
with open('Puzzle_2', 'r') as enigme:

    for line in enigme:
        print(line.strip()) # affiche chacun ligne contenant le note dimension ( affiche sans e
        splited_dimension = line.strip().split('x') # Supprime les espaces et les sauts de ligne avant de diviser
        splited_dimension =[int(n) for n in splited_dimension] # on convertit les dimension en entier int
        surface = calcule_surface(splited_dimension[0],splited_dimension[1],splited_dimension[2]) # on  calcule la surface
        small_extra = petit_cote(splited_dimension[0],splited_dimension[1],splited_dimension[2])
        print(splited_dimension)
        print(small_extra)
        resultat = surface + small_extra
        total += resultat
        print(f'Surface: {surface} + {small_extra} = {resultat} ')
        boxes.append(splited_dimension)
        extra.append(small_extra)




print("Reponse part 1 ")
print(f'surface total : {total}')

