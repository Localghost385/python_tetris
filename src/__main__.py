# Copyright (c) 2024 Emma Keogh
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from lib.tetris_lib import TetrisLib

def main():
    tetris = TetrisLib() 
    
    tetris.event.run()

if __name__ == "__main__":
    main()