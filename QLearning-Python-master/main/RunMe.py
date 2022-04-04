
from Maze import Maze
from Agent import Agent
from mysolution.MyQLearning import MyQLearning
from mysolution.MyEGreedy import MyEGreedy

def run(maze, robot, selection, learn, max_steps, alpha, epsilon, gamma, decay= None):
    trials = 0
    total_number_of_steps_before_reset = 0
    number_of_steps = 0
    final_path_length = -1

    # Continuous looping/learning until the max amount of steps is reached
    while (number_of_steps < max_steps):
        if (maze.get_reward(robot.get_state(maze)) > 0):
            trials += 1
            final_path_length = total_number_of_steps_before_reset
            total_number_of_steps_before_reset = 0
       
            epsilon = (1-decay) * epsilon
            robot.reset()
        else:
            action = selection.get_egreedy_action(robot, maze, learn, epsilon)
            state = robot.get_state(maze)
            next_state = robot.do_action(action, maze)
            total_number_of_steps_before_reset += 1
            number_of_steps += 1
            reward = maze.get_reward(next_state)
            new_q = learn.update_q(state, action, reward, next_state, maze.get_valid_actions(robot), alpha, gamma)
            
            learn.set_q(state, action, new_q)
    return final_path_length


if __name__ == "__main__":
    # load the maze
    # replace this with the location to your maze on your file system
    file = "../data/toy_maze.txt"
    maze = Maze(file)

    # Set the reward at the bottom right to 10
    maze.set_reward(maze.get_state(9, 9), 10)
    # Set second reward/goal to 5
    # maze.set_reward(maze.get_state(9, 0), 5)

    # create a robot at starting and reset location (0,0) (top left)
    robot = Agent(0, 0)

    # make a selection object (you need to implement the methods in this class)
    selection = MyEGreedy()

    # make a Qlearning object (you need to implement the methods in this class)
    learn = MyQLearning()
    
    # parameters
    total_steps_before_reset = 0
    max_steps = 30000
    trials = 0
    epsilon = 0.1
    alpha = 0.9
    gamma = 0.7
    decay = 0.001
    
    # prints final path, if none is found, then returns -1
    print("Length of the final path: ", run(maze , robot, selection, learn, max_steps, alpha, epsilon, gamma, decay))

    
    
    
    
        




