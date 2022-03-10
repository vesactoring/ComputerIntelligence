import os, sys
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
        for i in range(self.generations):
            for j in range(self.ants_per_gen):
                # antwalk: A list of numbers which represents the decisions
                antwalk = Route(coordinate_start)
                follow_route = coordinate_start

                #Coordinates
                forbidden_zone = []
                remember_last_spot = None
                while(not follow_route.__eq__(coordinate_end)):
                    possibilities = [0,1,2,3]
                    # possibilities.remove(last_dirction)
                    if(self.counting_walls(follow_route) == 3):
                        while(self.counting_walls(follow_route) >= 2):
                        # substract_direction on the previous direction
                            remember_last_spot = antwalk.remove_last()
                            follow_route = antwalk.subtract_direction(self.int_to_dir(remember_last_spot))
                        # Add the entrance of a forbidden zone
                        forbidden_zone.append(follow_route.add_direction(self.int_to.dir(remember_last_spot)))
                        

                    # Ants shouldn't go back
                    possibilities.remove(remember_last_spot)

                    number = np.random.choice(possibilities)
                    direction = self.int_to_dir(number)
                    new_coordinate = follow_route.add_direction(direction)

                    if (self.maze.in_bounds(new_coordinate) and self.maze.walls[new_coordinate.x][new_coordinate.y] != 0):
                        follow_route = new_coordinate
                        antwalk.add(direction)
                        # remember the reverse of the current direction. 
                        remember_last_spot = Direction.reverse(number)
                        break
                    else:
                        possibilities.remove(number)
                        

                        #     while(intWalk.size() != 4):
                        #         new_int = np.random.randint(0, 4)
                        #         if(not intWalk.contains(new_int)):

                        # if(antwalk.size() > 0):
                        #     antwalk.remove_last()
                        # antwalk.add(new_direction.dir_to_coordinate_delta(direction))
                    
                    # antwalk.add(direction)
                    #follow_route = start.add_coordinate(direction)
        return antwalk

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
    #parameters
    gen = 1
    no_gen = 1
    q = 1600
    evap = 0.1

    #construct the optimization objects
    maze = Maze.create_maze("./../data/easy maze.txt")
    # print(maze)
    spec = PathSpecification.read_coordinates("./../data/easy coordinates.txt")
    aco = AntColonyOptimization(maze, gen, no_gen, q, evap)

    #save starting time
    start_time = int(round(time.time() * 1000))

    #run optimization
    shortest_route = aco.find_shortest_route(spec)

    #print time taken
    print("Time taken: " + str((int(round(time.time() * 1000)) - start_time) / 1000.0))

    # print(shortest_route)
    #save solution!!!!!
    shortest_route.write_to_file("./../data/easy_solution.txt")

    #print route size
    print("Route size: " + str(shortest_route.size()))