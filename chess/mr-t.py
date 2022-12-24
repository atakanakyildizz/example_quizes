PLAYERS = 'players_short.csv'
GAMES = 'games_short.csv'


def delta(player_1, player_2):

    players = read_file(PLAYERS)
    players = make_dict(players)

    for pla, elo in players.items():
        if player_1 == pla:
            player_1 = int(elo[0])
        else:
            player_2 = int(elo[0])

    return 1 / (1 + 2**((player_1 - player_2) / 100))


def read_file(filename):
    try:
        with open(filename) as my_file:
            my_file = my_file.readlines()
            my_file = my_file[1:]
            return my_file

    except OSError as error:
        print(f"Whops we have a problem\n{error}")


def make_dict(file):

    foo = dict()
    for element in file:
        element = "".join(element)
        element = element.replace("\n", "")
        element = element.split(",")
        foo[element[0]] = element[1:]
    return foo


def main():

    games = read_file(GAMES)

    for element in games:
        element = "".join(element)
        element = element.replace("\n", "")
        element = element.split(",")
        print(element)
        if True:
            print(delta(element[0], element[1]))


if __name__ == "__main__":
    main()
