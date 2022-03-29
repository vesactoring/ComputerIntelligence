import traceback
import sys
from main.Action import Action
from main.State import State


class Maze:

    def __init__(self, file):
        # to build a 2-d maze from a file
        up = Action("up")
        down = Action("down")
        left = Action("left")
        right = Action("right")
        self.actions = [up, down, left, right]
        self.states = []
        # read in file
        try:
            f = open(file, "r")
            lines = f.read().splitlines()
            dimensions = lines[0].split(" ")
            w = int(dimensions[0])
            h = int(dimensions[1])
            y = 0
            for i in range(1, h + 1):
                line = lines[i].split(" ")
                states = []
                self.states.append(states)
                x = 0
                for j in range(0, w):
                    if line[j] != "":
                        state = State(x, y, line[j])
                        states.append(state)
                        x += 1
                y += 1
        except FileNotFoundError:
            print("Error reading maze file " + file)
            traceback.print_exc()
            sys.exit()
        print("Ready reading maze file " + file)
        self.rewards = {}

    def is_walkable(self, state):
        # the maze's way to check if you can walk on a particular state
        # you dont need to use this directly, use the method getValidActions()
        return state.type == "1"

    def get_valid_actions(self, agent):
        # use this method to retrieve the list of possible actions for an agent
        # the method checks if surrounding states are "walkable" and if the agent is not going out of the maze dimensions.
        # The method returns the list of actions
        action_list = []
        if agent.y > 0 and self.is_walkable(self.states[agent.y-1][agent.x]):
            action_list.append(self.actions[0])
        if agent.y < len(self.states)-1 and self.is_walkable(self.states[agent.y + 1][agent.x]):
            action_list.append(self.actions[1])
        if agent.x > 0 and self.is_walkable(self.states[agent.y][agent.x - 1]):
            action_list.append(self.actions[2])
        if agent.x < len(self.states[agent.y]) - 1 and self.is_walkable(self.states[agent.y][agent.x + 1]):
            action_list.append(self.actions[3])
        return action_list

    def set_reward(self, state, reward):
        # use this method to set the reward of the end state to the value in teh excercise
        # you can also play around with setting other states to a non-0 reward.
        # this is called reward shaping, and you can speed up the learning but also
        # teach the agent a suboptimal solution inadvertible.
        self.rewards[state] = float(reward)

    def get_reward(self, state):
        if state in self.rewards:
            return float(self.rewards[state])
        else:
            return 0

    def get_state(self, x, y):
        # simply returns the state at the location the agent is at
        # use this to find the current state of the agent, or use Agent.getState(Maze m)
        return self.states[y][x]