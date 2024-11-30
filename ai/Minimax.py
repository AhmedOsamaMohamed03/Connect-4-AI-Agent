from service.Service import get_children, eval


class Minimax:
    """
    Minimax algorithm class.
    The algorithm computes the best move for the player by evaluating
    all possible moves using the Minimax approach without alpha-beta pruning.
    """

    def __init__(self, turn="0"):
        """
        Initialize the Minimax agent.

        Args:
            turn (str): The agent's turn, either '0' or '1'. Default is '0'.
        """
        self.turn = turn
        self.minimax_tree = []

    def decision(self, state, k):
        """
        Decide the best move based on the current game state.

        This method initiates the maximization process and returns the optimal move.

        Args:
            state (int): The current state of the game represented as an integer.
            k (int): The depth of the search tree, which limits how many moves ahead to look.

        Returns:
            tuple: A tuple containing the best child state (next move) and its associated utility value.
        """
        return self.maximize(state, k)

    def maximize(self, state, k):
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
        if k == 0:
            return None, eval(state)

        max_child = None
        max_utility = -float("inf")

        for child in get_children(state, self.turn):
            _, utility = self.minimize(child, k - 1)
            if utility > max_utility:
                max_utility = utility
                max_child = child

        return max_child, max_utility

    def minimize(self, state, k):
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
        if k == 0:
            return None, eval(state)

        min_child = None
        min_utility = float("inf")

        for child in get_children(state, str(1 - int(self.turn))):
            _, utility = self.maximize(child, k - 1)
            if utility < min_utility:
                min_utility = utility
                min_child = child

        return min_child, min_utility

    def get_minimax_tree(self):
        """
        Retrieve the Minimax tree built during the decision-making process.

        This tree represents all the possible states explored by the Minimax algorithm.

        Returns:
            list: A list representing the Minimax tree.
        """
        return self.minimax_tree
