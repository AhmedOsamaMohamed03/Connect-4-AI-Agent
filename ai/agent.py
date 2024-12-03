import time

# Import the MinimaxFactory to create instances of the chosen minimax algorithm
from ai.minimax_factory import MinimaxFactory
# Import required services for board manipulation and score calculation
from service.Service import *


# Agent class represents the AI player in the game
class Agent:
    def __init__(self, algorithm_name, k):
        """
        Initialize the agent with the specified algorithm and depth limit (k).
        :param algorithm_name: The name of the minimax algorithm to use.
        :param k: The depth limit for the minimax algorithm.
        """
        self.k = k  # Depth limit for the minimax algorithm
        self.current_state = 0  # Encoded game state, initially empty
        self.algorithm = MinimaxFactory().create(algorithm_name)  # Create the algorithm instance
        self.last_position = None  # The column where the last disc was dropped
        self.algorithm_name = algorithm_name

    def drop_disc(self, column):
        """
        Simulate dropping a disc into the specified column.
        :param column: The column index where the disc is dropped.
        :return: The updated game state and the player's score.
        """
        # Convert the current state to a zero-padded string representation
        current_state_str = str(self.current_state).zfill(COLUMNS * ROWS)
        self.last_position = column

        # Find the lowest empty row in the specified column
        for row in reversed(range(column, column + SIZE, COLUMNS)):
            if current_state_str[row] == "0":
                # Replace the empty spot with the player's disc ("1")
                current_state_str = replace_at(current_state_str, row, "1")
                break

        # Update the current state
        self.current_state = current_state_str
        # Calculate the player's score after this move
        return self.current_state, self.calculate_score(0)

    def play(self):
        """
        Simulate the agent's move using the minimax algorithm.
        :return: The agent's decision (column), the agent's score, and the parent state from the algorithm.
        """
        start = time.time()
        # Use the algorithm to decide the next move
        if self.algorithm_name == 'Expectiminimax':
            state, _ = self.algorithm.decision(int(self.current_state), self.k, self.last_position)
        else:
            state, _ = self.algorithm.decision(int(self.current_state), self.k)
        # Determine the column chosen by the agent
        agent_decision = self.get_agent_decision(self.current_state, state)
        # Update the current state with the agent's move
        self.current_state = str(state).zfill(SIZE)
        print(f"runtime: {time.time() - start}")  # Print runtime for performance evaluation
        print()
        # Return the decision and the calculated score
        return agent_decision, self.calculate_score(1), self.algorithm.get_parent()

    def get_agent_decision(self, current_state, max_state):
        """
        Determine the column of the move made by comparing the current state with the resulting state.
        :param current_state: The current game state.
        :param max_state: The game state after the agent's move.
        :return: The column index of the move.
        """
        current_state_str = str(current_state).zfill(SIZE)
        max_state_str = str(max_state).zfill(SIZE)
        idx = -1

        # Find the index where the two states differ
        for i in range(SIZE):
            if current_state_str[i] != max_state_str[i]:
                idx = i
                break

        # Calculate the column index from the differing index
        col = idx % COLUMNS
        return col

    def print_minimax_tree(self):
        """
        Print the minimax tree for debugging purposes.
        :return: The minimax tree structure.
        """
        tree = self.algorithm.get_minimax_tree()
        i = 1
        # Print each level of the tree
        for level in tree:
            print(f"level {i} -> {level}")
            i += 1
        return tree

    def calculate_score(self, turn):
        """
        Calculate the score for the current player based on the board configuration.
        :param turn: The player's turn (0 or 1).
        :return: The total score.
        """
        # Convert the current state into a 2D board representation
        self.current_state = str(self.current_state).zfill(SIZE)
        board = [list(self.current_state[i * COLUMNS:(i + 1) * COLUMNS]) for i in range(ROWS)]

        # Count the score based on winning patterns (diagonal, vertical, horizontal)
        return (count_diagonal_disks(board, turn, 4) +
                count_vertical_disks(board, turn, 4) +
                count_horizontal_disks(board, turn, 4))

# Example usage:
# if __name__ == '__main__':
#     start = time.time()
#     agent = Agent("minimax alpha beta", 4)  # Initialize the agent with a minimax algorithm
#     print(agent.drop_disc(3))  # Player drops a disc in column 3
#     print(agent.play())        # Agent makes a move
#     print(agent.drop_disc(4))  # Player drops a disc in column 4
#     print(agent.play())        # Agent makes another move
#     print(agent.drop_disc(2))  # Player drops a disc in column 2
#     print(agent.play())        # Agent makes a move
#     print(f"runtime: {time.time() - start}")  # Print runtime for performance evaluation
