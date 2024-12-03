from service.Service import *


class Expectiminimax:

    def __init__(self):
       self.minimax_tree = []
       self.parent = {}

    def decision(self, state, k, column):
        self.minimax_tree = []
        for i in range(k):
            self.minimax_tree.append({})

        return self.maximize(state, k, column)
    
    def maximize(self, state, k, opponent_chosen_column):
        if k <= 1:
            self.minimax_tree[k-1][int(state)] = eval(state)
            return None, self.minimax_tree[k-1][int(state)]
       
        max_child = None
        max_utility = -float("inf")

        for child, prob, chosen_column in get_children_probability(state, "2", opponent_chosen_column):
            _, utility = self.minimize(child, k - 2, chosen_column)
            self.parent[child] = state

            if prob*utility > max_utility:
                max_utility = prob*utility
                max_child = child

        self.minimax_tree[k-1][int(state)] = max_utility
        return max_child, max_utility

    def minimize(self, state, k, opponent_chosen_column):
        if k <= 1:
            self.minimax_tree[k-1][int(state)] = eval(state)
            return None, self.minimax_tree[k-1][int(state)]

        min_child = None
        min_utility = float("inf")

        for child, prob, chosen_column in get_children_probability(state, "1", opponent_chosen_column):
            _, utility = self.maximize(child, k - 2, chosen_column)
            self.parent[child] = state

            if prob * utility < min_utility:
                min_utility = prob * utility
                min_child = child

        self.minimax_tree[k-1][int(state)] = min_utility
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
    
    def get_parent(self):
        return self.parent

