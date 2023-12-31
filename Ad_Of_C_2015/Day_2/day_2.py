



with open('test' ,'r' ,newline="") as enigme:
    puzzle = enigme.read()


print(puzzle)
print(len(puzzle))
dim = [puzzle.split('x')]
print(dim[0][2])

print()
boxe = []
# for line in puzzle:
#     dimensions = [int(n) for n in line.split('x')]
#     dimensions.sort()
#     boxe.append(tuple(dimensions))
#
# print(boxe)
    # print(dimension[0])
    # dim = [dimension[0]]
#     longueur,largeur,hauteur = int(dimension[0]), int(dimension[1]), int(dimension[2])
#     boxe.append((longueur,largeur,hauteur))
# print(boxe)
# #
#

# print()
# for i,o in zip(puzzle):
#     print(i , o)
#
# print(len(puzzle))