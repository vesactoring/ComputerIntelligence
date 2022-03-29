from main.Maze import Maze
from main.Agent import Agent
from main.mysolution.MyQLearning import MyQLearning
from main.mysolution.MyEGreedy import MyEGreedy

if __name__ == "__main__":
    # load the maze
    # TODO replace this with the location to your maze on your file system
    file = "..\\..\\data\\toy_maze.txt"
    maze = Maze(file)

    # Set the reward at the bottom right to 10
    maze.set_reward(maze.get_state(9, 9), 10)

    # create a robot at starting and reset location (0,0) (top left)
    robot = Agent(0, 0)

    # make a selection object (you need to implement the methods in this class)
    selection = MyEGreedy()

    # make a Qlearning object (you need to implement the methods in this class)
    learn = MyQLearning()

    stop = False

    # keep learning until you decide to stop
    while not stop:
        # TODO implement the action selection and learning cycle

        # TODO figure out a stopping criterion
