import json
import os


def __load_json(file):
    """
    :param str file: path
    :rtype: dict
    """
    path = os.path.join('config', file)
    with open(path, 'r', encoding='utf-8') as config_file:
        return json.load(config_file)


def load_card(file):
    """
    :param str file: path
    :rtype: dict
    """
    path = os.path.join('cards', file)
    config = __load_json(path)
    config["conf_name"] = file
    return config


def load_deck(file):
    """
    :param str file: path
    :rtype: dict
    """
    path = os.path.join('deck', file)
    return __load_json(path)


def load_hero(file):
    """
    :param str file: path
    :rtype: dict
    """
    path = os.path.join('hero', file)
    hero = __load_json(path)
    hero['deck'] = load_deck(hero['deck'])
    return hero


def load_battle(file):
    """
    :param str file: path
    :rtype: dict
    """
    path = os.path.join('battles', file)
    return __load_json(path)


def load_enemy(file):
    """
    :param str file: path
    :rtype: dict
    """
    path = os.path.join('enemies', file)
    return __load_json(path)


def load_next_quest(file='quest1.json'):
    """
    :param str file: path
    :rtype: dict
    """
    path = os.path.join('quests', file)
    return __load_json(path)
