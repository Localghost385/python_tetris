# Copyright (c) 2024 Emma Keogh
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import List
import random
import os
from ..tetromino.tetromino import TETROMINO_SHAPES

class PlayFieldCell:
    """
    Represents a cell in the playfield grid.

    Attributes:
        falling (bool): Indicates if the cell is currently falling.
        landed (bool): Indicates if the cell has landed.
    """
    def __init__(self, falling: bool = False, landed: bool = False):
        self.falling = falling
        self.landed = landed

    def __repr__(self):
        return f"PlayFieldCell(falling={self.falling}, landed={self.landed})"

class Tetromino:
    """
    Represents a tetromino and its possible rotations.

    Attributes:
        rotations (List[List[List[bool]]]): List of 2D grids representing the different rotations of the tetromino.
    """
    def __init__(self, rotations: List[List[List[bool]]] = None):
        if rotations is None:
            rotations = [[
                [False, False, False, False],
                [False, False, False, False],
                [False, False, False, False],
                [False, False, False, False],
            ] for _ in range(4)]
        self.rotations = rotations

    def __repr__(self):
        return f"Tetromino(rotations={self.rotations})"

class App:
    """
    Main application class that integrates all game components and handles game logic.

    Attributes:
        game_state (dict): Contains general game state such as running status, score, level, and pause status.
        playfield (List[List[PlayFieldCell]]): 2D grid representing the playfield.
        tetromino_manager (dict): Manages current, swap, and queue of tetrominos.
        timing (dict): Handles timing-related information.
        ui (dict): Manages UI elements like buttons.
    """
    def __init__(self, tetromino_shapes: List[Tetromino]):
        self.game_state = {
            'running': True,
            'paused': False,
            'score': 0,
            'high_score': 0,
            'level': 1
        }
        self.playfield = [[PlayFieldCell() for _ in range(18)] for _ in range(26)]
        self.tetromino_manager = {
            'current_tetromino': random.choice(tetromino_shapes),
            'swap_tetromino': Tetromino(),
            'tetromino_queue': [],
            'current_rotation': 0,
            'start_x': 7,
            'start_y': 4,
            'x': 7,
            'y': 4
        }
        self.timing = {
            'tick_count': 0,
            'tick_count_target': 15,
            'default_tick_count_target': 15,
            'grace_period': False
        }
        self.ui = {'buttons': []}
        self.check_for_highscore()

    def new(self) -> 'App':
        """
        Constructs a new instance of `App`.

        Returns:
            App: A new instance of the application with default settings.
        """
        return App([])  # Pass appropriate tetromino shapes here

    def tick(self):
        """
        Handles the tick event of the terminal. Updates game state and tetromino position based on timing and user actions.
        """
        if self.game_state['paused']:
            return

        if len(self.tetromino_manager['tetromino_queue']) < 7:
            self.populate_tetromino_queue()

        self.timing['tick_count'] += 1
        if self.timing['tick_count'] > self.timing['tick_count_target']:
            lines_cleared = self.check_for_line_clear()
            self.game_state['score'] += lines_cleared ** 2 * 100 * self.game_state['level']
            self.check_for_next_level()

            if self.has_landed_cells_at_offset(0, 1):
                if self.timing['grace_period']:
                    self.reset_tetromino()
                self.timing['grace_period'] = not self.timing['grace_period']

            self.timing['tick_count'] = 0

            if not self.has_landed_cells_at_offset(0, 1):
                self.move_tetromino(0, 1, self.tetromino_manager['current_tetromino'])
                self.timing['grace_period'] = False

        self.timing['tick_count_target'] = self.timing['default_tick_count_target']

    def quit(self):
        """
        Sets the running state to false to quit the application.
        """
        self.game_state['running'] = False

    def spawn_tetromino(self, start_x: int, start_y: int, tetromino: Tetromino) -> Tetromino:
        """
        Randomly spawns a tetromino at the specified position on the playfield.

        Args:
            start_x (int): The X position to spawn the tetromino.
            start_y (int): The Y position to spawn the tetromino.
            tetromino (Tetromino): The tetromino to spawn.

        Returns:
            Tetromino: The spawned tetromino.
        """
        self.check_for_game_over()

        for y in range(len(tetromino.rotations[self.tetromino_manager['current_rotation']])):
            for x in range(len(tetromino.rotations[self.tetromino_manager['current_rotation']][y])):
                if tetromino.rotations[self.tetromino_manager['current_rotation']][y][x]:
                    self.playfield[start_y + y][start_x + x].falling = True
        return tetromino

    def populate_tetromino_queue(self):
        """
        Fills the tetromino queue with a random order of tetrominoes.
        """
        tetromino_order = list(range(7))
        random.shuffle(tetromino_order)

        for tetromino in tetromino_order:
            self.tetromino_manager['tetromino_queue'].append(TETROMINO_SHAPES[tetromino])

    def reset_tetromino(self):
        """
        Prepares for the next tetromino by landing the current one and resetting its position.
        """
        self.land_tetromino()
        self.clear_falling()
        self.tetromino_manager['x'] = self.tetromino_manager['start_x']
        self.tetromino_manager['y'] = self.tetromino_manager['start_y']
        self.tetromino_manager['current_rotation'] = 0
        self.tetromino_manager['current_tetromino'] = self.spawn_tetromino(
            self.tetromino_manager['x'], self.tetromino_manager['y'], self.tetromino_manager['tetromino_queue'][0]
        )
        self.tetromino_manager['tetromino_queue'].pop(0)

    def land_tetromino(self):
        """
        Places the current tetromino on the playfield by marking its cells as landed.
        """
        for y, row in enumerate(self.tetromino_manager['current_tetromino'].rotations[self.tetromino_manager['current_rotation']]):
            for x, cell in enumerate(row):
                if cell:
                    self.playfield[self.tetromino_manager['y'] + y][self.tetromino_manager['x'] + x].landed = True

    def move_tetromino(self, move_x: int, move_y: int, tetromino: Tetromino):
        """
        Moves the tetromino by the specified offsets.

        Args:
            move_x (int): The offset to move in the X direction.
            move_y (int): The offset to move in the Y direction.
            tetromino (Tetromino): The tetromino to move.
        """
        self.clear_falling()
        new_x = self.tetromino_manager['x'] + move_x
        new_y = self.tetromino_manager['y'] + move_y

        for y in range(4):
            for x in range(4):
                if tetromino.rotations[self.tetromino_manager['current_rotation']][y][x]:
                    if new_y + y < len(self.playfield) and new_x + x < len(self.playfield[0]):
                        self.playfield[new_y + y][new_x + x].falling = True

        self.tetromino_manager['x'] = new_x
        self.tetromino_manager['y'] = new_y

    def drop_tetromino(self):
        """
        Instantly moves the tetromino as far down as possible.
        """
        min_drops = 20
        for y in range(4):
            for x in range(4):
                if self.tetromino_manager['current_tetromino'].rotations[self.tetromino_manager['current_rotation']][y][x]:
                    drops = 0
                    y_temp = y
                    while (self.tetromino_manager['y'] + y_temp < len(self.playfield) and
                           self.tetromino_manager['x'] + x < len(self.playfield[0]) and
                           not self.playfield[self.tetromino_manager['y'] + y_temp][self.tetromino_manager['x'] + x].landed):
                        y_temp += 1
                        drops += 1
                    if drops < min_drops:
                        min_drops = drops

        self.move_tetromino(0, min_drops - 1, self.tetromino_manager['current_tetromino'])
        self.reset_tetromino()

    def swap_tetromino(self):
        """
        Swaps the current tetromino with the swap tetromino, and spawns a new tetromino if the current one is empty.
        """
        self.tetromino_manager['current_tetromino'], self.tetromino_manager['swap_tetromino'] = (
            self.tetromino_manager['swap_tetromino'],
            self.tetromino_manager['current_tetromino']
        )
        self.clear_falling()
        self.tetromino_manager['x'] = self.tetromino_manager['start_x']
        self.tetromino_manager['y'] = self.tetromino_manager['start_y']
        self.tetromino_manager['current_rotation'] = 0
        if not any(cell for row in self.tetromino_manager['current_tetromino'].rotations[self.tetromino_manager['current_rotation']] for cell in row):
            self.tetromino_manager['current_tetromino'] = self.spawn_tetromino(
                self.tetromino_manager['x'], self.tetromino_manager['y'], self.tetromino_manager['tetromino_queue'][0]
            )
            self.tetromino_manager['tetromino_queue'].pop(0)

    def has_landed_cells_at_offset(self, x_offset: int, y_offset: int) -> bool:
        """
        Checks if there are landed cells at the specified offset from the tetromino's position.

        Args:
            x_offset (int): The X offset to check.
            y_offset (int): The Y offset to check.

        Returns:
            bool: True if there are landed cells at the offset, False otherwise.
        """
        for y in range(4):
            for x in range(4):
                if self.tetromino_manager['current_tetromino'].rotations[self.tetromino_manager['current_rotation']][y][x]:
                    check_y = self.tetromino_manager['y'] + y + y_offset
                    check_x = self.tetromino_manager['x'] + x + x_offset

                    out_of_bounds = (check_y >= len(self.playfield) or check_y < 0 or
                                     check_x < 4 or check_x >= 14)

                    if out_of_bounds or self.playfield[check_y][check_x].landed:
                        return True

        return False

    def check_for_line_clear(self) -> int:
        """
        Checks for any lines that are completely filled and clears them.

        Returns:
            int: The number of lines cleared.
        """
        lines_cleared = 0
        lines_to_be_cleared = []

        for y in range(len(self.playfield)):
            if all(self.playfield[y][x].landed for x in range(4, 14)):
                lines_to_be_cleared.append(y)
                lines_cleared += 1

        for row in lines_to_be_cleared:
            self.playfield.pop(row)
            self.playfield.insert(0, [PlayFieldCell() for _ in range(18)])

        return lines_cleared

    def check_for_game_over(self) -> bool:
        """
        Checks if the game is over (e.g., a tetromino cannot be spawned).

        Returns:
            bool: True if the game is over, False otherwise.
        """
        if self.playfield[self.tetromino_manager['start_y'] + 1][self.tetromino_manager['start_x'] + 1].landed:
            return True
        return False

    def check_for_highscore(self):
        """
        Checks and updates the high score from the high score file.
        """
        home_dir = os.path.expanduser("~")
        path = os.path.join(home_dir, ".tetrs_highscore")

        try:
            with open(path, 'r') as file:
                high_score = int(file.read().strip())
        except (FileNotFoundError, ValueError):
            high_score = 0
            with open(path, 'w') as file:
                file.write("0")

        self.game_state['high_score'] = high_score

    def check_for_next_level(self):
        """
        Checks if the score threshold for the next level has been reached and updates the level accordingly.
        """
        if self.game_state['score'] > 500 * self.game_state['level'] ** 3:
            self.game_state['level'] += 1
            self.timing['default_tick_count_target'] -= 1

    def clear_falling(self):
        """
        Clears the falling cells from the playfield by setting their falling status to False.
        """
        for row in self.playfield:
            for cell in row:
                if cell.falling:
                    cell.falling = False

    def playfield_string(self) -> str:
        """
        Returns a string representation of the playfield.

        Returns:
            str: The playfield as a string.
        """
        result = ""
        for row in self.playfield[4:]:
            for cell in row[4:]:
                if cell.landed:
                    result += "██"
                elif cell.falling:
                    result += "▒▒"
                else:
                    result += "  "
            result += '\n'
        return result

    def tetromino_string(self, tetromino: Tetromino) -> str:
        """
        Returns a string representation of a tetromino.

        Args:
            tetromino (Tetromino): The tetromino to represent as a string.

        Returns:
            str: The tetromino as a string.
        """
        result = ""
        for row in tetromino.rotations[1]:
            for cell in row[1:3]:
                result += "██" if cell else "  "
            result += '\n'
        return result

    def tetromino_queue_string(self) -> str:
        """
        Returns a string representation of the tetromino queue.

        Returns:
            str: The tetromino queue as a string.
        """
        result = ""
        for tetromino in self.tetromino_manager['tetromino_queue']:
            result += self.tetromino_string(tetromino)
            result += '\n'
        return result
