

with open('Puzzle_2' ,'r') as file :
    puzz = file.read().strip().split('\n')


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

SAC = {'red':'12','green':'13','blue':'14'}

# print(puzz)
game_part = []
Game_IDS = []
for e  in puzz:
    part= e.split(';')
    game_id = part[0].strip().split(':')
    # print(part_2)
    # print(part)       la  je  decoupe,recoupe tout les mots   et les ajoute  dans une liste
    part[0] = game_id[1]
    Game_IDS.append(game_id[0])
    print(e)
    # print(f'{game_id[0]}{part} ')
    print(f'Game Part: {part}')
    print(f'Number of set : {len(part)}')
    for o in part:
        series = {}
        cubes = o.split(',')
        # print(cubes)
        for c in cubes:
            numb,color = c.strip().split(' ')
            series[color] =int(numb)
            print(color)
            print(numb)
        game_part.append(series)


    # for series in game_part:
    #     for color,numb in series.items():
    #         if numb > int(SAC[color]):
    #             print("INCOMPATIBLE")
    #     print("COMPATIBLE")


print(f'GAME PART: {game_part}')
print(Game_IDS)



    # game_part.append(part)
    # print(game_part)

    # print(len(part))
    # print(e)
    # print(part)
    # print(len(part))