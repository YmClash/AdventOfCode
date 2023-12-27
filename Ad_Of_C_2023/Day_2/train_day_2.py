import sys



red_count = 12
green_count = 13
blue_count = 14

def game_line_parser(game_line) :
    game_parts = game_line.split(';')
    game_series = []
    for part in game_parts :
        series = {}
        cubes = part.split(',')
        print(series)
        for cube in cubes :
            parts = cube.strip().split()
            print(parts)
            if len(parts) == 2 :
                number,color = parts
                series[color] = int(number)
                print(f'{number} {color}')
            game_series.append(series)
        print(game_series)
        return game_series


games = {}

# with open('brouillon' ,'r') as file :
#     # puz = file.read().strip().split('\n')
#     for idx, line in enumerate(file,start=1):
#         games[idx] = game_line_parser(line.strip())

"""
print(puz)
print(len(puz))
part = puz[0].split(':')
print(part)
print(len(part))
puz[0] = part[1]

print(f'Game Part :{puz}')
print(len(puz))
print()

"""
# print()
# for i in puz:
#     print(i)



def possible(game,bag_contents):
    for series in game:
        for color,number in series.items():
            if number > bag_contents.get(color,0):
                print("impossible")
                return False


        print("Possible ")
        return True



bag_contents = {'red':12,'green':13,'blue': 14}


# with open('brouillon' ,'r') as file :
#     for idx, line in enumerate(file,start=1):
#         games[idx] = game_line_parser(line.strip())


possible_game = [game_id for game_id, game in games.items()]

print(f'Jeux Possible : {possible_game}')
print(f'Somme des IDs : {sum(possible_game)}')



    #
    #     count, color = w.strip().split(" ")
    #     count = int(count)
    #     if count > MaxV[color[0]]:
    #         return False
    # return True
    #
#
#
# MAX_RED = 12
# MAX_BLUE = 13
# MAX_GREEN = 14
#
# MaxV = {
#     "r":"12",
#     "b":"13",
#     "g":"14"
# # }

#
# sum = 0
#
# for line in puz:
#
#     print(line)
#
#     line = line.strip()
#     game,x = line.split(':')
#     game = int(game[5:])
#     resultat = all([possible(k.strip()) for k in  x.split(";")])
#     sum = sum + (game if resultat else 0 )
#     print(sum)
#
#
#
#
#
#
#
#
#
#
# #
# # def total_Sol(puzzle):
#     total = 0
#     for line in puzzle:
#     l ,w,h = [int(i) for i in line.split('x')]
#     rib = 2 * min()
#
#


#
# for i in puz :
#     print(i)
