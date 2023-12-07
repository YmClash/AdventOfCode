

with open('Puzzle_2' ,'r') as file :
    puzz = file.read().strip().split('\n')


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

COLOR = ['red','green','blue']

# print(puzz)
game_part = []
for e in puzz:
    part= e.split(';')
    part_2 = part[0].strip().split(':')
    # print(part_2)
    # print(part)       la  je  decoupe,recoupe tout les mots   et les ajoute  dans une liste
    part[0] = part_2[1]
    print(e)
    # print(f'{part_2[0]}{part} ')
    print(f'Game Part: {part}')
    print(f'Number of set : {len(part)}')
    for o in part:
        series = {}
        cubes = o.split(',')
        print(cubes)
        for c in cubes:
            numb,color = c.strip().split(' ')
            series[color] =int(numb)
            print(color)
            print(numb)

    # game_part.append(part)
    # print(game_part)

    # print(len(part))
    # print(e)
    # print(part)
    # print(len(part))