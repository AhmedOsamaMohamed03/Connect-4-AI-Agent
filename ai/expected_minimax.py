from service.Service import *


class Expectiminimax:
    def _init_(self, turn='0'):
        self.turn = turn

    def maximize(self, state, k):
        if k <= 0:
            return None, eval(state)

        max_child = None
        max_utility = -float("inf")

        for child, chosen_column in get_children(state, "2"):
            _, utility = self.minimize(child, k - 1, chosen_column)

            if utility > max_utility:
                max_utility = utility
                max_child = child

        return max_child, max_utility

    def minimize(self, state, k, chosen_column):
        if k <= 0:
            return None, eval(state)

        min_child = None
        min_utility = float("inf")

        for child, prob in get_children_probability(state, "1", chosen_column):
            _, utility = self.maximize(child, k - 2)

            if prob * utility < min_utility:
                min_utility = prob * utility
                min_child = child

        return min_child, min_utility

    def decision(self, state, k):
        return self.maximize(state, k)
