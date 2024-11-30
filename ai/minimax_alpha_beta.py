from service.Service import get_children, eval


class MinimaxAlphaBeta:
    """
    Minimax algorithm with alpha-beta pruning.
    This algorithm improves the basic Minimax by pruning branches of the game tree
    that cannot influence the final decision, improving efficiency.
    """

    def __init__(self):
        self.minimax_tree = []

    def decision(self, state, k):
        """
        Decide the best move based on the current game state using the alpha-beta pruning technique.

        Args:
            state (int): The current state of the game represented as an integer.
            k (int): The depth of the search tree, which limits how many moves ahead to explore.

        Returns:
            tuple: A tuple containing the best child state (next move) and its associated utility value.
        """
        self.minimax_tree = []
        for i in range(k + 1):
            self.minimax_tree.append({})

        return self.maximize(state, -float("inf"), float("inf"), k)

    def maximize(self, state, alpha, beta, k):
        """
        Maximize the utility of the game state by selecting the best possible move for the current player
        using alpha-beta pruning to eliminate branches that do not need to be explored.

        Args:
            state (int): The current state of the game represented as an integer.
            alpha (float): The best value the maximizing player can guarantee so far.
            beta (float): The best value the minimizing player can guarantee so far.
            k (int): The depth of the search tree.

        Returns:
            tuple: A tuple containing the best child state (next move) and its maximum utility value.
        """
        # Terminal state (leaf node in the game tree)
        if k == 0:
            self.minimax_tree[k][int(state)] = eval(state)
            return None, self.minimax_tree[k][int(state)]

        max_child = None
        max_utility = -float("inf")

        for child in get_children(state, "2"):
            _, utility = self.minimize(child, alpha, beta, k - 1)
            if utility > max_utility:
                max_utility = utility
                max_child = child

            # Alpha-beta pruning: if the utility is greater than or equal to beta, stop exploring further
            if max_utility >= beta:
                break

            # Update alpha
            alpha = max(alpha, max_utility)

        self.minimax_tree[k][int(state)] = max_utility
        return max_child, max_utility

    def minimize(self, state, alpha, beta, k):
        """
        Minimize the utility of the game state by selecting the best possible move for the opponent
        using alpha-beta pruning to eliminate branches that do not need to be explored.

        Args:
            state (int): The current state of the game represented as an integer.
            alpha (float): The best value the maximizing player can guarantee so far.
            beta (float): The best value the minimizing player can guarantee so far.
            k (int): The depth of the search tree.

        Returns:
            tuple: A tuple containing the best child state (next move for the opponent) and its minimum utility value.
        """
        # Terminal state (leaf node in the game tree)
        if k == 0:
            self.minimax_tree[k][int(state)] = eval(state)
            return None, self.minimax_tree[k][int(state)]

        min_child = None
        min_utility = float("inf")

        for child in get_children(state, "1"):
            _, utility = self.maximize(child, alpha, beta, k - 1)
            if utility < min_utility:
                min_utility = utility
                min_child = child

            # Alpha-beta pruning: if the utility is less than or equal to alpha, stop exploring further
            if min_utility <= alpha:
                break

            # Update beta
            beta = min(beta, min_utility)

        self.minimax_tree[k][int(state)] = min_utility
        return min_child, min_utility

    def get_minimax_tree(self):
        """
        Retrieve the Minimax alpha-beta pruning tree built during the decision-making process.

        This tree represents all the possible states explored by the Minimax algorithm with alpha-beta pruning.

        Returns:
            list: A list representing the Minimax tree.
        """
        self.minimax_tree.reverse()
        return self.minimax_tree
