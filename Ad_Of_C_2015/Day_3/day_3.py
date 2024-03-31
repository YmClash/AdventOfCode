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


def count_maison_with_robot(directions) :
    santa_houses = {}
    robot_houses = {}
    santa_position = (0, 0)
    robot_position = (0, 0)
    santa_houses[santa_position] = 1
    robot_houses[robot_position] = 1


    for i , direction in enumerate(directions) :
        if i % 2 == 0:
            santa_position = santa_move(direction,santa_position)
            if santa_position in santa_houses:
                santa_houses[santa_position] += 1
            else:
                santa_houses[santa_position] = 1

        else:
            robot_position = santa_move(direction,robot_position)
            if robot_position in robot_houses:
                robot_houses[robot_position] += 1
            else:
                robot_houses[robot_position] = 1

    all_houses =  set(santa_houses.keys()).union(set(robot_houses.keys()))
    return len(all_houses)










with open('Puzzle_3','r' ,encoding='utf-8') as file:
    puzzle = file.read()
    for o in puzzle:
        print(move(o))
    reponse_1 = count_maison(puzzle)
    reponse_2 = count_maison_with_robot(puzzle)
    print(f"Reponse part 1 : {reponse_1} ")
    print(f'Reponse part 2 : {reponse_2} ')