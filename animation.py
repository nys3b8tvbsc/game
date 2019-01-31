"""
Module provides Animation class for units animations.
"""
from itertools import cycle

import pygame


class Animation:
    def __init__(self, animation_path, cycle_len):
        """
        :param animation_path: str
        :param cycle_len: int
        :return: Animation object
        """
        frames = []
        for i in range(cycle_len):
            frame_path = animation_path + '_{}.png'.format(i + 1)
            frame = pygame.image.load(frame_path).convert_alpha()
            frames.append(frame)

        self._frames = cycle(frames)
        self._current_frame = next(self._frames)
        self._start_frame = self._current_frame

    @property
    def frame(self):
        return self._current_frame

    @property
    def is_finished(self):
        return self._current_frame == self._start_frame

    def update(self):
        self._current_frame = next(self._frames)
