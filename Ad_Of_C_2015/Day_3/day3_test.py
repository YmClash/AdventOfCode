
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
        print("NORD")
        return (position[0], position[1] + 1)
    elif direction == 'v' :
        print('SUD')
        return (position[0], position[1] -1 )
    elif direction =='>':
        print('EST')
        return (position[0] +1,position[1])
    elif direction == '<' :
        print('Ouest')
        return (position[0]-1,position[1])
    else:
        raise ValueError('invalid direction')




with open('input.txt','r') as file:
    enigme = file.read()

    for i in enigme:
        move = move(i)
        print(move)


    # print(enigme)