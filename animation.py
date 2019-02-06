"""
Module provides Animation class for units animations.
"""
import os
from itertools import cycle

import pygame


def iter_files(path):
    files = sorted(sorted(os.listdir(path)), key=str.__len__)
    for file in files:
        frame_path = os.path.join(path, file)
        yield pygame.image.load(frame_path).convert_alpha()


class Animation:
    def __init__(self, path, pause=1):
        """
        :param path: str
        :rtype: Animation object
        """
        t=list(iter_files(path))
        self._end=t[-1]
        self._frames = cycle(t)
        self._current_frame = next(self._frames)
        self._start_frame = self._current_frame
        self._pause=pause
        self._pause_rem=self._pause

    @property
    def frame(self):
        return self._current_frame

    @property
    def is_finished(self):
        return self._current_frame == self._end

    def update(self):
        self._pause_rem-=1
        if self._pause_rem==0:
            self._current_frame = next(self._frames)
            self._pause_rem=self._pause
