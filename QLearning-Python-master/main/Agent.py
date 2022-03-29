class Agent:

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.x = start_x
        self.y = start_y
        self.nr_of_actions_since_reset = 0

    def get_state(self, maze):
        return maze.get_state(self.x, self.y)

    def do_action(self, action, maze):
        # executes an action and returns the new State the agent is in according to the Maze
        self.nr_of_actions_since_reset += 1
        if action.id == "up":
            self.y -= 1
        if action.id == "down":
            self.y += 1
        if action.id == "left":
            self.x -= 1
        if action.id == "right":
            self.x += 1
        return self.get_state(maze)

    def reset(self):
        print(self.nr_of_actions_since_reset)
        self.x = self.start_x
        self.y = self.start_y
        self.nr_of_actions_since_reset = 0
