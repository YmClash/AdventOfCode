



with open('test' ,'r') as enigme:
    puzzle = enigme.read()


print(puzzle)
boxes = []
for line in puzzle:
    print(line.strip())
    splited_dimension = line.strip().split('x')
    try:
        splited_dimension =[int(n) for n in splited_dimension]
    except ValueError:
        continue

    print(splited_dimension)
    sorted_dimension = sorted(splited_dimension)
    boxes.append(sorted_dimension)

print(boxes)



# print(len(puzzle))
# dim = [puzzle.split('x')]
# print(dim[0][2])

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