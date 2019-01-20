import json
import os
from typing import Dict


def __load_json(file: str) -> Dict:
    path = os.path.join('config', file)
    with open(path, 'r') as config_file:
        return json.load(config_file)


def load_card(file: str) -> Dict:
    path = os.path.join('cards', file)
    return __load_json(path)


def load_player(file: str) -> Dict:
    path = os.path.join('players', file)
    player = __load_json(path)
    player['cards'] = [load_card(card) for card in player['cards']]
    return player


def load_battle(file: str) -> Dict:
    path = os.path.join('battles', file)
    return __load_json(path)


def load_next_quest(file: str = 'quest1.json') -> Dict:
    path = os.path.join('quests', file)
    return __load_json(path)
