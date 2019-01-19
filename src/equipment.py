"""
Provides hero equipment classes.
"""

from abc import ABCMeta, abstractmethod


class Equipment(metaclass=ABCMeta):
    def __init__(self, player, name: str, text: str):
        self.name = name
        self.player = player
        self.text = text

    @abstractmethod
    def equip(self):
        pass

    @abstractmethod
    def unequip(self):
        pass


class Boots(Equipment):
    def __init__(self, player, name: str, text: str):
        Equipment.__init__(self, player, name, text)


class Pants(Equipment):
    def __init__(self, player, name: str, text: str):
        Equipment.__init__(self, player, name, text)


class Hat(Equipment):
    def __init__(self, player, name: str, text: str):
        Equipment.__init__(self, player, name, text)


class Shield(Equipment):
    def __init__(self, player, name: str, text: str):
        Equipment.__init__(self, player, name, text)


class Weapon(Equipment):
    def __init__(self, player, name: str, text: str):
        Equipment.__init__(self, player, name, text)
