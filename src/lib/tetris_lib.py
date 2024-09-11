# Copyright (c) 2024 Emma Keogh
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from .app import App
from .event import Event
from .handler import Handler
from .renderer import Renderer
from .tetromino import Tetromino, TETROMINO_SHAPES

class TetrisLib:
    def __init__(self):
        self.app = App()
        self.event = Event()
        self.handler = Handler()
        self.renderer = Renderer()
        self.tetromino = TETROMINO_SHAPES

__all__ = ['App', 'Event', 'Handler', 'Renderer', 'Tetromino']
