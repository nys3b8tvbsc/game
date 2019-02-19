from game import Game


def main():
    player_file = 'hero1.json'
    game = Game(player_file)
    game.start()


if __name__ == '__main__':
    main()
