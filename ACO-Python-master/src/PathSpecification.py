import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import re
import traceback
from src.Coordinate import Coordinate

# Specification of a path containing a start and end coordinate.
class PathSpecification:

    # Constructs a new path specification.
    # @param start the start coordinate.
    # @param end the end coordinate.
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # Get starting coordinate
    # @return starting coordinate
    def get_start(self):
        return self.start

    # Get finish coordinate
    # @return finish coordinate
    def get_end(self):
        return self.end

    # Equals method for PathSpecification
    # @param other other PathSpecification
    # @return whether they're equal
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    # String representation of path specification
    # @return representation
    def __str__(self):
        return "Start: " + str(self.start) + " End: " + str(self.end)


    # Reads the coordinates file and returns a path specification
    # @param filePath String of the path to the file
    # @return Specification contained in the file
    @staticmethod
    def read_coordinates(file_path):
        try:
            f = open(file_path, "r")
            lines = f.read().splitlines()

            start = re.compile("[,;]\\s*").split(lines[0])
            start_x = int(start[0])
            start_y = int(start[1])

            end = re.compile("[,;]\\s*").split(lines[1])
            end_x = int(end[0])
            end_y = int(end[1])

            start_coordinate = Coordinate(start_x, start_y)
            end_coordinate = Coordinate(end_x, end_y)
            return PathSpecification(start_coordinate, end_coordinate)
        except FileNotFoundError:
            print("Error reading coordinate file " + file_path)
            traceback.print_exc()
            sys.exit()

