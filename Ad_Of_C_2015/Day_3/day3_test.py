
def move(direction):
    if direction == '^' :
        print("NORD")
    elif direction == 'v' :
        print('SUD')
    elif direction =='>':
        print('EST')

    elif direction == '<' :
        print('Ouest')

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
    print(len(enigme))

for i in enigme:
    print(move(i))


    # print(enigme)