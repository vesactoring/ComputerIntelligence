class Action:

    def __init__(self, action_id):
        # the action id is simply the identifier of the type of action, such as up down left etc...
        self.id = str(action_id)

    def __str__(self):
        return str(self.id)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
