PLAYERS = 'players_short.csv'
GAMES = 'games_short.csv'


def delta(player_1, player_2):
    return 1 / (1 + 2**((player_1 - player_2) / 100))


def main():

    SELO = 200 *delta(winner, loser)


if __name__ == "__main__":
    main()
