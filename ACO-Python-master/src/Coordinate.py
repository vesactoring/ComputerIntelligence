import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.Direction import Direction

# Class representing a coordinate.
class Coordinate:

     # Constructs a new coordinate object.
     # @param x the x coordinate
     # @param y the y coordinate
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add a coordinate to this coordinate
    # @param other the other coordinate to be added
    # @return the result coordinate (a new instance)

    def add_coordinate(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    # Move in a direction from this coordinate
    # @param dir direction of unit move
    # @return result the new coordinate
    def add_direction(self, dir):
         return self.add_coordinate(self.dir_to_coordinate_delta(dir))

    # Substract a coordinate from the current coordinate
    # @param other the to be subtracted coordinate
    # @return result the new coordinate
    def subtract_coordinate(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

        # Move in a inverted direction from this coordinate
        # @param Direction of unit move
        # @return result the new coordinate

    def subtract_direction(self, dir):
        return self.subtract_coordinate(self.dir_to_coordinate_delta(dir))

    # String representation of coordinate
    # @return String representation of coordinate
    def __str__(self):
        return str(self.x) + ", " + str(self.y)

    # Equals method for Coordinate
    # @param other Other Coordinate to check
    # @return boolean whether they're equal
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    # Check whether a point lies between a x range with [low,up)
    # @param low lower bound
    # @param up upper bound (non-inclusive)
    # @return boolean whether point lies between two coordinates
    def x_between(self, low, up):
        return low <= self.x and self.x < up

    # Check whether a point lies between a y range with [low,up)
    # @param low lower bound
    # @param up upper bound (non-inclusive)
    # @return boolean whether point lies between two coordinates
    def y_between(self, low, up):
        return low <= self.y and self.y < up

    # Returns x position
    # @return x
    def get_x(self):
        return self.x

    # Returns y position
    # @return y
    def get_y(self):
        return self.y

    # Get vector (coordinate) of a certain direction.
    # @param dir the direction
    # @return the coordinate
    def dir_to_coordinate_delta(self, dir):
        # all directions in a vector
        # Creates a map with a direction linked to its (direction) vector.
        map = {}
        map[Direction.east] = Coordinate(1, 0)
        map[Direction.west] = Coordinate(-1, 0)
        map[Direction.north] = Coordinate(0, -1)
        map[Direction.south] = Coordinate(0, 1)
        return map[dir]