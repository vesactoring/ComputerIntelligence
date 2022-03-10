import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.Direction import Direction

# Class representing a route.
class Route:

    # Route takes a starting coordinate to initialize
    # @param start starting coordinate
    def __init__(self, start):
        self.route = []
        self.start = start

    # After taking a step we add the direction we moved in
    # @param dir Direction we moved in
    def add(self, dir):
        self.route.append(dir)
        return

    # Returns the length of the route
    # @return length of the route
    def size(self):
        return len(self.route)

    # Getter for the list of directions
    # @return list of directions
    def get_route(self):
        return self.route

    # Getter for the starting coordinate
    # @return the starting coordinate
    def get_start(self):
        return self.start

    # Function that checks whether a route is smaller than another route
    # @param other the other route
    # @return whether the route is shorter
    def shorter_than(self, other):
        return self.size() < other.size()

    # Take a step back in the route and return the last direction
    # @return last direction
    def remove_last(self):
        return self.route.pop()

    # Build a string representing the route as the format specified in the manual.
    # @return string with the specified format of a route
    def __str__(self):
        string = ""
        for dir in self.route:
            string += str(Direction.dir_to_int(dir))
            string += ";\n"
        return string

    # Equals method for route
    # @param other Other route
    # @return boolean whether they are equal
    def __eq__(self, other):
        return self.start == other.start and self.route == other.route


    # Method that implements the specified format for writing a route to a file.
    # @param filePath path to route file.
    # @throws FileNotFoundException
    def write_to_file(self, file_path):
        f = open(file_path, "w")
        string = ""
        string += str(len(self.route))
        string += ";\n"
        string += str(self.start)
        string += ";\n"
        string += str(self)
        f.write(string)