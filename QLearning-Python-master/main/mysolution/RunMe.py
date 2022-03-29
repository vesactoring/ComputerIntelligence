from sympy import false
from main.Maze import Maze
from main.Agent import Agent
from main.mysolution.MyQLearning import MyQLearning
from main.mysolution.MyEGreedy import MyEGreedy

def run(maze, robot, selection, learn, max_steps, alpha, epsilon, gamma):
    # keep learning until you decide to stop
    trials = 0
    total_number_of_steps_before_reset = 0
    number_of_steps = 0
    while (number_of_steps < 30000):
        if (maze.get_reward(robot.get_stage(maze) == 10)):
            trials += 1
            print(total_number_of_steps_before_reset)
            total_number_of_steps_before_reset = 0
            robot.reset()
        else:
            action = selection.get_egreedy_action(robot, maze, learn, epsilon)
            state = robot.get_state(maze)
            next_state = robot.do_action(action, maze)
            total_number_of_steps_before_reset += 1
            number_of_steps += 1
            # self, state, action, r, state_next, possible_actions, alfa, gamma
            reward = maze.get_reward(next_state)
            # new_q = learn.update_q(state, action, reward, next_state, maze.get_valid_actions(robot), alpha, gamma)
            
            # learn.set_q(state, action, new_q)
            rewards_current_episode += reward



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
    file = ".\data\toy_maze.txt"
    maze = Maze(file)

    # Set the reward at the bottom right to 10
    maze.set_reward(maze.get_state(9, 9), 10)

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
    trials = 
    epsilon = 0.5
    alpha = 0.1
    gamma = 0.7
    stop = False
    
    run(maze , robot, selection, learn, max_steps, alpha, epsilon, gamma)

    

    
    
    
    
        




