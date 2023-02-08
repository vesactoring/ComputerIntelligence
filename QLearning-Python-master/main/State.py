class State:
    def __init__(self, x, y, state_type):
        self.x = x
        self.y = y
        # the type of the state is a 0 or a 1, 1 being path, 0 being the wall
        self.type = str(state_type)

    def __str__(self):
        return "State(x: " + str(self.x) + ", y: " + str(self.y) + ", " + str(self.type) + ")"

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
