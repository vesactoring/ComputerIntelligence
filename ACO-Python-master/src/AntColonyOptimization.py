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
        
        shortest_route = None
        for i in range(self.generations):
            routes = []
            for j in range(self.ants_per_gen):
                ant = Ant(self.maze, path_specification)
                ant_route = ant.find_route()
                if(shortest_route is None):
                    shortest_route = ant_route
                else:
                    if(ant_route.shorter_than(shortest_route)):
                        shortest_route = ant_route
                routes.append(ant_route)
            self.maze.evaporate(self.evaporation)
            self.maze.add_pheromone_routes(routes, self.q)
        return shortest_route

# Driver function for Assignment 1
# Here we create a AntColonyOptimization object and use the find_shortest_route function.
# The function uses an Ant obcject goes through every maze for each generation.
# The Ant finds a route through find_route which makes use of the class SurroundingPheromone to get the pheromone
# from the maze. With the pheromones the ant now can pick a route that he will take.
# After going through all ants and generations the shortest route will return and then be written to a file
if __name__ == "__main__":
    print("is this being used????")
    #parameters
    gen = 4
    no_gen = 10
    q = 1600
    evap = 0.2

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
    shortest_route.write_to_file("data\hard maze result.txt")

    #print route size
    print("Route size: " + str(shortest_route.size()))