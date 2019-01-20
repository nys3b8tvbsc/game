"""
Main game module.
Loads config create game object and starts in up.
"""
from game import Game


def main():
    player_file = 'player1.json'
    game = Game(player_file)


if __name__ == '__main__':
    main()
