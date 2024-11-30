from service.Service import *


class Expectiminimax:

    def __init__(self):
       self.minimax_tree = []

    def decision(self, state, k):
        self.minimax_tree = []
        for i in range(k + 1):
            self.minimax_tree.append({})

        return self.maximize(state, k)
    
    def maximize(self, state, k):
        if k <= 0:
            self.minimax_tree[k][int(state)] = eval(state)
            return None, self.minimax_tree[k][int(state)]

        max_child = None
        max_utility = -float("inf")

        for child, chosen_column in get_children(state, "2"):
            _, utility = self.minimize(child, k - 1, chosen_column)

            if utility > max_utility:
                max_utility = utility
                max_child = child

        self.minimax_tree[k][int(state)] = max_utility
        return max_child, max_utility

    def minimize(self, state, k, chosen_column):
        if k <= 0:
            self.minimax_tree[k][int(state)] = eval(state)
            return None, self.minimax_tree[k][int(state)]

        min_child = None
        min_utility = float("inf")

        for child, prob in get_children_probability(state, chosen_column):
            _, utility = self.maximize(child, k - 2)

            if prob * utility < min_utility:
                min_utility = prob * utility
                min_child = child

        self.minimax_tree[k][int(state)] = min_utility
        return min_child, min_utility
    
    def get_minimax_tree(self):
        """
        Retrieve the Minimax tree built during the decision-making process.

        This tree represents all the possible states explored by the Minimax algorithm.

        Returns:
            list: A list representing the Minimax tree.
        """
        self.minimax_tree.reverse()
        return self.minimax_tree
