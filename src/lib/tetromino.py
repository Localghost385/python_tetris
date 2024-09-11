# Copyright (c) 2024 Emma Keogh
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

class Tetromino:
    def __init__(self, rotations):
        self.rotations = rotations

# Predefined tetromino shapes
TETROMINO_SHAPES = [
    Tetromino([
        [
            [False, False, False, False],
            [True,  True,  True,  True],
            [False, False, False, False],
            [False, False, False, False],
        ],
        [
            [False, False, True,  False],
            [False, False, True,  False],
            [False, False, True,  False],
            [False, False, True,  False],
        ],
        [
            [False, False, False, False],
            [False, False, False, False],
            [True,  True,  True,  True],
            [False, False, False, False],
        ],
        [
            [False, True,  False, False],
            [False, True,  False, False],
            [False, True,  False, False],
            [False, True,  False, False],
        ],
    ]),
    Tetromino([
        [
            [True,  False, False, False],
            [True,  True,  True,  False],
            [False, False, False, False],
            [False, False, False, False],
        ],
        [
            [False, True,  True,  False],
            [False, True,  False, False],
            [False, True,  False, False],
            [False, False, False, False],
        ],
        [
            [False, False, False, False],
            [True,  True,  True,  False],
            [False, False, True,  False],
            [False, False, False, False],
        ],
        [
            [False, True,  False, False],
            [False, True,  False, False],
            [True,  True,  False, False],
            [False, False, False, False],
        ],
    ]),
    Tetromino([
        [
            [False, False, True,  False],
            [True,  True,  True,  False],
            [False, False, False, False],
            [False, False, False, False],
        ],
        [
            [False, True,  False, False],
            [False, True,  False, False],
            [False, True,  True,  False],
            [False, False, False, False],
        ],
        [
            [False, False, False, False],
            [True,  True,  True,  False],
            [True,  False, False, False],
            [False, False, False, False],
        ],
        [
            [True,  True,  False, False],
            [False, True,  False, False],
            [False, True,  False, False],
            [False, False, False, False],
        ],
    ]),
    Tetromino([
        [
            [False, True,  True,  False],
            [False, True,  True,  False],
            [False, False, False, False],
            [False, False, False, False],
        ],
        [
            [False, True,  True,  False],
            [False, True,  True,  False],
            [False, False, False, False],
            [False, False, False, False],
        ],
        [
            [False, True,  True,  False],
            [False, True,  True,  False],
            [False, False, False, False],
            [False, False, False, False],
        ],
        [
            [False, True,  True,  False],
            [False, True,  True,  False],
            [False, False, False, False],
            [False, False, False, False],
        ],
    ]),
    Tetromino([
        [
            [False, True,  True,  False],
            [True,  True,  False, False],
            [False, False, False, False],
            [False, False, False, False],
        ],
        [
            [False, True,  False, False],
            [False, True,  True,  False],
            [False, False, True,  False],
            [False, False, False, False],
        ],
        [
            [False, False, False, False],
            [False, True,  True,  False],
            [True,  True,  False, False],
            [False, False, False, False],
        ],
        [
            [True,  False, False, False],
            [True,  True,  False, False],
            [False, True,  False, False],
            [False, False, False, False],
        ],
    ]),
    Tetromino([
        [
            [False, True,  False, False],
            [True,  True,  True,  False],
            [False, False, False, False],
            [False, False, False, False],
        ],
        [
            [False, True,  False, False],
            [False, True,  True,  False],
            [False, True,  False, False],
            [False, False, False, False],
        ],
        [
            [False, False, False, False],
            [True,  True,  True,  False],
            [False, True,  False, False],
            [False, False, False, False],
        ],
        [
            [False, True,  False, False],
            [True,  True,  False, False],
            [False, True,  False, False],
            [False, False, False, False],
        ],
    ]),
    Tetromino([
        [
            [True,  True,  False, False],
            [False, True,  True,  False],
            [False, False, False, False],
            [False, False, False, False],
        ],
        [
            [False, False, True,  False],
            [False, True,  True,  False],
            [False, True,  False, False],
            [False, False, False, False],
        ],
        [
            [False, False, False, False],
            [True,  True,  False, False],
            [False, True,  True,  False],
            [False, False, False, False],
        ],
        [
            [False, True,  False, False],
            [True,  True,  False, False],
            [True,  False, False, False],
            [False, False, False, False],
        ],
    ]),
]
