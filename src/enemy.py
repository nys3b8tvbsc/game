import random
from typing import List, Callable

from unit import Unit, Player


class Enemy(Unit):
    def __init__(self, level: int, actions: List[Callable], image: str):
        Unit.__init__(self, level, image)
        self.actions = actions

    def make_action(self, player: Player):
        action = random.choice(self.actions)
        action(self, player)

    def take_damage(self, damage: int):
        pass
