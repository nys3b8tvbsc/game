"""
Module provides Animation class for units animations.
"""
import os
from itertools import cycle

import pygame


def iter_files(path):
    files = sorted(os.listdir(path))
    for file in files:
        frame_path = os.path.join(path, file)
        yield pygame.image.load(frame_path).convert_alpha()


class Animation:
    def __init__(self, path):
        """
        :param path: str
        :rtype: Animation object
        """
        self._frames = cycle(iter_files(path))
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
