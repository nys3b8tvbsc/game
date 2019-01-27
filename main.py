"""
Main game module.
Create game object and starts it up.
"""
from game import Game


def main():
    player_file = 'hero1.json'
    game = Game(player_file)


if __name__ == '__main__':
    main()
