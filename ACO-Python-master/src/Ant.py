import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import random
import numpy as np
from src.Maze import Maze
from src.PathSpecification import PathSpecification
from src.Route import Route
from src.SurroundingPheromone import SurroundingPheromone
from src.Coordinate import Coordinate
from src.Direction import Direction

#Class that represents the ants functionality.
class Ant:

    # Constructor for ant taking a Maze and PathSpecification.
    # @param maze Maze the ant will be running in.
    # @param spec The path specification consisting of a start coordinate and an end coordinate.
    def __init__(self, maze, path_specification):
        self.maze = maze
        self.start = path_specification.get_start()
        self.end = path_specification.get_end()
        self.current_position = self.start
        self.rand = random

    # Method that performs a single run through the maze by the ant.
    # @return The route the ant found through the maze.
    def find_route(self):        
        coordinate_start = Coordinate(self.start.x, self.start.y)
        coordinate_end = Coordinate(self.end.x, self.end.y)

        ant_route = Route(coordinate_start)
        coordinate_current = coordinate_start

        been_before = []
        been_before.append(coordinate_current)
        while(not coordinate_current.__eq__(coordinate_end)):
            # print(coordinate_current)
            # Returns Surrounding Pheromone class
            surrounding_pheromone = self.maze.get_surrounding_pheromone(coordinate_current)
            # total_pheromone = surrounding_pheromone.get_total_surrounding_pheromone()
            probabilities = []
            choices = [0, 1, 2, 3]

            for i in range(4):
                direction = self.int_to_dir(i)
                direction_pheromone = surrounding_pheromone.get(direction)
                new_coordinate = coordinate_current.add_direction(direction)
                if(direction_pheromone > 0 and (new_coordinate not in been_before) and (self.maze.in_bounds(new_coordinate)) and self.maze.walls[new_coordinate.x][new_coordinate.y] != 0):
                    probabilities.append(direction_pheromone)
                else:
                    choices.remove(i)

            probabilities = np.array(probabilities) / np.sum(probabilities)

            if(len(choices) > 0):
                step_choice_number = np.random.choice(choices, p=probabilities)
                step_direction = self.int_to_dir(step_choice_number)
                new_coordinate = coordinate_current.add_direction(step_direction)

                been_before.append(new_coordinate)
                coordinate_current = new_coordinate
                ant_route.add(step_direction)
            else: 
                previous_direction = ant_route.remove_last()
                coordinate_current = coordinate_current.subtract_direction(previous_direction)
        return ant_route

    def int_to_dir(self, number):
        if number == 0:
            return Direction.east
        elif number == 1:
            return Direction.north
        elif number == 2:
            return Direction.west
        elif number == 3:
            return Direction.south
        else:
            return -1
