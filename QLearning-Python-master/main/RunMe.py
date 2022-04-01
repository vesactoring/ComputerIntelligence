
# import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from Maze import Maze
from Agent import Agent
from mysolution.MyQLearning import MyQLearning
from mysolution.MyEGreedy import MyEGreedy
import matplotlib.pyplot as plt

def run(maze, robot, selection, learn, max_steps, alpha, epsilon, gamma, decay= None):
    # keep learning until you decide to stop
    trials = 0
    total_number_of_steps_before_reset = 0
    number_of_steps = 0
    sum_of_trial_steps = 0
    while (number_of_steps < 30000):
        if (maze.get_reward(robot.get_state(maze)) > 0):
            trials += 1
            sum_of_trial_steps += total_number_of_steps_before_reset
            total_number_of_steps_before_reset = 0
            # Q11
            # epsilon = (1-decay) * epsilon
            robot.reset()
        else:
            action = selection.get_egreedy_action(robot, maze, learn, epsilon)
            state = robot.get_state(maze)
            next_state = robot.do_action(action, maze)
            total_number_of_steps_before_reset += 1
            number_of_steps += 1
            # self, state, action, r, state_next, possible_actions, alfa, gamma
            reward = maze.get_reward(next_state)
            new_q = learn.update_q(state, action, reward, next_state, maze.get_valid_actions(robot), alpha, gamma)
            
            learn.set_q(state, action, new_q)
    return trials, sum_of_trial_steps / trials



    # for i in trials:
    #     # TODO implement the action selection and learning cycle'
    #     rewards_current_episode = 0
    #     for steps in range(max_steps):
    #         action = selection.get_egreedy_action(robot, maze, learn, epsilon)
    #         state = robot.get_state(maze)
    #         next_state = robot.do_action(action, maze)
    #         # self, state, action, r, state_next, possible_actions, alfa, gamma
    #         reward = maze.get_reward(next_state)
    #         new_q = learn.update_q(state, action, reward, next_state, maze.get_valid_actions(robot), alpha, gamma)
    #         learn.set_q(state, action, new_q)
    #         rewards_current_episode += reward
        # return 
        # TODO figure out a stopping criterion

if __name__ == "__main__":
    # load the maze
    # TODO replace this with the location to your maze on your file system
    file = "../data/easy_maze.txt"
    maze = Maze(file)

    # Set the reward at the bottom right to 10
    maze.set_reward(maze.get_state(9, 9), 10)
    # Set second reward/goal
    # maze.set_reward(maze.get_state(9, 0), 5)

    # create a robot at starting and reset location (0,0) (top left)
    robot = Agent(0, 0)

    # make a selection object (you need to implement the methods in this class)
    selection = MyEGreedy()

    # make a Qlearning object (you need to implement the methods in this class)
    learn = MyQLearning()
    
    # parameters
    # trialalphaalpha
    total_steps_before_reset = 0
    max_steps = 30000
    trials = 0
    epsilon = 0.1
    alpha = 0.8
    gamma = 0.7
    stop = False
    decay = 0.1
    
    x_lab = []
    y = []

    for i in range(10):
        trials, avg = run(maze , robot, selection, learn, max_steps, alpha, epsilon, gamma)
        x_lab.append(trials)
        y.append(avg)
    
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.xticks(ticks=x, labels=x_lab)
    plt.xlabel("Amount of trials")
    plt.ylabel("Average length per trial")
    plt.title("Alpha: 0.8")
    ax = plt.gca()
    ax.set_ylim([0, 4000])
    plt.plot(x, y)
    plt.show

    
    
    
    
        




