from service.Service import *


class MinimaxAlphaBeta:
    def __init__(self, turn='1'):
        self.turn = turn
        self.minimax_tree = list()

    def maximize(self, state, alpha, beta, K):
        # terminal state
        if K == 0:
            return None, eval(state)

        max_child = None
        max_utility = -float('inf')

        for child in get_children(state, self.turn):
            _, utility = self.minimize(child, alpha, beta, K - 1)
            if utility > max_utility:
                max_utility = utility
                max_child = child

            if max_utility >= beta:
                break

        return max_child, max_utility

    def minimize(self, state, alpha, beta, K):
        # terminal state
        if K == 0:
            return None, eval(state)

        min_child = None
        min_utility = float('inf')

        for child in get_children(state, str(1 - int(self.turn))):
            _, utility = self.maximize(child, alpha, beta, K - 1)
            if utility < min_utility:
                min_utility = utility
                min_child = child

            if min_utility <= alpha:
                break

        return min_child, min_utility

    def print_minimax_tree(self, state):
        # TODO -> printing the minimax tree
        pass
