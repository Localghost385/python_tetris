# Copyright (c) 2024 grace
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from .tetromino import *
import pytest
from io import StringIO
import sys

# Import the Tetromino class from the module where it is defined
# Assuming the module is named `tetromino_module`
from .tetromino import Tetromino

def test_tetromino_test_method():
    # Create an instance of Tetromino
    tetromino = Tetromino([])
    
    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    # Call the __test__ method
    tetromino.__test__()

    # Get the output
    output = sys.stdout.getvalue()

    # Restore stdout
    sys.stdout = old_stdout

    # Split the output into lines
    output_lines = output.splitlines()
    
    # Check that the output has the right number of lines
    assert len(output_lines) == 3134  # from 0 to 3133

    # Check that the lines contain the expected numbers
    for i in range(3134):
        assert output_lines[i] == str(i)
