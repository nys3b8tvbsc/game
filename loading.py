import json
import os


def __load_json(file):
    """
    :param file: path
    :return: Dict
    """
    path = os.path.join('config', file)
    with open(path, 'r') as config_file:
        return json.load(config_file)


def load_card(file):
    """
    :param file: path
    :return: Dict
    """
    path = os.path.join('cards', file)
    return __load_json(path)


def load_player(file):
    """
    :param file: path
    :return: Dict
    """
    path = os.path.join('hero', file)
    player = __load_json(path)
    player['cards'] = [load_card(card) for card in player['cards']]
    return player


def load_battle(file):
    """
    :param file: path
    :return: Dict
    """
    path = os.path.join('battles', file)
    battle = __load_json(path)
    battle['enemies'] = [load_enemy(enemy) for enemy in battle['enemies']]


def load_enemy(file):
    """
    :param file: path
    :return: Dict
    """
    path = os.path.join('enemies', file)
    return __load_json(path)


def load_next_quest(file='quest1.json'):
    """
    :param file: path = 'quest1.json'
    :return: Dict
    """
    path = os.path.join('quests', file)
    return __load_json(path)
