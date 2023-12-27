def possible_games(red_count, green_count, blue_count, games):
  """
  Détermine quels jeux sont possibles avec un sac contenant les nombres spécifiés de cubes rouges, verts et bleus.

  Args:
    red_count: Le nombre de cubes rouges dans le sac.
    green_count: Le nombre de cubes verts dans le sac.
    blue_count: Le nombre de cubes bleus dans le sac.
    games: Une liste de jeux.

  Returns:
    Une liste des identifiants des jeux qui sont possibles.
  """

  possible_games = []
  for game in games:
    possible = True
    for set in game:
      for color in set:
        if color > red_count or color > green_count or color > blue_count:
          possible = False
          break
      if not possible:
        break
    if possible:
      possible_games.append(game[0])
  return possible_games


def main():
  red_count = 12
  green_count = 13
  blue_count = 14
  games = [
    [3, 4],
    [1, 2, 6],
    [2],
    [1, 2],
    [8, 6, 20],
    [5, 4, 13],
    [5, 1],
    [1, 3, 6],
    [3, 6],
    [3, 15, 14],
    [6, 1, 3],
    [2, 1, 2]
  ]
  possible_gamess = possible_games(red_count, green_count, blue_count, games)
  print("Les jeux possibles sont :", possible_games)


if __name__ == "__main__":
  main()
