import numpy as np
import sys as sys
from Action import Action
class MyEGreedy:

    def __init__(self):
        print("Made EGreedy")

    def get_random_action(self, agent, maze):
        possible_actions = maze.get_valid_actions(agent)
        action = possible_actions[np.random.randint(len(possible_actions))]
        return action

    def get_best_action(self, agent, maze, q_learning):
        actions = maze.get_valid_actions(agent)
        action_values = q_learning.get_action_values(agent.get_state(maze), actions)
        best_act_val = 0
        best_indexes_arr = []
        for i in range(len(action_values)):
            if(action_values[i] > best_act_val):
                best_indexes_arr = []
                best_act_val = action_values[i]
                best_indexes_arr.append(i)
            elif(action_values[i] == best_act_val):
                best_indexes_arr.append(i)
        random_best_action = np.random.randint(len(best_indexes_arr))
        return actions[best_indexes_arr[random_best_action]]

    def get_egreedy_action(self, agent, maze, q_learning, epsilon):
        if (np.random.uniform(0, 1) < epsilon): 
            return self.get_random_action(agent, maze)
        return self.get_best_action(agent, maze, q_learning)

