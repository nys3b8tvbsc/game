"""
Module provides Animation class for units animations.
"""
import os
from itertools import cycle

import pygame


def count_files(path):
    return len([0 for obj in os.scandir(path) if obj.is_file()])


class Animation:
    def __init__(self, animation_path):
        """
        :param animation_path: str
        :rtype: Animation object
        """
        cycle_len = count_files(animation_path)
        frames = []
        for i in range(cycle_len):
            frame_path = animation_path + '_{}.png'.format(i)
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
