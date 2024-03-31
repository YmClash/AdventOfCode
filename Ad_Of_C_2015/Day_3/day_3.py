def move(direction:str):
    if direction == '^' :
        print("NORD")
        return
    elif direction == 'v' :
        print('SUD')
        return
    elif direction =='>':
        print('EST')
        return
    elif direction == '<' :
        print('Ouest')
        return
    else:
        raise ValueError('invalid direction')


def santa_move(direction:str,position:list):
    if direction == '^' :
        return (position[0], position[1] + 1)
    elif direction == 'v' :
        return (position[0], position[1] -1 )
    elif direction =='>':
        return (position[0] +1,position[1])
    elif direction == '<' :
        return (position[0]-1,position[1])
    else:
        raise ValueError('invalid direction '
                         '')


with open('Puzzle_3','r' ,encoding='utf-8') as file:
    puzzle = file.read()

    for i in puzzle:
        print(i,move(i))