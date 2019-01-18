import random
from typing import List, Callable

from player import Player
from unit import Unit


class Enemy(Unit):
    def __init__(self, level: int, actions: List[Callable], img_path: str):
        super().__init__(level, img_path)
        self.actions = actions

    def make_action(self, player: Player):
        action = random.choice(self.actions)
        action(self, player)

    def take_damage(self, damage: int):
        pass
