# Copyright (c) 2024 Emma Keogh
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import time
from ..app.app import App
from ..renderer.renderer import Renderer

class Event:
    def __init__(self, app: App, renderer: Renderer, tick_rate: float = 1.0):
        """
        Initializes the event loop with the given app and renderer.

        Args:
            app (App): The application instance.
            renderer (Renderer): The renderer instance.
            tick_rate (float): How often to update the app (in seconds).
        """
        self.app = app
        self.renderer = renderer
        self.tick_rate = tick_rate

    def run(self):
        """
        Starts the event loop.
        """
        while self.app.game_state['running']:
            self.tick()
            self.render()
            time.sleep(self.tick_rate)

    def tick(self):
        """
        Updates the app state by calling the tick method on the app.
        """
        self.app.tick()

    def render(self):
        """
        Renders the current state of the app.
        """
        self.renderer.display()
