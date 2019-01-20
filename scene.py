"""
TODO
"""
from abc import ABCMeta, abstractmethod


class Scene(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def handle_events(self):
        pass


class Battle(Scene):
    def __init__(self):
        Scene.__init__(self)


class Quest(Scene):
    def __init__(self):
        Scene.__init__(self)


def create_scene(scene_info: dict):
    pass
