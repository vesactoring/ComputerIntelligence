import numpy as np
from Action import Action
class MyEGreedy:

    def __init__(self):
        print("Made EGreedy")

    def get_random_action(self, agent, maze):
        # TODO to select an action at random in State s
        possible_actions = maze.get_valid_actions(agent)
        action = possible_actions[np.random.randint(len(possible_actions))]
        return action

    def get_best_action(self, agent, maze, q_learning):
        # TODO to select the best possible action currently known in State s.
        max = 0
        actions = maze.get_valid_actions(agent)
        action = None
        for i in actions:
            if max < q_learning.get_q(agent.get_state(maze), i):
                max = q_learning.get_q(agent.get_state(maze), i)
                action = i
        return action

    def get_egreedy_action(self, agent, maze, q_learning, epsilon):
        # TODO to select between random or best action selection based on epsilon.
        if (np.random.uniform(0, 1) < epsilon): 
            return self.get_random_action(agent, maze)
        return self.get_best_action(agent, maze, q_learning)

