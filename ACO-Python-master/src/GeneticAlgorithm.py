import os, sys

from sklearn.utils import shuffle
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import random
import numpy as np
from src.TSPData import TSPData

# TSP problem solver using genetic algorithms.
class GeneticAlgorithm:

    # Constructs a new 'genetic algorithm' object.
    # @param generations the amount of generations.
    # @param popSize the population size.
    def __init__(self, generations, pop_size):
        self.generations = generations
        self.pop_size = pop_size

     # Knuth-Yates shuffle, reordering a array randomly
     # @param chromosome array to shuffle.
    def shuffle(self, chromosome):
        n = len(chromosome)
        for i in range(n):
            r = i + int(random.uniform(0, 1) * (n - i))
            swap = chromosome[r]
            chromosome[r] = chromosome[i]
            chromosome[i] = swap
        return chromosome

    # This method should solve the TSP.
    # @param pd the TSP data.
    # @return the optimized product sequence.
    def solve_tsp(self, tsp_data):
        list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17]
        p_cross = 0.7
        p_mutate = 0.1
        population = []
        for i in range(self.pop_size):
            population.append(shuffle(list))
        # print(population)
        for i in range(self.generations):
            population = self.select(population, p_cross, p_mutate, tsp_data)
        population = sorted(population, key = lambda chromosome: self.fitness(chromosome, tsp_data))
        # print("FIRST: ", self.fitness(population[0], tsp_data))
        # print("SECOND: ", self.fitness(population[1], tsp_data))
        # print("LAST: ", self.fitness(population[17], tsp_data))
        # print("LENGTH: ", len(population))
        return population[0]


    def fitness(self, gene, tsp_data):
        gene_fitness = tsp_data.get_start_distances()[gene[0]]
        for i in range(1, len(gene)):
            gene_fitness += tsp_data.get_distances()[gene[i-1]][gene[i]]
        gene_fitness += tsp_data.get_end_distances()[len(gene)]
        return gene_fitness
    
    def crossover(self, chromosome1, chromosome2, p_cross_over):
        if(len(chromosome1) != len(chromosome2)):
            raise ValueError("Chromosomes are not of equal length")
        
        number = random.uniform(0, 1)
        # print("Number: ", number)
        
        # print("PARENT 1: ", chromosome1)
        # print("PARENT 2: ", chromosome2)
        if(number <= p_cross_over):
            crossover_line = np.random.randint(1,len(chromosome1)-1)
            # print("LINE: ", crossover_line)
            child_1 = chromosome1[0:crossover_line]
            child_2 = chromosome2[0:crossover_line]
            for i in chromosome2:
                if(i not in child_1):
                    child_1.append(i)

            for i in chromosome1:
                if(i not in child_2):
                    child_2.append(i)
            
            return child_1, child_2
        else:
            return chromosome1, chromosome2
        
    
    def select(self, population, p_cross_over, p_mutation, tsp_data):
        offSprings = []
        population = sorted(population, key = lambda chromosome: self.fitness(chromosome, tsp_data))
        offSprings.append(population[0])
        offSprings.append(population[1])
        for i in range(int((self.pop_size)/2) - 1):
            pairs = random.choices(population = population, weights = reversed([self.fitness(parent, tsp_data) for parent in population]), k = 2)
            # print("PAIRS: ", pairs, "In iteration: ", str(i))
            child1, child2 = (self.crossover(pairs[0], pairs[1], p_cross_over))
            offSprings.append(child1)
            offSprings.append(child2)
        #     print("CHILD1: ", child1)
        #     print("CHILD2: ", child2)
        # print(offSprings)
        for i, kid in enumerate(offSprings): 
            number = random.uniform(0, 1)
            if(number <= p_mutation):
                offSprings[i] = shuffle(kid)
        
        return offSprings

# Assignment 2.b
# The Genetic algorithm will take a population size and amount of generations as parameters.
# After creating the productMatrixdist file in TSPData, which contains all distances from a product to another product + all distances from start of maze to products + all distances from end of maze to products.
# We will use this file also as a parameter to find the near-optimal solution of the shortest path for getting all the products (by referencing to it).
# We will start with population size x amount of random routes,
# Calculate the fitness of each of these random routes, 
# Keep 2 of the shortest routes and then crossover x-2 childroutes with possible mutated childroutes.
# We will do this for y amount of generations and return the shortest route found by then.
if __name__ == "__main__":
    #parameters
    population_size = 20
    generations = 40
    persistFile = "data\productMatrixDist"
        
    #setup optimization
    tsp_data = TSPData.read_from_file(persistFile)
    # print(tsp_data.get_end_distances())
    ga = GeneticAlgorithm(generations, population_size)

    #run optimization and write to file
    solution = ga.solve_tsp(tsp_data)
    tsp_data.write_action_file(solution, "data/tsp solution.txt")
