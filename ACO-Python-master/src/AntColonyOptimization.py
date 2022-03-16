import os, sys
from secrets import choice
from turtle import shape
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import numpy as np
import time
from src.Maze import Maze
from src.PathSpecification import PathSpecification
from src.Route import Route
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

        shortest_route = Route(coordinate_start)
        for i in range(self.generations):
            routes = []
            for j in range(self.ants_per_gen):
                # antwalk: A list of numbers which represents the decisions
                antwalk = Route(coordinate_start)
                coordinate_current = coordinate_start

                #Coordinates
                forbidden_zone = []
                forbidden_zone.append(coordinate_current)
                while(not coordinate_current.__eq__(coordinate_end)):
                    choices = [0,1,2,3]
                    probabilities = self.maze.get_surrounding_pheromone(coordinate_current)
                    pheromone_sum = sum(probabilities)
                    probabilities = np.array(probabilities) / pheromone_sum
                #     if(self.counting_walls(follow_route) == 3):
                #         while(self.counting_walls(follow_route) >= 2):
                #         # substract_direction on the previous direction
                #             remember_last_spot = antwalk.remove_last()
                #             follow_route = antwalk.subtract_direction(self.int_to_dir(remember_last_spot))
                #         # Add the entrance of a forbidden zone
                #         forbidden_zone.append(follow_route.add_direction(self.int_to.dir(remember_last_spot)))
                    while(len(choices) > 0):
                        number = np.random.choice(choices, p=probabilities)
                        probabilities = np.delete(probabilities, choices.index(number))
                        if(np.sum(probabilities) == 0):
                            choices.clear()
                        else:
                            probabilities = probabilities / np.sum(probabilities)
                            choices.remove(number)

                        direction = self.int_to_dir(number)
                        new_coordinate = coordinate_current.add_direction(direction)
                        

                        # The step setp should not be the path the ant has taken
                        if (self.maze.in_bounds(new_coordinate) and self.maze.walls[new_coordinate.x][new_coordinate.y] != 0 and (not new_coordinate in forbidden_zone)):
                            forbidden_zone.append(new_coordinate)
                            coordinate_current = new_coordinate
                            antwalk.add(direction)
                            break            
                        else:  
                            if(len(choices) == 0):
                                direction = self.int_to_dir(Direction.reverse(Direction.dir_to_int(antwalk.remove_last())))
                                coordinate_current = coordinate_current.add_direction(direction)                                 
                    if(shortest_route.size() == 0):
                        shortest_route = antwalk
                    if(antwalk.shorter_than(shortest_route)):
                        shortest_route = antwalk

                    routes.append(antwalk)

            self.maze.evaporate(self.evaporation)
            self.maze.add_pheromone_routes(routes, self.q)

                        #     while(intWalk.size() != 4):
                        #         new_int = np.random.randint(0, 4)
                        #         if(not intWalk.contains(new_int)):

                        # if(antwalk.size() > 0):
                        #     antwalk.remove_last()
                        # antwalk.add(new_direction.dir_to_coordinate_delta(direction))
                    
                    # antwalk.add(direction)
                    #follow_route = start.add_coordinate(direction)
            
            
        return shortest_route

    def counting_walls(self, coordinate):
        count = 0
        for i in range(4):
            check = self.int_to_dir(i)
            new_coordinate = coordinate.add_direction(check)
            if (not self.maze.in_bounds(new_coordinate) or self.maze.walls[new_coordinate.x][new_coordinate.y] == 0):
                count += 1

    # # antwalk: The currect coordinate of the ant 
    # def nextStep(antwalk, intWalk):
    #     direction = self.int_to_dir(int_direction[0])
    #     new_coordinate = follow_route.add_direction(direction)

    #     if (self.maze.in_bounds(new_coordinate) and self.maze.walls[new_coordinate.x][new_coordinate.y] != 0):
    #         follow_route = new_coordinate
    #         antwalk.add(direction)
    #     else:
    #         while(intWalk.size() != 4):
    #             new_int = np.random.randint(0, 4)
    #             if(not intWalk.contains(new_int)):
        

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
    maze = Maze.create_maze("../data/easy maze.txt")
    spec = PathSpecification.read_coordinates("../data/easy coordinates.txt")
    aco = AntColonyOptimization(maze, gen, no_gen, q, evap)

    #save starting time
    start_time = int(round(time.time() * 1000))

    #run optimization
    shortest_route = aco.find_shortest_route(spec)

    #print time taken
    print("Time taken: " + str((int(round(time.time() * 1000)) - start_time) / 1000.0))

    # print(shortest_route)
    #save solution!!!!!
    shortest_route.write_to_file("../data/easy_solution.txt")

    #print route size
    print("Route size: " + str(shortest_route.size()))