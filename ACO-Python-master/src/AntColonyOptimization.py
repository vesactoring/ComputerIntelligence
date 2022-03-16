import os, sys
from secrets import choice
from turtle import shape
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import numpy as np
import time
from src.Ant import Ant
from src.Maze import Maze
from src.PathSpecification import PathSpecification
from src.Route import Route
from src.SurroundingPheromone import SurroundingPheromone
from src.Coordinate import Coordinate
from src.Direction import Direction

# Class representing the first assignment. Finds shortest path between two points in a maze according to a specific
# path specification.
class AntColonyOptimization:

    # Constructs a new optimization object using ants.
    # @param maze the maze .
    # @param antsPerGen the amount of ants per generation.
    # @param generations the amount of generations.
    # @param Q normalization factor for the amount of dropped pheromone
    # @param evaporation the evaporation factor.
    def __init__(self, maze, ants_per_gen, generations, q, evaporation):
        self.maze = maze
        self.ants_per_gen = ants_per_gen
        self.generations = generations
        self.q = q
        self.evaporation = evaporation

     # Loop that starts the shortest path process
     # @param spec Spefication of the route we wish to optimize
     # @return ACO optimized route
    def find_shortest_route(self, path_specification):
        self.maze.reset()
        start = path_specification.get_start()
        end = path_specification.get_end()
        
        coordinate_start = Coordinate(start.x, start.y)
        coordinate_end = Coordinate(end.x, end.y)

        shortest_route = None
        for i in range(self.generations):
            routes = []
            for j in range(self.ants_per_gen):
                ant_route = Route(coordinate_start)
                coordinate_current = coordinate_start

                been_before = []
                been_before.append(coordinate_current)
                while(not coordinate_current.__eq__(coordinate_end)):
                    # Returns Surrounding Pheromone class
                    surrounding_pheromone = self.maze.get_surrounding_pheromone(coordinate_current)
                    # total_pheromone = surrounding_pheromone.get_total_surrounding_pheromone()
                    probabilities = []
                    choices = [0, 1, 2, 3]

                    for i in range(4):
                        direction = self.int_to_dir(i)
                        direction_pheromone = surrounding_pheromone.get(direction)
                        if(direction_pheromone > 0 and (coordinate_current.add_direction(direction) not in been_before) and (self.maze.in_bounds(coordinate_current.add_direction(direction)))):
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
                if(shortest_route is None):
                    shortest_route = ant_route
                else:
                    if(ant_route.shorter_than(shortest_route)):
                        shortest_route = ant_route
                routes.append(ant_route)
            self.maze.evaporate(self.evaporation)
            self.maze.add_pheromone_routes(routes, self.q)
        print(shortest_route)
        return shortest_route


        

        # return None
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

    def get_evaporate(self):
        return self.evaporation
# Driver function for Assignment 1
if __name__ == "__main__":
    print("is this being used????")
    #parameters
    gen = 1
    no_gen = 1
    q = 1600
    evap = 0.1

    #construct the optimization objects
    maze = Maze.create_maze("data\hard maze.txt")
    spec = PathSpecification.read_coordinates("data\hard coordinates.txt")
    aco = AntColonyOptimization(maze, gen, no_gen, q, evap)

    #save starting time
    start_time = int(round(time.time() * 1000))

    #run optimization
    shortest_route = aco.find_shortest_route(spec)

    #print time taken
    print("Time taken: " + str((int(round(time.time() * 1000)) - start_time) / 1000.0))

    # print(shortest_route)
    #save solution!!!!!
    shortest_route.write_to_file("data\easy maze result.txt")

    #print route size
    print("Route size: " + str(shortest_route.size()))