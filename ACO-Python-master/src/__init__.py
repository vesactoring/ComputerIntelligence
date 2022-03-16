import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.Coordinate import Coordinate
from src.Direction import Direction
from src.PathSpecification import PathSpecification
from src.AntColonyOptimization import AntColonyOptimization
import numpy as np
from src.Maze import Maze

test = Maze.create_maze("data\easy maze.txt")
coordin = Coordinate(0,0)
coordin = coordin.add_direction(Direction.east)
aoc = AntColonyOptimization(test, 10, 10, 100, 0.5)
spec = PathSpecification.read_coordinates("data\easy coordinates.txt")
path = aoc.find_shortest_route(spec)
print("the path size : ", path.size())
path.write_to_file("data\easy maze result.txt")

