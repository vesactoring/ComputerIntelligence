import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import enum

# Enum representing the directions an ant can take.
class Direction(enum.Enum):
    east = 0
    north = 1
    west = 2
    south = 3

    # Direction to an int.
    # @param dir the direction.
    # @return an integer from 0-3.
    @classmethod
    def dir_to_int(cls, dir):
        return dir.value

    # reverse the direction.
    # @param dir the direction.
    # @return an integer from 0-3
    @classmethod
    def reverse(cls, int_dir):
        if(int_dir == 0): return 2
        if(int_dir == 1): return 3
        if(int_dir == 2): return 0
        if(int_dir == 3): return 1

