

with open('brouillon' ,'r') as file :
    puzz = file.read().strip().split('\n')


# print(puzz)
game_part = []
for e in puzz:
    part= e.split(';')
    part_2 = part[0].split(':')
    print(part_2)
    print(part)
    part[0] = part_2[1]
    print(e)
    print(part)
    # print(len(part))
    # print(e)
    # print(part)
    # print(len(part))