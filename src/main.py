"""
Main game module.
Loads config create game object and starts in up.
"""
import json


def main():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    # game = Game()


if __name__ == '__main__':
    main()
