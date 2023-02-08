class QLearning:

    def __init__(self):
        # dictionary (State, <Action, Value>)
        self.q = {}

    def get_q(self, state, action):
        # checks if it can find a value for <s,a> in q and returns it, if not return 0.
        try:
            action_values = self.q[state]
            try:
                value = action_values[action]
                return value
            except KeyError:
                return 0
        except KeyError:
            return 0

    def set_q(self, state, action, value):
        # sets the value of am <s,a> pair to q
        try:
            action_values = self.q[state]
            float_value = float(value)
            action_values[action] = float_value
        except KeyError:
            # no entry known for s, make one and store the action value too
            action_values = {}
            float_value = float(value)
            action_values[action] = float_value
            self.q[state] = action_values

    def get_action_values(self, state, actions):
        # returns the associated action values for all actions in <actions> in that order;
        result = []
        for action in actions:
            result.append(self.get_q(state, action))
        return result
