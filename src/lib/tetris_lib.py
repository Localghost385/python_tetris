# Copyright (c) 2024 Emma Keogh
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from .app.app import App
from .event.event import Event
from .handler.handler import Handler
from .renderer.renderer import Renderer
from .tetromino.tetromino import Tetromino, TETROMINO_SHAPES


class TetrisLib:
    def __init__(self):
        self.app = App(TETROMINO_SHAPES)
        self.handler = Handler()
        self.renderer = Renderer(self.app)
        self.event = Event(self.app, self.renderer, 0.01)
        self.tetromino = TETROMINO_SHAPES


__all__ = ['App', 'Event', 'Handler', 'Renderer', 'Tetromino']
