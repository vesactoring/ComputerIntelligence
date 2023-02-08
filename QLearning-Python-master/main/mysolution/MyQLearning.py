from QLearning import QLearning


class MyQLearning(QLearning):

    def update_q(self, state, action, r, state_next, possible_actions, alpha, gamma):
        best_action_q = self.get_q(state_next, possible_actions[0])

        for i in possible_actions:
            if (best_action_q < self.get_q(state_next, i)):
                best_action_q = self.get_q(state_next, i)

        result = self.get_q(state, action) + alpha*(r + (gamma * best_action_q) - self.get_q(state, action))

        return result
