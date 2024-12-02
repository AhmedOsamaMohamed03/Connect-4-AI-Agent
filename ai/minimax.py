from service.Service import get_children, eval


class Minimax:
    """
    Minimax algorithm class.
    The algorithm computes the best move for the player by evaluating
    all possible moves using the Minimax approach without alpha-beta pruning.
    """

    def __init__(self):
        self.minimax_tree = []

    def decision(self, state: int, k: int):
        """
        Decide the best move based on the current game state.

        This method initiates the maximization process and returns the optimal move.

        Args:
            state (int): The current state of the game represented as an integer.
            k (int): The depth of the search tree, which limits how many moves ahead to look.

        Returns:
            tuple: A tuple containing the best child state (next move) and its associated utility value.
        """
        self.minimax_tree = []
        for i in range(k):
            self.minimax_tree.append({})

        return self.maximize(state, k)

    def maximize(self, state: int, k: int):
        """
        Maximize the utility of the game state by selecting the best possible move.

        This method recursively explores the game tree and selects the child state with the maximum utility.

        Args:
            state (int): The current state of the game represented as an integer.
            k (int): The depth of the search tree.

        Returns:
            tuple: A tuple containing the best child state (next move) and its maximum utility value.
        """
        # Terminal state (leaf node in the game tree)
        if k == 1:
            self.minimax_tree[k-1][int(state)] = eval(state)
            return None, self.minimax_tree[k-1][int(state)]

        max_child = None
        max_utility = -float("inf")

        for child, _ in get_children(state, "2"):
            _, utility = self.minimize(child, k - 1)

            if utility > max_utility:
                max_utility = utility
                max_child = child

        self.minimax_tree[k-1][int(state)] = max_utility
        return max_child, max_utility

    def minimize(self, state: int, k: int):
        """
        Minimize the utility of the game state by selecting the best possible move for the opponent.

        This method recursively explores the game tree and selects the child state with the minimum utility.

        Args:
            state (int): The current state of the game represented as an integer.
            k (int): The depth of the search tree.

        Returns:
            tuple: A tuple containing the best child state (next move for the opponent) and its minimum utility value.
        """
        # Terminal state (leaf node in the game tree)
        if k == 1:
            self.minimax_tree[k-1][int(state)] = eval(state)
            return None, self.minimax_tree[k-1][int(state)]

        min_child = None
        min_utility = float("inf")

        for child, _ in get_children(state, "1"):
            _, utility = self.maximize(child, k - 1)

            if utility < min_utility:
                min_utility = utility
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
