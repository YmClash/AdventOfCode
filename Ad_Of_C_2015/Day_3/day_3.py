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
        raise ValueError('invalid direction')

def count_maison(directions):
    houses = {}
    position  = (0,0)
    houses[position] = 1
    for direction in directions:
        position = santa_move(direction,position)
        if position in houses:
            houses[position] += 1
        else:
            houses[position] = 1
    return  len(houses)









with open('Puzzle_3','r' ,encoding='utf-8') as file:
    puzzle = file.read()
    for o in puzzle:
        print(move(o))
    reponse = count_maison(puzzle)
    print(f"Reponse part 1 : {reponse} ")