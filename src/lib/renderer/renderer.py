# Copyright (c) 2024 Emma Keogh
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from ..app.app import App
from ..tetromino.tetromino import Tetromino

class Renderer:
    def __init__(self, app: App):
        self.app = app

    def render_playfield(self) -> str:
        """
        Renders the playfield as a string representation.

        Returns:
            str: The string representation of the playfield.
        """
        return self.app.playfield_string()

    def render_tetromino(self, tetromino: Tetromino) -> str:
        """
        Renders a tetromino as a string representation.

        Args:
            tetromino (Tetromino): The tetromino to render.

        Returns:
            str: The string representation of the tetromino.
        """
        return self.app.tetromino_string(tetromino)

    def render_tetromino_queue(self) -> str:
        """
        Renders the tetromino queue as a string representation.

        Returns:
            str: The string representation of the tetromino queue.
        """
        return self.app.tetromino_queue_string()

    def render_game_state(self) -> str:
        """
        Renders the current game state including playfield, score, and level.

        Returns:
            str: The string representation of the game state.
        """
        output = f"Score: {self.app.game_state['score']}\n"
        output += f"High Score: {self.app.game_state['high_score']}\n"
        output += f"Level: {self.app.game_state['level']}\n"
        output += "Playfield:\n"
        output += self.render_playfield()
        # output += "Tetromino Queue:\n"
        # output += self.render_tetromino_queue()
        return output

    def display(self):
        """
        Displays the current game state.
        """
        print(self.render_game_state())
