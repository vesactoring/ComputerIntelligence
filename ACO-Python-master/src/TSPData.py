import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import pickle
import re
import traceback
from src.AntColonyOptimization import AntColonyOptimization
from src.Coordinate import Coordinate
from src.Maze import Maze
from src.PathSpecification import PathSpecification

# Class containing the product distances. Can be either build from a maze, a product
# location list and a PathSpecification or be reloaded from a file.
class TSPData:

    # Constructs a new TSP data object.
    # @param productLocations the productlocations.
    # @param spec the path specification.
    def __init__(self, product_locations, spec):
        self.product_locations = product_locations
        self.spec = spec

        self.distances = None
        self.start_distances = None
        self.end_distances = None
        self.product_to_product = None
        self.start_to_product = None
        self.product_to_end = None

    # Calculate the routes from the product locations to each other, the start, and the end.
    # Additionally generate arrays that contain the length of all the routes.
    # @param maze
    def calculate_routes(self, aco):
        self.product_to_product = self.build_distance_matrix(aco)
        self.start_to_product = self.build_start_to_products(aco)
        self.product_to_end = self.build_products_to_end(aco)
        self.build_distance_lists()
        return

    # Build a list of integer distances of all the product-product routes.
    def build_distance_lists(self):
        number_of_products = len(self.product_locations)
        self.distances = []
        self.start_distances = []
        self.end_distances = []

        for i in range(number_of_products):
            self.distances.append([])
            for j in range(number_of_products):
                self.distances[i].append(self.product_to_product[i][j].size())
            self.start_distances.append(self.start_to_product[i].size())
            self.end_distances.append(self.product_to_end[i].size())
        return

    # Distance product to product getter
    # @return the list
    def get_distances(self):
        return self.distances

    # Distance start to product getter
    # @return the list
    def get_start_distances(self):
        return self.start_distances

    # Distance product to end getter
    # @return the list
    def get_end_distances(self):
        return self.end_distances

    # Equals method
    # @param other other TSPData to check
    # @return boolean whether equal
    def __eq__(self, other):
        return self.distances == other.distances \
               and self.product_to_product == other.product_to_product \
               and self.product_to_end == other.product_to_end \
               and self.start_to_product == other.start_to_product \
               and self.spec == other.spec \
               and self.product_locations == other.product_locations

    # Persist object to file so that it can be reused later
    # @param filePath Path to persist to
    def write_to_file(self, file_path):
        pickle.dump(self, open(file_path, "wb"))

    # Write away an action file based on a solution from the TSP problem.
    # @param productOrder Solution of the TSP problem
    # @param filePath Path to the solution file
    def write_action_file(self, product_order, file_path):
        total_length = self.start_distances[product_order[0]]
        for i in range(len(product_order) - 1):
            frm = product_order[i]
            to = product_order[i + 1]
            total_length += self.distances[frm][to]

        total_length += self.end_distances[product_order[len(product_order) - 1]] + len(product_order)

        string = ""
        string += str(total_length)
        string += ";\n"
        string += str(self.spec.get_start())
        string += ";\n"
        string += str(self.start_to_product[product_order[0]])
        string += "take product #"
        string += str(product_order[0] + 1)
        string += ";\n"

        for i in range(len(product_order) - 1):
            frm = product_order[i]
            to = product_order[i + 1]
            string += str(self.product_to_product[frm][to])
            string += "take product #"
            string += str(to + 1)
            string += ";\n"
        string += str(self.product_to_end[product_order[len(product_order) - 1]])

        f = open(file_path, "w")
        f.write(string)

    # Calculate the optimal routes between all the individual routes
    # @param maze Maze to calculate optimal routes in
    # @return Optimal routes between all products in 2d array
    def build_distance_matrix(self, aco):
        number_of_product = len(self.product_locations)
        product_to_product = []
        for i in range(number_of_product):
            product_to_product.append([])
            for j in range(number_of_product):
                start = self.product_locations[i]
                end = self.product_locations[j]
                product_to_product[i].append(aco.find_shortest_route(PathSpecification(start, end)))
        return product_to_product


    # Calculate optimal route between the start and all the products
    # @param maze Maze to calculate optimal routes in
    # @return Optimal route from start to products
    def build_start_to_products(self, aco):
        start = self.spec.get_start()
        start_to_products = []
        for i in range(len(self.product_locations)):
            start_to_products.append(aco.find_shortest_route(PathSpecification(start, self.product_locations[i])))
        return start_to_products

    # Calculate optimal routes between the products and the end point
    # @param maze Maze to calculate optimal routes in
    # @return Optimal route from products to end
    def build_products_to_end(self, aco):
        end = self.spec.get_end()
        products_to_end = []
        for i in range(len(self.product_locations)):
            products_to_end.append(aco.find_shortest_route(PathSpecification(self.product_locations[i], end)))
        return products_to_end

    # Load TSP data from a file
    # @param filePath Persist file
    # @return TSPData object from the file
    @staticmethod
    def read_from_file(file_path):
        return pickle.load(open(file_path, "rb"))

    # Read a TSP problem specification based on a coordinate file and a product file
    # @param coordinates Path to the coordinate file
    # @param productFile Path to the product file
    # @return TSP object with uninitiatilized routes
    @staticmethod
    def read_specification(coordinates, product_file):
        try:
            f = open(product_file, "r")
            lines = f.read().splitlines()

            firstline = re.compile("[:,;]\\s*").split(lines[0])
            product_locations = []
            number_of_products = int(firstline[0])
            for i in range(number_of_products):
                line = re.compile("[:,;]\\s*").split(lines[i + 1])
                product = int(line[0])
                x = int(line[1])
                y = int(line[2])
                product_locations.append(Coordinate(x, y))
            spec = PathSpecification.read_coordinates(coordinates)
            return TSPData(product_locations, spec)
        except FileNotFoundError:
            print("Error reading file " + product_file)
            traceback.print_exc()
            sys.exit()

# Assignment 2.a
if __name__ == "__main__":
    #parameters
    gen = 1
    no_gen = 1
    q = 1000
    evap = 0.1
    persist_file = "./../tmp/productMatrixDist"
    tsp_path = "./../data/tsp products.txt"
    coordinates = "./../data/hard coordinates.txt"
        
    #construct optimization
    maze = Maze.create_maze("./../data/hard maze.txt")
    pd = TSPData.read_specification(coordinates, tsp_path)
    aco = AntColonyOptimization(maze, gen, no_gen, q, evap)
        
    #run optimization and write to file
    pd.calculate_routes(aco)
    pd.write_to_file(persist_file)
        
    #read from file and print
    pd2 = TSPData.read_from_file(persist_file)
    print(pd == pd2)