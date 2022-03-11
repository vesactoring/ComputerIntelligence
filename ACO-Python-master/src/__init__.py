import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.Coordinate import Coordinate
from src.Direction import Direction
from src.PathSpecification import PathSpecification
import numpy as np
from src.Maze import Maze


test = Maze.create_maze("./data/easy maze.txt")
print(test)
coordin = Coordinate(0,0)
coordin = coordin.add_direction(Direction.east)
print(coordin)

spec = PathSpecification.read_coordinates("./data/hard coordinates.txt")
print("SPEC: ", spec.start.x)

print("test")
# print()
# print(dr.(east))